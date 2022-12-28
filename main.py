import string
import random
from tkinter import *

### Sukuriam langa
window = Tk()
window.title("Password Generator")
window.iconbitmap(r"icon.icns")

### Sukuriam funkcija
def generate_password():
  ### Gaunas norimo slaptazodzio ilgi
  length = length_entry.get()

  ### Tikrinam ar ilgis integeris
  try:
    length = int(length)
  except ValueError:
    result_label.config(text="Ilgis turi but skaicius!")
    return

  ### Tikrinam ar reikalingi specialus simboliai
  if special_characters_var.get() == 1:
    characters = string.ascii_letters + string.digits + string.punctuation
  else:
    characters = string.ascii_letters + string.digits

  ### Generuojam slaptazodi
  password = "".join(random.choices(characters, k=length))

  ### Atvaizduojam slaptazodi
  result_label.config(text=password)

### Sukuriam grafinius objektus
length_label = Label(text="Ilgis:")
length_entry = Entry()
special_characters_var = IntVar()
special_characters_checkbutton = Checkbutton(text="Ar reikalingi specialus simboliai?", variable=special_characters_var)
generate_button = Button(text="Generuojam", command=generate_password)
result_label = Label(text="")

### Pridedam grafinius objektus i langa
length_label.pack()
length_entry.pack()
special_characters_checkbutton.pack()
generate_button.pack()
result_label.pack()




window.mainloop()
