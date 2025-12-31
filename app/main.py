from fastapi import FastAPI , HTTPException
import uvicorn
from pydantic import BaseModel, Field
import data_interactor

class Item(BaseModel):
    id : int | None = Field(default=None)
    first_name: str | None = Field(default=None, max_length=50)
    last_name: str | None = Field(default=None, max_length=50)
    phone_number: str | None = Field(default=None, max_length=50)
    

app = FastAPI()

qury = data_interactor.Dataservice()#Creating a database connection

@app.get('/contacts')
def get_all_contacts():
    try:
        return qury.get_all_contacts()
    except Exception as e:
            raise HTTPException(status_code= 500, detail=str(e))   


@app.post('/contacts')
def post_contacts(item: Item):
    # try:
        data = data_interactor.Contact()
        dict_data = data.convert_item_to_dict(item)
        print(dict_data) #Converts the object to a dict
        result = qury.create_contact(dict_data) #return id
        return {'message': 'Contact creation successful', "id": result}
    # except Exception as e:
    #         raise HTTPException(status_code=500, detail=str(e))  


@app.put('/contacts/{id}')
def contact_update(item: Item, id: str):
    try:
        data = data_interactor.Contact()
        dict_data = data.convert_item_to_dict(item) #Converts the object to a dict 
        print(qury.update_contact(id, dict_data))
        if qury.update_contact(id, dict_data):
            return {'message': 'Contact update successful.'}
        return {'message':'Contact person update failed.'}
    except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))

@app.delete('/contacts/{id}')
def delete_contact(id: str):
    try:
        qury.delete_contact(id)
        return {'massege': 'Contact deletion successful'}
    except Exception as e:
         raise HTTPException(status_code=404, detail=str(e))    


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000,reload=True)
