import pytest, requests

def test_main_page():
    urls_and_status = [
        (200, "https://t.me/belavia_official"),
        (200, "https://t.me/belaviabot"),
        (200, "https://belavia.by/novosti/"),
        (200, "https://belavia.by/table/"),
        (200, "https://belavia.by/obrashheniya-grazhdan/"),
        (200, "https://belavia.by/novosti/4890988/"),
        (200, "https://belavia.by/perevozka-gruzov/"),
        (200, "https://belavia.by/kategorii-passazhirov/"),
        (200, "https://belavia.by/bagazh/"),
        (200, "https://hotels.belavia.by/?utm_content=main_banner_march25"),]
    for status_code, url_name in urls_and_status:
        response = requests.request("GET", url_name, timeout=3)
        assert response.status_code == status_code, f'Status code of {url_name} is not {status_code}, but {response.status_code}'

# (200,"https://t.me/belavia_official"),
# (200,"https://t.me/belaviabot"),
# (200,"https://belavia.by/novosti/"),
# (200,"https://belavia.by/table/"),
# (200,"https://belavia.by/obrashheniya-grazhdan/"),
# (200,"https://belavia.by/novosti/4890988/"),
# (200,"https://belavia.by/perevozka-gruzov/"),
# (200,"https://belavia.by/kategorii-passazhirov/"),
# (200,"https://belavia.by/bagazh/"),
# (200,"https://hotels.belavia.by/?utm_content=main_banner_march25"),
# (200,"https://www.instagram.com/belavia.airlines/"),
# (200,"https://www.mintrans.gov.by/ru/pervyj-god-pyatiletki-kachestva-god-blagoustrojstva-strany"),
# (200,"https://leader.belavia.by/loyalty/frame/registration/"),
# (200,"https://vk.com/belavia_airlines"),
# (200,"https://belavia.by/"),
# (200,"https://belavia.by/#ibe"),
# (200,"https://belavia.by/#hotel"),
# (200,"https://belavia.by/#wci"),
# (200,"https://belavia.by/#trip-case"),
# (200,"https://belavia.by/#"),
# (200,"https://belavia.by/#transfer"),
# (200,"https://belavia.by/predlozheniya/"),
# (200,"https://belavia.by/kontakty/"),
# (404,"https://www.youtube.com/user/OfficialBelavia"),
# (408,"https://belavia.by/"),
# (408,"https://belavia.by/kontakty/"),
# (408,"https://belavia.by/predlozheniya/"),
# (408,"https://belavia.by/bilety-po-beznalichnomu-raschetu/")
# (408,"https://belavia.by/reserve/"),
# (408,"https://belavia.by/izmenenie-biletov-cherez-internet/"),
# (408,"https://belavia.by/vozvrat-bileta/"),
# (408,"https://belavia.by/spravka-o-polete/"),
# (300,"https://belavia.by/redirect.php?OriginLocation=MSQ&DestinationLocation=BAK&JourneySpan=Rt&lang=ru"),
# (300,"https://belavia.by/account"),
# (300,"https://belavia.by/redirect.php?OriginLocation=MSQ&DestinationLocation=TAS&lang=ru&Adults=1&Children=0&Infants=0"),
# (300,"http://www.facebook.com/belavia"),
# (300,"https://belavia.by/account"),
#      "
# 300,"http://twitter.com/Belavia_by",""
# 300,"https://wa.me/18782060106",""
# 300,"https://belavia.by/time-table/","Р Р°СЃРїРёСЃР°РЅРёРµ"
