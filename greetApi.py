
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_post():
    # Retrieve JSON data from the request body
    data = request.get_json() 
    print(data)
    # Process the data (example: echo it back)
    return jsonify({
        "message": "Data received successfully!",
        "your_data": data
    }), 201


  
if __name__ == '__main__':
    app.run(debug=True)





