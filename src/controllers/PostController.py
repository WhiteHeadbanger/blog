from models.queries import get_post_by_id, get_post_by_uid, get_posts, create_post, edit_post, delete_post, get_user_by_uid

from uuid import uuid4

class PostController:
    
    @classmethod
    def get_posts(cls):
        posts = get_posts()
        result = [post.serialize() for post in posts]

        return result

    @classmethod
    def get_post_by_id(cls, id: str, serialize: bool = False):
        post = get_post_by_id(id)
        if serialize:
            return post.serialize()
        return post

    @classmethod
    def get_post_by_uid(cls, uid: str):
        posts = get_post_by_uid(uid)
        username = get_user_by_uid(uid)
        result = [
            {
                'id': post.id,
                'uid': post.uid,
                'title': post.title,
                'body': post.body
            }
            for post in posts
        ]

        return result, username

    @classmethod
    def create(cls, post_data):
        title = post_data['title']
        body = post_data['body']
        uid = post_data['uid']

        post = create_post(uid = uid, title = title, body = body)

        return post

    @classmethod
    def edit(cls, post_data, post_obj):
        title = post_data['title']
        body = post_data['body']

        post = edit_post(post_obj = post_obj, title = title, body = body)

        return post
    
    @classmethod
    def delete(cls, post_obj):
        post = delete_post(post_obj)
        return {"deleted": post}
