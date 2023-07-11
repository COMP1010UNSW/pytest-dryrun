# Pytest Assessor Plugin

A Pytest plugin to facilitate auto-marking using Pytest.

## Provided markers

### Dryrun

When the `--assessor-dryrun` flag is passed to Pytest, only tests marked with
`dryrun` will be collected and run.

If the `--assessor-no-dryrun` flag is given, only tests not marked with `dryrun`
will be collected.

```py
@pytest.mark.dryrun
def test_thing_one():
    """This test will be run, even during dryruns"""
    box = get_box()
    assert "thing one" in box

def test_thing_two():
    """This test will not by run if the `--dryrun` flag is given to Pytest"""
    box = get_box()
    assert "thing two" in box
```

### Weighting

Weightings can be assigned to individual tests. When a test session completes,
an overall mark is printed.

```py
@pytest.mark.weighting(3)
def test_thing_three():
    """This test is worth three points"""
    box = get_box()
    assert "thing three" not in box
```

If a test is parametrized, the marks are distributed evenly between each test
case.

```py
@pytest.mark.weighting(5)
@pytest.mark.parametrize(
    'number',
    # Generate 10 test cases
    [i for i in range(3, 13)],
)
def test_thing_three(number):
    """
    Each test case will be worth 0.5 points, since the 5 total marks are evenly
    distributed between each test.
    """
    box = get_box()
    num_str = number_to_string(number)
    assert f"thing {num_str}" not in box
```
