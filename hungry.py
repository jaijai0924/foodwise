from flask import Flask, render_template, url_for
from static import background.css


app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)
