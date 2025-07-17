import uuid
from acangatu import Storage

storage = Storage()

storage.load("storage.json")

#for i in range(5000):
#    storage.insert(
#        str(uuid.uuid4()),
#        {"features": ["azs", "internal", "employee", "llmaas"]},
#    )


print(storage.count())
print(storage.get("414a671d-63c3-4ce0-a276-d66df52336ea"))
#storage.dump("storage.json")
