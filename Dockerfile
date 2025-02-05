FROM docker.io/python:alpine
LABEL org.opencontainers.image.description="Latest image for the Archiver bot built on every commit. See https://archiver.asterisk.lol/selfhost/docker for a setup guide."
LABEL org.opencontainers.image.licenses=AGPL-3.0-or-later
WORKDIR /archiver
COPY . /archiver
RUN adduser -D archiver
RUN chown -R archiver:archiver /archiver
USER archiver
RUN chmod u+x start.sh
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "./main_emoji.py"]
