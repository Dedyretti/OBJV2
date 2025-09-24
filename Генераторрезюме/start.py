#!/usr/bin/env python3
"""
Простой запускатель для программ генератора резюме
"""

import os
import sys
import subprocess

def main():
    print("🚀 Меню запуска - Генератор резюме")
    print("=" * 40)
    print("1. 📝 Генератор резюме")
    print("2. 🔍 Читалка резюме")
    print("3. ❌ Выход")
    print("=" * 40)
    
    while True:
        choice = input("Выберите программу (1-3): ").strip()
        
        if choice == "1":
            launch_generator()
        elif choice == "2":
            launch_reader()
        elif choice == "3":
            print("До свидания! 👋")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")

def launch_generator():
    """Запускает генератор резюме"""
    try:
        script_path = os.path.join("src", "gui.py")
        if os.path.exists(script_path):
            print("🔄 Запуск генератора резюме...")
            subprocess.run([sys.executable, script_path])
        else:
            print("❌ Файл gui.py не найден!")
    except Exception as e:
        print(f"❌ Ошибка запуска: {e}")

def launch_reader():
    """Запускает читалку резюме"""
    try:
        script_path = os.path.join("src", "resume_reader.py")
        if os.path.exists(script_path):
            print("🔄 Запуск читалки резюме...")
            subprocess.run([sys.executable, script_path])
        else:
            print("❌ Файл resume_reader.py не найден!")
    except Exception as e:
        print(f"❌ Ошибка запуска: {e}")

if __name__ == "__main__":
    main()