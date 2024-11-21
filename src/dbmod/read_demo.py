from pymongo import MongoClient

def read_all_user():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["abhidemo"]  
    collection = db["users"]
    
    user_cursor = collection.find() 
    users_list = list(user_cursor)
    
    for item in users_list:
        item["_id"] = str(item["_id"])
    
    return users_list