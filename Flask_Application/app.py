from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, my name is chaha, clap ch clap chcha a cha cha cha cha cha cha cha cha'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)