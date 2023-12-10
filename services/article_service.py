from models.article import Article
from routes import db
from sqlalchemy import Select, func


class ArticleService:

    def get_article(self, id):
        return db.session.get(Article, id)

    def get_articles(self):
        query = Select(Article)
        return db.session.scalars(query).all()

    def create_article(self, article: Article):
        query = Select(Article).where(Article.title == article.title)
        exist_articles = db.session.scalars(query)
        if exist_articles:
            return article, '同标题的文章已经存在'

        db.session.add(article)
        db.session.commit()

        return article, None

    def update_article(self, article: Article):
        exist_article = db.session.get(Article, article.id)
        if not exist_article:
            return article, '文章不存在'

        # TODO: 检查同标题的文章是否存在

        exist_article.title = article.title
        exist_article.content = article.content
        exist_article.update_time = func.now()

        db.session.commit()

        return article, None
