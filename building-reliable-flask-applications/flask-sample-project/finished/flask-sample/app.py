from flask import Flask, request, jsonify
from routes import routes
from flask_debugtoolbar import DebugToolbarExtension
import aws
import logging

app = Flask(__name__)
app.secret_key = 'THISISPYTHONIST@SECRET'
app.debug = True
routes.define_routes(app)
toolbar = DebugToolbarExtension(app)


@app.route('/logs', methods=['GET', 'POST'])
def post_log():
    if request.method == 'POST':
        payload = {
            'msg': request.form.get('msg'),
            'level': request.form.get('level'),
            'process_id': request.form.get('process_id'),
            'req_url': request.form.get('req_url')
        }
        aws.invoke_function(payload)
        return jsonify({'message': 'Log sent to database successfully.'})


if __name__ == '__main__':
    logging.warning('This is a sample log message.')
    app.run(host='0.0.0.0', port='8000')
