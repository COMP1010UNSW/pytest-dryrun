
import pytest


def test_thing_one():
    assert False


@pytest.mark.dryrun
def test_thing_two():
    assert True
