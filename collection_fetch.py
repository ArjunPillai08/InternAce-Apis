from db_auth import connect_to_db
import json 
from bson import json_util

collection = connect_to_db()
all_instances = list(collection.find({}))
new_list = list()
#print(all_instances)#
counter = 0
for i in all_instances:
    dictionary = all_instances[counter]
    dictionary.pop("_id", None)
    print(dictionary)
    print("")
    new_list.append(dictionary)
    counter += 1
print(len(new_list))

"""for instance in all_instances:
    print(instance)"""