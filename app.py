from flask import Flask, request, render_template

app = Flask(__name__)

responses = {
    "hello": "Hi there!",
    "how are you": "I'm a your bot, feeling bot-tastic!",
    "bye": "Goodbye!",
    "what is your name": "I’m your ChatBot buddy!"
}

@app.route("/", methods=["GET", "POST"])
def chat():
    reply = ""
    if request.method == "POST":
        msg = request.form["message"].lower()
        reply = responses.get(msg, "I don't understand that yet.")
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)

