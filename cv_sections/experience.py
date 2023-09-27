from pylatex import Command, NoEscape, Section


def add_experience(doc, cv_data):
    with doc.create(Section("Research Experience")):
        for index, research in enumerate(cv_data["research"]):
            doc.append(Command("textbf", arguments=NoEscape(research["title"])))
            doc.append(", ")
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(research["organization_url"]),
                    extra_arguments=research["organization"],
                )
            )
            doc.append(Command("hfill", arguments=NoEscape(research["duration"])))
            doc.append(NoEscape("\\\\Supervised by "))
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(research["supervisor_url"]),
                    extra_arguments=research["supervisor"],
                )
            )
            doc.append(Command("begin", arguments="innerlist"))
            for description in research["description"]:
                doc.append(Command("item", arguments=NoEscape(description)))

            doc.append(Command("end", arguments="innerlist"))
            if index == len(cv_data["research"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))

    with doc.create(Section("Academic Projects")):
        for index, experience in enumerate(cv_data["experience"]):
            doc.append(Command("textbf", arguments=(experience["title"] + " - ")))
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(experience["url"]),
                    extra_arguments="Project Link",
                )
            )
            doc.append(Command("hfill", arguments=NoEscape(experience["duration"])))
            doc.append(Command("begin", arguments="innerlist"))
            for description in experience["description"]:
                doc.append(Command("item", arguments=NoEscape(description)))

            doc.append(Command("end", arguments="innerlist"))
            if index == len(cv_data["experience"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))
