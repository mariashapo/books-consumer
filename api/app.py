from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def consume_service():
    # The URL of the first service
    service_url = "http://book-api-server-vadim-mariia.h4h0dqcndhhch8ga.uksouth.azurecontainer.io:5000/books"
    
    # Get the genre query parameter
    genre = request.args.get('genre')
    author = request.args.get('author')
    title = request.args.get('title')

    params = {'genre': genre, 'author': author, 'title': title}
    
    response = requests.get(service_url)
    books = response.json()
    
    filtered_books = []

    # Check if genre or author filter is applied
    if genre or author or title:
        for book in books:
            genre_match = str.lower(genre) in str.lower(book['genre']) if genre else True
            author_match = str.lower(author) in str.lower(book['author']) if author else True
            title_match = str.lower(title) in str.lower(book['title']) if title else True

            # Add the book if it matches both genre and author criteria
            if genre_match and author_match and title_match:
                filtered_books.append(book)
    else:
        # If no filters are provided, use all books
        filtered_books = books

    return render_template('index.html', books=filtered_books, params=params)

if __name__ == '__main__':
    app.run(debug=True)
