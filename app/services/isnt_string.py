def inst_string(name, email):
    obj = {"wrong_fields":[]}
    primitive_types = {
        "int": "integer",
        "dict":"dictonary",
        "list":"list",
        "float":"float",
        "tuple":"tuple"
    }

    if primitive_types.get(type(name).__name__) :
        obj["wrong_fields"].append({"name":primitive_types.get(type(name).__name__)}) 

    if primitive_types.get(type(email).__name__) :
        obj["wrong_fields"].append({"email":primitive_types.get(type(email).__name__)}) 
    
    return obj

