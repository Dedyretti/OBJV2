#!/usr/bin/env python3
"""
Программа для чтения и поиска анкет
Упрощенная версия без ошибок
"""

import os
import tkinter as tk
from tkinter import messagebox, scrolledtext, Listbox
import glob
from datetime import datetime

def find_resumes(username=None):
    """
    Ищет файлы анкет по имени пользователя или все анкет
    """
    resumes_folder = "резюме"
    
    # Если папки нет - создаем
    if not os.path.exists(resumes_folder):
        os.makedirs(resumes_folder)
        return []
    
    # Шаблон для поиска файлов
    if username:
        pattern = f"{resumes_folder}/RESUME_{username}_*.md"
    else:
        pattern = f"{resumes_folder}/RESUME_*.md"
    
    # Ищем файлы
    resume_files = glob.glob(pattern)
    
    # Сортируем по дате (новые сначала)
    resume_files.sort(reverse=True)
    
    return resume_files

def read_resume(file_path):
    """
    Читает содержимое файла анкет
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"❌ Ошибка чтения файла: {e}"

def parse_filename(filename):
    """
    Извлекает информацию из имени файла
    """
    try:
        # RESUME_username_20240115_143025.md
        name_parts = filename.replace('RESUME_', '').replace('.md', '').split('_')
        username = name_parts[0]
        date_str = name_parts[1] if len(name_parts) > 1 else ""
        time_str = name_parts[2] if len(name_parts) > 2 else ""
        
        # Преобразуем дату в читаемый формат
        if date_str and len(date_str) == 8:
            date_obj = datetime.strptime(date_str, "%Y%m%d")
            pretty_date = date_obj.strftime("%d.%m.%Y")
            if time_str and len(time_str) == 6:
                time_obj = datetime.strptime(time_str, "%H%M%S")
                pretty_time = time_obj.strftime("%H:%M:%S")
                return username, f"{pretty_date} {pretty_time}"
            return username, pretty_date
        
        return username, "Неизвестная дата"
    except:
        return filename, "Неизвестная дата"

def create_gui():
    """
    Создает графический интерфейс для поиска анкет
    """
    window = tk.Tk()
    window.title("🔍 Поиск анкет")
    window.geometry("800x600")
    window.configure(bg="#f0f0f0")
    
    # Заголовок
    title_label = tk.Label(
        window, 
        text="🔍 Поиск и просмотр анкет", 
        font=("Arial", 16, "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    title_label.pack(pady=15)
    
    # Фрейм поиска
    search_frame = tk.Frame(window, bg="#f0f0f0")
    search_frame.pack(fill="x", padx=20, pady=10)
    
    # Поле для ввода имени пользователя
    tk.Label(search_frame, text="👤 Имя пользователя:", 
             bg="#f0f0f0", font=("Arial", 10)).pack(side="left")
    
    username_entry = tk.Entry(search_frame, width=30, font=("Arial", 10))
    username_entry.pack(side="left", padx=10)
    
    # Переменная для хранения путей к файлам
    file_paths = []
    
    def search_by_username():
        """Поиск анкет по конкретному пользователю"""
        nonlocal file_paths
        username = username_entry.get().strip()
        
        if username:
            resume_files = find_resumes(username)
            status_text = f"Анкета пользователя: {username}"
        else:
            resume_files = find_resumes()
            status_text = "Все Анкеты"
        
        display_results(resume_files, status_text)
        file_paths = resume_files  # Сохраняем пути файлов
    
    def show_all_resumes():
        """Показать все анкеты"""
        nonlocal file_paths
        resume_files = find_resumes()
        display_results(resume_files, "Все анкеты")
        file_paths = resume_files
    
    # Кнопки поиска
    button_frame = tk.Frame(search_frame, bg="#f0f0f0")
    button_frame.pack(side="left", padx=20)
    
    tk.Button(
        button_frame,
        text="🔍 Найти анкеты",
        command=search_by_username,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 9)
    ).pack(side="left", padx=5)
    
    tk.Button(
        button_frame,
        text="📁 Показать все",
        command=show_all_resumes,
        bg="#2196F3",
        fg="white",
        font=("Arial", 9)
    ).pack(side="left", padx=5)
    
    # Статус поиска
    status_label = tk.Label(
        window,
        text="Введите имя пользователя и нажмите 'Найти анкеты'",
        bg="#f0f0f0",
        font=("Arial", 9),
        fg="#666666"
    )
    status_label.pack(pady=5)
    
    # Фрейм для списка и содержимого
    content_frame = tk.Frame(window, bg="#f0f0f0")
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Левая часть - список файлов
    left_frame = tk.Frame(content_frame, bg="#f0f0f0")
    left_frame.pack(side="left", fill="y", padx=(0, 10))
    
    tk.Label(
        left_frame, 
        text="📁 Найденные анкеты:", 
        font=("Arial", 10, "bold"),
        bg="#f0f0f0"
    ).pack(anchor="w")
    
    # Listbox для отображения файлов
    listbox = Listbox(left_frame, width=40, height=15, font=("Arial", 9))
    listbox.pack(fill="y", expand=True)
    
    # Прокрутка для listbox
    listbox_scroll = tk.Scrollbar(left_frame, orient="vertical")
    listbox_scroll.pack(side="right", fill="y")
    listbox.config(yscrollcommand=listbox_scroll.set)
    listbox_scroll.config(command=listbox.yview)
    
    # Правая часть - содержимое файла
    right_frame = tk.Frame(content_frame, bg="#f0f0f0")
    right_frame.pack(side="right", fill="both", expand=True)
    
    tk.Label(
        right_frame, 
        text="📄 Содержимое анкеты:", 
        font=("Arial", 10, "bold"),
        bg="#f0f0f0"
    ).pack(anchor="w")
    
    # Текстовая область для содержимого
    content_text = scrolledtext.ScrolledText(
        right_frame,
        wrap=tk.WORD,
        width=60,
        height=15,
        font=("Consolas", 9)
    )
    content_text.pack(fill="both", expand=True)
    
    def display_results(resume_files, status):
        """Отображает найденные анкеты"""
        # Обновляем статус
        status_label.config(text=f"{status} (найдено: {len(resume_files)})")
        
        # Очищаем список
        listbox.delete(0, tk.END)
        
        if not resume_files:
            listbox.insert(tk.END, "❌ анкеты не найдены")
            content_text.delete(1.0, tk.END)
            content_text.insert(tk.END, "анкеты не найдены. Попробуйте другой запрос.")
            return
        
        # Заполняем список
        for file_path in resume_files:
            filename = os.path.basename(file_path)
            username, date_str = parse_filename(filename)
            display_text = f"{username} | {date_str}"
            listbox.insert(tk.END, display_text)
    
    def on_resume_select(event):
        """Обработчик выбора анкеты в списке"""
        selection = listbox.curselection()
        if not selection or not file_paths:
            return
        
        index = selection[0]
        if index < len(file_paths):
            content = read_resume(file_paths[index])
            content_text.delete(1.0, tk.END)
            content_text.insert(tk.END, content)
    
    # Привязываем обработчик выбора
    listbox.bind("<<ListboxSelect>>", on_resume_select)
    
    # Кнопка открытия папки с анкеты
    def open_resumes_folder():
        """Открывает папку с анкетые"""
        resumes_folder = "резюме"
        if not os.path.exists(resumes_folder):
            os.makedirs(resumes_folder)
            messagebox.showinfo("Информация", f"Создана папка '{resumes_folder}'")
        os.startfile(resumes_folder)
    
    # Фрейм для нижних кнопок
    bottom_frame = tk.Frame(window, bg="#f0f0f0")
    bottom_frame.pack(pady=10)
    
    tk.Button(
        bottom_frame,
        text="📂 Открыть папку с анкетами",
        command=open_resumes_folder,
        bg="#FF9800",
        fg="white",
        font=("Arial", 10)
    ).pack(side="left", padx=5)
    
    tk.Button(
        bottom_frame,
        text="❌ Закрыть программу",
        command=window.destroy,
        bg="#f44336",
        fg="white",
        font=("Arial", 10)
    ).pack(side="left", padx=5)
    
    # Автоматически загружаем все анкеты при запуске
    window.after(100, show_all_resumes)
    
    window.mainloop()

def simple_console_version():
    """
    Простая консольная версия для быстрого использования
    """
    print("🔍 Поиск анкет")
    print("=" * 40)
    
    username = input("Введите имя пользователя (или нажмите Enter для всех): ").strip()
    
    if username:
        resume_files = find_resumes(username)
        title = f"Анкеты пользователя: {username}"
    else:
        resume_files = find_resumes()
        title = "Все анкеты"
    
    if not resume_files:
        print("❌ Анкеты не найдены")
        input("Нажмите Enter для выхода...")
        return
    
    print(f"\n📁 {title}: {len(resume_files)}")
    print("-" * 50)
    
    for i, file_path in enumerate(resume_files, 1):
        filename = os.path.basename(file_path)
        username, date_str = parse_filename(filename)
        print(f"{i}. 👤 {username} | 📅 {date_str}")
        print(f"   📄 {filename}")
    
    # Предлагаем посмотреть конкретную Анкету
    try:
        choice = input(f"\nВыберите номер для просмотра (1-{len(resume_files)}, или 0 для выхода): ")
        if choice == '0':
            return
        
        if choice.isdigit() and 1 <= int(choice) <= len(resume_files):
            content = read_resume(resume_files[int(choice)-1])
            print("\n" + "="*60)
            print(content)
            print("="*60)
    except:
        pass
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    # Всегда запускаем графическую версию
    create_gui()