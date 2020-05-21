from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello World</h1>
    <p>It is currently {time}.</p>

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

