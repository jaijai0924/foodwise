from flask import Flask, render_template, url_for



app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/inventory')
def inventory():
    return render_template('')

@app.route('/receipts')
def receipts():
    return render_template('')



if __name__ == '__main__':
    app.run(debug=True)
