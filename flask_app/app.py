from flask import Flask, render_template, make_response, Request, jsonify, json
from flask_restful import Resource, Api
import socket, os

app = Flask(__name__, template_folder='templates_folder')

@app.route("/goku")
def goku():
  return render_template('goku.html')

@app.route("/ping/<host>", methods=['GET'])
def ping_host(host):
    result = os.system(f'ping -c 3 {host}')

    if result == 0:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})

@app.route("/host")
def host():
  return render_template('host.html', id_container=socket.gethostname())

@app.route("/mdc", methods=["GET"])
def mdc():
    response = make_response("<h1>Mentoria Devops Cloud! Status 200!</h1>", 200)
    return response

@app.route("/success", methods=["GET"])
def success():
    response = make_response("<h1>Success</h1>", 200)
    return response

@app.route("/denied", methods=["GET"])
def denied():
    response = make_response("<h1>Denied</h1>", 500)
    return response

@app.route("/notfound", methods=["GET"])
def notfound():
    response = make_response("<h1>NotFound</h1>", 404)
    return response

if __name__ == "__main__":
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host='0.0.0.0', port=port)
