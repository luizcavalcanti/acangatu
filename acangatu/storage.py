import json
import time

from collections.abc import Callable
from dataclasses import dataclass, is_dataclass, asdict
from typing import Any

@dataclass
class Entry:
    data: Any
    ttl: int
    last_hit: int


class DataclassEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


class Storage:
    def __init__(self):
        self.database: dict[str, Entry] = {}
        self.callbacks: list[Callable[[str, Any, Any], None]] = []

    def put(self, key: Any, data: Any, ttl=0) -> None:
        e = Entry(data, ttl, Storage._current_time())
        self.database[key] = e
        self._notify("put", key, data)

    def get(self, key: Any) -> Any:
        entry = self.database.get(key, None)
        data = None
        if entry:
            data = entry.data
            self._notify_expiration(key, entry)
        return data

    def delete(self, key: Any) -> None:
        self.database.pop(key, None)

    def count(self) -> int:
        return len(self.database)

    def load(self, file: str) -> None:
        with open(file) as f:
            self.database = json.load(f)

    def dump(self, file: str) -> None:
        with open(file, "w") as f:
            json.dump(self.database, f, cls=DataclassEncoder)

    def add_callback(self, callback: Callable[[str, Any, Any], None]) -> None:
        self.callbacks.append(callback)

    def _notify(self, operation: str, key: Any, data: Any) -> None:
        for cb in self.callbacks:
            cb(operation, key, data)

    def _notify_expiration(self, key, entry: Entry):
        if entry.ttl > 0 and entry.ttl + entry.last_hit > Storage._current_time():
            self._notify("expiration", key, entry.data)

    @staticmethod
    def _current_time():
        return round(time.time() * 1000)
