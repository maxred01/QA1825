import requests
import time


def test_run_api_tests() -> str:
    """Запускает тесты и возвращает результаты в виде строки"""
    urls = [
        ("https://www.spacex.com/vehicles/falcon-9/", "главная страница spacex"),
        ("https://www.spacex.com/vehicles/starship/", "spacex_starship"),
        ("https://www.spacex.com/vehicles/falcon-heavy/", "spacex_falcon-heavy"),
        ("https://shop.spacex.com/cart", "spacex cart"),
        ("https://www.spacex.com/supplier/", "supplier"),
        ("https://shop.spacex.com/collections/all", "shop spacex" ),
        ("https://www.spacex.com/humanspaceflight/", "spacex_human spaceflight" ),
        ("https://shop.spacex.com/products/unisex-spacex-zipper-hoodi", "просмотр товара" ),
        ("https://shop.spacex.com/cart/change", 'удаление товара из корзины'),
        ("https://shop.spacex.com/cart/add", 'добавление товара в корзину POST')
        ("https://api.hcaptcha.com/checksiteconfig", 'страница регистрации сайта POST'),
        ("https://otlp-http-production.shopifysvc.com/v1/metrics", 'регистрация на сайте POST')

    ]


    results = []
    passed_count = 0
    failed_count = 0

    for url, name in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            response_time = round((time.time() - start_time) * 1000)
            status = response.status_code

            if status == 200:
                result = f"✅ {name} ({url}) - Успешно! Статус: {status}, Время: {response_time}мс"
                passed_count += 1
            else:
                result = f"❌ {name} ({url}) - Ошибка! Статус: {status} (ожидался 200), Время: {response_time}мс"
                failed_count += 1

        except Exception as e:
            result = f"⚠️ {name} ({url}) - Критическая ошибка: {str(e)}"
            failed_count += 1

        results.append(result)

    # Итоговая статистика
    total_tests = len(urls)
    success_rate = round(passed_count / total_tests * 100) if total_tests else 0

    summary = (
        f"\n\n📊 ИТОГИ ТЕСТИРОВАНИЯ:\n"
        f"✅ Успешных тестов: {passed_count}\n"
        f"❌ Проваленных тестов: {failed_count}\n"
        f"🔢 Всего тестов: {total_tests}\n"
        f"🏁 Процент успеха: {success_rate}%"
    )

    return "\n".join(results) + summary





#  Проверки POST

import requests

url = "https://shop.spacex.com/cart/add"

payload = {'form_type': 'product',
'utf8': '✓',
'option-0': 'Black',
'id': '42221541064783',
'quantity': '1',
'email': '',
'selected_variant_id': '42221541064783',
'product-id': '7613343137871',
'section-id': 'product-template'}
files=[

]
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'origin': 'https://shop.spacex.com',
  'priority': 'u=0, i',
  'referer': 'https://shop.spacex.com/collections/women-outerwear/products/unisex-spacex-sweatshirt',
  'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'Cookie': 'localization=US; cart_currency=USD; _shopify_y=383D31A3-155b-4C5B-8940-f22b4bcd2072; _tracking_consent=3.AMPS_BYHM_f_f_KXF2JnoSTyu-JygdTJZRAA; _orig_referrer=https%3A%2F%2Fwww.spacex.com%2F; _landing_page=%2F; cart=Z2NwLXVzLWVhc3QxOjAxSlhaR0E5VlY0WFlaWjE3WEg1Tkg3Q1pT%3Fkey%3D9dfae736a876f8b84b6f5ae898cb49d4; _hc_cart=1897377787; cart_sig=e5e1bd2239ece91fa6088c27773f9c94; _shopify_essential=:AZd_JSTfAAEA6Nf4xWrq2w8T2dW-2cpUDZo81abIBrqMs9HiwP_66QJYBJzKQZNhK-eLveUOJUMdCM29G_Kbp0201teW7nnyR7mnBYP_4osiMecL:; _hc_exp={*_cr*!1750771432519}; shopify_pay_redirect=pending; _shopify_s=75f820da-6f3e-4391-b729-63b146c55a76; keep_alive=eyJ2IjoyLCJ0cyI6MTc1MDc4Nzg5ODQxNSwiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjoyNCwiY2EiOjAsImthIjowLCJzYSI6MTIsInRhIjowLCJrYmEiOjAsInQiOjUsIm5tIjoxLCJtcyI6MC4zOCwibWoiOjAuMDIsIm1zcCI6MC4wMiwidmMiOjAsImNwIjowLCJyYyI6MCwia2oiOjAsImtpIjowLCJzcyI6MC41NSwic2oiOjAuNTIsInNzbSI6MSwic3AiOjEsInRzIjowLCJ0aiI6MCwidHAiOjAsInRzbSI6MH0sInNlcyI6eyJwIjozLCJzIjoxNzUwNzcxNDMwNDM5LCJkIjoxNjQyNH19; _hc_vid={*id*!*b2462bda-ab50-42a2-b78b-8cce44c7d84d*~*created*!1750182731767~*psq*!27~*ord*!81~*cl*!30~*gbl*!0}; _hc_ses={*id*!*6348195a-bf68-4982-8d87-b500caf93848*~*created*!1750786799414~*isNew*!false~*psq*!9~*ord*!26~*cl*!9~*ser*!false~*attr*![*(direct)*~*direct*~*(not+set)*~*(not+set)*~*(none)*~*(direct)*]~*ap*!*account*}; _landing_page=%2Fcollections%2Fall; _orig_referrer=https%3A%2F%2Fshop.spacex.com%2Fcart; _shopify_s=75f820da-6f3e-4391-b729-63b146c55a76; _shopify_y=383D31A3-155b-4C5B-8940-f22b4bcd2072; _tracking_consent=3.AMPS_USVA_f_f_KXF2JnoSTyu-JygdTJZRAA; _shopify_essential=%3AAZd_JSTfAAEAD4fs6fg5PmDlnSIj9jfK3d-DSH3nwYzpdcibtCpF6XIrzxYBfCUcXQr6zzvzOV6Y_WGbwynUPgPt3vkoyszFwFvt2Utbp4AxTYEwxUJUZKPYytF2HkjKiCweDEBLTg%3A; cart=Z2NwLXVzLWVhc3QxOjAxSlhaR0E5VlY0WFlaWjE3WEg1Tkg3Q1pT%3Fkey%3D9dfae736a876f8b84b6f5ae898cb49d4; cart_currency=USD; cart_sig=2b6aad483b027f0d4c7d8266c7929281; keep_alive=eyJ2IjoyLCJ0cyI6MTc1MDc4Nzg5ODQxNSwiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjoyNCwiY2EiOjAsImthIjowLCJzYSI6MTIsInRhIjowLCJrYmEiOjAsInQiOjUsIm5tIjoxLCJtcyI6MC4zOCwibWoiOjAuMDIsIm1zcCI6MC4wMiwidmMiOjAsImNwIjowLCJyYyI6MCwia2oiOjAsImtpIjowLCJzcyI6MC41NSwic2oiOjAuNTIsInNzbSI6MSwic3AiOjEsInRzIjowLCJ0aiI6MCwidHAiOjAsInRzbSI6MH0sInNlcyI6eyJwIjozLCJzIjoxNzUwNzcxNDMwNDM5LCJkIjoxNjQyNH19; localization=US'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


# POST
import requests

url = "https://api.hcaptcha.com/checksiteconfig?v=2345f279ad09eba46a641f838740fb06023e4005&host=shop.spacex.com&sitekey=f06e6c50-85a8-45c8-87d0-21a2b65856fe&sc=1&swa=1&spst=1"

payload = {}
headers = {
  'accept': 'application/json',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-length': '0',
  'content-type': 'text/plain',
  'origin': 'https://newassets.hcaptcha.com',
  'priority': 'u=1, i',
  'referer': 'https://newassets.hcaptcha.com/',
  'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'sec-fetch-storage-access': 'active',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'Cookie': 'hmt_id=e392b7db-8823-41e7-b1df-461c9e6dee2e; __cf_bm=AzacOqVeUyvNcLPLcrxQ41hzUeUHeoO.bKv.k2ec5kg-1750789585-1.0.1.1-S5HBhH8U4o6ZUPjZitcK04cwtEMyWNKDt3Clb1YRhYBNjcLEI1_x7FiLDqbVMwDdWZJw7WQdvl.PfLTKzelXDCvUON4Lm8fzEshKpUJH04M; __cf_bm=9zBGkl6fpTxw9P6asHVcGACj2jxf.l.Y_8uZeGcKFP4-1750789669-1.0.1.1-0n1t2BAtQabqFhWqpLO0nsxypXy8CB1potRS0.yVUI5UUmnELVsIiB0gZStqZ4d_H5EYq2bh3cl4v5l3Gv75ZcbrxJTDtuCrHfZLhbi8.a8'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


import requests
import json

url = "https://otlp-http-production.shopifysvc.com/v1/metrics"

payload = json.dumps({
  "resourceMetrics": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "shop-server-js"
            }
          }
        ]
      },
      "scopeMetrics": [
        {
          "scope": {
            "name": "open-telemetry-mini-client",
            "version": "1.1.0",
            "attributes": []
          },
          "metrics": [
            {
              "name": "shop_server_js_shop_pay_authorize_default_event",
              "unit": "1",
              "sum": {
                "aggregationTemporality": 1,
                "isMonotonic": True,
                "dataPoints": [
                  {
                    "startTimeUnixNano": 1750790013892000000,
                    "timeUnixNano": 1750790013892000000,
                    "asDouble": 1,
                    "attributes": [
                      {
                        "key": "analyticsContext",
                        "value": {
                          "stringValue": "loginWithShopClassicCustomerAccounts"
                        }
                      },
                      {
                        "key": "isCompactLayout",
                        "value": {
                          "stringValue": "true"
                        }
                      },
                      {
                        "key": "isMobile",
                        "value": {
                          "stringValue": "false"
                        }
                      },
                      {
                        "key": "type",
                        "value": {
                          "stringValue": "loaded"
                        }
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ]
})
headers = {
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/json',
  'origin': 'https://shop.app',
  'priority': 'u=1, i',
  'referer': 'https://shop.app/',
  'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
