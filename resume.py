from pylatex import Document, Command, NoEscape
from sections import overview, work, experience, education
import packages as pkgs
import docsetup
import colors
import json
import os


def add_heading(doc, resume_data):
    doc.append(Command("begin", arguments="center"))
    doc.append(NoEscape(r"{}".format("""
        \\color{SeparatorPink} \\transparent{0.5}\\rule{0.8\\textwidth}{1pt} \\\\ \\vspace{1pt}
        \\color{HeaderBrown} \\transparent{1.0}
        """)))

    doc.append(NoEscape(r"{}".format("\\href{" + resume_data["heading"]["personal_url"] + "}{\\timesnewroman \\Large \\addfontfeatures{LetterSpace=15} \\MakeUppercase{" + resume_data["heading"]["name"] + "}} \\\\ \\vspace{5pt}")))

    doc.append(NoEscape(r"{}".format("{\\avenirnext \\small {Github: \\href{" + resume_data["heading"]["github_url"] + "}{\\uline{" + resume_data["heading"]["github_handle"] + "}}} \\hspace{2pt} {LinkedIn: \\href{" + resume_data["heading"]["linkedin_url"] + "}{\\uline{" + resume_data["heading"]["linkedin_handle"] + "}}} \\hspace{2pt} {" + resume_data["heading"]["phone"] + "} \\hspace{2pt} {\\href{mailto:" + resume_data["heading"]["email"] + "}{\\uline{" + resume_data["heading"]["email"] + "}}}}")))

    doc.append(NoEscape(r"{}".format("""
        \\vspace{0pt} \\color{SeparatorPink} \\transparent{0.5} \\rule{0.8\\textwidth}{3pt}
        """)))
    doc.append(Command("end", arguments="center"))


def fill_document(doc):
    resume_file = open("resume.json")
    resume_data = json.load(resume_file)
    add_heading(doc, resume_data)
    overview.add_overview(doc, resume_data)
    work.add_work_experience(doc, resume_data)
    experience.add_experience(doc, resume_data)
    education.add_education(doc, resume_data)


def build_resume(directory="./generated_resume/", filename="resume"):
    documentclass = Command("documentclass", options=("letterpaper", "11pt"), arguments="article")
    doc = Document(filename, documentclass=documentclass)
    # add resume layout required packages
    pkgs.add_packages(doc)
    # add defined colors
    colors.add_colors(doc)
    docsetup.setup_document(doc)
    fill_document(doc)
    # compile latex file and pdf file
    doc.generate_tex()
    doc.generate_pdf(clean=False, clean_tex=False, compiler="lualatex")
    doc.generate_pdf(clean=False, clean_tex=False, compiler="lualatex")  # compile twice in order for transparent package to work, reference: https://tex.stackexchange.com/questions/297294/pdflatex-transparent-package-seems-not-to-work


if __name__ == "__main__":
    build_resume()
