from pymongo import MongoClient


def mongo_insert_demo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["abhidemo"]  
    collection = db["users"] 
    
    document = {"name" : "abhinav", "age": 21, "id":3}
    result = collection.insert_one(document)
    print(result)


def mongo_insert1_demo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["abhidemo"]  
    collection = db["users"] 
    
    username = input("Enter Username")
    
    document = {"name" : username, "age": 21, "id":3}
    result = collection.insert_one(document)
    print(result)




def main():
    print("Mongo Demo")
    # mongo_insert_demo()
    mongo_insert1_demo()


if __name__ == "__main__":
    main()