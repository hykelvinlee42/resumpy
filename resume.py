import json
import shutil
import sys

from pylatex import Command, Document

from resume_sections import (education, experience, heading, overview,
                             volunteering, work)
from resume_setups import colors, docsetup
from resume_setups import packages as pkgs


def fill_document(doc):
    resume_file = open("./import/resume.json")
    resume_data = json.load(resume_file)
    heading.add_heading(doc, resume_data)
    overview.add_overview(doc, resume_data)
    work.add_work_experience(doc, resume_data)
    volunteering.add_volunteering(doc, resume_data)
    experience.add_experience(doc, resume_data)
    education.add_education(doc, resume_data)
    resume_file.close()


def build_resume(debug, compiler, filename="resume"):
    documentclass = Command(
        "documentclass", options=("letterpaper", "11pt"), arguments="article"
    )
    doc = Document(filename, documentclass=documentclass)
    # add resume layout required packages
    pkgs.add_packages(doc)
    colors.add_colors(doc)
    docsetup.setup_document(doc)
    fill_document(doc)
    # compile latex file and pdf file
    doc.generate_tex()
    doc.generate_pdf(clean=False, clean_tex=False, compiler=compiler)
    doc.generate_pdf(
        clean=(not debug), clean_tex=False, compiler=compiler
    )  # compile twice in order for transparent package to work, reference: https://tex.stackexchange.com/questions/297294/pdflatex-transparent-package-seems-not-to-work
    # move files to export directory
    shutil.move("./{0}.pdf".format(filename), "./export/{0}.pdf".format(filename))
    shutil.move("./{0}.tex".format(filename), "./export/{0}.tex".format(filename))


if __name__ == "__main__":
    compiler = None
    try:
        compiler = sys.argv[1]
    except:
        pass

    build_resume(debug=False, compiler=compiler)
