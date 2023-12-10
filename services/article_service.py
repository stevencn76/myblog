from models.article import Article
from routes import db
from sqlalchemy import Select


class ArticleService:

    def get_article(self, id):
        return db.session.get(Article, id)

    def get_articles(self):
        query = Select(Article)
        return db.session.scalars(query).all()

    def create_article(self, article: Article):
        # todo: 添加同标题文章是否存在的检测，如果数据库中存在了相同标题的文章，那么这里抛出一个异常
        db.session.add(article)
        db.session.commit()

        return article
