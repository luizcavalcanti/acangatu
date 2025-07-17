# Acangatu

A Python in-memory key-value proof of concept database

Acangatu (or Akangatu) means "memory" in [Tupi-Guarani](https://en.wikipedia.org/wiki/Tupi%E2%80%93Guarani_languages).

---

## Usage

```python
from acangatu import Storage

st = Storage()

# load from json
st.load("my_storage_file.json")

# Add callbacks to get notified when data changes
def my_callback(operation, key, data):
  do_something_with(data)

st.add_callback(my_callback)

# insert/update data
st.put("my-key", {"my-data": [1, 2, 3]})
# retrieve data
st.get("my-key")
# count records
st.count()

# save data to disk
st.dump("my_new_storage_file.json")
```
