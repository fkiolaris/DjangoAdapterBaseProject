from jsonschema import validate
import json
import jsonschema

# http://sacharya.com/validating-json-using-python-jsonschema/

    # def postMatch(self, json):
    #     schema = {
    #         "type" : "object",
    #         "properties" : {
    #             "createdBy" :  {
    #                 "type" : "object",
    #                 "properties" : {
    #                     "displayName" : {"type" : "string"},
    #                     "type" : {"type" : "string"},
    #                     "id" : {"type" : "string"},
    #                 },
    #                 "required" : ["displayName", "type", "id"]         
    #             },
    #             "name" : {"type" : "string"}       
    #         },
    #         "required" : ["createdBy", "name"] 
    #     }
    
    #     return validation(schema, json)

class Apps:
    
    @staticmethod    
    def addApp(json):
        schema = {
            "type" : "object",
            "properties" : {
                "name" : {"type" : "string"},
                "category" : {"type" : "string"},
                "block" : {"type" : "boolean"}
            },
            "required" : ["name", "category"] 
        }
        return validation(schema, json)

    @staticmethod 
    def editApp(json):
        schema = {
            "type" : "object",
            "properties" : {
                "name" : {"type" : "string"},
                "category" : {"type" : "string"},
                "block" : {"type" : "boolean"}
            }
        }
        return validation(schema, json)    

def validation(schema, json):
    try:
        validate(instance=json, schema=schema)
        return True
    except jsonschema.ValidationError as e:
        print(e.message)
        return e.message
