FROM debian:bookworm AS builder

RUN apt-get update && apt-get install -y \
    man-db manpages manpages-dev \
    groff procps coreutils bash util-linux

WORKDIR /app

COPY . .

RUN bash generate_man_markdown.sh

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/all_man_pages_md ./manpages
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/exams ./exams
COPY --from=builder /app/static ./static
COPY --from=builder /app/app.py ./app.py
COPY --from=builder /app/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]