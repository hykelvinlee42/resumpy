from pylatex import Command, NoEscape, UnsafeCommand

CV_HEADING_EXTRA_ARGUMENTS = rf"""

    {{
        \hspace{{-\marginparsep minus \marginparwidth}}
        \begin{{minipage}}[t]{{\textwidth + \marginparwidth + \marginparsep}}
        \centering
        {{\Large \bfseries {{#1 - Curriculum Vitae}}}}\\
        \vspace{{0.1cm}}
        \rule{{\columnwidth}}{{1.2pt}}
        \end{{minipage}}
    }}

"""


def add_heading(doc, cv_data):
    doc.preamble.append(
        UnsafeCommand(
            "newcommand",
            "\\cvHeading",
            options=1,
            extra_arguments=NoEscape(CV_HEADING_EXTRA_ARGUMENTS),
        )
    )

    doc.append(Command("cvHeading", cv_data["contact"]["name"]))
