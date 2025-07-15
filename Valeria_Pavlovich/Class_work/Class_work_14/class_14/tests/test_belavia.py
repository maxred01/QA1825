from Valeria_Pavlovich.Class_work.Class_work_14.class_14.conftest import api_client
import pytest

def test_product_search(api_client):

    respons = api_client.search_products('ноутбук')


    print(respons)

# class TestClassTests:
#
#     def test_sum(self):
#         assert 2 + 2 == 4
#
#     def test_division(self):
#         assert 10 / 2 == 5
#
#     def test_list(self):
#         words = ['test', 'code', 'pytest']
#
#         assert 'pytest' in words
#
#     @pytest.fixture
#     def student_list():
#         return ('Ann', 'Bob', 'Sid')
#
#     def test_first_student(student_list):
#         assert student_list[0] == 'Ann'
#
# @pytest.mark.parametrize('a, b, expect', [(1, 1, 2),
#                                           (0, 5, 5),
#                                           (-1, 3, 2),
#                                           ])
# def test_sum(a, b, expect):
#     assert a + b == expect