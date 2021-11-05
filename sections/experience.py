from pylatex import Section, Command, UnsafeCommand, NoEscape


def add_experience(doc, resume_data):
    doc.append(UnsafeCommand("newcommand", "\\resumeProject", options="3", extra_arguments=NoEscape(r"{}".format("""
        \\item
        \\begin{tabular*}\\textwidth[t]{l@{\\extracolsep{\\fill}}r}
        \\avenir \\uline{#1} & {\\color{TextBlack} \\avenir \\small #3} \\vspace{1pt}\\\\
        \\avenirheavy{#2} \\\\
        \\end{tabular*}\\vspace{-4pt}
        \\resumeItemListStart
        """))))
    with doc.create(Section("RELATED EXPERIENCE")):
        doc.append(Command("resumeSubHeadingListStart"))
        for project in resume_data["experience"]:
            link_and_name = Command("href", arguments=project["url"], extra_arguments=project["title"])
            doc.append(Command("resumeProject", arguments=link_and_name, extra_arguments=[project["nature"], NoEscape(project["duration"])]))
            for description in project["description"]:
                doc.append(Command("resumeItem", arguments=description))

            doc.append(Command("resumeItemListEnd"))

        doc.append(Command("resumeSubHeadingListEnd"))
