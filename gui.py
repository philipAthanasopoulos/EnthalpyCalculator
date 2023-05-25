import tkinter as tk
from tkinter import Label, PhotoImage
import pyromat as pm
from PIL import ImageTk, Image

#create a window
window = tk.Tk()

#set the units
pm.config["unit_energy"] = "kJ"
pm.config["unit_molar"] = "mol"
pm.config["unit_pressure"] = "atm"
pm.config["unit_matter"] = "mol"

#set the logo
img = ImageTk.PhotoImage(Image.open("ChemLogo.png").resize((300,200)))
imgLabel = tk.Label(window , image=img)
imgLabel.pack()
#leave some break lines
tk.Label(window, text="").pack()
tk.Label(window, text="").pack()



# create a frame for the labels and entry boxes
frame = tk.Frame(window)
frame.pack()

# set the label for element
labelElement = tk.Label(frame, text="Enter element:")
labelElement.grid(row=0, column=0)

# set the entry box for element
entryElement = tk.Entry(frame, bd=4)
entryElement.grid(row=0, column=1)

# set the label for pressure
labelPressure = tk.Label(frame, text="Enter pressure:")
labelPressure.grid(row=1, column=0)

# set the entry box for pressure
entryPressure = tk.Entry(frame, bd=4)
entryPressure.grid(row=1, column=1)

# set the dropdown menu for pressure units
unitPressure = tk.StringVar()
unitPressure.set("Pa") # set the default unit to Pascal
menuPressure = tk.OptionMenu(frame, unitPressure, "Pa", "kPa", "MPa", "bar", "psi")
menuPressure.grid(row=1, column=2)

# function to get the unit of pressure
def getPressureUnit():
    return unitPressure.get()

# set the unit of pressure to the selected option on the menu
pressureUnit = getPressureUnit()

# set the label for temperature
labelTemp = tk.Label(frame, text="Enter temperature:")
labelTemp.grid(row=2, column=0)

# set the entry box for temperature
entryTemp = tk.Entry(frame, bd=4)
entryTemp.grid(row=2, column=1)

# set the dropdown menu for temperature units
unitTemp = tk.StringVar()
unitTemp.set("K") # set the default unit to Kelvin
menuTemp = tk.OptionMenu(frame, unitTemp, "K", "C")
menuTemp.grid(row=2, column=2)

# function to get the unit of temperature
def getTempUnit():
    return unitTemp.get()

# set the unit of temperature to the selected option on the menu
tempUnit = getTempUnit()

#calculate the enthalpy
def calcEnthalpy():
    #change the units
    pm.config["unit_pressure"] = getPressureUnit()
    pm.config["unit_temperature"] = getTempUnit()

    element = pm.get("ig." + entryElement.get())
    res = element.h(T = entryTemp.get() , p = entryPressure.get() )
    unit = "kJ/kmol"
    output = "%s %s" %(res , unit)
    label.config(text = output)

#set the window size and title
window.geometry("1000x900")
window.title("ChemLab")

#set the button
buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0 , weight=1)

button = tk.Button(buttonFrame , text="Calculate Enthalpy (per mol)" , bg = "#2746d8" , fg = "white" , activebackground= "#9019e5" , command = calcEnthalpy)
button.grid(row=0 , column=0 , sticky="news")
buttonFrame.pack()

#set the label
label=tk.Label(window, text="", font=('Calibri 15'))
label.pack()

window.mainloop()