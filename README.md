# Money Match Digital Scorecard Application

#### Video Demo:(https://youtu.be/uWMNxbJ1QH0)

This Flask application enables users to manage a golf match between two players or teams, focusing on tracking financial bets alongside scores. It offers robust features:

### Features:

- **Setting Up the Match:** Define the number of holes, set values for each hole and birdie, and input player/team names.
- **Score Entry:** Input par and scores for each hole per player/team. Calculates money earned per hole and birdie.
- **Game Progression:** Automatically moves to the next hole after each round until all holes are complete.
- **Final Score Display:** Shows final scores and declares the winner. Calculates owed money based on scores.

### Files Included:

- **`app.py`:** Flask application code.
- **`style.css`:** Stylesheet for HTML templates.
- **`rules.html`:** Template for match setup.
- **`scorecard.html`:** Template for score entry.
- **`final_scorecard.html`:** Template displaying final scores.

### Usage:

1. Clone the repository.
2. Install dependencies (`Flask` and `Flask-Session`).
3. Run `python app.py` to start the Flask server.
4. Access the application at `http://localhost:5000`.

### Requirements:

- Python 3.x
- Flask
- Flask-Session

### Note:

- Uses Flask-Session for managing session variables to maintain game state.
