from pymongo import MongoClient
from fastapi import HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId



class Valid:   
    @staticmethod    
    def check_to_post(item: dict):#בודק האם יש את כל הפרמטרים ליצירת איש קשר חדש
        if item['firt_name'] and item['last_name'] and item['phone_number']:
            return True
        return False


load_dotenv()
class Contact:
    def __init__(self, contact_info: object=None):
        if contact_info:    
            data = self.convert_to_dict(contact_info)
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.phone_number = data['phone_number']

    def convert_to_dict(self,contact):
        return {

                "id": str(contact["_id"]),
                "first_name": contact["first_name"],
                "last_name": contact["last_name"],
                "phone_number": contact["phone_number"]

            }
    def convert_item_to_dict(self, contect):
        return {'first_name': contect.first_name,
                'last_name': contect.last_name,
                'phone_number': contect.phone_number
                }
  
class Dataservice:
    def __init__(self):
        try:  
            self.client = MongoClient(
                host = os.getenv("MONGO_HOST"),
                port = int(os.getenv("MONGO_PORT"))#Establishes the connection to a data server
            )
            self.db = self.client['contactsdb']
            self.collection = self.db['contacts']
        except  Exception as e:
            raise HTTPException(status_code=500, detail=str(e))   
         
    def get_all_contacts(self):#Returns a list of all contacts.
        contacts_list = []
        cursor = self.collection.find()
        for doc in cursor:
            contect = Contact(doc)
            contacts_list.append(contect)
        return contacts_list

    def create_contact(self, contact_data: dict):#Creates a new contact
        if Valid.check_to_post(dict): #Checks that all required fields are present.   
            self.collection.insert_one(contact_data)
            document = self.collection.find_one(contact_data)#Returns all contacts with their id
            return str(document['_id'])
        return False

    def update_contact(self, id: str, contact_data: dict):
        for key, value in contact_data.items(): #A loop that goes through all keys and sends a query to update the contact person
            if not key or not value: 
                continue
            result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {key: value}})
            if result.matched_count == 1:#Checks that an update has been made.
                continue
            return False
        return True


    def delete_contact(self, id: str):
        result = self.collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:#Checks that a deletion has been made.
            return True
        return False

        
    
            
