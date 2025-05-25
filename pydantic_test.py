"""
Why to use pydantic? For scale, it makes applying validation and checks on input data and data types from the user with a simple class. 
"""

from pydantic import BaseModel
class Patient(BaseModel): # Define the schema of the data. Now it becomes easy to simply define schemat at one place and use everywhere
    name: str
    age: int

data = {"name": "Devesh", "age": 30}
data2 = {"name": "Dan", "age": "twenty"}

py_object = Patient(**data) # Since data is a dictionary we ahve to pass through kwargs which is equivalent to writing py_object = Patient(name="Devesh", age=30)
print(py_object)
# py_oject2 = Patient(**data2) # This won't work! but pydantic is smart enough, if someone give "30" then it converts it to integer!
# print(py_oject2) 

#------------------------
from pydantic import EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated 
#Note: Once the vars are defined pydantic expect all to exist so if user is not expected to provide allergies list we use Optional to tell what is optional (necessary is by default)
# The default values of optional is kept none if not provided.
class Patient2(BaseModel):
    # name: str  # Annotated to add metadata along with variables
    namename: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    age: int
    weight: float = Field(gt=0) # Can't set value less than one. Using field can also set constraint on string  
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None #can't directly do list since we want to mention the inside of list should contain str! two level validation from importing List from typing
    contact_details: Dict[str, str]
    email: Optional[EmailStr] # This ensures the email is in the right format
    url: Optional[AnyUrl] #Helps to write regex from scratch

patient_info = {'name': 'Devesh', 'age': '30', 'weight': 60.2, 'contact_details': {' email':'abc@gmail.com', 'phone': '2353462' }}
obj3 = Patient2(**patient_info)
print(obj3)

#--------------------------------
# Field validation: @feild validator to create custom logics like value less than greater than, created multiple classes etc... (Pydantic documentation)
# Model validator: To link two fields: example, if age>50 then phone number must exist otherwise fail
# Computed fields: Fields that are not asked form the user but created from the already taken values ex: BMI can be created if we have height and weight
# Nested models: Address contains value: house no 2, sec 66, gurgaon, haryana, 122002' Now addresss contains complex or multiple fields that is city, pin-code, city...
# So it's better to create a nested class of addresss that will break it down and store fields individually
# We can export existing base models of pydantic using serialisatoin to json or dictionary,