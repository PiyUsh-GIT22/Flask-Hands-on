from flask import Flask
from routes import routes


def test_define_routes():
    app = Flask(__name__)
    routes.define_routes(app)
    client = app.test_client()
    resp = client.get('/')
    assert resp.get_data() == b'Hello, World!'
    assert resp.status_code == 404
