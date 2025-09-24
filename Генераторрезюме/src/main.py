
"""
Главный модуль программы для генерации Анкет GitHub
Автор: Данила
Версия: 2.0
"""


import os
import webbrowser
from datetime import datetime

def generate_resume(username, skills, experience, education):
    """
    Генерирует содержимое файла Анкет в формате Markdown
    """
    resume_content = f"""# 🎯 О себе {username}

## 👤 Обо мне
Привет! Я {username}, начинающий/опытный разработчик.

## 🛠️ Навыки
{skills}

## 💼 Опыт 
{experience}

## 🎓 Образование
{education}

## 📈 Статистика
- **Дата создания Анкеты**: {datetime.now().strftime("%d.%m.%Y")}
- **Платформа**: GitHub

## 🔗 Ссылки
- [Мой GitHub](https://github.com/{username})

---
*Анкета сгенерировано автоматически* 🚀
"""
    return resume_content

def save_resume_to_file(username, content):
    """
    Сохраняет Анкеты в файл
    """
    filename = f"RESUME_{username.upper()}.md"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Анкета сохранена в файл: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
        return None

def open_github_new_file(content):
    """
    Открывает GitHub для создания нового файла с готовым содержимым
    """
    import urllib.parse
    encoded_content = urllib.parse.quote(content)
    github_url = f"https://github.com/new?filename=RESUME.md&value={encoded_content}"
    webbrowser.open(github_url)
    print("🌐 Открываю GitHub в браузере...")

# УДАЛИТЕ функцию main() отсюда или оставьте пустой
def main():
    """Основная функция программы"""
    print("🚀 Запуск генератора Анкеты GitHub...")
    # Теперь GUI запускается из gui.py

if __name__ == "__main__":
    # Вместо запуска GUI, просто сообщим что нужно запустить gui.py
    print("📝 Запустите программу командой: python src/gui.py")