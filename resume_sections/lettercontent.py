from pylatex import Command, NoEscape, UnsafeCommand


def add_content(doc, date, recipient, letter_data, resume_data, signature="Signature"):
    doc.append(
        UnsafeCommand(
            "newcommand",
            r"\lettercontent",
            options="1",
            extra_arguments=NoEscape(
                r"\justifying \color{TextBlack} \avenirnext \small #1 \\"
            ),
        )
    )

    doc.append(
        UnsafeCommand(
            "newcommand",
            r"\addsignature",
            options="1",
            extra_arguments=NoEscape(
                r"\vspace{.1cm} \hspace{-.5cm} \includegraphics[width=4cm]{#1} \\"
            ),
        )
    )

    doc.append(Command("lettercontent", arguments=date.strftime("%B %d, %Y\n")))
    doc.append(Command("lettercontent", arguments="Dear {},\n".format(recipient)))
    letter_data_lines = [line for line in letter_data.readlines() if line != "\n"]
    for line in letter_data_lines:
        doc.append(Command("lettercontent", arguments="{}".format(line)))

    doc.append(Command("lettercontent", arguments="Sincerely,"))
    doc.append(Command("addsignature", arguments=signature))
    doc.append(
        Command("lettercontent", arguments="{}".format(resume_data["heading"]["name"]))
    )
