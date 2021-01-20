from tkinter import *
import calendar

def showcalender():
    gui = Tk()
    year=2021
    gui.title("Calender of the year")
    gui.config(background="yellow")
    gui.geometry("550x600")
    gui_content = calendar.calendar(year)
    cal_Year=Label(gui, text=gui_content, font='bold')
    cal_Year.grid(row=5, column=1, padx=20)
    gui.mainloop()

showcalender()