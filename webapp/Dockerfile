FROM python:3.11-slim

WORKDIR /app/webapp
COPY . .

RUN pip install \
    --requirement requirements.txt \
    --no-cache-dir 

CMD [ \
    "streamlit", \
    "run", \
    "app.py"\
]
