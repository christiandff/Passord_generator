import random
import string
from tkinter import Tk, Label, Button, Entry, Checkbutton, IntVar, messagebox

def generer_passord():
    """Genererer et passord basert på brukerens valg."""
    try:
        lengde = int(lengde_input.get())
        if lengde <= 0:
            raise ValueError("Lengden må være større enn 0.")

        # Tegnsett basert på brukerens valg
        små_bokstaver = string.ascii_lowercase
        store_bokstaver = string.ascii_uppercase if inkluder_store_bokstaver.get() else ''
        tall = string.digits if inkluder_tall.get() else ''
        spesialtegn = string.punctuation if inkluder_spesialtegn.get() else ''

        tilgjengelige_tegn = små_bokstaver + store_bokstaver + tall + spesialtegn

        if not tilgjengelige_tegn:
            raise ValueError("Velg minst én type tegn.")

        # Generer passord
        global generert_passord  # Gjør passordet tilgjengelig for kopiering
        generert_passord = ''.join(random.choice(tilgjengelige_tegn) for _ in range(lengde))
        passord_label.config(text=f"Generert passord: {generert_passord}")
    except ValueError as e:
        messagebox.showerror("Feil", str(e))

def kopier_til_utklippstavle():
    """Kopierer det genererte passordet til utklippstavlen."""
    try:
        if generert_passord:
            root.clipboard_clear()
            root.clipboard_append(generert_passord)
            root.update()  # Oppdater utklippstavlen
            messagebox.showinfo("Kopiert", "Passordet er kopiert til utklippstavlen.")
        else:
            raise NameError("Ingen passord generert enda.")
    except NameError as e:
        messagebox.showerror("Feil", str(e))

# Opprett hovedvinduet
root = Tk()
root.title("Passordgenerator")
root.geometry("600x400")

# GUI-komponenter
Label(root, text="Passordgenerator", font=("Arial", 14)).pack(pady=10)

Label(root, text="Lengde på passord:", font=("Arial", 12)).pack(pady=5)
lengde_input = Entry(root, width=10, font=("Arial", 12))
lengde_input.pack(pady=5)
lengde_input.insert(0, "12")  # Standardlengde

inkluder_store_bokstaver = IntVar(value=1)  # Standard: Inkluder store bokstaver
Checkbutton(root, text="Inkluder store bokstaver", variable=inkluder_store_bokstaver, font=("Arial", 10)).pack()

inkluder_tall = IntVar(value=1)  # Standard: Inkluder tall
Checkbutton(root, text="Inkluder tall", variable=inkluder_tall, font=("Arial", 10)).pack()

inkluder_spesialtegn = IntVar(value=1)  # Standard: Inkluder spesialtegn
Checkbutton(root, text="Inkluder spesialtegn", variable=inkluder_spesialtegn, font=("Arial", 10)).pack()

Button(root, text="Generer passord", command=generer_passord, font=("Arial", 12), bg="green", fg="white").pack(
    pady=20)

Button(root, text="Kopier passord", command=kopier_til_utklippstavle, font=("Arial", 12), bg="blue", fg="white").pack(
    pady=10)

passord_label = Label(root, text="", font=("Arial", 12), fg="black")
passord_label.pack(pady=10)

# Variabel for å holde det genererte passordet
generert_passord = ""

# Start GUI
root.mainloop()