import os
import sys
import json
from dotenv import load_dotenv
import pymongo.mongo_client
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from Network_Security.exception.exception import NetworkSecurityError
from Network_Security.mylogging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityError(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityError(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityError(e,sys)

if __name__=='__main__':
    FILE_PATH =r"C:\Users\rajba\OneDrive\Documents\ML_Project_2\Network_Data\Phishing_Legitimate_full.csv"
    DATABASE = "Phishing"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(no_of_records)

        
