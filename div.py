from flask import Flask, request
import pymongo

app = Flask(__name__)

@app.route('/div')

def disprec():
    d = request.args.get('d')
    myclient = pymongo.MongoClient("mongodb+srv://saanya:saanya@cluster0.6c3n1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb = myclient["sj"]
    mycol = mydb["student"]
    myquery = {"div":d}
    mydoc = mycol.find(myquery)
    string = ""
    for x in mydoc:
        string = string + "<h1> %s %s %s </h1>" %(x["studname"],x["div"],x["elective"])
    return string
    
if __name__ == '__main__':
    app.run(debug=True)
