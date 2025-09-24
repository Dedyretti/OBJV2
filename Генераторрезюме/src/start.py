#!/usr/bin/env python3
"""
Универсальный запускатель для программ генератора резюме
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox

def run_generator():
    """Запускает генератор резюме"""
    try:
        sys.path.append('src')
        from gui import create_gui
        create_gui()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось запустить генератор:\n{e}")

def run_reader():
    """Запускает читалку резюме"""
    try:
        sys.path.append('src')
        from resume_reader import create_gui
        create_gui()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось запустить читалку:\n{e}")

def create_launcher_gui():
    """Создает меню выбора программ"""
    window = tk.Tk()
    window.title("🚀 Генератор резюме - Меню запуска")
    window.geometry("400x300")
    window.configure(bg="#f0f0f0")
    
    # Заголовок
    title_label = tk.Label(
        window, 
        text="🚀 Генератор резюме GitHub", 
        font=("Arial", 16, "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    title_label.pack(pady=30)
    
    # Кнопки выбора программы
    button_frame = tk.Frame(window, bg="#f0f0f0")
    button_frame.pack(pady=20)
    
    tk.Button(
        button_frame,
        text="📝 Генератор резюме",
        command=run_generator,
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)
    
    tk.Button(
        button_frame,
        text="🔍 Читалка резюме",
        command=run_reader,
        font=("Arial", 12, "bold"),
        bg="#2196F3",
        fg="white",
        width=20,
        height=2
    ).pack(pady=10)
    
    # Информация
    info_label = tk.Label(
        window, 
        text="💡 Выберите программу для запуска",
        font=("Arial", 10),
        bg="#f0f0f0",
        fg="#666666"
    )
    info_label.pack(pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    # Если переданы аргументы командной строки
    if len(sys.argv) > 1:
        if sys.argv[1] == "generator":
            run_generator()
        elif sys.argv[1] == "reader":
            run_reader()
        else:
            create_launcher_gui()
    else:
        create_launcher_gui()