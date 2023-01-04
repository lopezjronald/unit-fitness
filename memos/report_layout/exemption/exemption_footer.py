from reportlab.platypus import Table


def generate_footer_table(width, height, ufpm, commander):

    height_list = [
        height * .1,
        height * .1,
        height * .2,
        height * .1,
    ]

    footer_table = Table([
        [f"{ufpm.ufpm_first_name} {ufpm.ufpm_last_name}, {ufpm.rank}, USAF"],
        ["UFPM"],
        [f"{commander.commander_first_name} {commander.commander_last_name}, {commander.rank}, USAF"],
        ["349th ASTS Commander"],
    ],
        colWidths=width,
        rowHeights=height_list
    )

    footer_table.setStyle([
        ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 40),
        ("RIGHTPADDING", (0, 0), (-1, -1), 40),
        ("TEXTCOLOR", (0, 0), (-1, -1), "BLACK"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
        ("LEADING", (0, 1), (0, 1), 25),
        ("LEADING", (0, 3), (0, 3), 25),
    ])

    return footer_table
