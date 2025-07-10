import os
import requests
import time
import json

class TestCase:
    def __init__(self, name, url, method="GET", headers=None, params=None, data=None,
                 expected_status=200, check_field=None, expected_value=None):
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers or {}
        self.params = params or {}
        self.data = data
        self.expected_status = expected_status
        self.check_field = check_field
        self.expected_value = expected_value

    def run(self):
        try:
            start = time.time()
            resp = requests.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                data=self.data,
                timeout=10
            )
            elapsed_ms = round((time.time() - start) * 1000)
            # статус
            if resp.status_code != self.expected_status:
                return False, f"❌ {self.name}: статус {resp.status_code}, ожидалось {self.expected_status}, {elapsed_ms}ms"
            # проверка JSON-поля
            if self.check_field:
                js = resp.json()
                actual = js.get(self.check_field)
                if actual != self.expected_value:
                    return False, f"❌ {self.name}: «{self.check_field}»={actual}, ожидалось {self.expected_value}, {elapsed_ms}ms"
            return True, f"✅ {self.name}: OK, {elapsed_ms}ms"
        except Exception as e:
            return False, f"⚠️ {self.name}: ошибка {e}"

# Читаем cookie из переменной окружения для авторизации
HOYOLAB_COOKIE = os.getenv("HOYOLAB_COOKIE", "")

TEST_CASES = [
    # 1. Главная страница
    TestCase(
        name="HoYoLab Главная",
        url="https://www.hoyolab.com/",
        method="GET"
    ),
    # 2. Получаем список постов в официальном BBS (Genshin Impact, bbs_id=2)
    TestCase(
        name="BBS: последние посты",
        url="https://bbs-api-os.hoyolab.com/community/post/wapi/getPostList",
        method="GET",
        params={
            "gids[]": 2,
            "bbs_id": 2,
            "page_size": 5,
            "page_num": 1
        },
        check_field="retcode",
        expected_value=0
    ),
    # 3. Информация о пользователе (нужен cookie авторизации)
    TestCase(
        name="Инфо о пользователе",
        url="https://bbs-api-os.hoyolab.com/community/user/wapi/getUserFullInfo",
        method="GET",
        headers={
            "Cookie": HOYOLAB_COOKIE
        },
        params={
            "uid": os.getenv("HOYOLAB_UID", "ВАШ_UID")
        },
        check_field="retcode",
        expected_value=0
    ),
]

def test_run_api_tests() -> str:
    results = []
    passed = failed = 0

    for tc in TEST_CASES:
        ok, msg = tc.run()
        results.append(msg)
        if ok: passed += 1
        else: failed += 1

    total = len(TEST_CASES)
    rate = round(passed / total * 100) if total else 0
    results.append("\n📊 Итоги:")
    results.append(f"✅ Пройдено: {passed}")
    results.append(f"❌ Провалено: {failed}")
    results.append(f"🔢 Всего: {total}")
    results.append(f"🏁 Успех: {rate}%")

    return "\n".join(results)

if __name__ == "__main__":
    print(test_run_api_tests())
