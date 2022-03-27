from flask import render_template, Blueprint, request
from functions import load_posts
import logging

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    posts = []
    search_post = request.args['s']
    logging.info(f'Слово для поиска: {search_post}')
    for i in load_posts():
        if search_post.lower() in i['content'].lower():
            posts.append(i)
    return render_template('post_list.html', search_post=search_post, posts=posts)
