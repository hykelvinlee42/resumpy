from pylatex import NoEscape, Section


def add_contact(doc, cv_data):
    def entry(contact):
        latex_str = rf"""
            \textbf{{Work E-mail}}: 
            {", ".join([f"\\href{{mailto:{email}}}{{{email}}}" for email in contact["work_email"]])} \\
            \textbf{{Personal E-mail}}: 
            \href{{mailto:{contact["email"]}}}{{{contact["email"]}}} \\
            \textbf{{Phone}}: {contact["phone"]} \\
            \textbf{{Portfolio Websites}}:
            \href{{{contact["orcid"]}}}{{ORCID}},
            \href{{{contact["personal_url"]}}}{{Personal Website}},
            \href{{{contact["github_url"]}}}{{GitHub}},
            \href{{{contact["linkedin_url"]}}}{{LinkedIn}}
        """
        return NoEscape(latex_str)

    with doc.create(Section("Contact")):
        doc.append(entry(cv_data["contact"]))
