from flask import Flask, request, render_template
from gpt_engine import GPTClient

app = Flask(__name__)
gpt = GPTClient()

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form.get("question", "")
        if question.strip():
            answer = gpt.ask(question)
    return render_template("index.html", answer=answer)