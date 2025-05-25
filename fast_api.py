from fastapi import FastAPI, HTTPException, Path, Query
import pandas as pd
app = FastAPI()

def fetch_data():
    return {"p1": {"age": 55, "disease": "no"}, "p2": {"age":56, "disease": "yes"}}

@app.get("/") # Creating an end point through route
def hello():
    return {"message": "Hello World"} # We are returning a json file.

@app.get("/about") # This is a second end point below which we can define our funciotn
def about():
    return {"About section": "Be carful"}

@app.get("/view") # In view if we want to filter the data based on some categories! we use path parameters.
def view_data():
    data = fetch_data()
    return data

@app.get("/patient/{patient_id}") # THis is Path parameter, that is dynamic based on client input
def get_patient_data(patient_id): # We can also put Path parameter to clarify client what to put in patient_id
    data = fetch_data()
    if patient_id in data.keys():
        return data[patient_id] # This will return 200 OK
    # return {"message": "error"} # Static way to show error
    raise HTTPException(status_code=404, detail="Patient not found") # This will raise error

# Query parameter to sort the given data based on certain parameters like filter, sort, search, pagination. After '?', we use key: value pair
@app.get("/sort") # 8000/sort?disease=yes&age=50
def sort_patients(disease: str = Query(..., description = "sort on the basis of disease"), #Note ... means must exist
                                  age: int = Query(None, description = "sort based on age")):
    data = fetch_data()
    filtered_data = {}
    # if (disease=="yes" or disease == "no") and isinstance(age, int):
    if (disease=="yes" or disease == "no"):
        print("Inside function")
        for patient_id, patient_data in data.items():
            if patient_data["disease"] == disease:
                filtered_data[patient_id] = patient_data
    return filtered_data



#http://127.0.0.1:8000/docs This is fastAPI feature that automatically creates documentation. We don't even use Postaman app