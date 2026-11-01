"""Минимальное Flask-приложение для лабораторной работы по PaaS."""

from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = "1.0"  # Для повторного деплоя замени на "2.0".


@app.get("/")
def home():
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Лабораторная работа — PaaS</title>
  <style>
    body {{ margin: 0; background: #f3f6fa; font-family: Arial, sans-serif; color: #172333; }}
    main {{ max-width: 680px; margin: 10vh auto; padding: 32px; border-radius: 16px;
            background: white; box-shadow: 0 5px 24px #0b23401a; }}
    h1 {{ font-size: 28px; }}
    .version {{ display: inline-block; background: #e7f0ff; color: #1552a0;
                padding: 7px 12px; border-radius: 8px; font-weight: bold; }}
    .hint {{ color: #536477; line-height: 1.6; }}
    a {{ color: #1552a0; }}
  </style>
</head>
<body>
  <main>
    <h1>Лабораторная работа: PaaS</h1>
    <p><span class="version">Версия {APP_VERSION}</span></p>
    <p class="hint">Python + Flask. Приложение подготовлено для запуска
    через Docker и развёртывания на Render вместо Heroku.</p>
    <p><a href="/health">Проверить /health</a></p>
  </main>
</body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


if __name__ == "__main__":
    # Для прямого тестового запуска; в Docker/Render используется Gunicorn.
    app.run(host="0.0.0.0", port=10000)
