import tkinter
import tkintermapview
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
from key import key  # Make sure this file has your OpenCage API key

root = tkinter.Tk()
root.geometry("500x600")  # Adjusted height for better layout

label1 = Label(text="GEO TRACKER!", font=('calibri', 24, 'bold'))
label1.pack(pady=10)

# Function to get the result based on the input phone number
def getResult():
    num = number.get("1.0", END).strip()  # Get input and remove extra spaces
    if not num:
        messagebox.showerror("Error", "Please enter a phone number.")
        return

    try:
        num1 = phonenumbers.parse(num)  # Parse the phone number
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number format. Please include the country code.")
        return

    # Check if the number is valid
    if not phonenumbers.is_valid_number(num1):
        messagebox.showerror("Error", "The phone number is not valid.")
        return

    # Get location and service provider
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    # Get coordinates using OpenCage
    ocg = OpenCageGeocode(key)
    results = ocg.geocode(location)  # Directly use the location description for geocoding

    if not results:
        messagebox.showerror("Error", "Location not found.")
        return

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    # Create a map widget to display the location
    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    # Create and configure the map widget
    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat, lng)  # Set the position based on coordinates
    map_widget.set_marker(lat, lng, text="PHONE LOCATION")  # Add a marker for the phone location
    map_widget.set_zoom(10)  # Set the zoom level
    map_widget.pack(padx=10, pady=10)  # Use pack to display the map

    # Get the address details
    adr = tkintermapview.convert_coordinates_to_address(lat, lng)

    # Display the results in the result text box
    result.delete(1.0, END)  # Clear previous results
    result.insert(END, "THE COUNTRY OF THIS NUMBER IS LOCATED: " + str(location))
    result.insert(END, "\nTHE SIM CARD OF THIS NUMBER: " + str(service_provider))
    result.insert(END, "\nLATITUDE: " + str(lat))
    result.insert(END, "\nLONGITUDE: " + str(lng))

    if adr:
        result.insert(END, "\nSTREET ADDRESS: " + str(adr.street))
        result.insert(END, "\nCITY ADDRESS: " + str(adr.city))
        result.insert(END, "\nPOSTAL CODE: " + str(adr.postal))

# Input field for phone number
number = Text(height=1, width=30)
number.pack(pady=10)

# Style for buttons
style = Style()
style.configure("TButton", font=('calibri', 20, 'bold'), borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'green')], 
                     background=[('active', 'black')])

# Search button
button = Button(text="Search", command=getResult)
button.pack(pady=10, padx=100)

# Result display
result = Text(height=15, width=60)
result.pack(pady=10)

root.mainloop()
