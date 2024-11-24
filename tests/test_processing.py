import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(test_processing_fixture, test_processing_fixture_executed):
    assert filter_by_state(test_processing_fixture) == test_processing_fixture_executed


def test_filter_by_state_canceled(test_processing_fixture, test_processing_fixture_canceled):
    assert filter_by_state(test_processing_fixture, state="CANCELED") == test_processing_fixture_canceled


def test_filter_by_state_without_state(test_processing_fixture_without_state):
    with pytest.raises(ValueError):
        filter_by_state(test_processing_fixture_without_state)


@pytest.mark.parametrize("test_value", [123,
                                        ["state"],
                                        [123456]])
def test_filter_by_state_wrong_type(test_value):
    with pytest.raises(TypeError):
        filter_by_state(test_value)
