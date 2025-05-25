# HTTPS
1. Static Softwares: No interaction from user -> Just show an end-point with no interactions
2. Dynamic Softwares -> Example, Sheets: Users can only do 4 types of interaction CRUD -> Create, Retrieve, Update, Delete

Websites: They are installed on different machine and used on different machine, hence they are different from software.
Server -> Host; Client -> Where the user interacts. The interaction b/w server and client is done through HTTP protocols.
1.  CREATE -> HTTP: POST
2.  RETRIVE -> HTTP: GET
3.  UPDATE -> HTTP: PUT
4.  Delete -> HTTP: DELETE

All these words, POST, GET, PUT, DELETE are combinedly called **HTTP methods**.

# Pydantic for data validation
- Python has dynamic variable: you can assign any value: str, int, float and the variable will assign the type afterward where in static variable, once the variable is defined as str, it can't take int values to it
- We can explicitly use isinstance or define simple logic to ensure right data type, but to deal with large code, we can't do that everytime so pydantic solves the problem for scale. If data doesn't meet the right format, it returns the validationError
- 
