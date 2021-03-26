FROM python:3.7.6
WORKDIR .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


