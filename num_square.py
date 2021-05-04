from flask import Flask,request
#import pymongo
app = Flask(__name__)

@app.route('/sqnum')
def number_square():
    num=int(request.args.get('n'))
    sq=int(num) * int(num)
    return "The square is %d" %sq

if __name__ == '__main__':
    app.run(debug = True)