from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Header
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # Shirt Image
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # Text on Shirt
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=50, y=140, txt=f"{name} took CS50P")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
