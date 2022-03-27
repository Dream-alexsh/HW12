import json

POSTS_JSON = 'posts.json'


def load_posts():
    with open(POSTS_JSON, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def uploads(posts):
    with open(POSTS_JSON, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)

