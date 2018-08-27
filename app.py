from flask import Flask, jsonify, request

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
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(store)
	return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store['items'])
	return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})
	pass

app.run(debug=True,host='0.0.0.0',port=80)