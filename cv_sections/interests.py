from pylatex import NoEscape, Section


def add_research_interests(doc, cv_data):
    with doc.create(Section("Research Interests")):
        doc.append(NoEscape(", ".join(cv_data["interests"])))
