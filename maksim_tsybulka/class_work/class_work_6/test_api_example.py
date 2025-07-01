import pytest, requests

def test_main_page():
    urls_and_status = [
        (200, "https://jobs.e-dostavka.by/vacancy/minsk/Ekspeditor_mk/"),
        (200, "https://groshyk.by/"),
        (200, "https://t.me/Emall1Bot"),
        (200, "https://emall.tilda.ws/"),
        (200, "https://hitdiscount.by/"),
        (200, "https://t.me/emall_by"),
        (200, "https://ok.ru/group/68762826309691"),
        (200, "https://play.google.com/store/apps/details?id=by.e_mall"),
        (200, "https://evroopt.by/"),
        (200, "https://www.facebook.com/emallby.discounter"),
        (200, "https://edostavka.by/"),
        (200, "https://www.instagram.com/emall_by/"),
        (200, "https://apps.apple.com/us/app/emall-by/id1603232448"),
        (200, "https://edostavka.by/"),
        (200, "https://vk.com/public210123351"),
        (200, "https://www.tiktok.com/@emall_by"),
        (200, "https://jobs.e-dostavka.by/"),
        (408, "https://emall.by/information/help/132"),
        (408, "https://seller.emall.by/"),

             ]
    for status_code, url_name in urls_and_status:
        response = requests.request("GET", url_name, timeout=3)
        assert response.status_code == status_code, f'Статус код страницы "{url_name}" равен не {status_code} а {response.status_code}'
