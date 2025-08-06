import streamlit as st
from tensorflow.keras.models import load_model
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# --- 1. LOAD DATA AND MODELS ---

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the trained model and other necessary files
try:
    model = load_model('trained_model.keras')
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    with open('intents.json') as file:
        intents = json.load(file)
except FileNotFoundError:
    st.error("Model or data files not found. Please run `train.py` to generate them.")
    st.stop()


# --- 2. CHATBOT LOGIC FUNCTIONS ---

def clean_up_sentence(sentence):
    """Tokenize and lemmatize the sentence."""
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    """Create a bag of words from the sentence."""
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence, model):
    """Predict the class/intent of the sentence."""
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]), verbose=0)[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    """Get a random response from the predicted intent."""
    if not ints:
        return "I'm sorry, I don't understand. Can you please rephrase?"
    
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = np.random.choice(i['responses'])
            break
    else:
        result = "I'm sorry, I don't understand. Can you please rephrase?"
    return result

# --- 3. STREAMLIT UI ---

st.set_page_config(page_title="Healthcare Chatbot", page_icon="🤖")

st.title("🤖 Healthcare Chatbot")
st.write("Ask me anything about healthcare, symptoms, or finding medical facilities.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I assist you with your health today?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ints = predict_class(prompt, model)
            response = get_response(ints, intents)
            st.markdown(response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

