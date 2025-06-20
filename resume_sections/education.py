from pylatex import Command, NoEscape, Section, UnsafeCommand

RESUME_EDUCATION_EXTRA_ARGUMENT = r"""
    \vspace{-1pt}\item
    \begin{tabular*}\textwidth[t]{l@{\extracolsep{\fill}}r}
    \avenirheavy{#1} & {\color{TextBlack} \avenir \small #2}\\
    \end{tabular*}\vspace{-4pt}
    \resumeItemListStart
"""


def add_education(doc, resume_data):
    doc.append(
        UnsafeCommand(
            "newcommand",
            r"\resumeEducation",
            options="2",
            extra_arguments=NoEscape(RESUME_EDUCATION_EXTRA_ARGUMENT),
        )
    )
    with doc.create(Section("Education".upper())):
        doc.append(Command("resumeSubHeadingListStart"))
        for education in resume_data["education"]:
            doc.append(
                Command(
                    "resumeEducation",
                    arguments=NoEscape(education["school"]),
                    extra_arguments=NoEscape(education["duration"]),
                )
            )
            doc.append(Command("resumeItem", arguments=education["degree"]))
            doc.append(Command("resumeItemListEnd"))

        doc.append(Command("resumeSubHeadingListEnd"))
