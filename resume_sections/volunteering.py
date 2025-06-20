from pylatex import Command, NoEscape, Section, UnsafeCommand

RESUME_VOLUNTEERING_EXTRA_ARGUMENT = r"""
    \vspace{-1pt}\item
    \begin{tabular*}\textwidth[t]{l@{\extracolsep{\fill}}r}
    \avenirheavy{#1}\vspace{1pt}\\
    \avenir{#2} & {\color{TextBlack} \avenir \small #3}\\
    \end{tabular*}\vspace{-4pt}
"""

RESUME_VOLUNTEERING_EXTRA_ARGUMENT_NULL_ORGANIZATION = r"""
    \vspace{-20pt}\item
    \begin{tabular*}\textwidth[t]{l@{\extracolsep{\fill}}r}\\
    \avenir{#1} & {\color{TextBlack} \avenir \small #2}\\
    \end{tabular*}\vspace{-4pt}
"""


def add_volunteering(doc, resume_data):
    doc.append(
        UnsafeCommand(
            "newcommand",
            r"\resumeVolunteetingServices",
            options="3",
            extra_arguments=NoEscape(RESUME_VOLUNTEERING_EXTRA_ARGUMENT),
        )
    )
    doc.append(
        UnsafeCommand(
            "newcommand",
            r"\resumeVolunteetingServicesNullOrganization",
            options="2",
            extra_arguments=NoEscape(
                RESUME_VOLUNTEERING_EXTRA_ARGUMENT_NULL_ORGANIZATION
            ),
        )
    )
    with doc.create(Section("Volunteering and Services".upper())):
        doc.append(Command("resumeSubHeadingListStart"))
        for work in resume_data["volunteer"]:
            for index, position in enumerate(work["positions"]):
                if index == 0:
                    doc.append(
                        Command(
                            "resumeVolunteetingServices",
                            arguments=NoEscape(work["organization"]),
                            extra_arguments=[
                                NoEscape(position["title"]),
                                NoEscape(position["duration"]),
                            ],
                        )
                    )
                else:
                    doc.append(
                        Command(
                            "resumeVolunteetingServicesNullOrganization",
                            arguments=NoEscape(position["title"]),
                            extra_arguments=NoEscape(position["duration"]),
                        )
                    )

        doc.append(Command("resumeSubHeadingListEnd"))
