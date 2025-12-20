FROM python:3.10-slim
WORKDIR /AQI_status
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD [ "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]