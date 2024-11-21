from dbmod import insert_demo
from dbmod import read_demo

def main():
    print("Mongo Demo")
    # insert_demo.mongo_insert_demo()
    # insert_demo.mongo_insert1_demo()
    list = read_demo.read_all_user()
    
    for item in list:
        print(item)


if __name__ == "__main__":
    main()