from reportlab.platypus import Image, Table


def generate_header_table(width, height):
    width_list = [
        width * .25,
        width * .5,
        width * .25,
    ]

    header_text_row_one = str.upper("DEPARTMENT OF THE AIR FORCE")
    header_text_row_two = str.upper("AIR FORCE RESERVE COMMAND")

    left_image_path = "dod-af-logo.jpg"
    left_image_width = width_list[0]
    left_image = Image(
        left_image_path,
        left_image_width,
        height,
        kind="proportional",
    )

    right_image_path = "af-reserve-logo.jpg"
    right_image_width = width_list[2]
    right_image = Image(
        right_image_path,
        right_image_width,
        height,
        kind="proportional",
    )

    header_table = Table([
        [left_image, header_text_row_one, right_image, header_text_row_two],
    ],
        colWidths=width_list,
        rowHeights=height,
    )

    header_table.setStyle([
        ("GRID", (0, 0), (-1, -1), 1, "RED"),
        ("FONTSIZE", (1, 0), (1, 0), 14),
        ("FONTSIZE", (3, 0), (3, 0), 12),
        ("LEFTPADDING", (3, 0), (3, 0), -750),
        ("BOTTOMPADDING", (3, 0), (3, 0), 45),
        ("TEXTCOLOR", (0, 0), (-1, -1), "DARKBLUE"),
        ("VALIGN", (1, 0), (1, 0), "TOP"),
        ("TOPPADDING", (1, 0), (1, 0), 30),
        ("FONTNAME", (0, 0), (-1, -1), "Times-Bold"),
        ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
        ("VALIGN", (2, 0), (2, 0), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ])

    return header_table
