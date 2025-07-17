import pytest

from acangatu import Storage


def test_just_initialized_storage_contains_no_data():
    st = Storage()
    assert 0 == st.count()


def test_data_insertion_and_retrieval():
    st = Storage()

    st.put("key-1", 3)
    st.put("key-2", "test")

    assert 2 == st.count()
    assert 3 == st.get("key-1")
    assert "test" == st.get("key-2")


def test_data_deletion():
    st = Storage()

    st.put("key-1", 3)
    st.put("key-2", "test")

    assert 2 == st.count()
    assert 3 == st.get("key-1")
    assert "test" == st.get("key-2")

    st.delete("key-2")

    assert 1 == st.count()
    assert 3 == st.get("key-1")
    assert not st.get("key-2")


def test_callbacks_get_called_when_data_is_put():
    st = Storage()

    calls_cb1 = []
    calls_cb2 = []

    def cb1(op, key, data):
        calls_cb1.append((op, key, data))

    def cb2(op, key, data):
        calls_cb2.append((op, key, data))

    st.add_callback(cb1)
    st.put("key1", "data")

    st.add_callback(cb2)
    st.put("key2", "other-data")
    st.put("key1", "new-data")

    assert 3 == len(calls_cb1)
    assert ("put", "key1", "data") == calls_cb1[0]
    assert ("put", "key2", "other-data") == calls_cb1[1]
    assert ("put", "key1", "new-data") == calls_cb1[2]

    assert 2 == len(calls_cb2)
    assert ("put", "key2", "other-data") == calls_cb2[0]
    assert ("put", "key1", "new-data") == calls_cb2[1]


# TODO: test dump and load
