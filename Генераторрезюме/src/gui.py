import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import webbrowser
from datetime import datetime
import os

def generate_resume(username, skills, experience, education):
    resume_content = f"""# 🎯 О себе {username}

## 👤 Обо мне
Привет! Я {username}, начинающий разработчик.

## 🛠️ Навыки
{skills}

## 💼 Опыт 
{experience}

## 🎓 Образование
{education}

## 📈 Статистика
- **Дата создания**: {datetime.now().strftime("%d.%m.%Y %H:%M")}
- **Платформа**: GitHub

## 🔗 Ссылки
- [Мой GitHub](https://github.com/{username})

---
*Резюме сгенерировано автоматически* 🚀
"""
    return resume_content

def create_gui():
    window = tk.Tk()
    window.title("🚀 Генератор Анкеты о себе для GitHub")
    window.geometry("700x600")  # Увеличим окно
    window.configure(bg="#f0f0f0")
    
    # Создаем frame с прокруткой
    main_frame = tk.Frame(window, bg="#f0f0f0")
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Canvas для прокрутки
    canvas = tk.Canvas(main_frame, bg="#f0f0f0")
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Заголовок
    title_label = tk.Label(
        scrollable_frame, 
        text="📝 Генератор Анкеты для GitHub", 
        font=("Arial", 16, "bold"),
        bg="#f0f0f0",
        fg="#333333"
    )
    title_label.pack(pady=15)
    
    # Фрейм для полей ввода
    input_frame = tk.LabelFrame(
        scrollable_frame, 
        text=" 📋 Заполните данные ", 
        font=("Arial", 11, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=10
    )
    input_frame.pack(fill="x", pady=10, padx=5)
    
    # Поле для имени пользователя GitHub
    tk.Label(input_frame, text="👤 Имя пользователя GitHub:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=8)
    username_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    username_entry.grid(row=0, column=1, pady=8, padx=10)
    
    # Поле для навыков
    tk.Label(input_frame, text="🛠️Ваши навыки:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=8)
    skills_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    skills_entry.grid(row=1, column=1, pady=8, padx=10)
    
    # Поле для опыта 
    tk.Label(input_frame, text="💼 Опыт :", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=8)
    experience_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    experience_entry.grid(row=2, column=1, pady=8, padx=10)
    
    # Поле для образования
    tk.Label(input_frame, text="🎓 Образование:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=8)
    education_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    education_entry.grid(row=3, column=1, pady=8, padx=10)
    
    # Кнопки
    button_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
    button_frame.pack(pady=15)
    
    def save_resume():
     username = username_entry.get().strip()
     if not username:
         messagebox.showerror("Ошибка", "❌ Введите имя пользователя GitHub!")
         return
     
     # Генерируем резюме
     resume_content = generate_resume(
         username,
         skills_entry.get(),
         experience_entry.get(),
         education_entry.get()
     )
     
     # УНИКАЛЬНОЕ ИМЯ С ДАТОЙ И ВРЕМЕНЕМ
     current_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # ГодМесяцДень_ЧасМинутаСекунда
     filename = f"RESUME_{username}_{current_time}.md"
     
     file_path = filedialog.asksaveasfilename(
         defaultextension=".md",
         filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
         initialfile=filename,  # Автоматически подставит уникальное имя
         title="Сохранить резюме как..."
     )
     
     if file_path:
         try:
             with open(file_path, 'w', encoding='utf-8') as file:
                 file.write(resume_content)
             
             # Обновим сообщение об успехе
             show_success_instruction(username, file_path)
             
             # Открываем папку с файлом
             os.startfile(os.path.dirname(file_path))
             
         except Exception as e:
             messagebox.showerror("Ошибка", f"❌ Не удалось сохранить файл: {e}")
            
    def open_github():
        webbrowser.open("https://github.com")
        messagebox.showinfo(
            "GitHub", 
            "Открыта главная страница GitHub.\n\n"
            "Если у вас еще нет репозитория:\n"
            "1. Нажмите '+' → 'New repository'\n"
            "2. Назовите 'resume' или 'portfolio'\n"
            "3. Создайте репозиторий"
        )
    
    def show_success_instruction(username, file_path):
        """Показывает подробную инструкцию в отдельном окне"""
        instruction_window = tk.Toplevel(window)
        instruction_window.title("✅ Анкета сохранена!")
        instruction_window.geometry("600x500")
        instruction_window.configure(bg="#f0f0f0")
        
        # Заголовок
        tk.Label(
            instruction_window, 
            text="🎉 Анкета успешна сохранена!", 
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="green"
        ).pack(pady=10)
        
        # Информация о файле
        info_text = f"""📁 **Сохраненный файл:** 
RESUME_{username}.md

📂 **Папка:**
{os.path.dirname(file_path)}

"""
        
        tk.Label(
            instruction_window, 
            text=info_text,
            font=("Arial", 10),
            bg="#f0f0f0",
            justify="left"
        ).pack(pady=5)
        
        # Прокручиваемая инструкция
        instruction_label = tk.Label(
            instruction_window, 
            text="📋 ПОШАГОВАЯ ИНСТРУКЦИЯ:",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        instruction_label.pack(pady=5)
        
        instruction_text = scrolledtext.ScrolledText(
            instruction_window,
            wrap=tk.WORD,
            width=70,
            height=15,
            font=("Arial", 9)
        )
        instruction_text.pack(padx=10, pady=5, fill="both", expand=True)
        
        instruction_content = """ШАГ 1: ОТКРОЙТЕ GITHUB
• Нажмите кнопку «Открыть GitHub» ниже
• Или перейдите на https://github.com вручную

ШАГ 2: СОЗДАЙТЕ/ОТКРОЙТЕ РЕПОЗИТОРИЙ
• Если у вас нет репозитория:
  1. Нажмите «+» в правом верхнем углу
  2. Выберите «New repository»
  3. Введите название: resume или my-portfolio
  4. Нажмите «Create repository»

• Если репозиторий уже есть:
  1. Откройте ваш репозиторий
  2. Перейдите на главную страницу репозитория

ШАГ 3: ЗАГРУЗИТЕ ФАЙЛ АНКЕТЫ
1. На странице репозитория нажмите «Add file»
2. Выберите «Upload files»
3. Перетащите файл RESUME_ВАШЕ_ИМЯ.md в окно
4. Или нажмите «choose your files» и выберите файл

ШАГ 4: СОХРАНИТЕ ИЗМЕНЕНИЯ
1. Прокрутите вниз до раздела «Commit changes»
2. Введите описание: «Add resume»
3. Нажмите «Commit changes»

ШАГ 5: ПРОВЕРЬТЕ РЕЗУЛЬТАТ
• Ваше резюме теперь доступно по адресу:
  https://github.com/ВАШ_ЛОГИН/НАЗВАНИЕ_РЕПОЗИТОРИЯ

💡 СОВЕТЫ:
• Назовите файл README.md чтобы он показывался на главной
• Добавьте больше информации о ваших проектах
• Обновляйте резюме по мере получения нового опыта"""
        
        instruction_text.insert(tk.END, instruction_content)
        instruction_text.config(state=tk.DISABLED)  # Только для чтения
    
        # Кнопки в окне инструкции
        button_frame = tk.Frame(instruction_window, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="🌐 Открыть GitHub",
            command=open_github,
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            width=15
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame,
            text="📂 Открыть папку с файлом",
            command=lambda: os.startfile(os.path.dirname(file_path)),
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            width=20
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame,
            text="❌ Закрыть",
            command=instruction_window.destroy,
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            width=10
        ).pack(side="left", padx=5)
    
    # Основные кнопки
    tk.Button(
        button_frame,
        text="💾 Сохранить Анкету на компьютер",
        command=save_resume,
        font=("Arial", 11, "bold"),
        bg="#4CAF50",
        fg="white",
        width=30,
        height=2
    ).pack(pady=10)
    
    tk.Button(
        button_frame,
        text="🌐 Открыть GitHub",
        command=open_github,
        font=("Arial", 10, "bold"),
        bg="#2196F3",
        fg="white",
        width=30,
        height=2
    ).pack(pady=5)
    
    # Краткая инструкция
    short_instruction = """💡 КАК ПОЛЬЗОВАТЬСЯ:
1. Заполните поля слева
2. Нажмите «Сохранить Анкету»
3. Следуйте инструкциям в новом окне"""

    tk.Label(
        scrollable_frame, 
        text=short_instruction,
        font=("Arial", 9),
        bg="#e8f5e8",
        relief="solid",
        borderwidth=1,
        padx=10,
        pady=10,
        justify="left"
    ).pack(pady=10, fill="x")
    
    # Упаковка canvas и scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Настройка прокрутки колесиком мыши
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    # Фокус на первое поле
    username_entry.focus()
    
    window.mainloop()

if __name__ == "__main__":
    create_gui()