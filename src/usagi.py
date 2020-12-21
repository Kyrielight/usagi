#pylint:disable=unused-wildcard-import,undefined-variable,import-error,anomalous-backslash-in-string

import re
import sys

from flask import Flask, request, redirect
from urllib.parse import quote

from resolvers import *

# Flask application
app = Flask(__name__)

PATHS = {
    '^a(?:\ .+)?$': amazon.resolve,
    '^f(?:\ .+)?$': facebook.resolve,
    '^g(?:\ .+)?$': google.resolve,
    '^j[wksn]?(?:\ .+)?$': jisho.resolve,
    '^r\/\w*$': reddit.subreddit,
    '^re?((18)|(nsfw))? .+$': reddit.search,
    '^t@.+$': twitter.at,
}

def resolve_path(command, default=google.default):
    for key, path in PATHS.items():
        if re.match(r"{}".format(key), command.strip(), re.IGNORECASE):
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
    #print(resolve_path(" ".join(sys.argv[1:]))(sys.argv[1:]))
    app.run(host='0.0.0.0', port=8080, debug=False)