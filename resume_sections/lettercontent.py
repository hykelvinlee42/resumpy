from pylatex import Command, UnsafeCommand, NoEscape


def add_content(doc, date, recipient, letter_data, resume_data, signature="Signature"):
    doc.append(UnsafeCommand("newcommand", "\\lettercontent", options="1", extra_arguments=NoEscape(r"{}".format("""
        \\justifying \\color{TextBlack} \\avenirnext \\small #1 \\\\
        """))))
    
    doc.append(UnsafeCommand("newcommand", "\\addsignature", options="1", extra_arguments=NoEscape(r"{}".format("""
        \\vspace{.1cm} \\hspace{-.5cm} \\includegraphics[width=4cm]{#1} \\\\
        """))))

    doc.append(Command("lettercontent", arguments=date.strftime("%B %d, %Y\n")))
    doc.append(Command("lettercontent", arguments="Dear {},\n".format(recipient)))
    for line in letter_data.readlines():
        doc.append(Command("lettercontent", arguments="{}".format(line)))
    
    doc.append(Command("lettercontent", arguments="Sincerely,"))
    doc.append(Command("addsignature",  arguments=signature))
    doc.append(Command("lettercontent", arguments="{}".format(resume_data["heading"]["name"])))
