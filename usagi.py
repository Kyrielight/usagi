#pylint:disable=unused-wildcard-import,undefined-variable

import re
import sys

from flask import Flask, request, redirect
from urllib.parse import quote

from resolvers import *

# Flask application
app = Flask(__name__)

PATHS = {
    'a.? .*': amazon.resolve,
    'f.? .*': facebook.resolve,
    'g.? .*': google.resolve,
    'j.? .*': jisho.resolve,
}

def resolve_path(command, default=google.resolve):
    for key, path in PATHS.items():
        if re.match(r"{}".format(key), command, re.IGNORECASE):
            return path
    return default

@app.route("/bunny", methods=['GET'])
def bunny():
    try:
        if 'query' not in request.args or not request.args['query']:
            raise Exception()

        command = request.args['query']
        return redirect(resolve_path(command)(command.split(" ")))

    except:
        return redirect('https://google.com')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    #args_comb = " ".join(sys.argv[1:])
    #print(resolve_path(args_comb)(sys.argv[1:]))
