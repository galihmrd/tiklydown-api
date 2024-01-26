import requests
from flask import Flask, jsonify, make_response


app = Flask(__name__)

@app.route("/tiklydown", methods=["GET"])
def tikly():
    try:
        BASE_URL = "https://api.tiklydown.eu.org"
        r = requests.get(BASE_URL + f"/api/download?url={request.args.get("url")}", timeout=10)
        return make_response(jsonify({r.json()}), 200)
    except BaseException:
        raise Exception("No results found!")

if __name__ == "__main__":
    app.run()
