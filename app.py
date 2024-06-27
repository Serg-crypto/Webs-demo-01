from flask import Flask, render_template, jsonify
import sqlalchemy
from info import datos


#print(sqlalchemy.__version__)


app = Flask(__name__)

@app.route('/api')
def show_json():
    return jsonify(datos)


@app.route('/')
def home():
    return render_template('home.html', company_name='Soller')



if __name__ == '__main__':
    app.run(debug=True)
