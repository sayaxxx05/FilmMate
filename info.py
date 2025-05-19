import tkinter as tk
from bs4 import BeautifulSoup
import requests
from tkinter import *
import os


class Info:
    def __init__(self):
        self.names = []
        self.description = []
        self.c = 0
        self.y = 0

    def get_info(self):

        url = "https://www.timeout.com/film/best-movies-of-all-time"
        try:
            page = requests.get(url)
            print("No internet connection.")
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")

        soup = BeautifulSoup(page.text, "html.parser")

        self.names = soup.findAll('h3', class_="_h3_19kvp_1")
        self.description = soup.findAll('div', class_="_p_1xfg7_1")

    def save_names(self):
        file = open("Name_of_film.txt", "w", encoding="utf-8")
        for i in self.names:
            b = i.text
            file.write(b + "\n")
        file.close()

    def save_description(self):
        file = open("Description_of_film.txt", "w", encoding="utf8")
        for i in self.description:
            b = i.text
            if len(b) != 1:
                file.write(b + "\n")
        file.close()

    def get_data(self):
        self.name = []
        with open("Name_of_film.txt", encoding="utf8") as f:
            self.name = f.readlines()
        self.name.append("over")

    # def get_description(self):
    #     self.descriptions = []
    #     with open("Description_of_film.txt", encoding="utf8") as f:
    #         self.descriptions = f.readlines()
    #     self.descriptions.append("over")

    def get_description(self):
        self.descriptions = []
        with open("Description_of_film.txt", encoding="utf8") as f:
            lines = f.readlines()
            # Чтение по 4 строки за раз
            for i in range(0, len(lines), 4):
                chunk = lines[i:i+4]
                self.descriptions.append(''.join(chunk).strip())  # Объединяет 4 строки в одну запись
        self.descriptions.append("over")


    def window(self):
        box = Tk()

        box.geometry("900x500")
        box.resizable(False, False)
        box.title("RECOMMENDATION")
        icon = PhotoImage(file="logo.png")
        box.iconphoto(False, icon)
        box.config(bg="#ffbed2")
        self.Text_box = Text(box, bg="#ffd4d1", height=15, width=75)

        logo = tk.Label(box, text="AlA-TOO INTERNATIONAL UNIVERSITY")
        self.label = tk.Label(box, pady=20, bg="#ffbed2", text=self.name[self.c])
        self.label.config(font=("Courier", 18))

        self.Fact = self.descriptions[self.c]

        next = tk.Button(box, text='Next', padx=100, pady=25, command=self.next_button)
        prev = tk.Button(box, text='Prev', padx=100, pady=25, command=self.prev_button)

        self.label.pack(side=TOP)
        self.Text_box.pack()
        logo.pack(side=TOP, pady=1, padx=1)
        next.pack(side=RIGHT, pady=30, padx=100)
        prev.pack(side=LEFT, pady=30, padx=100)
        self.Text_box.insert(tk.END, self.Fact)

        tk.mainloop()

    def next_button(self):
        self.c += 1
        self.y += 1

        self.label["text"] = self.name[self.c]
        if len(self.descriptions[self.y]) == 1:
                self.y += 1
        self.Fact = self.descriptions[self.y]
        if self.c > 99 and self.y > 100:
            self.Fact = "OVER"
            self.label["text"] = "OVER"
            print("GOOD BYE")
            quit()

        self.Text_box.delete("1.0", tk.END)
        self.Text_box.insert(tk.END, self.Fact)

    def prev_button(self):
        self.c -= 1
        self.y -= 1

        self.label["text"] = self.name[self.c]
        if len(self.descriptions[self.y]) == 1:
            self.y -= 1
        self.Fact = self.descriptions[self.y]
        if self.c < 0 and self.y < 0:
            self.Fact = "OVER"
            self.label["text"] = "OVER"
            print("GOOD BYE")
            quit()

        self.Text_box.delete("1.0", tk.END)
        self.Text_box.insert(tk.END, self.Fact)

