from pylatex import NoEscape, Section


def add_license(doc, cv_data):
    def entry(license):
        latex_str = rf"""
            {license["title"]}, \href{{{license["issuer_url"]}}}{{{license["issuer"]}}} \\
            {{Issued {license["issued"]}. }}{f"Expires {license['expiration']}." if "expiration" in license else ""}\vspace{{0.1cm}}
        """
        return latex_str

    with doc.create(Section("Professional Memberships & Licenses")):
        doc.append(
            NoEscape("".join([entry(license) for license in cv_data["license"]]))
        )
