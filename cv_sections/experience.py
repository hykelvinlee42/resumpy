from pylatex import NoEscape, Section


def add_experience(doc, cv_data):
    def entry(research):
        latex_str = rf"""
            \textbf{{{research["title"]}}}, \href{{{research["organization_url"]}}}{{{research["organization"]}}}
            \hfill{{{research["duration"]}}} \\
            Supervised by \href{{{research["supervisor_url"]}}}{{{research["supervisor"]}}}\vspace{{0.1cm}}
            \begin{{innerlist}}
            {"".join([f"\n\t\t\t\\item {desc}" for desc in research["description"]]) + "\n"}
            \end{{innerlist}}
            \vspace{{0.2cm}}
        """
        return latex_str

    with doc.create(Section("Academic Research Experience")):
        doc.append(
            NoEscape("".join([entry(research) for research in cv_data["research"]]))
        )


def add_projects(doc, cv_data):
    def entry(project):
        latex_str = rf"""
            \textbf{{{project["title"]}}} - \href{{{project["url"]}}}Project Link
            \hfill{{{project["duration"]}}}
            \vspace{{0.1cm}}
            \begin{{innerlist}}
            {"".join([f"\n\t\t\t\\item {desc}" for desc in project["description"]]) + "\n"}
            \end{{innerlist}}
            \vspace{{0.2cm}}
        """
        return latex_str

    with doc.create(Section("Academic Projects")):
        doc.append(
            NoEscape("".join([entry(project) for project in cv_data["experience"]]))
        )


def add_work_experience(doc, cv_data):
    def entry(work):
        latex_str = rf"""
            {work["title"]}, \href{{{work["organization_url"]}}}{{{work["organization"]}}}
            \hfill{{{work["duration"]}}}\vspace{{0.1cm}}
        """
        return latex_str

    with doc.create(Section("Professional Experience")):
        doc.append(NoEscape("".join([entry(work) for work in cv_data["work"]])))
