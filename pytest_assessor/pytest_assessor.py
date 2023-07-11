"""
# Pytest Assessor Plugin

Provides Pytest markers to facilitate auto-marking using Pytest.
"""
import pytest


def pytest_addoption(parser: pytest.Parser):
    """
    Add --dryrun and --no-dryrun options
    """
    parser.addoption(
        "--dryrun",
        action="store_true",
        help="Only run tests that have the dryrun mark",
    )
    parser.addoption(
        "--no-dryrun",
        action="store_true",
        help="Only run tests that don't have the dryrun mark",
    )


def pytest_collection_modifyitems(
    session: pytest.Session,
    config: pytest.Config,
    items: list[pytest.Item],
) -> None:
    """
    Filter out tests to implement --dryrun and --no-dryrun
    behaviour.
    """
    remove_non_dryrun = config.getoption('--dryrun')
    remove_dryrun = config.getoption('--no-dryrun')
    new_items = []
    for item in items:
        if item.get_closest_marker('dryrun') is None:
            if not remove_non_dryrun:
                new_items.append(item)
        else:
            if not remove_dryrun:
                new_items.append(item)

    # Overwrite the old items array
    # https://stackoverflow.com/a/8037476/6335363
    items[:] = new_items
