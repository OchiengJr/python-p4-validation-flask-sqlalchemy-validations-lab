from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    if authors:
        authors_data = [author.to_dict() for author in authors]
        return make_response(jsonify(authors_data), 200)
    else:
        return make_response(jsonify({'message': 'No authors found.'}), 404)

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    if posts:
        posts_data = [post.to_dict() for post in posts]
        return make_response(jsonify(posts_data), 200)
    else:
        return make_response(jsonify({'message': 'No posts found.'}), 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
