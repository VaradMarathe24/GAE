from flask import Flask, request, render_template_string

app = Flask(__name__)

QUIZ_FORM = '''
    <h2>Cricket Quiz</h2>
    <form method="post">
        Name: <input type="text" name="name" required><br>
        Nationality: <input type="text" name="coo" required><br>
        Age: <input type="number" name="age" required><br><br>

        1. Who is known as the 'God of Cricket'?<br>
        <input type="text" name="q1"><br><br>

        2. How many players are there in a cricket team?<br>
        <input type="text" name="q2"><br><br>

        3. Which country won the ICC Cricket World Cup in 2011?<br>
        <input type="text" name="q3"><br><br>

        4. Who won the orange cap of IPL 2008?<br>
        <input type="text" name="q4"><br><br>

        5. Who was the Most Valuable Player of IPL 2017?<br>
        <input type="text" name="q5"><br><br>

        6. Who was the inaugural World Cup winner?<br>
        <input type="text" name="q6"><br><br>

        7. One of the two new teams playing in IPL 2017 were Gujarat and ?<br>
        <input type="text" name="q7"><br><br>

        8. I have played for DD, KXIP, MI, PWI, SRH. Who am I?<br>
        <input type="text" name="q8"><br><br>

        9. Who was the captain of West Indies in 1983 World Cup?<br>
        <input type="text" name="q9"><br><br>

        10. Who was the purple cap winner of IPL 2016?<br>
        <input type="text" name="q10"><br><br>

        <input type="submit" value="Submit">
    </form>
'''

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = {
            "q1": ['b', 'sachin tendulkar'],
            "q2": ['b', '11'],
            "q3": ['a', 'india'],
            "q4": ['b', 'shaun marsh'],
            "q5": ['c', 'ben stokes'],
            "q6": ['a', 'west indies'],
            "q7": ['c', 'pune'],
            "q8": ['c', 'yuvraj singh'],
            "q9": ['c', 'clive lloyd'],
            "q10": ['a', 'bhuvneshwar kumar']
        }

        score = 0
        for q in answers:
            user_ans = request.form.get(q, "").strip().lower()
            if user_ans in answers[q]:
                score += 1

        result_msg = f"""
        <h2>Thank you, {request.form['name']}!</h2>
        <p>Nationality: {request.form['coo']}</p>
        <p>Age: {request.form['age']}</p>
        <p>Your final score is: <strong>{score}/10</strong></p>
        """

        if score == 10:
            result_msg += "<p>Excellent! You're a cricket champ!</p>"
        elif score >= 8:
            result_msg += "<p>Bravo, you are entering into the world of cricket.</p>"
        elif score >= 6:
            result_msg += "<p>Good job! You know your cricket.</p>"
        else:
            result_msg += "<p>Keep learning. Cricket has a lot to offer!</p>"

        return result_msg

    return render_template_string(QUIZ_FORM)

if __name__ == "__main__":
    app.run()
