from pylatex import NoEscape, Section


def add_education(doc, cv_data):
    def entry(education):
        latex_str = rf"""
            \textbf{{{education["degree"]}}}, \href{{{education["school_url"]}}}{{{education["school"]}}}
            \hfill{{{education["completion"]}}}
        """
        return latex_str

    with doc.create(Section("Education")):
        doc.append(
            NoEscape("".join([entry(education) for education in cv_data["education"]]))
        )
