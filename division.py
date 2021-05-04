from flask import Flask, request
import pymongo
import dns

app = Flask(__name__)


@app.route('/division')
def disprec():
    myclient = pymongo.MongoClient("mongodb+srv://saanya:saanya@cluster0.6c3n1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["sj"]
    mycol = mydb["student"]
    myquery = {"div":"A"}
    mydoc = mycol.find(myquery)
    string = ""
    for x in mydoc:
        string = string + "<h1> %s %s %s </h1>" %(x["studname"],x["div"],x["elective"])
    return string
    
if __name__ == '__main__':
    app.run()
