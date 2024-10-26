FROM python:3.9-slim
WORKDIR /app
COPY process_subtitles /app

RUN apt-get update && apt-get install -y cron ffmpeg
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
