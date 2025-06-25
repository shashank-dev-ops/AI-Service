# Use a Python 3.9 slim-buster image as the base.
FROM python:3.9-slim-buster

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker's build cache.
COPY requirements.txt .

# Install the Python dependencies. This will be very fast now.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application file into the container.
COPY app.py .

# Expose port 5000 from the container.
EXPOSE 8000

# Define the command to run the application using Gunicorn.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

