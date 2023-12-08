from flask_login import logout_user

from forms.login_form import LoginForm
from routes import app
from flask import render_template, abort, redirect, url_for, flash
from services.article_service import ArticleService
from services.user_service import UserService


@app.route('/')
@app.route('/index.html')
def home_page():
    articles = ArticleService().get_articles()
    return render_template('index.html', articles=articles)


@app.route('/article/<article_id>.html')
def article_page(article_id):
    article = ArticleService().get_article(article_id)
    if article:
        return render_template('article.html', article=article)

    abort(404)


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data, password=form.password.data)
        if result:
            flash(f'欢迎{form.username.data}回来', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('用户名或密码错误，请重试!', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout.html')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))
