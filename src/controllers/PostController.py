from models.queries import get_post_by_id, get_post_by_uid, get_posts, create_post

from uuid import uuid4

class PostController:
    
    def __init__(self):
        pass
    
    @classmethod
    def get_posts(cls):
        posts = get_posts()
        result = [
            {
                'id': post.id,
                'uid': post.uid,
                'title': post.title,
                'body': post.body
            }
            for post in posts
        ]

        return {"count": len(result), "posts": result}

    @classmethod
    def get_post_by_id(cls):
        pass

    @classmethod
    def get_post_by_uid(cls, uid: str):
        posts = get_post_by_uid(uid)
        result = [
            {
                'id': post.id,
                'uid': post.uid,
                'title': post.title,
                'body': post.body
            }
            for post in posts
        ]

        return {"count": len(result), "posts": result}

    @classmethod
    def create(cls, post_data):
        title = post_data['title']
        body = post_data['body']
        uid = post_data['uid']

        post = create_post(uid = uid, title = title, body = body)

        return post

    def edit(self):
        pass

    def delete(self):
        pass
