FROM python

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask application's files into the container
COPY ./api/. ./

# Inform Docker that the container listens on port 5000
EXPOSE 5000

# ENTRYPOINT [ "python" ]
ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
