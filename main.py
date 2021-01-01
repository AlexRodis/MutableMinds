from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return 'Hello World'



@app.route('/about')
def about():
    return 'Page Description'

if __name__ == '__main__':
    app.run(debug=True)