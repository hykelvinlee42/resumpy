from pylatex import NoEscape, Section


def add_reward(doc, cv_data):
    def entry(award):
        latex_str = rf"""
            {award["achievement"]}, \href{{{award["organizer_url"]}}}{{{award["organizer"]}}}
            \hfill{{{award["completion"]}}}
        """
        return latex_str

    with doc.create(Section("Honours and Awards")):
        doc.append(NoEscape("".join([entry(award) for award in cv_data["award"]])))
