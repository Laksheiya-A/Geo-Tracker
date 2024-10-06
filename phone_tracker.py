import tkinter
from click import style
from colorama import Style
from numpy import insert
import tkintermapview
import phonenumbers
import opencage

from key import key

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("500x500")

label1 = Label(text="GEO TRACKER!")
label1.pack()

def getResult():
    num = number.get("1.0", END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error", "Number box is empty or the input is not numeric. \nPlease enter a 10 digit numerical value along with your country code!")

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    my_label = LabelFrame(root)
    my_label.pack(pady=20)
    
    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text = "PHONE LOCATION ")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    adr = tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END, "THE COUNTRY OF THIS NUMBER IS LOCATED : " + location)
    result.insert(END, "\nTHE SIM CARD OF THIS NUMBER : " + service_provider)

    result.index(END, "\nLATITUDE : " + str(lat))
    result.index(END, "\nLONGITUDE : " + str(lng))

    result.insert(END, "\nSTREET ADDRESS : " + adr.street)
    result.insert(END, "\nCITY ADDRESS : " + adr.city)
    result.insert(END, "\nPOSTAL CODE : " + adr.postal)

number = Text(height=1)
number.pack()

style = Style()
style.configure("TButton", font= ('calibri', 20, 'bold'), borderwidth='4')
style.map('TButton', foreground = [('active', '!disabled', 'green')], 
                     background = [('active', 'black')])

button = Button(text="Search", command=getResult)
button.pack(pady = 10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()
