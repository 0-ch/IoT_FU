import json
from flask_cors import CORS
import pymongo
from bson import json_util

def connectMongo():
     #  MongoDB atlas
    myclient = pymongo.MongoClient('mongodb+srv://<Your name and password>@iot.n37xdq2.mongodb.net/?retryWrites=true&w=majority') 
    mydb = myclient['IOT_DB']  
    mycol = mydb['db1']  
    return mycol

def getMongo():
    mycol = connectMongo()

    # myquery = {"id": '64698523ea65f4f95d15d10a'}   
    mydoc = mycol.find({})    
   
    dataList = []
    for x in mydoc:
       
        x = json.loads(json_util.dumps(x))
        dataList.append(x)
        # print(x)
        # return x
    return dataList

def InsertMongo(photo,num,name):
    mycol = connectMongo()
    post = {"photo": photo,
         "num": num,
         "name": name}
    post_id = mycol.insert_one(post).inserted_id
    if(post_id != None):
        return "successful"
    else:
        return "error"
    # print (post_id) # if ObjectId('...') then successful!

print("mongo test")
print(getMongo())
print(InsertMongo("https://i.imgur.com/Fdo12tA.jpg", "000000", "tst"))
print(getMongo())
