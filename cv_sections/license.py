from pylatex import Command, NoEscape, Section


def add_license(doc, cv_data):
    with doc.create(Section("Professional Memberships & Licenses")):
        for index, license in enumerate(cv_data["license"]):
            doc.append(Command("textbf", arguments=NoEscape(license["title"])))
            date = f"Issued {license['issued']}"
            if "expiration" in license:
                date += f". Expires {license['expiration']}"

            doc.append(Command("hfill", arguments=NoEscape(f"{date}")))
            doc.append(NoEscape("\\\\"))
            doc.append(
                Command(
                    "href",
                    arguments=NoEscape(license["issuer_url"]),
                    extra_arguments=license["issuer"],
                )
            )
            if index == len(cv_data["license"]) - 1:
                doc.append(NoEscape("\n\n\n"))
            else:
                doc.append(NoEscape("\n\\vspace{0.1cm}\n\n"))
