from pylatex import Document, Command
from resume_sections import heading, lettercontent
from resume_setups import packages as pkgs, colors, docsetup
import datetime
import json
import sys
import os


def fill_document(doc):
    resume_file = open("./import/resume.json", "r")
    resume_data = json.load(resume_file)
    heading.add_heading(doc, resume_data, doc_type="letter")
    date = datetime.datetime.now()
    recipient = sys.argv[1] if len(sys.argv) > 1 else "Hiring Manager"
    letter_data = open("./import/letter.txt", "r")
    lettercontent.add_content(doc, date, recipient, letter_data, resume_data)
    resume_file.close()
    letter_data.close()


def build_letter(debug, filename="cover-letter"):
    documentclass = Command("documentclass", options=("letterpaper", "11pt"), arguments="article")
    doc = Document(filename, documentclass=documentclass)
    # add resume layout required packages
    pkgs.add_packages(doc)
    colors.add_colors(doc)
    docsetup.setup_document(doc, doc_type="letter")
    fill_document(doc)
    # compile latex file and pdf file
    doc.generate_tex()
    doc.generate_pdf(clean=False, clean_tex=False, compiler="lualatex")
    doc.generate_pdf(clean=(not debug), clean_tex=False, compiler="lualatex")  # compile twice in order for transparent package to work, reference: https://tex.stackexchange.com/questions/297294/pdflatex-transparent-package-seems-not-to-work
    # move files to export directory
    os.rename("./{0}.pdf".format(filename), "./export/{0}.pdf".format(filename))
    os.rename("./{0}.tex".format(filename), "./export/{0}.tex".format(filename))


if __name__ == "__main__":
    build_letter(debug=False)
