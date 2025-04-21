from flask import Flask, render_template, request, abort
import os
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/man/<command>')
def man_page(command):
    filepath = os.path.join("data", "manpages", f"{command}.md")
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
        manpages_dir = os.path.join("data", "manpages")
        for fname in os.listdir(manpages_dir):
            full_path = os.path.join(manpages_dir, fname)
            if os.path.isfile(full_path) and fname.endswith(".md") and query in fname.lower():
                results.append(fname.replace(".md", ""))
    return render_template("search.html", query=query, results=results)


@app.route('/commands')
def command_list():
    manpages_dir = os.path.join("data", "manpages")
    commands = []
    for f in os.listdir(manpages_dir):
        full_path = os.path.join(manpages_dir, f)
        if os.path.isfile(full_path) and f.endswith(".md"):
            commands.append(f.replace(".md", ""))
    commands.sort()
    return render_template("commands.html", commands=commands)



if __name__ == "__main__":
    app.run(debug=True)
