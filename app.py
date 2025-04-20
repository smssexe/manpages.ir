from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/man/<command>')
def man_page(command):
    filepath = os.path.join("data", "manpages", f"{command}.txt")
    if not os.path.isfile(filepath):
        abort(404)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    return render_template("man.html", command=command, content=content)

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    if query:
        for fname in os.listdir("data/manpages"):
            if query in fname.lower():
                results.append(fname.replace(".txt", ""))
    return render_template("search.html", query=query, results=results)

@app.route('/commands')
def command_list():
    files = os.listdir("data/manpages")
    commands = [f.replace(".txt", "") for f in files if f.endswith(".txt")]
    commands.sort()
    return render_template("commands.html", commands=commands)


if __name__ == "__main__":
    app.run(debug=True)
