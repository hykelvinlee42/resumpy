from pylatex import Command, Package


def add_packages(doc):
    # font encoding for better character support
    doc.packages.append(Command("RequirePackage", options="T1", arguments="fontenc"))

    # move margin notes to the left side
    doc.packages.append(Command("reversemarginpar"))

    # list of packages with optional arguments
    packages = [
        ("times", None),  # use times font
        ("calc", None),  # enable arithmetic with lengths
        ("extdash", "shortcuts"),  # provide extended dash commands
        ("graphicx", None),  # support for including images
        ("enumitem", "shortlabels"),  # customize list environments
        ("fancyhdr,lastpage", None),  # headers/footers and page count
        ("color,hyperref", None),  # color and hyperlink support
        ("doi", None),  # format digital object identifiers
        ("url", None),  # format urls properly
        (
            "geometry",  # configure page layout and margins
            [
                "paper=letterpaper",  # use us letter paper size
                "marginparwidth=1.1in",  # width of margin notes
                "marginparsep=.075in",  # space between text and margin notes
                "margin=0.5in",  # general margin size
                "tmargin=0.65in",  # top margin size
                "includemp",  # include marginpar in layout
            ],
        ),
    ]

    for pkg, opts in packages:
        doc.packages.append(Package(pkg, options=opts))
