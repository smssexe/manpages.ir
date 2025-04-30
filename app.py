from flask import Flask, redirect, render_template, request, abort, session, url_for
import os
import json
import random
import markdown
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"

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

@app.route('/tips')
def tips_list():
    tips_dir = os.path.join("data", "tips")
    entries = []
    for fname in os.listdir(tips_dir):
        if fname.endswith(".md"):
            date = fname.replace(".md", "")
            path = os.path.join(tips_dir, fname)
            tags = []
            with open(path, encoding="utf-8") as f:
                for line in f:
                    if "tags" in line.lower():
                        cleaned = line.replace("**", "").strip()
                        parts = cleaned.split(":", 1)
                        if len(parts) == 2:
                            tags = [t.strip() for t in parts[1].split(",")]
                        break
            entries.append({"date": date, "tags": tags})
    entries.sort(key=lambda x: x["date"], reverse=True)
    return render_template("tips_list.html", entries=entries)



@app.route('/tips/<date>')
def tip_for_date(date):
    filepath = os.path.join("data", "tips", f"{date}.md")
    if not os.path.isfile(filepath):
        abort(404)
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    import markdown
    html = markdown.markdown(content)
    return render_template("tip_day.html", date=date, content=html)

@app.route('/tips/search')
def search_tips():
    query = request.args.get("q", "").lower()
    tips_dir = os.path.join("data", "tips")
    results = []

    if query:
        for fname in os.listdir(tips_dir):
            if fname.endswith(".md"):
                date = fname.replace(".md", "")
                path = os.path.join(tips_dir, fname)
                with open(path, encoding="utf-8") as f:
                    content = f.read().lower()
                    if query in content:
                        results.append(date)
    results.sort(reverse=True)
    return render_template("tips_search.html", query=query, results=results)

@app.route('/tips/tag/<tag>')
def tips_by_tag(tag):
    tag = tag.lower()
    tips_dir = os.path.join("data", "tips")
    matched = []

    for fname in os.listdir(tips_dir):
        if fname.endswith(".md"):
            date = fname.replace(".md", "")
            path = os.path.join(tips_dir, fname)
            with open(path, encoding="utf-8") as f:
                for line in f:
                    if line.lower().startswith("**tags:**"):
                        tags_line = line.split(":", 1)[1].strip().lower()
                        tags = [t.strip() for t in tags_line.split(",")]
                        if tag in tags:
                            matched.append(date)
                        break
    matched.sort(reverse=True)
    return render_template("tips_by_tag.html", tag=tag, dates=matched)

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


@app.route("/exams")
def exams():
    # List available topics (each .json file in data/exams)
    topics = [f.replace(".json", "") for f in os.listdir("data/exams") if f.endswith(".json")]
    return render_template("exam_topics.html", topics=topics)

@app.route("/exams/start")
def start_exam():
    topic = request.args.get("topic")
    if not topic:
        return redirect(url_for("exams"))
    path = os.path.join("data", "exams", f"{topic}.json")
    if not os.path.isfile(path):
        return "Invalid topic", 404
    
    with open(path, encoding="utf-8") as f:
        questions = json.load(f)
    
    selected = random.sample(questions, min(20, len(questions)))
    session['exam'] = {
        "topic": topic,
        "questions": selected,
        "current": 0,
        "score": 0,
        "answers": []
    }
    return redirect(url_for("show_question"))

@app.route("/exams/question", methods=["GET", "POST"])
def show_question():
    if 'exam' not in session:
        return redirect(url_for("exams"))

    exam = session['exam']
    current = exam["current"]
    questions = exam["questions"]

    if request.method == "POST":
        selected = request.form.get("answer")
        correct = questions[current]['answer']
        exam['answers'].append({
            "question": questions[current]['question'],
            "selected": selected,
            "correct": correct,
            "explanation": questions[current].get("explanation", "")
        })
        if selected == correct:
            exam['score'] += 1
        exam['current'] += 1
        session['exam'] = exam
        return redirect(url_for("show_question"))

    if current >= len(questions):
        return redirect(url_for("exam_result"))

    question = questions[current]
    return render_template("exam_question.html", index=current+1, total=len(questions), question=question)

@app.route("/exams/result")
def exam_result():
    if 'exam' not in session:
        return redirect(url_for("exams"))
    exam = session.pop('exam')
    return render_template("exam_result.html", score=exam['score'], total=len(exam['questions']), answers=exam['answers'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
