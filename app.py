from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage(name=None):
    return render_template('index.html', name=name)



@app.route('/aiga')
def aiga(name=None):
    return render_template('aiga.html', name=name)



@app.route('/madi')
def madi(name=None):
    return render_template('madi.html', name=name)

# Default port:
if __name__ == '__main__':
    app.run()
