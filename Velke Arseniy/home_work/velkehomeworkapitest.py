import requests
import pytest

def test_main_page():
    urls = [
        ('https://www.harrypotter.com/', 'harrypotter main page'),
        ('https://www.harrypotter.com/login', 'harrypotter login'),
        ('https://www.harrypotter.com/register', 'harrypotter register'),
        ('https://www.harrypotter.com/news', 'harrypotter news'),
        ('https://www.harrypotter.com/features', 'harrypotter features'),
        ('https://www.harrypotter.com/quiz', 'harrypotter quiz'),
        ('https://www.harrypotter.com/collections/potter-puzzles', 'harrypotter puzzles'),
        ('https://www.harrypotter.com/writing-by-jk-rowling', 'harrypotter rowling archive'),
        ('https://www.harrypotter.com/discover/books', 'harrypotter discover books'),
        ('https://www.harrypotter.com/discover/films', 'harrypotter discover films'),
        ('https://www.harrypotter.com/discover-portkey-games', 'harrypotter discover portkey games'),
        ('https://www.harrypotter.com/discover-on-stage', 'harrypotter discover on stge')
    ]



    for url_link, url_name in urls:
        response = requests.request ("GET", url_link)
        assert response.status_code == 200, f'Status code of {url_name} is not 200, but {response.status_code}'