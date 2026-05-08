import tkinter as tk
from tkinter import messagebox, filedialog

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator (Weighted & Unweighted)")
        self.root.geometry("450x400")

        # Weighted Scale (from first image)
        self.weighted_scale = {
            'A+': {'Honors': 6.33, 'Accelerated': 5.33, 'Regular': 4.33},
            'A':  {'Honors': 6.00, 'Accelerated': 5.00, 'Regular': 4.00},
            'A-': {'Honors': 5.67, 'Accelerated': 4.67, 'Regular': 3.67},
            'B+': {'Honors': 5.33, 'Accelerated': 4.33, 'Regular': 3.33},
            'B':  {'Honors': 5.00, 'Accelerated': 4.00, 'Regular': 3.00},
            'B-': {'Honors': 4.67, 'Accelerated': 3.67, 'Regular': 2.67},
            'C+': {'Honors': 4.33, 'Accelerated': 3.33, 'Regular': 2.33},
            'C':  {'Honors': 4.00, 'Accelerated': 3.00, 'Regular': 2.00},
            'C-': {'Honors': 3.67, 'Accelerated': 2.67, 'Regular': 1.67},
            'D':  {'Honors': 1.00, 'Accelerated': 1.00, 'Regular': 1.00},
            'F':  {'Honors': 0.00, 'Accelerated': 0.00, 'Regular': 0.00},
        }

        # Unweighted Scale (from second image)
        self.unweighted_scale = {
            'A+': 4.33, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 
            'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D': 1.0, 'F': 0.0
        }

        # UI Setup
        tk.Label(root, text="GPA Calculator", font=("Arial", 16, "bold")).pack(pady=15)
        
        self.calc_button = tk.Button(root, text="Select grades.txt & Calculate", 
                                     command=self.calculate_gpa, bg="#2196F3", fg="white", padx=10)
        self.calc_button.pack(pady=10)

        self.w_result = tk.Label(root, text="Weighted GPA: --", font=("Arial", 12, "bold"))
        self.w_result.pack(pady=5)

        self.u_result = tk.Label(root, text="Unweighted GPA: --", font=("Arial", 12))
        self.u_result.pack(pady=5)

    def calculate_gpa(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path: return

        w_total_pts = 0.0
        u_total_pts = 0.0
        total_credits = 0.0

        try:
            with open(file_path, "r") as file:
                for line in file:
                    if not line.strip(): continue
                    parts = [p.strip() for p in line.split(',')]
                    if len(parts) != 4: continue
                    
                    _, level, grade, credits = parts
                    credits = float(credits)

                    # Calculate Weighted
                    if grade in self.weighted_scale and level in self.weighted_scale[grade]:
                        w_total_pts += (self.weighted_scale[grade][level] * credits)
                    
                    # Calculate Unweighted
                    if grade in self.unweighted_scale:
                        u_total_pts += (self.unweighted_scale[grade] * credits)
                    
                    total_credits += credits

            if total_credits > 0:
                self.w_result.config(text=f"Weighted GPA: {w_total_pts / total_credits:.2f}")
                self.u_result.config(text=f"Unweighted GPA: {u_total_pts / total_credits:.2f}")
            else:
                messagebox.showwarning("Error", "No valid credits found.")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()