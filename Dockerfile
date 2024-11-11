FROM python:3.12-slim-bullseye
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir qr_codes
COPY . .
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "https://github.com/sashankpannala"]
