import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg="lightgray")
frame.pack()

label = tk.Label(frame, text="Hello depuis le frame !")
label.pack()

root.title("Exemple standard")

frame = tk.Frame(root, bg="#dddddd", padx=10, pady=10, borderwidth=2, relief="groove")
frame.pack(padx=20, pady=20)

for row in range(3):
    for col in range(3):
        cell = tk.Label(frame, text=f"{row},{col}", width=10, height=2, bg="white", borderwidth=1, relief="solid")
        cell.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
