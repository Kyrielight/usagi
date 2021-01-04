
import paths
import sys

from flask import Flask, request, redirect
from urllib.parse import quote

# Flask application
app = Flask(__name__)

@app.route("/bunny", methods=['GET'])
def bunny():
    try:
        if 'query' not in request.args or not request.args['query']:
            raise Exception()

        command = request.args['query']
        return redirect(paths.resolve_path(command)(command.split(" ")))

    except:
        return redirect('https://google.com')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)