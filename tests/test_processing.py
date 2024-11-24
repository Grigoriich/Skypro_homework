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


def test_sort_by_date_increase(test_processing_fixture, test_processing_fixture_increase_date):
    assert sort_by_date(test_processing_fixture) == test_processing_fixture_increase_date


def test_sort_by_date_decrease(test_processing_fixture, test_processing_fixture_decrease_date):
    assert sort_by_date(test_processing_fixture, increase=False) == test_processing_fixture_decrease_date


def test_sort_by_date_without_date(test_processing_fixture_without_date):
    with pytest.raises(ValueError):
        sort_by_date(test_processing_fixture_without_date)


@pytest.mark.parametrize("test_value", [123,
                                        ["state"],
                                        [123456]])
def test_sort_by_date_wrong_type(test_value):
    with pytest.raises(TypeError):
        sort_by_date(test_value)