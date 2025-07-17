import json


class Storage:
    def __init__(self):
        self.database = {}
        self.callbacks = []

    def put(self, key, data):
        self.database[key] = data
        self._notify("put", key, data)

    def get(self, key):
        return self.database.get(key, None)

    def count(self):
        return len(self.database)

    def load(self, file):
        with open(file) as f:
            self.database = json.load(f)

    def dump(self, file):
        with open(file, "w") as f:
            json.dump(self.database, f)

    def add_callback(self, callback_function):
        self.callbacks.append(callback_function)

    def _notify(self, operation, key, data):
        for cb in self.callbacks:
            cb(operation, key, data)
