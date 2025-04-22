# manpages.ir

A minimal, nerdy web interface for exploring Linux man pages — in Markdown.

## What is this?

A lightweight Flask-based web app that serves Linux man pages in a readable, searchable Markdown format.

### Features

- **Search** manpages by name or content
- **Markdown-rendered** manual pages
- **Future sections** (under development):
  - `daily tips`: random/cool terminal tricks
  - `linux exams`: CLI study materials & practice
- **Minimal UI** — terminal-ish and intentionally plain

## Run with Docker

```bash
docker run -p 5000:5000 smssexe/manpages.ir:latest
```

Then visit:
http://localhost:5000

## Run from source:

```bash
git clone https://github.com/smssexe/manpages.ir.git
cd manpages.ir
pip install -r requirements.txt
python app.py
```

Make sure you have the templates/ and data/manpages/ folders.

## Project structure:

```bash
.
├── app.py              # Flask app
├── requirements.txt
├── templates/          # HTML templates
├── data/
│   └── manpages/       # Markdown files
└── Dockerfile
```

## Philosophy:

This project is made for terminal nerds. It's intentionally minimal.
No frontend frameworks, no JS clutter — just plain old Flask, HTML, and Markdown.

## Roadmap:

Markdown-based man page rendering
Basic search
Daily tips section
Linux exams section
Minimal responsive layout (still terminal vibes)

## License:

GPLv3
