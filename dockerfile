# python version
FROM python:3.11

# workspace
WORKDIR /code

# copy requirements.txt to code directory
COPY requirements.txt .

# install python libraries
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy code to code/app
COPY . .

EXPOSE 8000

# run command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]