from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://dada:dada@cluster0-0qy57.mongodb.net/test?retryWrites=true"#i have changed the passw
client = MongoClient(MONGODB_URI)
db = client.get_database("Users")
user = db.Users

workers =user.estimated_document_count()
print(workers)

testData = {
    "Name": "tes",
    "Res_id": "0",
    "Role": "testcomp",
    "Age": 0
}

user.insert_one(testData)

workers =user.estimated_document_count()
print(workers)
