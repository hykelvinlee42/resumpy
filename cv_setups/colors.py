colors = {"DarkBlue": ["rgb", "0.0, 0.0, 0.3"]}


def add_colors(doc):
    for color in colors.keys():
        doc.add_color(color, model=colors[color][0], description=colors[color][1])
