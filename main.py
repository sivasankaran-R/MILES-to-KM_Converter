from tkinter import *
window = Tk()
window.title('MILES TO KILOMETER CONVERTER')
window.config(padx=20,pady=20)

def mile_to_km():
  miles = float(my_input.get())
  #we can use miles*1.609 also...!
  km = round((miles/5)*8)
  my_label_3.config(text = f"{km}")

my_input = Entry(width=6)
my_input.grid(column=1,row=0)

my_label_1 = Label(text="MILES")
my_label_1.grid(column=2,row=0)

my_label_2 = Label(text="is equal to")
my_label_2.grid(column=0,row=1)

my_label_3= Label(text="0")
my_label_3.grid(column=1,row=1)

my_label_4= Label(text="KM")
my_label_4.grid(column=2,row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1,row=2)



