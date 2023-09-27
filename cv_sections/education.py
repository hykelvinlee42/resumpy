from pylatex import Command, NoEscape, Section


def add_education(doc, cv_data):
    with doc.create(Section("Education")):
        for index, education in enumerate(cv_data["education"]):
            doc.append(Command("textbf", arguments=NoEscape(education["degree"])))
            doc.append(", ")
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(education["school_url"]),
                    extra_arguments=education["school"],
                )
            )
            doc.append(Command("hfill", arguments=NoEscape(education["completion"])))
            if index == len(cv_data["education"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))
