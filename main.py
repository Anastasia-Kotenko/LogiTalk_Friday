from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.minsize(400, 300)

        # Налаштування grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ===== MENU FRAME =====
        self.frame_width = 0
        self.max_width = 200
        self.is_show_menu = False

        self.frame = CTkFrame(self, width=0)
        self.frame.grid(row=0, column=0, sticky="ns")
        self.frame.grid_propagate(False)

        self.label = CTkLabel(self.frame, text="Ваше Ім`я")
        self.label.pack(pady=30)

        self.entry = CTkEntry(self.frame)
        self.entry.pack(pady=5)

        self.label_theme = CTkOptionMenu(
            self.frame,
            values=["Темна", "Світла"],
            command=self.change_theme
        )
        self.label_theme.pack(side="bottom", pady=20)

        # ===== MAIN AREA =====
        self.main_frame = CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Текст чату
        self.chat_text = CTkTextbox(self.main_frame, state="disabled")
        self.chat_text.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Поле вводу
        self.message_input = CTkEntry(self.main_frame, placeholder_text="Введіть повідомлення:")
        self.message_input.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # Кнопка
        self.send_button = CTkButton(self.main_frame, text="▶", width=40)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

        # ===== MENU BUTTON =====
        self.btn = CTkButton(self, text="▶", command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)

        self.menu_show_speed = 15

    # ===== MENU CONTROL =====
    def toggle_show_menu(self):
        self.is_show_menu = not self.is_show_menu
        self.animate_menu()

    def animate_menu(self):
        if self.is_show_menu:
            if self.frame_width < self.max_width:
                self.frame_width += self.menu_show_speed
                self.frame.configure(width=self.frame_width)
                self.btn.configure(text="◀")
                self.after(10, self.animate_menu)
        else:
            if self.frame_width > 0:
                self.frame_width -= self.menu_show_speed
                self.frame.configure(width=self.frame_width)
                self.btn.configure(text="▶")
                self.after(10, self.animate_menu)

    # ===== THEME =====
    def change_theme(self, value):
        if value == "Темна":
            set_appearance_mode("dark")
        else:
            set_appearance_mode("light")


win = MainWindow()
win.mainloop()