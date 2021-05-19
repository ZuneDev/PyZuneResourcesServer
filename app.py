from flask import Flask, abort, send_from_directory

from locale import *


app = Flask(__name__)


@app.route(f"/<path:filepath>")
def get_image(filepath: str):
    try:
        print(filepath)
        return send_from_directory("./static", filename=filepath, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(port=80)
