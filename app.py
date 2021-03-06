from flask import Flask
from flask import request

import socket
from ResponseDTO import ResponseDTO

import time
import json
import os

app = Flask(__name__)


@app.route('/api/backend')
def hello_world():
    greet = request.args.get("greeting", "")

    responseDTO = ResponseDTO()

    # Greeting
    greeting = greet + " from cluster Backend"

    # Ip
    ip = socket.gethostbyname(socket.gethostname())

    # DateTime
    now = time.time()

    responseDTO.greeting = greeting
    responseDTO.ip = ip
    responseDTO.time = now

    jsonResponse = json.dumps(responseDTO.__dict__, indent=True)

    response = app.response_class(
        response=jsonResponse,
        status=200,
        mimetype="application/json")
    return response

    # return jsonResponse


if __name__ == '__main__':
    svcHost = "0.0.0.0"
    svcPort = 80

    if os.environ["SVC_HOST"]:
        svcHost = os.environ["SVC_HOST"]
        print("CONFIGURAZIONE - [SVC_HOST]: " + svcHost)

    if os.environ["SVC_PORT"]:
        svcPort = os.environ["SVC_PORT"]
        print("CONFIGURAZIONE - [SVC_PORT]: " + svcPort)

    app.run(host=svcHost, port=svcPort)
