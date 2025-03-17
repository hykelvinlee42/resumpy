from pylatex import NoEscape, Section


def add_research_interests(doc, cv_data):
    with doc.create(Section("Research Interests")):
        techniques = ""
        for index, technique in enumerate(cv_data["interests"]):
            techniques += technique + (
                ", " if index < len(cv_data["interests"]) - 1 else ""
            )

        doc.append(NoEscape(techniques))
