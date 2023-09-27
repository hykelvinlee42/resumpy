from pylatex import Command, NoEscape, Section, UnsafeCommand


def add_overview(doc, resume_data):
    doc.append(
        UnsafeCommand(
            "newcommand",
            "\\resumeOverview",
            extra_arguments=NoEscape(
                r"{}".format(
                    """
        \\item\\resumeItemListStart
        """
                )
            ),
        )
    )
    with doc.create(Section("OVERVIEW")):
        doc.append(Command("resumeSubHeadingListStart"))
        doc.append(Command("resumeOverview"))
        for overview in resume_data["overview"]:
            doc.append(Command("resumeItem", arguments=overview))

        doc.append(Command("resumeItemListEnd"))
        doc.append(Command("resumeSubHeadingListEnd"))
