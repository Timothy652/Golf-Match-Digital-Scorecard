Money Match Digital Scorecard Application

#### Video Demo: <URL HERE>

This Flask application allows users to keep track of a golf match between two players or teams. It supports the following features:

Setting Up the Match: Users can set the number of holes, specify how much each hole and birdie are worth, and enter the names of the players or teams.

Score Entry: For each hole, users can input the par and scores for each player/team. Based on the scores, the application calculates money earned per hole and per birdie for each player/team.

Game Progression: After each hole, the application automatically progresses to the next hole until all holes are completed.

Final Score Display: Once all holes are completed, the application displays the final scores and declares the winner. It also calculates any owed money between the players/teams based on their final scores.

Files Included:
app.py: Contains the Flask application code.
style.css: Stylesheet for the HTML templates.
rules.html: Template for setting up the match rules.
scorecard.html: Template for entering scores for each hole.
final_scorecard.html: Template for displaying the final scores and declaring the winner.
Usage:
Clone the repository.
Install the necessary dependencies (Flask and Flask-Session).
Run python app.py to start the Flask development server.
Access the application at http://localhost:5000.
Requirements:
Python 3.x
Flask
Flask-Session
Note:
This application uses Flask-Session to manage session variables for maintaining game state across requests.
