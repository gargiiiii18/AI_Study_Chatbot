# 📚 AI Study Chatbot

**AI_Study_Chatbot** is a Streamlit-based web application designed to assist users in studying by providing three core functionalities: answering questions, summarizing notes, and generating multiple-choice questions (MCQs) on a given topic. 

> **Note:** This repository does not include a pre-configured API URL. Users are required to obtain an AI model API endpoint of their choice and modify the code accordingly to integrate with the selected API.

---

## Features

- **Question Answering:** Provides detailed and accurate answers to user queries.
- **Note Summarization:** Summarizes large volumes of text into concise and informative summaries.
- **MCQ Generation:** Automatically generates multiple-choice questions based on the input topic or text.

---

## Web Application Screenshots

*Please replace the placeholder image paths with your actual screenshots.*

![Home Screen](path/to/screenshot1.png)  
*Main interface of the AI_Study_Chatbot.*

![Answering Questions](path/to/screenshot2.png)  
*Example of the question answering feature in action.*

![MCQ Generation](path/to/screenshot3.png)  
*Multiple-choice questions generated from a provided topic.*

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
