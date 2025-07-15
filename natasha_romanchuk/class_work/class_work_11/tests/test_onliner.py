from natasha_romanchuk.class_work.class_work_11.conftest import api_client
import pytest

@pytest.mark.parametrize('query, min_results',[
    ('ноутбук',10),
    ('телевизор',4),
     ('смартфон',15),
                                                     ])
def test_product_search(api_client, query, min_results):

    respons = api_client.search_products(query)
    assert 'products' in respons
    assert isinstance(respons['products'], list)
    assert isinstance(respons, dict)
    assert len(respons['products'] [0]) >= min_results

    print(respons)



def test_сложение():
    assert 2 + 2 == 4  # Утверждение (проверяемое). Будет падать, если условие ложное


def test_деление():
    assert 10/2 == 5


def test_список():
    слова = ['тест', 'код', 'pytest']

    assert 'pytest' in слова


# Фикстура - шаблон для проверок   (как гост), шаблон в действиях/ не начинается со лова test

@pytest.fixture
def список_студентов():
    return ['Аня','Борис', 'Виктор']    # шаблон


def test_первый_студент(список_студентов):
    assert список_студентов[0] == 'Аня'       # сам тест


@pytest.mark.parametrize('a, b, ожидание', [(1 ,1 ,2 ),     # для создания большого количества комбинаций
                                            (0 ,5 ,5 ),
                                            (-1 ,3 ,2 ),
                                            ])
def test_сложение(a, b, ожидание):
    assert a + b == ожидание


