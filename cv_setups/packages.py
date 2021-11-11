from pylatex import Command

def add_packages(doc):
    doc.packages.append(Command("RequirePackage", options="T1", arguments="fontenc"))

    doc.packages.append(Command("usepackage", arguments="times"))
    doc.packages.append(Command("usepackage", arguments="calc"))
    doc.packages.append(Command("usepackage", options="shortcuts", arguments="extdash"))
    doc.packages.append(Command("usepackage", arguments="graphicx"))
    doc.packages.append(Command("reversemarginpar"))

    doc.packages.append(Command("usepackage", options=["paper=letterpaper", "marginparwidth=1.1in", "marginparsep=.075in", "margin=0.5in", "tmargin=0.65in", "includemp"], arguments="geometry"))

    doc.packages.append(Command("usepackage", options="shortlabels", arguments="enumitem"))
    doc.packages.append(Command("usepackage", arguments="fancyhdr,lastpage"))
    doc.packages.append(Command("usepackage", arguments="color,hyperref"))
    doc.packages.append(Command("usepackage", arguments="doi"))
    doc.packages.append(Command("usepackage", arguments="url"))
