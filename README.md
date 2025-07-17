# Acangatu

A Python in-memory key-value database proof of concept package

Acangatu (or Akangatu) means "Memory" in Tupi-Guarani, a South American indigenous language.

---

## Usage

```python
from acangatu import Storage

st = Storage()

# load from json
st.load("my_storage_file.json")

# insert/update data
st.put("my-key", {"my-data": [1, 2, 3]})

# retrieve data
st.get("my-key")

# count records
st.count()

# save data to disk
st.dump("my_new_storage_file.json")
```
