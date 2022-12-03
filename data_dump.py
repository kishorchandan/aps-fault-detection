import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv"

DATABASE_name="aps"
collection_name="sensor" 

if __name__=="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")

    #convert dataframe to json so that we can dump these records in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #INSERT CONVERTED JSON RERCORD TO MONGO DB
    client[DATABASE_name][collection_name].insert_many(json_record)