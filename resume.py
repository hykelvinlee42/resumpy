from pylatex import Document, Command, NoEscape
from sections import heading, overview, work, experience, education
import packages as pkgs
import docsetup
import colors
import json
import os


def fill_document(doc):
    resume_file = open("./resume.json")
    resume_data = json.load(resume_file)
    heading.add_heading(doc, resume_data)
    overview.add_overview(doc, resume_data)
    work.add_work_experience(doc, resume_data)
    experience.add_experience(doc, resume_data)
    education.add_education(doc, resume_data)


def build_resume(debug, directory="./generated_resume/", filename="resume"):
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
    doc.generate_pdf(clean=(not debug), clean_tex=False, compiler="lualatex")  # compile twice in order for transparent package to work, reference: https://tex.stackexchange.com/questions/297294/pdflatex-transparent-package-seems-not-to-work


if __name__ == "__main__":
    build_resume(debug=False)
