from pylatex import Command, NoEscape, Section


def add_contact(doc, cv_data):
    with doc.create(Section("Contact")):
        doc.append(Command("textbf", arguments=NoEscape("Work E-mail" + " ")))
        for index, email in enumerate(cv_data["contact"]["work_email"]):
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape("mailto:" + email),
                    extra_arguments=email,
                )
            )
            if index != len(cv_data["contact"]["work_email"]) - 1:
                doc.append(", ")

        doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))

        doc.append(Command("textbf", arguments=NoEscape("Personal E-mail" + " ")))
        doc.append(
            Command(
                "href",
                arguments=NoEscape("mailto:" + cv_data["contact"]["email"]),
                extra_arguments=cv_data["contact"]["email"],
            )
        )
        doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))

        doc.append(Command("textbf", arguments="Phone" + " "))
        doc.append(NoEscape(cv_data["contact"]["phone"]))
        doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))

        doc.append(Command("textbf", arguments="Portfolio Websites" + " "))
        doc.append(
            Command(
                "href",
                arguments=NoEscape(cv_data["contact"]["orcid"]),
                extra_arguments="ORCID",
            )
        )
        doc.append(", ")
        doc.append(
            Command(
                "href",
                arguments=NoEscape(cv_data["contact"]["personal_url"]),
                extra_arguments="Personal Website",
            )
        )
        doc.append(", ")
        doc.append(
            Command(
                "href",
                arguments=NoEscape(cv_data["contact"]["github_url"]),
                extra_arguments="GitHub",
            )
        )
        doc.append(", ")
        doc.append(
            Command(
                "href",
                arguments=NoEscape(cv_data["contact"]["linkedin_url"]),
                extra_arguments="LinkedIn",
            )
        )
        doc.append(NoEscape("\n\n\n"))
