import json


class Storage:
    def __init__(self):
        self.database = {}

    def insert(self, key, data):
        self.database[key] = data
        self._notify("insert", key, data)

    def get(self, key):
        return self.database.get(key, None)

    def count(self):
        return len(self.database)

    def recover(self, file):
        with open(file) as f:
            self.database = json.load(f)

    def dump(self, file):
        with open(file, "w") as f:
            json.dump(self.database, f)

    def _notify(self, operation, key, data):
        print(f"enqueue >> {operation} on {key} ({data})")
