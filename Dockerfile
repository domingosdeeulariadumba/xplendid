# Using a lightweight 3.12 Python image
FROM python:3.12-slim

# Setting the root directory
WORKDIR /app

# Installing required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev libffi-dev \
    nano \    
    && rm -rf /var/lib/apt/lists/*

# Copying the application files
COPY . /app

# Updating PIP and installing Python dependencies without cache
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposing streamlit default port
EXPOSE 8501

# Running the Streamlit app
CMD ["streamlit", "run", "app.py"]