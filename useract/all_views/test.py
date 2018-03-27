from flask import Flask, render_template

app =Flask(__name__)

@app.route("/output")
def output():
    return render_template("test/test.html", name="Joe")

if __name__ == "__main__":
 app.run()