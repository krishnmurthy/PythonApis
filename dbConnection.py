from flask import Flask, request, jsonify
import oracledb

app=Flask(__name__)

@app.route('/api/users', methods=['POST'])
def users():
    data = request.get_json()
    return "krishna"

if(__name__)=='__main__':
    app.run(debug=True)
