import json
import shutil
import sys

from cv_sections import (
    contact,
    education,
    experience,
    heading,
    interests,
    license,
    reward,
    volunteering,
)
from cv_setups import colors, docsetup
from cv_setups import packages as pkgs
from pylatex import Command, Document


def fill_document(doc):
    cv_file = open("./import/cv.json")
    cv_data = json.load(cv_file)
    heading.add_heading(doc, cv_data)
    contact.add_contact(doc, cv_data)
    interests.add_research_interests(doc, cv_data)
    education.add_education(doc, cv_data)
    reward.add_reward(doc, cv_data)
    experience.add_experience(doc, cv_data)
    experience.add_projects(doc, cv_data)
    experience.add_work_experience(doc, cv_data)
    volunteering.add_committees(doc, cv_data)
    # volunteering.add_editorials(doc, cv_data)
    license.add_license(doc, cv_data)
    cv_file.close()


def build_cv(debug, compiler, filename="cv"):
    documentclass = Command(
        "documentclass", options=("letterpaper", "10pt"), arguments="article"
    )
    doc = Document(filename, documentclass=documentclass, fontenc=None, inputenc=None)
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

    build_cv(debug=False, compiler=compiler)
