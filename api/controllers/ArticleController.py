from models.queries import get_article_by_id, get_article_by_uid, get_articles, create_article, edit_article, delete_article, get_user_by_uid

from uuid import uuid4

class ArticleController:
    
    @classmethod
    def get_articles(cls):
        articles = get_articles()
        result = [article.serialize() for article in articles]

        return result

    @classmethod
    def get_article_by_id(cls, id: str, serialize: bool = False):
        article = get_article_by_id(id)
        if serialize:
            return article.serialize()
        return article

    @classmethod
    def get_article_by_uid(cls, uid: str):
        articles = get_article_by_uid(uid)
        username = get_user_by_uid(uid)
        result = [
            {
                'id': article.id,
                'uid': article.uid,
                'title': article.title,
                'json': article.json,
                'brief': article.brief,
                'date': article.date
            }
            for article in articles
        ]

        return result, username

    @classmethod
    def create(cls, uid, title, json_data, brief_description):
        article = create_article(uid = uid, title = title, json_data = json_data, brief_description = brief_description)

        return article

    @classmethod
    def edit(cls, title, brief_description, json_data, article_id):
        article = edit_article(title = title, brief_description = brief_description, json = json_data, article_id = article_id)

        return article
    
    @classmethod
    def delete(cls, article_object):
        article = delete_article(article_object = article_object)
        return article
