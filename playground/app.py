from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/welcome/<string:name>")
def wel(name):
    return render_template("welcome.html", name=name)


@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    class_roster = [("Hermione","A","Sophomore"), ("Harry","B","Sophomore"), ("Ron", "C", "Sophomore"), ("Ginny","B-","Freshman"), ("Neville","D","Sophomore"), ("Luna","A", "Freshman"), ("Percy","A", "Senior"), ("Fred","C", "Junior"), ("George","C+", "Junior")]
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)


if __name__ == '__main__':
    app.run(debug=True)
