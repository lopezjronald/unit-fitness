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
        height * .35,
        height * .05,
        height * .3,
    ]
    result = Table([
        ["", headline_and_date_table(width_list[1], height_list[0]), ""],
        ["", address_and_subject_line_table(width_list[1], height_list[1]), ""],
        ["", exemption_line_table(width_list[1], height_list[2]), ""],
        ["", member_information_table(width_list[1], height_list[3]), ""],
        ["", contact_line_table(width_list[1], height_list[4]), ""],
        ["", ""],
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
    width_list = [
        width * .05,
        width * .95
    ]

    result = Table([
        ["1. ", "IAW AFI 36-2905, requesting medical exemption for:"]
    ],
        colWidths=width_list,
        rowHeights=height)

    result.setStyle([
        # ("GRID", (0, 0), (-1, -1), 1, "red"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
    ])

    return result


def member_information_table(width, height):
    width_list = [
        width * .05,
        width * .95
    ]

    height_list = [
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
        height * .1,
    ]

    paragraph_style = ParagraphStyle("paragraph")
    paragraph_style.fontName = "Times-Roman"
    paragraph_style.fontSize = 12
    paragraph_1 = Paragraph("<b>Rank/Name: </b>SrA Salas, Paige", paragraph_style)
    paragraph_2 = Paragraph("<b>DoD #: </b>SrA Salas, Paige", paragraph_style)
    paragraph_3 = Paragraph("<b>Start Date: </b>SrA Salas, Paige", paragraph_style)
    paragraph_4 = Paragraph("<b>End Date: </b>SrA Salas, Paige", paragraph_style)
    paragraph_5 = Paragraph("<b>Test Month: </b>SrA Salas, Paige", paragraph_style)
    paragraph_6 = Paragraph("<b>Reason for Exemption: </b>SrA Salas, Paige", paragraph_style)
    paragraph_7 = Paragraph("<b>AF Form 422/469 and or supporting documentation attached (if applicable): </b>N/A",
                            paragraph_style)

    result = Table([
        ["", ""],
        ["", paragraph_1],
        ["", paragraph_2],
        ["", paragraph_3],
        ["", paragraph_4],
        ["", paragraph_5],
        ["", paragraph_6],
        ["", paragraph_7],
        ["", ""],
        ["", ""],
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


def contact_line_table(width, height):
    width_list = [
        width * .05,
        width * .95
    ]

    paragraph_style = ParagraphStyle("paragraph")
    paragraph_style.fontName = "Times-Roman"
    paragraph_style.fontSize = 12
    paragraph_style.leading = 15
    paragraph_1 = Paragraph(
        "Please contact TSgt Ronald Lopez at Ronald.Lopez.4@us.af.mil with questions, or concerns at 707-424-3406",
        paragraph_style)

    result = Table([
        ["2. ", paragraph_1],
    ],
        colWidths=width_list,
        rowHeights=height)

    result.setStyle([
        # ("GRID", (0, 0), (-1, -1), 1, "red"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ])

    return result
