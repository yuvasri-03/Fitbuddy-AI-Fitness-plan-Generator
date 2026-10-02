FitBuddy – AI Fitness Plan Generator

FitBuddy is an AI-powered fitness plan generator that creates personalized workout and fitness plans based on the user's age, gender, fitness goal, experience level, and dietary preference.

Features

- Personalized AI-generated fitness plans
- Workout recommendations based on fitness goals
- Beginner-friendly fitness guidance
- Dietary preference support
- User result management
- Update fitness goals
- FastAPI-based backend
- Gemini AI integration

Technologies Used

- Python
- FastAPI
- Google Gemini AI
- SQLite
- HTML/CSS
- Uvicorn

Project Structure

FitBuddy/
├── app/
├── templates/
├── .env
├── .gitignore
├── fitbuddy.db
├── requirements.txt
└── README.md

Installation

1. Clone or download the project.

2. Open the project folder in VS Code.

3. Create and activate a Python virtual environment.

4. Install the required dependencies:

pip install -r requirements.txt

API Key Configuration

Create a ".env" file and add your Google Gemini API key.

GEMINI_API_KEY=your_api_key_here

Do not share or upload your API key publicly.

Running the Project

Start the FastAPI server using:

python -m uvicorn app.main:app --reload

The application will run locally at:

http://127.0.0.1:8000

API documentation is available at:

http://127.0.0.1:8000/docs

API Endpoints

- "GET /" – Home
- "POST /generate" – Generate a personalized fitness plan
- "GET /result/{user_id}" – View generated result
- "GET /users" – List users
- "PUT /update/{user_id}" – Update fitness goal

How It Works

1. The user enters their basic fitness information.
2. FitBuddy sends the information to the backend.
3. The Gemini AI model generates a personalized fitness plan.
4. The generated plan is returned to the user.
5. The user can view and update their fitness information.

Future Enhancements

- Exercise form detection using computer vision
- Progress tracking
- Mobile application
- More personalized workout recommendations
- Fitness progress analytics

Team Project

FitBuddy was developed as a team project for the Naan Mudhalvan program.