# 🌦️ MyWeatherBot

MyWeatherBot is a Python-based chatbot that provides real-time weather information using the OpenWeatherMap API. It’s designed to work with Dialogflow and can be easily integrated into web or mobile applications for a smooth conversational experience.

## ✨ Features

- Retrieves current weather data for any city
- Easy integration with Dialogflow (Google’s NLP platform)
- Modular and scalable code structure
- API key secured using environment variables
- Clear separation of concerns with `app.py`, `weather_data.py`, and logging modules

## 📁 Project Structure

```
myweatherbot/
├── app.py               # Main Flask application
├── weather_data.py      # Weather-fetching logic using OpenWeatherMap
├── app_logger/          # Custom logging setup
├── app_exception/       # Custom exception classes
├── logs/                # Log output directory
├── .gitignore
├── requirements.txt     # Python dependencies
└── README.md
```

## 🔧 Prerequisites

- Python 3.8+
- OpenWeatherMap API key
- Flask
- Dialogflow (for chatbot integration)

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/myweatherbot.git
cd myweatherbot

# 2. Create a virtual environment
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```
