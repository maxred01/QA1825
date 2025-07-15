import pytest, requests

def test_api_status():
    urls_and_status = [
        (200, "https://you.regettingold.com/privacy.php"),
        (200, "https://you.regettingold.com/press.php"),
        (200, "https://www.cookiesandyou.com/"),
        (200, "https://you.regettingold.com/press.php"),
        (200, "https://you.regettingold.com/ad.php"),
        (200, "https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fyou.regettingold.com%2F"),
        (451, "http://www.everyothershot.com/"),
        (200,
         "http://www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fyou.regettingold.com%2F&title=You%27re+getting+old%21&summary=How+old+are+you+getting%3F+Let+us+explain+it+properly%21"),
        (200,
         "https://pinterest.com/pin/create/button/?url=http%3A%2F%2Fyou.regettingold.com%2F&media=http://you.regettingold.com/media/ygo.png&description=You%27re+getting+old%21"),
        (400, "https://twitter.com/@urgettinold"),
        (400,
         "https://twitter.com/home?status=You%27re+getting+old%21%20http%3A%2F%2Fyou.regettingold.com%2F%20%23youregettingold%20@urgettinold"),
        (200, "https://plus.google.com/share?url=You%27re+getting+old%21%20http%3A%2F%2Fyou.regettingold.com%2F"),
        (200, "http://www.reddit.com/submit?url=http%3A%2F%2Fyou.regettingold.com%2F"),
        (200, "https://tumblr.com/share?s=&v=3&t=You%27re+getting+old%21&u=http%3A%2F%2Fyou.regettingold.com%2F"),

    ]
    for status_code, url_name in urls_and_status:
        response = requests.request("GET", url_name, timeout=3)
        assert response.status_code == status_code, f'Статус код страницы "{url_name}" равен не {status_code} а {response.status_code}'



