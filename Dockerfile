FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /webecomercce

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django (inside the container)
EXPOSE 8000

# Run the application with gunicorn
CMD ["gunicorn", "webecomercce.wsgi:application", "--bind", "0.0.0.0:8000"]
