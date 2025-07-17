import json
from collections.abc import Callable


class Storage:
    def __init__(self):
        self.database = {}
        self.callbacks = []

    def put(self, key: any, data: any) -> any:
        self.database[key] = data
        self._notify("put", key, data)

    def get(self, key: any) -> any:
        return self.database.get(key, None)

    def count(self) -> int:
        return len(self.database)

    def load(self, file: str) -> None:
        with open(file) as f:
            self.database = json.load(f)

    def dump(self, file: str) -> None:
        with open(file, "w") as f:
            json.dump(self.database, f)

    def add_callback(self, callback: Callable[[str, any, any], None]) -> None:
        self.callbacks.append(callback)

    def _notify(self, operation: str, key: any, data: any) -> None:
        for cb in self.callbacks:
            cb(operation, key, data)
