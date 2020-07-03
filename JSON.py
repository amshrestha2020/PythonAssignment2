'Find a package in the Python standard library for dealing with JSON.'
'Import the library module and inspect the attributes of the module.'
'Use the help function to learn more about how to use the module.'
'Serialize a dictionary mapping name to your name and age to your age, to a JSON string.'
'Deserialize the JSON back into Python.'

'importing python standard library json package'
import json

person = {}
person["name"] = "Steve Jobs"
person["age"] = 24

def json_dictionary():

    'serialize a dictionary mapping to name and age only'
    print("Person dictionary :", person)

    'serialize a dictionary mapping to name and age to a JSON string'
    json_string = json.dumps(person)
    print("Person dictionary as JSON string :", json_string)

    deserialized_person = json.loads(json_string)
    print("Deserialized from JSON string back into Python:", deserialized_person)

if __name__ == "__main__":
    json_dictionary()