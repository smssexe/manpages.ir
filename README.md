# manpages.ir 🐧📚

A minimal, nerdy web interface for exploring Linux man pages — in Markdown.

## 📦 What is this?

This is a lightweight Flask-based web app that serves man pages in a readable, searchable Markdown format.

### Features:

- 🔍 **Search** manpages by name or content
- 📖 View Markdown-rendered manpages
- ✍️ Planned sections:
  - `daily tips`: random or curated command-line tricks
  - `linux exams`: a study guide-like section for sysadmins and power users
- 🎨 Minimal UI with terminal-like vibes (on purpose)

## 🚀 How to run it

### 🐳 With Docker:

```bash
docker run -p 5000:5000 smssexe/manpages.ir:latest
```

Then open your browser:
http://localhost:5000
🛠️ From source:

```bash
git clone https://github.com/smssexe/manpages.ir.git
cd manpages.ir
pip install -r requirements.txt
python app.py
```

Make sure you have your templates/ and data/manpages/ folders in place.
📁 Project structure
.
├── app.py # Main Flask app
├── requirements.txt
├── templates/ # HTML templates
├── data/
│ └── manpages/ # Your Markdown manpages live here
└── Dockerfile # For containerized deployment

💭 Philosophy
This site is made for the nerds. It’s intentionally minimal, almost retro.
The idea is to keep things fast, clean, and terminal-friendly — no JavaScript madness, no fancy animations.

🛣️ Roadmap
Markdown-based man page rendering

Basic search functionality

daily tips section

linux exams module

    Responsive layout (but still nerdy)

☕ Contributing

Pull requests welcome. Make it better, cleaner, or more Unixy.
📜 License
