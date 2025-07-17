import pytest

from acangatu import Storage


def test_just_initialized_storage_contains_no_data():
    st = Storage()
    assert 0 == st.count()


def test_data_insertion_and_retrieval():
    st = Storage()
    assert 0 == st.count()

    st.insert("key-1", 3)
    st.insert("key-2", "test")

    assert 2 == st.count()
    assert 3 == st.get("key-1")
    assert "test" == st.get("key-2")


# TODO: test dump and load
