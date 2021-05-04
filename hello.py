from flask import Flask
app = Flask(__name__)
@app.route('/mit')

def success():
   return "<body bgcolor=pink><h2>Hello World</h2></body>"

if __name__ == '__main__':
   app.run()