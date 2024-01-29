import os
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/books', methods=['GET', 'POST'])
def index():
    # Call the books API with parameters
    service_url = os.getenv('BOOKS_API_URL')

    if request.method == 'POST':
        # Extract data from form
        genre = request.form.get('genre')
        author = request.form.get('author')
        title = request.form.get('title')
        
        params = {'genre': genre, 'author': author, 'title': title}
        response = requests.get(service_url, params=params)
        books_response = response.json()

        return render_template('index.html', books=books_response, params=params)

    else:
        # Get query parameters
        genre = request.args.get('genre')
        author = request.args.get('author')
        title = request.args.get('title')
        
        params = {'genre': genre, 'author': author, 'title': title}
        response = requests.get(service_url, params=params)
        books_response = response.json()
        
        return render_template('index.html', books=books_response, params=params)

if __name__ == '__main__':
    app.run(debug=True)
