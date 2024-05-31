from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    con = sqlite3.connect('components.db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/computers', methods=['GET'])
def get_computers():
    processor = request.args.get('processor', '')
    gpu = request.args.get('gpu', '')
    motherboard = request.args.get('motherboard', '')
    ram = request.args.get('ram', '')

    query = """SELECT * FROM components WHERE 
               processor LIKE ? AND 
               gpu LIKE ? AND 
               motherboard LIKE ? AND 
               ram LIKE ?"""
    args = (f'%{processor}%', f'%{gpu}%', f'%{motherboard}%', f'%{ram}%')
    results = query_db(query, args)

    data = []
    for row in results:
        data.append({
            'processor': row[0],
            'gpu': row[1],
            'motherboard': row[2],
            'ram': row[3]
        })

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)