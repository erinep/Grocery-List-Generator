import pymongo

class MyMongo:

    def __init__(self, dbconfig):
        self.uri = f'mongodb://{dbconfig["mongo_host"]}'
        self.db_name = dbconfig['mongo_db_name']


    def __enter__(self):
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.db_name]
        
        # Access your collection
        collection_name = "testCollection"
        self.collection = self.db[collection_name]

        return self

    def __exit__(self, exc_type, exc_valu, exc_tb):

        self.client.close()


    def insertfakedata(self):

        task_list = [
                {"task_type": 'text', "task_content": "1,2,3", "task_id": 0},
                {"task_type": 'text', "task_content": '4,5,6', "task_id": 1},
                {"task_type": "other", "task_content": "7, 8, 9", "task_id": 2}
            ]
        return self.insertlist(task_list)

    def insertlist(self, my_list):

        status = self.collection.insert_one({
            "task_list": my_list,
            "task_index": len(my_list) -1
        })
        
        return {"insert_result": status.acknowledged}
    

    def getdata(self):

        # Retrieve a list of objects
        cur = self.collection.find({}, {'_id': 0})
        all_data = []
        for item in cur:
            all_data.append(item)

        return { "response": all_data}