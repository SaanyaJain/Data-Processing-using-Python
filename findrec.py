from flask import Flask,request
import pymongo
app = Flask(__name__)

@app.route('/div1')
def disprec():
    myclient=pymongo.MongoClient("mongodb+srv://saanya:saanya@cluster0.6c3n1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    y=""
    d=request.args.get('division')
    mydb=myclient["MIT"]
    mycol=mydb["student"]
    myquery={"div":d}
    mydoc=mycol.find(myquery)
    for x in mydoc:
        y=y + str(x) +"<br>"
    return "%s" %y
if __name__ == '__main__':
   app.run()