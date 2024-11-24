import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
                                                   ("5742123489604342", "5742 12** **** 4342"),
                                                   ("4200212289601234", "4200 21** **** 1234")])
def test_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("card_number", [("123"),
                                         (""),
                                         ("11112222333344445555")])
def test_invalid_card_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_wrong_type_card_number():
    with pytest.raises(TypeError):
        get_mask_card_number(123)