
import flask
import json

from pipguitool.PIP import PIP

from flask import request, abort


p = PIP()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/list', methods=['GET'])
def list():
    return json.dumps(p.list())

@app.route('/install', methods=['POST'])
def install():

	if not request.json or not 'packages' in request.json or not hasattr(request.json['packages'], "append"):
		abort(400)
	
	return str(p.install(request.json['packages']))+"<br/>", 201

@app.route('/remove', methods=['POST'])
def remove():

	if not request.json or not 'packages' in request.json or not hasattr(request.json['packages'], "append"):
		abort(400)
	
	return str(p.remove(request.json['packages']))+"<br/>", 201


def main():
	app.run()

if __name__ == '__main__':
    main()