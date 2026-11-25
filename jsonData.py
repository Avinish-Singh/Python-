import json

cities = {
    "Dehli_popu" : 488,
    "Pune_po" : 566,
    "noida" : 675,
}


with open("cities.json" , "w") as f :
    json.dump(cities,f,indent=4) 



json_str = '{"key" : "value" , "IsTeacher" : true}'

py_obj = json.loads(json_str)
print(py_obj)

dict = {
    "key" : "value",
    "Istacher" : True
}

json_str = json.dumps(dict)
print(json_str)