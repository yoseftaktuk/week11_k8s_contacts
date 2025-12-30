from pymongo import MongoClient


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
        self.client = MongoClient(
            host='localhost',
            port=27017,
            username='user',
            password='pass',
            authSource='admin'
        )
        self.db = self.client['contacts_db']
        self.collection = self.db['contacts']
    def ger_all_contacts(self):
            