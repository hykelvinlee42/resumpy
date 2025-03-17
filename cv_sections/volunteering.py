from pylatex import Command, NoEscape, Section


def add_committees(doc, cv_data):
    with doc.create(Section("Governance & Oversight Committees")):
        for index, work in enumerate(cv_data["governance"]):
            doc.append(f"{work["duration"]}: {work["title"]}, ")
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(work["organization_url"]),
                    extra_arguments=work["organization"],
                )
            )
            if index == len(cv_data["work"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))


def add_editorials(doc, cv_data):
    with doc.create(Section("Editorials")):
        pass
