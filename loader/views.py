from flask import render_template, Blueprint, request
from functions import load_posts, uploads
import logging

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix='/post', static_folder='static',
                             template_folder='templates')


@loader_blueprint.route('/form/')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
def upload_post():
    try:
        file = request.files.get('picture')
        filename = file.filename
        content = request.values.get('content')
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split('.')[1] not in ['png', 'jpeg']:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return '<h2> Файл не найден </h2>'
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)