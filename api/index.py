import requests
from flask import Flask, jsonify, make_response, request


app = Flask(__name__)

@app.route("/tiklydown", methods=["GET"])
def tikly():
    if request.args.get('url').endswith("@fhd"):
        input_url = request.args.get('url').split("@fhd")[0]
    else:
        input_url = request.args.get('url')
    try:
        BASE_URL = "https://api.tiklydown.eu.org"
        r = requests.get(BASE_URL + f"/api/download?url={input_url}", timeout=10)
        return make_response(r.json(), 200)
    except BaseException:
        raise Exception("No results found!")

if __name__ == "__main__":
    app.run()
