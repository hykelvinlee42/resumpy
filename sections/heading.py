from pylatex import Section, Command, UnsafeCommand, NoEscape

def add_heading(doc, resume_data):
    doc.append(UnsafeCommand("newcommand", "\\resumeHeading", options=8, extra_arguments=NoEscape(r"{}".format("""
        \\begin{center}
            \\color{SeparatorPink} \\transparent{0.5}\\rule{0.8\\textwidth}{1pt} \\\\ \\vspace{1pt}
            \\color{HeaderBrown}
            \\transparent{1.0}
            \\href{#2}{\\timesnewroman \\Large \\addfontfeatures{LetterSpace=15} \\MakeUppercase{#1}} \\\\ \\vspace{5pt}
            {\\avenirnext \\small {Github: \\href{#4}{\\uline{@#3}}} \\hspace{2pt} {LinkedIn: \\href{#6}{\\uline{@#5}}} \\hspace{2pt} {#7} \\hspace{2pt} {\\href{mailto:#8}{\\uline{#8}}}}
            \\vspace{0pt} \\color{SeparatorPink} \\transparent{0.5} \\rule{0.8\\textwidth}{3pt}
        \\end{center}
        """))))
    doc.append(Command("resumeHeading", resume_data["heading"]["name"], extra_arguments=[resume_data["heading"]["personal_url"], resume_data["heading"]["github_handle"], resume_data["heading"]["github_url"], resume_data["heading"]["linkedin_handle"], resume_data["heading"]["linkedin_url"], NoEscape(resume_data["heading"]["phone"]), resume_data["heading"]["email"]]))
