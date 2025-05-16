# FitPal - Fitness Tracking Application


FitPal is a web application designed to help users plan, track, and share their fitness routines. Users can create accounts, build weekly workout plans, log their workouts, view progress analytics, and even chat with an AI fitness assistant.

Zack Chen 23859398
Jarrah Oatham 23907753
Shutong Li 22913221
Jayden Nguyen 24217276



## Features

- User Authentication (Login, Registration)
- Weekly Workout Planner
- Workout Logging & History
- Progress Analytics (Volume, Calories, Lift Progress)
- Workout Plan Sharing
- AI Fitness Chatbot (OpenAI-powered)
- User Profile & BMR Calculation
- Responsive, Modern UI

---

## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, JavaScript (Chart.js)
- **Backend:** Flask, Flask-Login, Flask-Migrate, Flask-WTF
- **Database:** SQLite with SQLAlchemy
- **Testing:** Unittest (and optionally Selenium)
- **Other:** OpenAI API, python-dotenv

---

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static
│   │   ├── css
│   │   └── js
│   ├── templates
│   │   ├── base.html
│   │   ├── profile.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── posts.html
│   │   ├── workout_tools.html
│   │   └── ...
│   └── instance
│       └── app.db
├── migrations
├── tests
│   ├── test_selenium.py
│   └── test_app.py
├── .env
├── .flaskenv
├── .gitignore
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Setup

The following is a basic outline for getting FitPal up and running. For the most up-to-date information, please check the release notes.

### Prerequisites

- Flask (3.0.3+)
- Flask-Login (0.6.3+)
- Flask-Migrate (4.0.7+)
- Flask-SQLAlchemy (3.1.1+)
- Flask-WTF (1.2.1+)
- python-dotenv (1.0.1+)
- SQLAlchemy (2.0.29+)
- WTForms (3.1.2+)
- Chart.js (via CDN)
- OpenAI (for chatbot)
- (See `requirements.txt` for full list)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Zackggiitt/CITS3403-group-57.git
   
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root with your `SECRET_KEY` and `OPENAI_API_KEY`:
      ```
      SECRET_KEY=your-secret-key
      OPENAI_API_KEY=your-openai-api-key
      ```

5. **Initialize the database:**
    ```bash
    flask init-db
    ```

---

## Running the Application

1. **Start the Flask server:**
    ```bash
    flask run
    ```
2. **Open your web browser and go to:**  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Running Tests

1. **Ensure the Flask server is running (if needed).**
2. **In a separate terminal, run:**
    ```bash
    python -m unittest discover -s tests
    ```

---

## Usage

### User Authentication
- **Login:** Users can log in with their email and password.
- **Registration:** New users can create an account.

### Workout Planning & Logging
- **Weekly Planner:** Drag and drop exercises to build your weekly plan.
- **Save Workouts:** Log your completed workouts for progress tracking.

### Progress Analytics
- **Charts:** View your lift progress, workout volume, and calories burned.
- **Weekly Summary:** See your total volume and calories for the week.

### Plan Sharing
- **Share:** Send your workout plan to other users by email.

### AI Fitness Chatbot
- **Chat:** Get fitness advice and encouragement from the built-in AI assistant.

### Profile & BMR
- **Profile:** Edit your personal info and bio.
- **BMR Calculator:** See your Basal Metabolic Rate and daily calorie needs.

---

## Contribution

Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## Troubleshooting

- **Database Issues:**  
  If you encounter issues with the database, try re-initializing it:
  ```bash
  flask init-db
  ```

- **OpenAI Errors:**  
  Ensure your `OPENAI_API_KEY` is set correctly in your `.env` file.

- **Missing Dependencies:**  
  Make sure all required packages are installed:
  ```bash
  pip install -r requirements.txt
  ```

- **General Errors:**  
  Check the Flask server logs for detailed error messages and stack traces.

---

## External Sources Used

- Bootstrap v5.3.3 from Bootstrap CDN
- Chart.js from CDN
- OpenAI API
- UI Avatars: https://ui-avatars.com/
- Font: [Google Fonts](https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap)
- Exercise images: [Pexels](https://www.pexels.com/)

---

## License

MIT


