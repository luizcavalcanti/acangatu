import pytest

from acangatu import Storage

def test_plain_initialized_storage_contains_no_data():
    storage = Storage()
    assert 0 == storage.count()
