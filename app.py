import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'super_secret_key'  # Change this in production
Session(app)

@app.route("/scorecard", methods=["GET", "POST"])
def scorecard():
    # Initialize session variables if not set
    if 'current_hole' not in session:
        session['current_hole'] = 1
        session['p1_money'] = 0
        session['p2_money'] = 0

    if request.method == 'POST':
        session['current_hole'] += 1

        par = int(request.form.get("par"))
        p1_score = int(request.form.get("p1_score"))
        p2_score = int(request.form.get("p2_score"))

        if p1_score < p2_score:
            session['p1_money'] += session['money_per_hole']
        elif p1_score > p2_score:
            session['p2_money'] += session['money_per_hole']

        if p1_score < par:
            session['p1_money'] += session['money_per_birdie']
        if p2_score < par:
            session['p2_money'] += session['money_per_birdie']
        


        if session['current_hole'] > session['number_of_holes']:
            # Reset for a new game or show final score
            final_scores = {
                'p1_money': session['p1_money'],
                'p2_money': session['p2_money']
            }
            session.pop('current_hole', None)
            session.pop('p1_money', None)
            session.pop('p2_money', None)
            return render_template("final_scorecard.html", final_scores=final_scores)
        else:
            return redirect(url_for('scorecard'))

    return render_template("scorecard.html", current_hole=session['current_hole'], p1_money=session['p1_money'], p2_money=session['p2_money'])


@app.route("/new_game")
def new_game():
    # Reset session variables for a new game
    session['current_hole'] = 1
    session['p1_money'] = 0
    session['p2_money'] = 0
    return redirect(url_for('rules'))


@app.route("/", methods=["GET", "POST"])
def rules():
    if request.method == "POST":
        session['number_of_holes'] = int(request.form.get("number_of_holes"))
        session['money_per_hole'] = int(request.form.get("money_per_hole"))
        session['money_per_birdie'] = int(request.form.get("money_per_birdie"))
        session['p1_name'] = request.form.get("p1_name")
        session['p2_name'] = request.form.get("p2_name")
        return redirect(url_for('scorecard'))
    else:
        return render_template("rules.html")



if __name__ == "__main__":
    app.run(debug=True)
