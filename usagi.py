from bunny.bunny import BunnyCommands
from flask import Flask, request, redirect, render_template
from urllib.parse import quote

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # TODO: Implement home page!
    return redirect('https://google.com')

@app.route('/bunny', methods=['GET'])
def query():
    # Handle a standard query.
    try:

        # If no args were provided, redirect to /
        if 'query' not in request.args or not request.args['query']:
            return redirect('/')
        
        # Get the passed in command and extract the first word
        command_joined = request.args['query']
        command_split = command_joined.split(" ")

        command = None
        option_args = None # Maintain support for potentially 2+ argument commands in the future.

        if len(command_split) == 1:
            command = command_split[0]
            option_args = list()
        else:
            command = command_split[0]
            option_args = command_split[1:]
        
        try:
            return redirect(getattr(globals()['BunnyCommands'], command)(option_args))
        except:
            return redirect('https://www.google.com/search?q={}'.format(quote(request.args['query'])))

    except:
        return redirect('https://google.com/')

if __name__ == "__main__":
    #print(getattr(globals()['Commands'], 'a')('hello world'))
    app.run(host='0.0.0.0', port=8080, debug=True)