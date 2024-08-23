# Guess the Number Game 🎮

Welcome to **Guess the Number Game**, a simple yet fun number guessing game implemented in Python using Flask. The game randomly selects a number between 1 and 50, and the player tries to guess it with feedback after every attempt.

Play it live at: [Guess the Number Game](https://adidas7717.pythonanywhere.com/)
Note: The live website may go down as its hosted on pythonanywhere and they give only 3 months of free hosting :(

## 🚀 Features

- Random number generation between 1 and 50.
- User-friendly web interface built with Flask.
- Real-time feedback on user guesses.
- Automatically resets after guessing the correct number.

## 💻 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Flask Jinja Templating)
- **Hosting**: [PythonAnywhere](https://pythonanywhere.com)

## 🛠 How to Set Up Locally

1. Clone the repository:
   git clone https://github.com/username/repo.git
   cd repo

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the application:
   flask run

4. Open your browser and go to `http://127.0.0.1:5000/` to play the game locally.

## 📝 Game Rules

1. The computer randomly selects a number between 1 and 50.
2. Enter your guess in the input field and submit.
3. The game will guide you whether the guess is too high or too low.
4. Once you guess the correct number, the game will reset, allowing you to play again.

## 🎨 Screenshots

![Home Page](/gmply.jpg)


## 📂 Project Structure

```bash
.
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── Procfile              # For deployment (if applicable)
├── templates
│   └── index.html        # HTML template for the game UI
├── static
│   └── style.css         # Optional CSS for styling (if applicable)
└── README.md             # Project documentation
```

## 🌍 Live Demo

Check out the live version here: [https://adidas7717.pythonanywhere.com/](https://adidas7717.pythonanywhere.com/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/username/repo/issues).

## 🧑‍💻 Author

- **Aditya Vikram Singh** - [LinkedIn](https://linkedin.com/in/aditya-vikrsam-singh-770163224) | [GitHub](https://github.com/eluzaa)

```

---

### Architecture File

Here's an architecture diagram for your project. The description below can be included in a separate markdown file (e.g., `architecture.md`), and you can create a diagram using tools like **Lucidchart**, **draw.io**, or **Microsoft PowerPoint**.

#### Architecture Diagram
```md
# Architecture Overview

The **Guess the Number Game** is a web application built using Python and Flask. Below is an overview of the architecture.

## 🏛️ Architecture Layers

### 1. **User Interface (UI)**
- **HTML/CSS**: The user interacts with the web page via forms where they input their guesses. 
- **Flask Jinja Templating**: Dynamically renders HTML pages based on the user's input and the backend's response.

### 2. **Backend Logic**
- **Flask**: Handles the routing and logic for the game.
  - **`/` Route**: Handles GET and POST requests. Displays the form for inputting guesses and returns feedback.
  - **Game Logic**: Generates a random number, compares it with the user's guess, and provides feedback.

### 3. **Hosting Layer**
- **PythonAnywhere**: Hosts the application, serving the static HTML files and the Flask app to the user.

## 📊 Workflow

1. **User Accesses Website**: The user opens the game URL in their browser.
2. **Initial Render**: Flask renders the initial page (`index.html`) with a form for the user to input their guess.
3. **User Submits Guess**: The user submits their guess via the form.
4. **Backend Processing**: The Flask backend processes the input, compares it with the generated random number, and returns feedback to the user.
5. **Page Update**: Based on the comparison, the page is updated with feedback (higher, lower, correct) and the game continues until the number is guessed.

