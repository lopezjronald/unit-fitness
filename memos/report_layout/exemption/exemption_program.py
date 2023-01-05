from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import time
from exemption_header import generate_header_table
from exemption_body import generate_body_table
from exemption_footer import generate_footer_table


# example data
class Commander:
    def __init__(self, rank, commander_first_name, commander_last_name):
        self.rank = rank
        self.commander_first_name = commander_first_name
        self.commander_last_name = commander_last_name


class UFPM:
    def __init__(self, rank, ufpm_first_name, ufpm_last_name):
        self.rank = rank
        self.ufpm_first_name = ufpm_first_name
        self.ufpm_last_name = ufpm_last_name


commander = Commander("Colonel", "Robert", "Noll")
ufpm = UFPM("TSgt", "Ronald", "Lopez")

first_name = "first_name"
last_name = "last_name"
# date_time = time.strftime('%Y-%m-%d-%H%M%S%p')
date_time = time.strftime("%Y-%m-%d")
file_name = f"Exemption-{last_name}-{first_name}-{date_time}.pdf"
letter_width, letter_height = letter

width_list = letter_width
height_list = [
    letter_height * .13,
    letter_height * .6,
    letter_height * .27,
]

pdf = canvas.Canvas(file_name, pagesize=letter)
pdf.setTitle(f"{first_name} {last_name}")

main_table = Table([
    [generate_header_table(letter_width, height_list[0])],
    [generate_body_table(letter_width, height_list[1])],
    [generate_footer_table(letter_width, height_list[2], ufpm, commander)],
],
    colWidths=width_list,
    rowHeights=height_list,
)

main_table.setStyle([
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
    ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
])

main_table.wrapOn(pdf, 0, 0)
main_table.drawOn(pdf, 0, 0)

pdf.showPage()
pdf.save()
