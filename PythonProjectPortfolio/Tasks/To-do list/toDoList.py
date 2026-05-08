import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import os

class UltraDarkTodo:
    def __init__(self, root):
        self.root = root
        self.root.title("Tasks")
        self.root.geometry("500x750")
        self.file_path = "tasks.txt"
        
        # --- True Dark Palette ---
        self.bg_color = "#191919"        
        self.input_bg = "#252525"        
        self.text_color = "#D3D3D3"      
        self.dim_text = "#757575"        
        self.accent_color = "#373737"    
        self.apple_font = ".AppleSystemUIFont"

        self.root.configure(bg=self.bg_color)

        # --- Header ---
        tk.Label(root, text="Tasks", font=(self.apple_font, 28, "bold"), 
                 bg=self.bg_color, fg=self.text_color).pack(anchor="w", padx=30, pady=(40, 10))

        self.container = tk.Frame(root, bg=self.bg_color, padx=30)
        self.container.pack(fill="both", expand=True)

        # Input Section
        tk.Label(self.container, text="NAME", font=(self.apple_font, 9, "bold"), 
                 bg=self.bg_color, fg=self.dim_text).pack(anchor="w", pady=(10, 5))
        
        self.task_entry = tk.Entry(self.container, font=(self.apple_font, 14), 
                                   bg=self.input_bg, fg=self.text_color, 
                                   insertbackground=self.text_color, bd=0, 
                                   highlightthickness=1, highlightbackground=self.accent_color)
        self.task_entry.pack(fill="x", ipady=8)

        # Date Section
        tk.Label(self.container, text="DATE", font=(self.apple_font, 9, "bold"), 
                 bg=self.bg_color, fg=self.dim_text).pack(anchor="w", pady=(15, 5))

        # Add Button
        self.add_btn = tk.Label(self.container, text="Add Task", 
                                font=(self.apple_font, 12, "bold"),
                                bg=self.accent_color, fg=self.text_color,
                                cursor="hand2", pady=10)
        self.add_btn.pack(fill="x", pady=25)
        self.add_btn.bind("<Button-1>", lambda e: self.add_task())

        # --- Treeview (Table) ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", 
                        background=self.bg_color, 
                        foreground=self.text_color, 
                        fieldbackground=self.bg_color, 
                        font=(self.apple_font, 11), 
                        rowheight=35, 
                        borderwidth=0)
        
        style.configure("Treeview.Heading", 
                        background=self.bg_color, 
                        foreground=self.dim_text, 
                        font=(self.apple_font, 10, "bold"), 
                        borderwidth=0)
        
        # HIGHLIGHT FIX: This makes the selected row visible in dark mode
        style.map("Treeview", background=[('selected', self.input_bg)], 
                              foreground=[('selected', self.text_color)])

        columns = ("task", "due", "status")
        self.tree = ttk.Treeview(self.container, columns=columns, show="headings", height=10, selectmode="browse")
        self.tree.heading("task", text="PROPERTY")
        self.tree.heading("due", text="DATE")
        self.tree.heading("status", text="DAYS")
        
        self.tree.column("task", width=180)
        self.tree.column("due", width=100)
        self.tree.column("status", width=100)
        self.tree.pack(fill="both", expand=True)

        # --- Delete Button ---
        self.del_btn = tk.Label(root, text="Remove Selected", font=(self.apple_font, 10),
                                bg=self.bg_color, fg="#803535", cursor="hand2")
        self.del_btn.pack(pady=20)
        self.del_btn.bind("<Button-1>", lambda e: self.delete_task())

        self.refresh_tree()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text: return
        
        date_str = self.cal.get_date().strftime("%Y-%m-%d")
        
        with open(self.file_path, "a") as f:
            f.write(f"{task_text}|{date_str}\n")
        
        self.task_entry.delete(0, tk.END)
        self.refresh_tree()

    def delete_task(self):
        selection = self.tree.selection()
        if not selection:
            return
        
        # Get the index of the selected item
        index_to_remove = self.tree.index(selection[0])
        
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                lines = f.readlines()
            
            # Remove the line by index
            if 0 <= index_to_remove < len(lines):
                lines.pop(index_to_remove)
            
            with open(self.file_path, "w") as f:
                f.writelines(lines)
        
        self.refresh_tree()

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if not os.path.exists(self.file_path): return
        
        today = date.today()
        with open(self.file_path, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    t_text, t_date_str = parts
                    t_date = datetime.strptime(t_date_str, "%Y-%m-%d").date()
                    
                    delta = t_date - today
                    if delta.days < 0: status = "Overdue"
                    elif delta.days == 0: status = "Today"
                    else: status = f"{delta.days}d"
                    
                    self.tree.insert("", tk.END, values=(t_text, t_date.strftime("%b %d"), status))

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraDarkTodo(root)
    root.mainloop()