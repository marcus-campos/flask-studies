from flask import Flask, jsonify

app = Flask(__name__)

stores = [
	{
		'name': "My store",
		'items': [
			{
				'name': 'My item',
				'price': 10.59
			}
		]
	}
]


@app.route('/store', methods=['POST'])
def create_store():
	pass

@app.route('/store/<string:name>')
def get_store(name):
	pass

@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})
	pass

app.run(debug=True,host='0.0.0.0',port=80)