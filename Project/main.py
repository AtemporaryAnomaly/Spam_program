import keyboard
import threading
from sys import exit
from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import path, listdir
# Importing urllib request module in the program
import webbrowser



class Bruteforce:
    def time_message(self):  #Изменение времени задержки
        intell = self.TimeEntry.get()
        self.delay = int(intell)
    def start(self):
        with open(self.filepath, 'r', encoding='UTF-8') as file:
            while line := file.readline():
                keyboard.write(line.rstrip())
                keyboard.send("enter")
                sleep(self.delay)
    def keyB(self):  #Изменение ключа
        self.key = keyboard.read_key()
        self.label2["text"] = self.key
        keyboard.add_hotkey(self.key, lambda: self.start())
    def open_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath != "":
            with open(self.filepath, "r") as file:
                text = file.read()
                lines = [line.rstrip() for line in file]
                self.text_editor.delete("1.0", END)
                self.text_editor.insert("1.0", text)

    def __init__(self):
        rt = Toplevel()
        rt.geometry("500x500")
        self.text_editor = Text(rt)
        self.text_editor.pack()

        self.open_button = ttk.Button(rt,text="Открыть файл", command=self.open_file)
        self.label = ttk.Label(rt, text="горячая Клавиша")  # создаем текстовую метку
        self.label2 = ttk.Label(rt, text="Клавиша не задана")
        self.btn3 = ttk.Button(rt, text="Изменить клавишу", command=self.keyB, )
        self.TimeEntry = ttk.Entry(rt, style="My.TLabel")
        self.TimeEntry.insert(0, "")

        self.open_button.pack()
        self.label.pack()
        self.label2.pack()
        self.btn3.pack(anchor=NW, padx=6, pady=6)
        self.TimeEntry.pack(anchor=NW, padx=6, pady=6)
        self.btn3 = ttk.Button(rt, text="Введите задержку и нажмите сюда", command=self.time_message, )
        self.btn3.pack(anchor=NW, padx=6, pady=6)



class setting:

    def btn4Add(self):  #Регистрация новой клавиши для чата игры
        global new_key
        new_key = keyboard.read_key()
        self.lb2["text"] = new_key

    def new_send(self):  #Добавляет новую клавишу для нажатия
        global new_key

        self.lb2["text"] = new_key

        if enabled.get() == 1:

            return new_key

        elif enabled.get() == 0:

            new_key = "space"

    def __init__(self):
        rt = Toplevel()

        rt.geometry("500x500")

        global enabled, new_key

        enabled = IntVar()

        self.btn4 = ttk.Button(rt, text="Добавить клавишу для чата", command=self.btn4Add)
        self.btn4.pack()

        self.enabled_checkbutton = ttk.Checkbutton(rt, text="Включить", variable=enabled, command=self.new_send)

        self.lb1 = ttk.Label(rt, text="Дополнительная клавиша\nдля открытия чата в играх")
        self.lb2 = ttk.Label(rt, text="y")

        self.enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
        self.lb1.pack()
        self.lb2.pack()


    @staticmethod
    def get_enabled():
        return enabled.get()

    @staticmethod
    def get_new_key():
        return new_key

class main:
    #ФУНКЦИИ
    def start(self, age, word, timeS):  #Запуск основной функции приложения
        global running

        running = True

        for i in range(age):

            if running == True:
                try:
                    get_val = setting.get_enabled()

                    if get_val == 1:

                        sleep(timeS)
                        keyboard.send(new_key)

                        sleep(0.5)
                        keyboard.write(word)
                        keyboard.send("enter")

                    else:

                        sleep(timeS)
                        keyboard.write(word)
                        keyboard.send("enter")

                except NameError:

                    sleep(timeS)
                    keyboard.write(word)
                    keyboard.send("enter")

            elif running == False:

                return 0
    def word_message(self):  #Изменение выводимого слова(предложения)
        a = self.wordEntry.get()
        self.word = a

    def age_message(self):  #Изменение повторов
        intell = self.AgeEntry.get()
        self.age = int(intell)

    def time_message(self):  #Изменение времени задержки
        intell = self.TimeEntry.get()
        self.timeS = int(intell)

    def help(self):  #объяснение функции программы
        webbrowser.open_new_tab('https://github.com/AtemporaryAnomaly/Spam_program/blob/main/README.md')
    def stopFunction(self):  #Остановка проги
        self.running = False

    def keyB(self):  #Изменение ключа
        self.key = keyboard.read_key()
        self.label2["text"] = self.key
        keyboard.add_hotkey(self.key, lambda: self.start(self.age, self.word, self.timeS))

    def file_open(self):  #Открывает данные текстового файла и отправляет их в wordEntry
        filepath = filedialog.askopenfilename(title="Файл для ввода", filetypes=self.filetypes)
        if filepath != "":
            with open(filepath, "r") as file:
                text = file.read()
                self.wordEntry.delete(0, END)
                self.wordEntry.insert(0, text)

    def __init__(self, root):
        #Задний фон

        ttk.Style().theme_use("classic")

        self.filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        #Меню
        self.main_menu = Menu(root)
        self.file_menu = Menu(root)
        self.settings_menu = Menu(root)

        self.settings_menu.add_command(label="additionally_the_game", command=setting)
        self.settings_menu.add_command(label="additionally_bruteforce", command=Bruteforce)
        self.file_menu.add_command(label="Открыть", command=self.file_open)

        self.main_menu.add_cascade(label='Настройки', menu=self.settings_menu)
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.main_menu.add_cascade(label='Помощь', command=self.help)
        self.main_menu.add_cascade(label="Выход", command=exit)

        root.config(menu=self.main_menu)

        #Стиль
        style = ttk.Style(root)
        style.theme_use("default")
        style.map("C.TButton",
                  foreground=[('!active', '#4169E1'), ('active', 'red')],
                  background=[('!active', '#000000'), ('active', 'black')]
                  )

        #ТЕКСТ
        self.wordEntry = ttk.Entry(root, style="My.TLabel")
        self.wordEntry.pack(anchor=NW, padx=6, pady=6)
        self.wordEntry.insert(0, "")
        self.btn = ttk.Button(root, text="Введите слово для ввода и нажмите сюда", command=self.word_message, )
        self.btn.pack(anchor=NW, padx=6, pady=6)

        #ЧИСЛО
        self.AgeEntry = ttk.Entry(root, style="My.TLabel")
        self.AgeEntry.pack(anchor=NW, padx=6, pady=6)
        self.AgeEntry.insert(0, "")

        self.btn3 = ttk.Button(root, text="Введите количество раз и нажмите сюда", command=self.age_message, )
        self.btn3.pack(anchor=NW, padx=6, pady=6)

        #Параметры задержки 
        self.TimeEntry = ttk.Entry(root, style="My.TLabel")
        self.TimeEntry.pack(anchor=NW, padx=6, pady=6)
        self.TimeEntry.insert(0, "")

        self.btn3 = ttk.Button(root, text="Введите задержку и нажмите сюда", command=self.time_message, )
        self.btn3.pack(anchor=NW, padx=6, pady=6)

        #Другие опции
        self.btn3 = ttk.Button(root, text="Изменить клавишу", command=self.keyB, )
        self.btn3.pack(anchor=NW, padx=6, pady=6)

        #ТЕКСТ
        self.label = ttk.Label(root, text="горячая Клавиша")  # создаем текстовую метку
        self.label2 = ttk.Label(root, text="Клавиша не задана")

        self.label.pack()
        self.label2.pack()


        self.btn3 = ttk.Button(root, text="Остановка", command=self.stopFunction)
        self.btn3.pack(anchor=CENTER, padx=6, pady=6)


root = Tk()
root.title("Spam_program")
root.iconbitmap("icon.ico")
root.geometry("450x500")
root.resizable(False, False)
main(root)

root.mainloop()
