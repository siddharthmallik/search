import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://test:test@cluster0.80jod.mongodb.net/collection?retryWrites=true&w=majority")

mydb = myclient["collection"]

"""print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")"""

mycol = mydb["customers"]

"""print(mydb.list_collection_names())"""

"""collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")"""

"""mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)"""

"""mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)"""

"""mydb.products.insert_many([
   { "item": "journal", "qty": 25, "tags": [
       "blank", "red"], "size": { "h": 14, "w": 21, "uom": "cm" } },
   { "item": "mat", "qty": 85, "tags": ["gray"], "size": {
       "h": 27.9, "w": 35.5, "uom": "cm" } },
   { "item": "mousepad", "qty": 25, "tags": [
       "gel", "blue"], "size": { "h": 19, "w": 22.85, "uom": "cm" } }
])"""

"""mydb.products.insert_one( { "item": "card", "qty": 15 } )"""

"""mydb.customers.find().limit(5)"""


"""x = mycol.find_one()

print(x)"""

"""for x in mycol.find():
  print(x)"""

"""for x in mycol.find({},{ "address": 0 }):
  print(x)"""

"""myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)"""

"""mydb.orders.count()"""

"""myresult = mycol.find().skip(10).limit(5)

#print the result:
for x in myresult:
  print(x)"""

"""mydb.mycol.insert_many(
   [
     { "_id": 16, "name": "Java Hut", "phone":45634, "description": "Coffee and cakes" },
     { "_id": 17, "name": "Burger Buns", "phone":65732, "description": "Gourmet hamburgers" },
     { "_id": 18, "name": "Coffee Shop", "phone":94952, "description": "Just coffee" },
     { "_id": 19, "name": "Clothes Clothes Clothes", "phone":48374, "description": "Discount clothing" },
     { "_id": 20, "name": "Java Shopping", "phone":30405, "description": "Indonesian goods" }
   ]
)"""

"""mydb.mycol.create_index( { "name": "text", "description": "text" } )"""

mydb.mycol.find({"name":"amy"})







