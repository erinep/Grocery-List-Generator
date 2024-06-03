import pymongo
from bson.objectid import ObjectId

class MyMongo:

    def __init__(self):
        self.host = 'mongodb'
        # self.host = 'localhost'
        self.port = 27017
        self.db_name = 'testdb'

        # create Connection Pool
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]
        self.recipes = self.db["recipeCollection"]
        self.tasks = self.db["taskCollection"]

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
                {"task_type": 'text', "task_content": "1,2,3"},
                {"task_type": 'text', "task_content": '4,5,6'},
                {"task_type": "other", "task_content": "7, 8, 9"}
            ]
        return self.CreateRecipe('test_recipe', task_list)

    def CreateRecipe(self, name, task_to_create):

        task_status = self.tasks.insert_one({'task_list': task_to_create})
        recipe_status = self.recipes.insert_one({"name": name, "task_id": task_status.inserted_id})
         
        return {
            "recipe_created": recipe_status.acknowledged,
            "tasks_created": task_status.acknowledged,
            "recipe_id": str(recipe_status.inserted_id),
            "tasks_id": str(task_status.inserted_id),
        }
    
    def GetRecipeList(self):

        # Retrieve a list of objects
        cur = self.recipes.find({})
        all_data = []
        for item in cur:
            item['_id'] = str(item['_id'])
            item['task_id'] = str(item['task_id'])
            all_data.append(item)

        return { "response": all_data}

    def DeleteRecipe(self, id):

        my_recipe = self.recipes.find_one({"_id": ObjectId(id)})

        if (my_recipe):
            tasks_response = self.tasks.delete_one({"_id":  my_recipe['task_id']})
            recipes_response = self.recipes.delete_one({"_id": ObjectId(id)})

            return {
                "recipe_deleted": recipes_response.acknowledged,
                "tasks_deleted": tasks_response.acknowledged,
                "recipes_deleted_count": recipes_response.deleted_count,
                "tasks_deleted_count": tasks_response.deleted_count,
            }

        else: 
            return {
                "recipe_deleted": False,
                "tasks_deleted": False,
            }


    def GetRecipe(self, id=None):

        try:

            response = {}
            
            my_recipe = self.recipes.find_one({"_id": ObjectId(id)})
            my_task = self.tasks.find_one({"_id": my_recipe['task_id']})
            response['recipe_id'] = str(my_recipe['_id'])
            response['task_id'] = str(my_recipe['task_id'])
            response['recipe_name'] = my_recipe['name']
            response['task_list'] = my_task["task_list"]

            return response

        except Exception as e:
            print('An error has occured:', e)
            return { "response": None}

    def SetTaskList(self, task_id, task_list):

        update_result = self.tasks.update_one(
            {"_id": ObjectId(task_id)},
            { 
                "$set": {
                    "task_list": task_list,
                }
            }
        )

        return { "task_updated": update_result.acknowledged } 