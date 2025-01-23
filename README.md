# JARVIS - A Personal Assistant

Welcome to **JARVIS**, a personal assistant inspired by the iconic AI from Ironman. This project aims to combine cutting-edge technologies to create a chatbot that can generate images, process speech, and interact with users in real-time.

## Features
- **Chatbot** powered by:
  - **Mixtral-8x7b-32768**
  - **Llama3-70b-8192**
  - **Command-R-Plus**
- **Image Generation** using **Stable-Diffusion-XL-Base-1.0**.
- **Real-time Data Access** with **Google Search API** for fetching up-to-date information.
- **Text-to-Speech** with **Edge TTS** for converting text responses into audio.
- **Speech-to-Text** via **Selenium**, enabling voice input from the user.
- **Chat Memory**: Stores chat data to provide context to future interactions.
- **GUI** for easy user interaction, making the experience intuitive and engaging.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/JARVIS.git
   
2. Navigate to the project directory:

    ```bash
    cd JARVIS

3. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt

4. Configure API keys:

Add your API keys for Google Search and other services to the .env file (refer to .env.example for the format).
