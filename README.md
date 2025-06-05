# 📚 AI Study Chatbot

<br/>

**AI_Study_Chatbot** is a Streamlit-based web application designed to assist users in studying by providing three core functionalities: answering questions, summarizing notes, and generating multiple-choice questions (MCQs) on a given topic. 

> **Note:** This repository does not include a pre-configured API URL. Users are required to obtain an AI model API endpoint of their choice and modify the code accordingly to integrate with the selected API.

---

## Features

- **Question Answering:** Provides detailed and accurate answers to user queries.
- **Note Summarization:** Summarizes large volumes of text into concise and informative summaries.
- **MCQ Generation:** Automatically generates multiple-choice questions based on the input topic or text.

---

## Web Application Screenshots

### HomeScreen & Modes

<img src="https://github.com/gargiiiii18/AI_Study_Chatbot/blob/main/screenshots/interface.png?raw=true" width="700"/>
<img src="https://github.com/gargiiiii18/AI_Study_Chatbot/blob/main/screenshots/modes.png?raw=true" width="300"/>

### Answering Questions

<img src="https://github.com/gargiiiii18/AI_Study_Chatbot/blob/main/screenshots/answering%20questions.png?raw=true" width="700"/>

### Summarizing Notes

<img src="https://github.com/gargiiiii18/AI_Study_Chatbot/blob/main/screenshots/summarizing%20notes.png?raw=true" width="700"/>

### Generating MCQ's

<img src="https://github.com/gargiiiii18/AI_Study_Chatbot/blob/main/screenshots/mcqs.png?raw=true" width="700"/>

---

## Technology Stack

- **Streamlit:** For building the interactive web interface.
- **Python:** Core programming language for application logic.
- **AI Model API:** External AI service used for natural language processing (to be provided and configured by the user).
- **Requests:** HTTP library used to communicate with the AI API.

---

## Installation

Follow these steps to set up and run the AI_Study_Chatbot locally:

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/gargiiiii18/AI_Study_Chatbot.git
   cd AI_Study_Chatbot

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   ```
   **On macOS/Linux**
   ```bash
   source venv/bin/activate
   ```
   **On Windows**
   ```bash
   venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Obtain an AI model API endpoint and credentials:**
   *Acquire an API URL and key from your preferred AI service provider (e.g., OpenAI, Google Gemini, Hugging Face).*

5. Configure the application:
   *Update the relevant sections of the code to include your API endpoint and authentication details, adhering to the chosen model’s API documentation.*
   
7. **Run the application:**
   ```bash
   streamlit run app.py
   ```
