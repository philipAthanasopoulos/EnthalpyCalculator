import tkinter as tk
from tkinter import Label, PhotoImage
import pyromat as pm
from PIL import ImageTk, Image



pm.config["unit_energy"] = "kJ"
pm.config["unit_molar"] = "mol"
pm.config["unit_pressure"] = "atm"
pm.config["unit_matter"] = "mol"




window = tk.Tk()

img = ImageTk.PhotoImage(Image.open("ChemLogo.png").resize((300,200)))
imgLabel = tk.Label(window , image=img)
imgLabel.pack()

entryElement = tk.Entry(window , bd = 4)
entryElement.pack()

    


def calcEnthalpy():
    element = pm.get("ig." + entryElement.get())
    res = element.h(T = 298 , p = 1 )
    unit = "kJ/kmol"
    output = "%s %s" %(res , unit)
    label.config(text = output)

window.geometry("1000x900")
window.title("ChemLab")



buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0 , weight=1)

button = tk.Button(buttonFrame , text="Calculate Enthalpy (per mol)" , bg = "#2746d8" , fg = "white" , activebackground= "#9019e5" , command = calcEnthalpy)
button.grid(row=0 , column=0 , sticky="news")
buttonFrame.pack()


label=tk.Label(window, text="", font=('Calibri 15'))
label.pack()

logo = PhotoImage(file = 'ChemLogo.png')
window.iconphoto(False, logo)
window.mainloop() 
