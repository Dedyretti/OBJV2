import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
from datetime import datetime
import os

def generate_resume(username, skills, experience, education):
    resume_content = f"""# 🎯 Анкета {username}

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
*Анкета сгенерировано автоматически* 🚀
"""
    return resume_content

def create_gui():
    window = tk.Tk()
    window.title("🚀 Генератор Анкет для GitHub")
    window.geometry("600x500")
    window.configure(bg="#f0f0f0")
    
    # Заголовок
    title_label = tk.Label(
        window, 
        text="📝 Создайте свою Анкету для GitHub", 
        font=("Arial", 14, "bold"),
        bg="#f0f0f0"
    )
    title_label.pack(pady=20)
    
    # Фрейм для полей ввода
    input_frame = tk.Frame(window, bg="#f0f0f0")
    input_frame.pack(padx=20, pady=10, fill="both", expand=True)
    
    # Поле для имени пользователя GitHub
    tk.Label(input_frame, text="👤 Имя пользователя GitHub:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=8)
    username_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    username_entry.grid(row=0, column=1, pady=8, padx=10)
    
    # Поле для навыков
    tk.Label(input_frame, text="🛠️ Ваши навыки:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=8)
    skills_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    skills_entry.grid(row=1, column=1, pady=8, padx=10)
    
    # Поле для опыта работы
    tk.Label(input_frame, text="💼 Опыт:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=8)
    experience_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    experience_entry.grid(row=2, column=1, pady=8, padx=10)
    
    # Поле для образования
    tk.Label(input_frame, text="🎓 Образование:", 
             bg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=8)
    education_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
    education_entry.grid(row=3, column=1, pady=8, padx=10)
    
    def save_resume():
        username = username_entry.get().strip()
        if not username:
            messagebox.showerror("Ошибка", "❌ Введите имя пользователя GitHub!")
            return
        
        resume_content = generate_resume(
            username,
            skills_entry.get(),
            experience_entry.get(),
            education_entry.get()
        )
        
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"RESUME_{username}_{current_time}.md"
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
            initialfile=filename
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(resume_content)
                
                messagebox.showinfo("Успех!", f"✅ Анкета сохранена!\nФайл: {filename}")
                os.startfile(os.path.dirname(file_path))
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"❌ Ошибка сохранения: {e}")
    
    def open_github():
        webbrowser.open("https://github.com")
    
    # Кнопки
    button_frame = tk.Frame(window, bg="#f0f0f0")
    button_frame.pack(pady=20)
    
    tk.Button(
        button_frame,
        text="💾 Сохранить Анкету",
        command=save_resume,
        font=("Arial", 11, "bold"),
        bg="#4CAF50",
        fg="white",
        width=20
    ).pack(pady=10)
    
    tk.Button(
        button_frame,
        text="🌐 Открыть GitHub",
        command=open_github,
        font=("Arial", 10),
        bg="#2196F3",
        fg="white",
        width=20
    ).pack(pady=5)
    
    window.mainloop()

    

if __name__ == "__main__":
    create_gui()