import uuid
from contextlib import contextmanager
from datetime import timedelta
from timeit import default_timer as timer

from acangatu import Storage


@contextmanager
def elapsed_timer(timer_name):
    start = timer()
    yield
    end = timer()
    print(f"{timer_name}: {timedelta(seconds=end - start)}")


def dummy_callback(op, key, data):
    pass


ENTRIES_COUNT = 2_000_000
FILENAME = "storage.json"

st = Storage()
st.add_callback(dummy_callback)

with elapsed_timer(f"time to insert {ENTRIES_COUNT} entries"):
    for i in range(ENTRIES_COUNT):
        st.put(
            str(uuid.uuid4()),
            {"features": ["azs", "internal", "employee", "llmaas"]},
        )

with elapsed_timer("time to dump to disk"):
    st.dump(FILENAME)

with elapsed_timer("time to load from disk"):
    st.load(FILENAME)

with elapsed_timer("time to retrieve entry"):
    _ = st.get("414a671d-63c3-4ce0-a276-d66df52336ea")

with elapsed_timer(f"time to count {ENTRIES_COUNT} entries"):
    st.count()
