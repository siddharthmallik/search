import pymongo

myclient = pymongo.MongoClient("mongodb+srv://test:test@cluster0.scilq.mongodb.net/product_db?retryWrites=true&w=majority")
mydb = myclient["product_db"]
mycol = mydb["product_records"]

"""myquery = { "name": "apple" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)"""

"""myquery = { "name": { "$gt": "c" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)"""

"""myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)"""

"""x = mycol.find_one()

print(x)"""

"""for x in mycol.find():
  print(x)"""

"""for x in mycol.find({},{ "_id": 0, "name": "rocket", "price": 60000 }):
  print(x)"""

for x in mycol.find({},{ "name": 0 }):
  print(x)