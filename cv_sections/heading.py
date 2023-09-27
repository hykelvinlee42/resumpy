from pylatex import Command, NoEscape, UnsafeCommand


def add_heading(doc, cv_data):
    doc.preamble.append(
        UnsafeCommand(
            "newcommand",
            "\\cvHeading",
            options=1,
            extra_arguments=NoEscape(
                r"{}".format(
                    """
        {\\hspace{-\\marginparsep minus \\marginparwidth}
        \\begin{minipage}[t]{\\textwidth + \\marginparwidth + \\marginparsep}
            \\centering
            {\\Large \\bfseries {#1 - Curriculum Vitae}}\\\\
            \\vspace{0.1cm}
            \\rule{\\columnwidth}{1.2pt}
        \\end{minipage}}
        
        """
                )
            ),
        )
    )

    doc.append(Command("cvHeading", cv_data["contact"]["name"]))
    doc.append(Command("vspace", "0.2cm"))
