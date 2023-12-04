from routes import app


@app.route('/create_article.html')
def create_article():
    return "Create Article"
