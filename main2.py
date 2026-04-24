from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x400')
        self.minsize(400, 300)

        # ===== MENU =====
        self.menu_width = 30
        self.max_menu_width = 200
        self.is_show_menu = False
        self.speed = 10

        self.menu_frame = CTkFrame(self, width=self.menu_width)
        self.menu_frame.place(x=0, y=0)

        self.btn = CTkButton(self, text='▶️', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)

        # створюємо ОДИН раз
        self.label = CTkLabel(self.menu_frame, text='Імʼя')
        self.entry = CTkEntry(self.menu_frame)

        # ===== MAIN =====
        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.place(x=0, y=0)

        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)

        self.send_button = CTkButton(self, text='>', width=50, height=40)
        self.send_button.place(x=0, y=0)

        # адаптація тільки при зміні вікна
        self.bind("<Configure>", self.adaptive_ui)

    # ===== MENU =====
    def toggle_show_menu(self):
        self.is_show_menu = not self.is_show_menu

        if self.is_show_menu:
            self.btn.configure(text='◀️')
            self.label.pack(pady=30)
            self.entry.pack()
        else:
            self.btn.configure(text='▶️')
            self.label.pack_forget()
            self.entry.pack_forget()

        self.animate_menu()

    def animate_menu(self):
        if self.is_show_menu:
            if self.menu_width < self.max_menu_width:
                self.menu_width += self.speed
                self.menu_frame.configure(width=self.menu_width)
                self.after(10, self.animate_menu)
        else:
            if self.menu_width > 30:
                self.menu_width -= self.speed
                self.menu_frame.configure(width=self.menu_width)
                self.after(10, self.animate_menu)

    # ===== ADAPTIVE UI =====
    def adaptive_ui(self, event=None):
        w = self.winfo_width()
        h = self.winfo_height()

        # ❗ ВАЖЛИВО: тільки place, НЕ configure(height)
        self.menu_frame.place(x=0, y=0, height=h)

        # чат
        self.chat_field.place(x=self.menu_width, y=0)
        self.chat_field.configure(
            width=w - self.menu_width,
            height=h - 40
        )

        # кнопка
        self.send_button.place(x=w - 50, y=h - 40)

        # поле вводу
        self.message_entry.place(x=self.menu_width, y=h - 40)
        self.message_entry.configure(
            width=w - self.menu_width - 50
        )


win = MainWindow()
win.mainloop()