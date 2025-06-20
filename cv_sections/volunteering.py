from pylatex import NoEscape, Section


def add_committees(doc, cv_data):
    def entry(work):
        latex_str = rf"""
            {work["duration"]}: {work["title"]}, \href{{{work["organization_url"]}}}{{{work["organization"]}}}\vspace{{0.1cm}}
        """
        return latex_str

    with doc.create(Section("Governance & Oversight Committees")):
        doc.append(NoEscape("".join([entry(work) for work in cv_data["governance"]])))


def add_editorials(doc, cv_data):
    with doc.create(Section("Editorials")):
        pass
