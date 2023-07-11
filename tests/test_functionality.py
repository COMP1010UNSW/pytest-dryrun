from pytest import Pytester


def test_dryrun_flag_skips_unmarked(pytester: Pytester):
    pytester.makepyfile(
        """
        def test_not_dryrun():
            assert False
        """
    )

    result = pytester.runpytest('--dryrun')
    # No tests passed or failed
    result.assert_outcomes()


def test_dryrun_flag_runs_marked(pytester: Pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.dryrun
        def test_not_dryrun():
            assert True
        """
    )

    result = pytester.runpytest('--dryrun')
    # No tests passed or failed
    result.assert_outcomes(passed=1)


def test_no_dryrun_flag_skips_marked(pytester: Pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.dryrun
        def test_not_dryrun():
            assert False
        """
    )

    result = pytester.runpytest('--no-dryrun')
    # No tests passed or failed
    result.assert_outcomes()


def test_no_dryrun_flag_runs_unmarked(pytester: Pytester):
    pytester.makepyfile(
        """
        def test_not_dryrun():
            assert True
        """
    )

    result = pytester.runpytest('--no-dryrun')
    # No tests passed or failed
    result.assert_outcomes(passed=1)


def test_dryrun_no_dryrun_mutually_exclusive(pytester: Pytester):
    pytester.makepyfile(
        """
        def test_example():
            assert True
        """
    )

    # Need to run in a subprocess or Pytest kinda freaks out
    result = pytester.runpytest_subprocess("--dryrun", "--no-dryrun")

    # Status code 4 -> command line usage error
    # https://docs.pytest.org/en/7.1.x/reference/exit-codes.html
    assert result.ret == 4
