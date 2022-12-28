import tkinter as tk
from tkinter import Label
import pyromat as pm



pm.config["unit_energy"] = "kJ"
pm.config["unit_molar"] = "kmol"
pm.config["unit_pressure"] = "atm"
pm.config["unit_matter"] = "kmol"




window = tk.Tk()
entryElement = tk.Entry(window , bd = 4)
entryElement.pack()


def calcEnthalpy():
    element = pm.get("ig." + entryElement.get())
    res = element.h(T = 310 , p = 1 )
    label.config(text = res)

window.geometry("1000x900")
window.title("ChemLab")



buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0 , weight=1)

button = tk.Button(buttonFrame , text="Calculate Internal Energy (per gram)" , bg = "#2746d8" , fg = "white" , activebackground= "#9019e5" , command = calcEnthalpy)
button.grid(row=0 , column=0 , sticky="news")


buttonFrame.pack()

label=tk.Label(window, text="", font=('Calibri 15'))
label.pack()




#comment to test commit via VScode


window.mainloop() 













