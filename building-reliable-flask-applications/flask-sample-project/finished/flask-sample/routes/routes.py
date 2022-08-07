from flask import render_template, make_response, redirect, url_for

posts = [
    {
        'title': 'Python is Fun',
        'content': 'Python is a general purpose programming language.'
    },
    {
        'title': 'PHP for dummies',
        'content': 'PHP is scripting programming language designed ofr web.'
    },
    {
        'title': 'Java for Everyone',
        'content': 'Java is a language for everyone from personal to enterprise.'
    },
    {
        'title': 'Flutter a new Player',
        'content': 'Flutter is a way to build mobile apps for multiple platforms with single codebase.'
    }
]


def define_routes(app):
    @app.route('/')
    def hello_world():
        return render_template('posts.html')
        # return redirect(url_for('contact'), 301)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        return render_template('contact.html')

    @app.route('/posts')
    def all_posts():
        response = make_response(render_template('posts.html', data=posts))
        response.headers['key'] = 'value'
        response.status_code = 200
        return response
