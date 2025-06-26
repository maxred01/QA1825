# reports.py

def _analyze(data):
    if not data:
        return {"count": 0, "avg": 0, "max": None}
    return {
        "count": len(data),
        "avg": round(sum(data) / len(data), 1),
        "max": max(data)
    }

def generate_text_report(data):
    stats = _analyze(data)
    return (
        "Отчет:\n"
        "=======\n"
        f"Всего записей: {stats['count']}\n"
        f"Среднее значение: {stats['avg']}\n"
        f"Максимум: {stats['max']}"
    )

def generate_html_report(data):
    stats = _analyze(data)
    return f"""
<table border="1">
  <tr><th>Метрика</th><th>Значение</th></tr>
  <tr><td>Всего записей</td><td>{stats['count']}</td></tr>
  <tr><td>Среднее значение</td><td>{stats['avg']}</td></tr>
  <tr><td>Максимум</td><td>{stats['max']}</td></tr>
</table>
"""
