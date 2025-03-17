from pylatex import Command, NoEscape, Section, UnsafeCommand


def add_experience(doc, resume_data):
    doc.append(
        UnsafeCommand(
            "newcommand",
            "\\resumeProject",
            options="3",
            extra_arguments=NoEscape(
                r"{}".format(
                    """
        \\item
        \\begin{tabular*}\\textwidth[t]{l@{\\extracolsep{\\fill}}r}
        \\avenir \\uline{#1} & {\\color{TextBlack} \\avenir \\small #3} \\vspace{1pt}\\\\
        \\avenirheavy{#2} \\\\
        \\end{tabular*}\\vspace{-4pt}
        \\resumeItemListStart
        """
                )
            ),
        )
    )
    with doc.create(Section("Related Experience".upper())):
        doc.append(Command("resumeSubHeadingListStart"))
        for project in resume_data["experience"]:
            link_and_name = Command(
                "href",
                arguments=NoEscape(project["url"]),
                extra_arguments=project["title"],
            )
            doc.append(
                Command(
                    "resumeProject",
                    arguments=link_and_name,
                    extra_arguments=[project["nature"], NoEscape(project["duration"])],
                )
            )
            for description in project["description"]:
                doc.append(Command("resumeItem", arguments=NoEscape(description)))

            doc.append(Command("resumeItemListEnd"))

        doc.append(Command("resumeSubHeadingListEnd"))
