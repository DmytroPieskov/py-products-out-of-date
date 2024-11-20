import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products():
    with patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = datetime.date(2024, 2, 2)
        mocked_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2024, 2, 10), "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2024, 2, 5), "price": 120},
            {"name": "duck", "expiration_date": datetime.date(2024, 2, 1), "price": 160}
        ]
        assert outdated_products(products) == ['duck']

def test_no_outdated_products():
    with patch('datetime.date') as mocked_date:
        mocked_date.today.return_value = datetime.date(2024, 2, 2)
        mocked_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2024, 2, 10), "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2024, 2, 5), "price": 120}
        ]
        assert outdated_products(products) == []

# def test_all_outdated_products():
#     with patch('datetime.date') as mocked_date:
#         mocked_date.today.return_value = datetime.date(2024, 2, 2)
#         mocked_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)
#
#         products = [
#             {"name": "salmon", "expiration_date": datetime.date(2024, 1, 10), "price": 600},
#             {"name": "chicken", "expiration_date": datetime.date(2024, 1, 5), "price": 120}
#         ]
#         assert outdated_products(products) == ['salmon', 'chicken']
