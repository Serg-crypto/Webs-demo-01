from flask import Flask, render_template, jsonify
from info import datos

# comando para correr en local: python app.py

app = Flask(__name__)

@app.route('/api')
def show_json():
    return jsonify(datos)


@app.route('/')
def home():
    return render_template('home.html', company_name='Soller')



if __name__ == '__main__':
    app.run(debug=True)
