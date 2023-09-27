colors = {
    "HeaderBrown": ["rgb", "0.35, 0.29, 0.23"],
    "SeparatorPink": ["rgb", "0.94, 0.41, 0.25"],
    "TextBlack": ["rgb", "0.0, 0.0, 0.0"],
}


def add_colors(doc):
    for color in colors.keys():
        doc.add_color(color, model=colors[color][0], description=colors[color][1])
