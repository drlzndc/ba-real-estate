FROM jupyter/base-notebook:python-3.11

WORKDIR /app/lab
COPY . .

RUN pip install \
    --requirement requirements.txt \
    --no-cache-dir

CMD [ \
    "start-notebook.py", \
    "--NotebookApp.token=''", \
    "--NotebookApp.password=''" \
]
