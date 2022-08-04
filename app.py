import os
from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/topics')
    def topics():
        return render_template('topics.html')

    #potentially unnecessary
    import topicinfo, topicreview
    app.register_blueprint(topicinfo.bp)
    app.add_url_rule('/', endpoint='topicinfo')
    app.register_blueprint(topicreview.bp)
    app.add_url_rule('/', endpoint='topicgame')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app

app = create_app()