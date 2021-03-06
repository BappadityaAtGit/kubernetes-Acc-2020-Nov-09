from flask import Flask
import os 
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/amit")
def hello_amit():
    return "Hello EveryOne from Amit Vashist"

@app.route("/info")
def hello_info():
    html = "<h2>Welcome to the World of Containers.</h2>"\
           "<h2>Docker & K8s Rocks</h2>"\
           "<b>FQDN:</b> {fqdn}<br/>"
    return html.format(hostname=socket.gethostname(),fqdn=socket.getfqdn())
    

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8080)
