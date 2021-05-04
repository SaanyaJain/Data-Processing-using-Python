from flask import Flask,request
#import pymongo
app = Flask(__name__)

@app.route('/login')
def disprec():
    un=request.args.get('nm')
    return "Welcome %s" %un

if __name__ == '__main__':
    app.run(debug = True)