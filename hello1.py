from flask import Flask
app = Flask(__name__)
@app.route('/hello')

def home():
   return "<body bgcolor=red><h2>Hello World</h2></body>"

if __name__ == '__main__':
   app.run()