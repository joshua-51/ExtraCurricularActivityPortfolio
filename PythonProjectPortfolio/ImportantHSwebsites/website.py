import tkinter as tk
import webbrowser

def action_1():
    webbrowser.open("https://www.edison.k12.nj.us/page/placement-criteria") 

def action_2():
    webbrowser.open("https://www.edison.k12.nj.us/page/appealsandwaivers") 

def action_3():
    webbrowser.open("https://docs.google.com/document/d/1DYXDHMTlaQ0V4VZEb1qhoTZGviFZtvLizrP7UbOcq7E/edit?tab=t.0") 

def action_4():
    webbrowser.open("https://parents.edison.k12.nj.us/genesis/parents?gohome=true") 

def action_5():
    webbrowser.open("https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/4500/Ehs/d35c6aad-b884-4349-8ebd-0a8d52c3ab70/Final_Program_of_Studies_24-25.docx.pdf?disposition=inline") 

root = tk.Tk()
root.title("Action Panel")
root.geometry("300x250")

# Create Buttons
btn1 = tk.Button(root, text="Placement Criteria", command=action_1)
btn1.pack(pady=5, fill='x', padx=20)

btn2 = tk.Button(root, text="Waiver info", command=action_2)
btn2.pack(pady=5, fill='x', padx=20)

btn3 = tk.Button(root, text="Student Handbook", command=action_3)
btn3.pack(pady=5, fill='x', padx=20)

btn4 = tk.Button(root, text="Parent Portal", command=action_4)
btn4.pack(pady=5, fill='x', padx=20)

btn5 = tk.Button(root, text="Program of Studies", command=action_5)
btn5.pack(pady=5, fill='x', padx=20)
root.mainloop()
