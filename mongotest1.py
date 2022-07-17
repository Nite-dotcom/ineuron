import pymongo
client = pymongo.MongoClient("mongodb+srv://nitesh:Nitesh@cluster0.qdhaz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)