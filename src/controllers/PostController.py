from models.PostModel import PostModel

from uuid import uuid4

class PostController:
    
    def __init__(self):
        pass
    
    @classmethod
    def get_posts(cls):
        posts = PostModel.get_posts()
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

    def get_post(self):
        pass

    def create(self, post_data):
        title = post_data['title']
        body = post_data['body']
        uid = post_data['uid']

        new_post = PostModel(
            id = str(uuid4()),
            uid = uid,
            title = title,
            body = body
        )

        new_post.create_post()

    def edit(self):
        pass

    def delete(self):
        pass
