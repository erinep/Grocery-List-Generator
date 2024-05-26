import pymongo
from bson.objectid import ObjectId

class MyMongo:

    def __init__(self):
        self.host = 'mongodb'
        self.port = 27017
        self.db_name = 'testdb'


    def __enter__(self):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]
        
        # Access your collection
        collection_name = "testCollection"
        self.collection = self.db[collection_name]

        return self

    def __exit__(self, exc_type, exc_valu, exc_tb):

        print(exc_type)

    def TestConnection(self):
        client = pymongo.MongoClient(host=self.host, port=self.port,
                     connectTimeoutMS=3000,
                     socketTimeoutMS=3000,
                     serverSelectionTimeoutMS=3000 )
        try:
            client.admin.command("ping")
            return {"db_connected": True}
        except:
            print("could not connect to sever")
            return {"db_connected":  False}

    def CreateSampleRecipe(self):

        task_list = [
                {"task_type": 'text', "task_content": "1,2,3", "task_id": 0},
                {"task_type": 'text', "task_content": '4,5,6', "task_id": 1},
                {"task_type": "other", "task_content": "7, 8, 9", "task_id": 2}
            ]
        return self.CreateRecipe(task_list)

    def CreateRecipe(self, my_list):

        status = self.collection.insert_one({
            "task_list": my_list,
            "task_index": len(my_list) - 1
        })
        print(status)
         
        return {
            "acknowledged": status.acknowledged,
            "recipe_id": str(status.inserted_id)
        }
    
    def GetRecipeListFull(self):

        # Retrieve a list of objects
        cur = self.collection.find({})
        all_data = []
        for item in cur:
            item['_id'] = str(item['_id'])
            all_data.append(item)

        return { "response": all_data}
    
    def GetRecipeListIDs(self):

        # Retrieve a list of objects
        cur = self.collection.find({}, {'_id': 1})
        all_data_ids = []
        for item in cur:
            all_data_ids.append(str(item['_id']))

        return { "response": all_data_ids}


    def GetRecipe(self, id):

        try:
            obj = ObjectId(id)
            response = self.collection.find_one({"_id": obj})
            if (response):
                response["_id"] = str(response["_id"])
            return { "response": response}
        except:
            return { "response": None}

    def UpdateRecipe(self, recipe_id, task_list):
        result = self.collection.update_one(
            {"_id": ObjectId(recipe_id)},
            { 
                "$set": {
                    "task_list": task_list,
                    "task_index": len(task_list) - 1
                }
            }
        )

        return { "acknowledged": result.acknowledged } 