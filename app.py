from flask import Flask, render_template, request, abort
import os
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    if query:
        manpages_dir = os.path.join("data", "manpages")
        for fname in os.listdir(manpages_dir):
            full_path = os.path.join(manpages_dir, fname)
            if os.path.isfile(full_path) and fname.endswith(".md"):
                with open(full_path, encoding="utf-8") as f:
                    content = f.read().lower()
                    if query in fname.lower() or query in content:
                        results.append(fname.replace(".md", ""))
    return render_template("search.html", query=query, results=results)

@app.route('/man/<command>')
def man_page(command):
    query = request.args.get("q", "").strip().lower()
    filepath = os.path.join("data", "manpages", f"{command}.md")
    if not os.path.isfile(filepath):
        abort(404)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # if has query highlight it
    if query:
        import re
        def highlight(match):
            return f"<mark>{match.group(0)}</mark>"
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        content = pattern.sub(highlight, content)

    # Convert to HTML
    import markdown
    html_content = markdown.markdown(content)
    return render_template("man_md.html", command=command, content=html_content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
