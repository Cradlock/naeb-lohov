FROM python:3.12-slim 
RUN python -m venv /env

ENV PATH="/env/bin:$PATH"

RUN pip install --upgrade pip 
COPY r.txt . 
RUN pip install --no-cache-dir -r r.txt 
WORKDIR /app 
COPY . . 
ENTRYPOINT [ "python","init.py" ]
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
