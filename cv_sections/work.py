from pylatex import Command, NoEscape, Section


def add_work_experience(doc, cv_data):
    with doc.create(Section("Professional Experience")):
        for index, work in enumerate(cv_data["work"]):
            doc.append(f"{work["title"]}, ")
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(work["organization_url"]),
                    extra_arguments=work["organization"],
                )
            )
            doc.append(Command("hfill", arguments=NoEscape(work["duration"])))
            if index == len(cv_data["work"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))
