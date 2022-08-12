from flask import render_template, url_for, request, redirect
from src.main_module import app, Article, db

# /home
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


# /about
@app.route('/about')
def about():
    return render_template('about.html')


# /posts
@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.day.desc()).all()
    return render_template('posts.html', articles=articles)


# /posts/id
@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post_detail.html', article=article)


# /posts/id/delete
@app.route('/posts/<int:id>/delete')
def post_delete(id):
    article = Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении статьи произошла ошибка"


# /posts/id/update
@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        # Reading data to DB from page, if we've received POST request
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        try:
            db.session.commit()
            # Redirecting after updating page
            return redirect('/posts')
        except:
            return "При редактировании статьи произошла ошибка"
    else:
        return render_template('post_update.html', article=article)


# /create-article
@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        # POST request handling
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            # Redirecting after adding data to the Database
            return redirect('/posts')
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template('create-article.html')