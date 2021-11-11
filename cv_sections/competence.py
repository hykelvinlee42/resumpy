from pylatex import Section, Command, NoEscape


def add_competence(doc, cv_data):
    with doc.create(Section("Competences")):
        doc.append(Command("textbf", arguments=NoEscape("Techniques" + " ")))
        techniques = ""
        for technique in cv_data["technique"]:
            techniques += (technique + ", ")
        
        doc.append(NoEscape(techniques))
