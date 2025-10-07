import pytest, requests

def test_main_page():
    urls_and_status  = [
        (200, "https://groshyk.by/"),
        (200, "https://t.me/Emall1Bot"),
        (200, "https://play.google.com/store/apps/details?id=by.e_mall"),
        (200, "https://t.me/emall_by"),
        (200, "https://evroopt.by/"),
        (200, "https://edostavka.by/"),
        (200, "https://www.facebook.com/emallby.discounter"),
        (200, "https://edostavka.by/"),
        (200, "https://vk.com/public210123351"),
        (200, "https://hitdiscount.by/"),
        (200, "https://ok.ru/group/68762826309691"),
        (200, "https://www.instagram.com/emall_by/"),
        (200, "https://www.tiktok.com/@emall_by"),
        (408, "https://emall.by/category/4220"),
        (408, "https://emall.by/brands/530"),
        (408, "https://emall.by/brands/2824"),
        (408, "https://emall.by/brands/372"),
        (408, "https://emall.by/brands/36073"),
        (408, "https://emall.by/brands/379"),
        (408, "https://emall.by/brands/24302"),
        (408, "https://emall.by/product/2151379"),
        (404, "https://emall.by/actions/construction-renovation"),
        (408, "https://emall.by/actions/vacation-calling"),


    ]
    for status_code, url_name in urls_and_status:

        response = requests.request("GET", url_name,timeout = 3 )
        assert response.status_code == 200, f'Статус код страницы "{url_name}" равен не {status_code} а {response.status_code}'


