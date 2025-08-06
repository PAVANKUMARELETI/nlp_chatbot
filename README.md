# NLP Healthcare Chatbot

A simple, terminal-based chatbot built with Python, NLTK, and TensorFlow/Keras. This chatbot is designed to act as a basic healthcare assistant, capable of understanding user queries and providing relevant information based on a predefined set of intents.

## 🌟 Features

- **Natural Language Understanding**: Uses NLTK for tokenization, lemmatization, and processing user input.
- **Intent Recognition**: A deep learning model built with TensorFlow/Keras classifies user intent.
- **Interactive Terminal UI**: A clean, text-based user interface created with the `curses` library.
- **Extensible Knowledge Base**: Easily add new skills and responses by editing the `intents.json` file.

---

## 🛠️ Technologies Used

- **Python**
- **TensorFlow / Keras**: For building and training the neural network.
- **NLTK (Natural Language Toolkit)**: For all natural language processing tasks.
- **NumPy**: For numerical operations and handling training data.
- **Scikit-learn**: For splitting data.
- **Curses (`windows-curses`)**: For the command-line interface.

---

## 🚀 Setup and Installation

Follow these steps to get the chatbot running on your local machine.

### 1. Prerequisites

- Python 3.8+
- Git

### 2. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone [https://github.com/your-username/nlp-chatbot.git](https://github.com/your-username/nlp-chatbot.git)
cd nlp-chatbot
(Replace your-username and nlp-chatbot with your actual GitHub username and repository name.)3. Create a Virtual EnvironmentIt is highly recommended to use a virtual environment to manage project dependencies.# Create the virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
4. Install DependenciesInstall all the required packages using the requirements.txt file.pip install -r requirements.txt
Note: The requirements.txt file should also include windows-curses for Windows users.5. Train the ModelBefore you can run the chatbot, you must first train the neural network. This will process the intents.json file and create a trained_model.keras file.python train.py
This process may take a few minutes to complete.▶️ How to RunOnce the model is trained, you can start the chatbot with the following command:python main.py
You can then type your questions into the terminal and press Enter to get a response from the bot. To exit the application, press Ctrl + C.📂 Project Structure.
├── venv/
├── chatbot.ipynb       # The original Jupyter Notebook for development
├── intents.json        # The knowledge base for the chatbot
├── main.py             # Starts the application and runs the main loop
├── train.py            # Script to train the neural network model
├── ui.py               # Handles the terminal user interface
├── requirements.txt    # Lists all project dependencies
├── .gitignore          # Specifies files for Git to ignore
└── README.md           # You are here!
