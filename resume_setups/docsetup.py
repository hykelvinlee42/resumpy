from pylatex import Command, NoEscape, UnsafeCommand

def setup_document(doc):
    doc.preamble.append(Command("pagestyle", "fancy"))
    doc.preamble.append(Command("fancyhf", ""))
    doc.preamble.append(Command("fancyfoot", ""))

    doc.preamble.append(Command("renewcommand", NoEscape("\\headrulewidth"), extra_arguments="0pt"))
    doc.preamble.append(Command("renewcommand", NoEscape("\\footrulewidth"), extra_arguments="0pt"))

    doc.preamble.append(Command("addtolength", NoEscape("\\oddsidemargin"), extra_arguments=NoEscape("-0.5in")))
    doc.preamble.append(Command("addtolength", NoEscape("\\evensidemargin"), extra_arguments=NoEscape("0in")))
    doc.preamble.append(Command("addtolength", NoEscape("\\textwidth"), extra_arguments=NoEscape("1in")))
    doc.preamble.append(Command("addtolength", NoEscape("\\topmargin"), extra_arguments=NoEscape("-.5in")))
    doc.preamble.append(Command("addtolength", NoEscape("\\textheight"), extra_arguments=NoEscape("1.0in")))

    doc.preamble.append(Command("urlstyle", "same"))

    doc.preamble.append(Command("raggedbottom"))
    doc.preamble.append(Command("raggedright"))

    doc.preamble.append(Command("setlength", NoEscape("\\tabcolsep"), extra_arguments="0in"))

    doc.preamble.append(NoEscape("\\newfontfamily{\\timesnewroman}{TimesNewRoman}[Path = fonts/, Extension = .ttf]"))
    doc.preamble.append(NoEscape("\\newfontfamily{\\avenirnext}{AvenirNext}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=7}]"))
    doc.preamble.append(NoEscape("\\newfontfamily{\\avenirnextmedium}{AvenirNext}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=5}]"))
    doc.preamble.append(NoEscape("\\newfontfamily{\\avenir}{Avenir}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=0}]"))
    doc.preamble.append(NoEscape("\\newfontfamily{\\avenirheavy}{Avenir}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=4}]"))

    doc.preamble.append(NoEscape("\\titleformat{\\section}{\n\t\t\\bfseries \\vspace{2pt} \\centering \\large \\color{HeaderBrown} \\avenirnextmedium \\addfontfeatures{LetterSpace=10}\n}{}{0em}{}[\\color{SeparatorPink} \\transparent{0.5} {\\titlerule[0.5pt]} \\vspace{-4pt}]"))

    doc.preamble.append(UnsafeCommand("newcommand", "\\resumeItem", options=1, extra_arguments=NoEscape(r"{}".format("""\\item\\avenir\\small{
            #1 \\vspace{-1pt}
    }
    """))))
    doc.preamble.append(UnsafeCommand("renewcommand", "\\labelitemii", options=None, extra_arguments=NoEscape(r"{}".format("""$\\vcenter{\\hbox{\\small$\\bullet$}}$"""))))
    doc.preamble.append(UnsafeCommand("newcommand", "\\resumeSubHeadingListStart", options=None, extra_arguments=NoEscape(r"{}".format("""\\begin{itemize}[leftmargin=0in, label={}]"""))))
    doc.preamble.append(UnsafeCommand("newcommand", "\\resumeSubHeadingListEnd", options=None, extra_arguments=NoEscape(r"{}".format("""\\end{itemize}"""))))
    doc.preamble.append(UnsafeCommand("newcommand", "\\resumeItemListStart", options=None, extra_arguments=NoEscape(r"{}".format("""\\begin{itemize}"""))))
    doc.preamble.append(UnsafeCommand("newcommand", "\\resumeItemListEnd", options=None, extra_arguments=NoEscape(r"{}".format("""\\end{itemize}\\vspace{0pt}"""))))
    
    doc.preamble.append(Command("color", arguments="TextBlack"))
