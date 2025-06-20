from pylatex import Package
from pylatex.package import Package


def add_packages(doc):
    # list of packages with optional arguments
    packages = [
        ("fontspec", None),  # use system fonts (requires xelatex or lualatex)
        ("latexsym", None),  # provide additional math and symbol fonts
        ("fullpage", "empty"),  # reduce margins to use more page space
        ("titlesec", None),  # customize section and heading styles
        ("color", None),  # enable color support
        ("transparent", None),  # allow transparency in graphics
        ("enumitem", None),  # customize list environments
        ("hyperref", "hidelinks"),  # enable hyperlinks without colored boxes
        ("fancyhdr", None),  # create custom headers and footers
        ("tabularx", None),  # create tables with flexible column widths
        ("ulem", "normalem"),  # underline text while preserving normal emphasis
        ("ragged2e", None),  # improve ragged text alignment
        ("graphicx", None),  # include and scale images
    ]

    for pkg, opts in packages:
        doc.packages.append(Package(pkg, options=opts))
