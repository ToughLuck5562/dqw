from flask import Flask, render_template, request, jsonify

try:
    import api.utils.database as database
except:
    from utils import database

app = Flask(__name__, template_folder='client/templates', static_folder='client/static')

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
