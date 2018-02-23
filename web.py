import json
from flask import Flask, render_template, request
from ua_parser import user_agent_parser


app = Flask(__name__)


@app.route("/")
def index():
    ua = request.args.get('ua')
    if ua:
        parsed = user_agent_parser.Parse(ua)
        parsed_encoded = json.dumps(parsed, indent=2)
    else:
        parsed_encoded = None

    current_ua = request.headers.get('User-Agent')
    return render_template("index.html",
                           ua=ua,
                           current_ua=current_ua,
                           parsed_encoded=parsed_encoded)
