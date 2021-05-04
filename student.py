from flask import Flask,request
import pymongo
import dns
app = Flask(__name__)

@app.route('/stud')
def disprec():
    myclient=pymongo.MongoClient("mongodb+srv://saanya:saanya@cluster0.6c3n1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    mydb=myclient["sj"]
    mycol=mydb["student"]
    sn=request.args.get('sname')
    div1=request.args.get('division')
    elective=request.args.get('elective')
    mydict={"studname":sn,"div":div1,"elective":elective}
    mycol.insert_one(mydict)
    return "Record Inserted..."
                                 
if __name__ == '__main__':
    app.run()
