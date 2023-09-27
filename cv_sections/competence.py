from pylatex import Command, NoEscape, Section


def add_competence(doc, cv_data):
    with doc.create(Section("Competences")):
        doc.append(Command("textbf", arguments=NoEscape("Techniques" + " ")))
        techniques = ""
        for index, technique in enumerate(cv_data["technique"]):
            techniques += technique + (
                ", " if index < len(cv_data["technique"]) - 1 else ""
            )

        doc.append(NoEscape(techniques))
