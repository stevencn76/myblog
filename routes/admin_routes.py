from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from forms.article_form import ArticleForm
from models.article import Article
from routes import app
from services.article_service import ArticleService


@app.route('/createarticle.html', methods=['GET', 'POST'])
@login_required
def create_article_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data

        try:
            ArticleService().create_article(new_article)
            flash(f'发布文章完成', category='success')
            return redirect(url_for('home_page'))
        except Exception as error:
            flash(f'发布文章失败: {error}', category='danger')

    return render_template('editarticle.html', form=form)

