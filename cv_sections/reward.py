from pylatex import Command, NoEscape, Section


def add_reward(doc, cv_data):
    with doc.create(Section("Awards")):
        for index, award in enumerate(cv_data["award"]):
            doc.append(Command("textbf", arguments=NoEscape(award["achievement"])))
            doc.append(", ")
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(award["organizer_url"]),
                    extra_arguments=award["organizer"],
                )
            )
            doc.append(Command("hfill", arguments=NoEscape(award["completion"])))
            if index == len(cv_data["award"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))
