import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["customers"]

myquery = { "name": "John" }

mydoc = mycollection.find(myquery)

for x in mydoc:
  print(x)



# x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
# print(x.inserted_ids)