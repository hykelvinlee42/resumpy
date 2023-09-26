from pylatex import Section, Command, UnsafeCommand, NoEscape


def add_work_experience(doc, resume_data):
    doc.append(UnsafeCommand("newcommand", "\\resumeWork", options="3", extra_arguments=NoEscape(r"{}".format("""
        \\vspace{-1pt}\\item
        \\begin{tabular*}\\textwidth[t]{l@{\\extracolsep{\\fill}}r}
        \\avenirheavy{#1}\\vspace{1pt}\\\\
        \\avenir{#2} & {\\color{TextBlack} \\avenir \\small #3}\\\\
        \\end{tabular*}\\vspace{-4pt}
        \\resumeItemListStart
        """))))
    doc.append(UnsafeCommand("newcommand", "\\resumeWorkNullCompany", options="2", extra_arguments=NoEscape(r"{}".format("""
        \\vspace{-10pt}\\item
        \\begin{tabular*}\\textwidth[t]{l@{\\extracolsep{\\fill}}r}\\\\
        \\avenir{#1} & {\\color{TextBlack} \\avenir \\small #2}\\\\
        \\end{tabular*}\\vspace{-4pt}
        \\resumeItemListStart
        """))))
    with doc.create(Section("WORK EXPERIENCE")):
        doc.append(Command("resumeSubHeadingListStart"))
        for work in resume_data["work"]:
            for index, position in enumerate(work["positions"]):
                if index == 0:
                    doc.append(Command("resumeWork", arguments=NoEscape(work["organization"]), extra_arguments=[NoEscape(position["title"]), NoEscape(position["duration"])]))
                else:
                    doc.append(Command("resumeWorkNullCompany", arguments=NoEscape(position["title"]), extra_arguments=NoEscape(position["duration"])))

                for description in position["description"]:
                    doc.append(Command("resumeItem", arguments=NoEscape(description)))

                doc.append(Command("resumeItemListEnd"))

        doc.append(Command("resumeSubHeadingListEnd"))
