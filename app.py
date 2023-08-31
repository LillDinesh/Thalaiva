from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
Countries = [
    {"code": "108", "country_name": "India", "language": "Hindi"},
    {"code": "109", "country_name": "England", "language": "English"},
    {"code": "110", "country_name": "Germany", "language": "Maori"},
    {"code": "111", "country_name": "Peris", "language": "Metropolitan French"},
    {"code": "112", "country_name": "Finland", "language": "Swedish"},
]

@app.route('/', methods=['GET'])
def get():
    return jsonify(Countries)

@app.route('/<code>', methods=['GET'])
def get_Countries(code):
    return jsonify(Countries[code])

if __name__ == '__main__':
    app.run(debug=True)
