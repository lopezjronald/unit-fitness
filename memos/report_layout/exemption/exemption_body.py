from reportlab.platypus import Table, Paragraph
import datetime
from reportlab.lib.styles import ParagraphStyle


def generate_body_table(width, height):
    width_list = [
        width * .1,
        width * .8,
        width * .1,
    ]

    height_list = [
        height * .08,
        height * .17,
        height * .05,
        height * .65,
        height * .05,
    ]
    result = Table([
        ["", headline_and_date_table(width_list[1], height_list[0]), ""],
        ["", address_and_subject_line_table(width_list[1], height_list[1]), ""],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ],
        colWidths=width_list,
        rowHeights=height_list)

    result.setStyle([
        # ("GRID", (0, 0), (-1, -1), 1, "red"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
    ])
    return result


def headline_and_date_table(width, height):
    width_list = [
        width * .5,
        width * .5,
    ]

    result = Table([
        ["MEMORANDUM FOR 349th FSS/FAC", datetime.date.today().strftime("%B %d, %Y")]
    ],
        colWidths=width_list,
        rowHeights=height)

    result.setStyle([
        # ("GRID", (0, 0), (-1, -1), 1, "red"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
    ])

    return result


def address_and_subject_line_table(width, height):
    width_list = [
        width * .1,
        width * .9
    ]

    height_list = [
        height * .1,
        height * .2,
        height * .2,
        height * .2,
        height * .3,
    ]

    result = Table([
        ("", ""),
        ("FROM: ", "349th ASTS"),
        ("", "531 Waldron St, Bay B"),
        ("", "Travis AFB, CA 94535-2125"),
        ("SUBJECT: ", "Fitness Exemption for Members"),
    ],
        colWidths=width_list,
        rowHeights=height_list)

    result.setStyle([
        # ("GRID", (0, 0), (-1, -1), 1, "red"),
        ("LEFTPADDING", (0, 0), (0, 1), 0),
        ("LEFTPADDING", (1, 1), (1, 3), -8),
        ("LEFTPADDING", (0, 4), (0, 4), 0),
        ("LEFTPADDING", (1, 4), (1, 4), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
        ("SPACEAFTER", (0, 3), (1, 3), 20),

    ])

    return result


def exemption_line_table(width, height):
    return "Exemption line"


def member_information_table(width, height):
    return "Member information"


def contact_line_table(width, height):
    return "Contact line"
