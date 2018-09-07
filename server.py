#!/usr/bin/python3

from flask import Flask, request, abort, jsonify

app = Flask(__name__)

help_queue = []

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/queue/help', methods=['GET', 'POST'])
def help_queue_manager():
	msg = ''
	if request.method == 'POST':
		first_name = request.values.get('first_name')
		last_name = request.values.get('last_name')
		kerberos = request.values.get('kerberos')
		remove = True if request.values.get('remove') == 'true' else False

		if kerberos and first_name and last_name:
			if remove:
				help_queue.remove((first_name, last_name, kerberos))
				msg = 'removed from queue'
			else:
				help_queue.append((first_name, last_name, kerberos))
				msg = 'added to queue'
			return jsonify({'message': msg})
		else:
			msg = 'missing queue data'
	else:
		return jsonify({'help_queue': help_queue})

	return jsonify({'error_code': 400, 'message': msg})

if __name__ == "__main__":
    port = 5000
    app.run(host='0.0.0.0', port=port)
