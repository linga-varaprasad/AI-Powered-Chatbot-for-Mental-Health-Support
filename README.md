
# 🏥 Healthcare Support Chatbot

A healthcare support chatbot that provides empathetic and informative responses to user queries about health and well-being. This chatbot is built using **Streamlit** for the user interface and **Groq** AI for generating responses. It includes features like data encryption, anonymous usage, and real-time user interaction.

## Features

- **AI-Powered Healthcare Responses**: Uses Groq's LLaMA model to generate responses based on user input.
- **Interactive UI**: Built with Streamlit, providing a simple and clean interface for user queries.
- **Retry Mechanism**: Implements exponential backoff using the `tenacity` library to handle errors and API failures.
- **Privacy and Security**: Ensures that conversations are not stored and uses secure communication protocols (SSL/TLS).
- **Additional Features**: Includes health tips, emergency contacts, and session reset options.

---

## Table of Contents

1. [Features](#features)
2. [Demo](#demo)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Privacy & Security](#privacy--security)
7. [Testing & Feedback](#testing--feedback)
8. [Deployment & Monitoring](#deployment--monitoring)
9. [Future Enhancements](#future-enhancements)

---

## Demo

You can try the chatbot locally by following the [Installation](#installation) and [Usage](#usage) instructions below.

---

## Technologies

- **Python**: Backend scripting and AI integration.
- **Streamlit**: Web app framework for the UI.
- **Groq AI**: For generating healthcare-related chatbot responses.
- **Tenacity**: For retrying failed API calls.
- **dotenv**: For managing environment variables securely.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/healthcare-chatbot.git
   cd healthcare-chatbot
   ```

2. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root of your project and add the following:
   ```bash
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Start the Chatbot**: Open your browser at `http://localhost:8501`.
2. **Interact with the Chatbot**: Ask healthcare-related questions using the chat input field.
3. **Clear Conversation**: You can reset the chat history using the "Clear Conversation" button in the sidebar.
4. **Quick Health Tips**: Check out quick health tips for maintaining a healthy lifestyle in the sidebar.
5. **Emergency Contacts**: A reminder for emergency contact information is available in the sidebar.

---


## Testing & Feedback

- **Testing**: The chatbot has been rigorously tested for responsiveness, accuracy, and user experience.
- **User Feedback**: After each session, users are encouraged to provide feedback for continuous improvement.
- **Error Handling**: If the AI model fails to generate a response, error messages guide the user to try again later.

---

## Contributing

Feel free to contribute by creating a pull request, opening an issue, or suggesting features.

---
This README provides a comprehensive guide for setting up, using, and understanding your healthcare support chatbot project, making it suitable for an internship showcase.
