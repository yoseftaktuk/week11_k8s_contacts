from pymongo import MongoClient
from fastapi import HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

class Item(BaseModel):
    id : int | None = Field(default=None)
    first_name: str | None = Field(default=None, max_length=50)
    last_name: str | None = Field(default=None, max_length=50)
    phone_number: str | None = Field(default=None, max_length=50)

class Valid:   
    @staticmethod    
    def check_to_post(item: dict):#בודק האם יש את כל הפרמטרים ליצירת איש קשר חדש
        if item['firt_name'] and item['last_name'] and item['phone_number']:
            return True
        return False


load_dotenv()
class Contact:
    def __init__(self, contact_info: object):
        self.id = contact_info.id
        self.first_name = contact_info.first_name
        self.last_name = contact_info.last_name
        self.phone_number = contact_info.phone_number

    def convert_to_dict(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name, 
                "phone_number": self.phone_number}
    
class Dataservice:
    def __init__(self):
        try:  
            self.client = MongoClient('mongodb://localhost:27017/')  
            # self.client = MongoClient(
            #     MONGO_HOST = os.getenv("MONGO_HOST", "localhost"),
            #     MONGO_PORT = os.getenv("MONGO_PORT", "27017"),
            #     MONGO_DB = os.getenv("MONGO_DB", "contactsdb")
            # )
            self.db = self.client['contactsdb']
            self.collection = self.db['contacts']
        except  Exception as e:
            raise HTTPException(status_code=500, detail=str(e))    
    def get_all_contacts(self):
        contacts_list = []
        cursor = self.collection.find()
        print(cursor)
        for doc in cursor:
            contacts_list.append(doc)
        return contacts_list

    def create_contact(self, contact_data: dict):
        if Valid.check_to_post(dict):    
            result = self.collection.insert_one(contact_data)
            document = self.collection.find_one(contact_data)
            return str(document['_id'])
        return False

    def update_contact(self, id: str, contact_data: dict):
        try:    
            for key, value in contact_data.items():
                self.collection.update_one({"_id": ObjectId(id)}, {"$set": {key: value}})
            return True
        except:
            return False
         

    def delete_contact(self, id: str):
        result = self.collection.delete_one({'_id': ObjectId(id)})
        result.deleted_count
        if result.deleted_count == 1:
            return True
        return False

        
    
            

a = Dataservice()
# print(a.create_contact({

# "first_name": "John",

# "last_name": "Doe",

# "phone_number": "050-1234567"
# })) 
a.update_contact('69541e751a8b65f667eb487d',{"fist_name": "Johnnnn"})
# print(a.get_all_contacts())
# print(a.delete_contact('69541d0ccbbc776cd7377e20'))