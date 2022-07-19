from flask import Flask, send_from_directory
import random
import json
from Starlink import Starlink

app = Flask(__name__)
dishy = Starlink()

@app.route("/")
def base():
    return send_from_directory('../svelte/public', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../svelte/public', path)


@app.route("/hello")
def hello():
    return "<html><body><h1>Hello!</h1></body></html>"


@app.route("/rand")
def random_number():
    return str(random.randint(0, 100))


@app.route("/starlink/status")
def startlink_status():
    status = dishy.get_status()

    return json.dumps(status, indent=4)


if __name__ == "__main__":
    app.run(port=9999, debug=True)
