from pymongo import MongoClient
import pandas as pd
from sentiment_analysis import sentiment_text
from text_regulation import get_clean_text, preprocess_tweet

def connect_mongodb(database, collection):
    client = MongoClient('mongodb+srv://petyu:14BoLd69@cluster1.dts9z.mongodb.net/test')
    db = client[database]
    coll = db[collection]
    return coll


def insert_excel_data_to_mongodb(collection, data):
    records = data.to_dict("records")
    collection.insert_many(records)
    print(f"Inserted {len(records)} records from the Excel file")


def read_excel(file_path, sheet_name=0):
    return pd.read_excel(file_path, sheet_name=sheet_name)


def get_data_from_mongodb(collection, query=None):
    if query is None:
        query = {}
    results = collection.find(query)
    return pd.DataFrame(list(results))


database = "twitter_data"
collection_name = "tweet"

file_name = 'apple.xlsx'

data = get_clean_text(preprocess_tweet(file_name))

summary = sentiment_text(data)

# Connect to MongoDB
collection = connect_mongodb(database, collection_name)

# Insert data into MongoDB
insert_excel_data_to_mongodb(collection, summary)

# Get data from MongoDB
retrieved_data = get_data_from_mongodb(collection)
print("Data retrieved from MongoDB:")
print(retrieved_data)
