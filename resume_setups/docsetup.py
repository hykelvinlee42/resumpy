from pylatex import Command, NoEscape, UnsafeCommand

CUSTOM_SECTION_FORMAT = r"""
\titleformat{\section}{
    \bfseries \vspace{2pt} \centering \large \color{HeaderBrown} \avenirnextmedium \addfontfeatures{LetterSpace=10}
}{}{0em}{}[\color{SeparatorPink} \transparent{0.5} {\titlerule[0.5pt]} \vspace{-4pt}]
"""

RESUME_ITEM_EXTRA_ARGUMENT = r"""
\item\avenir\small{
    #1 \vspace{-1pt}
}
"""


def setup_document(doc, doc_type="resume"):
    # set page style and clear headers/footers
    doc.preamble += [
        Command("pagestyle", "fancy"),
        Command("fancyhf"),
        Command("fancyfoot"),
        UnsafeCommand("renewcommand", r"\headrulewidth", extra_arguments="0pt"),
        UnsafeCommand("renewcommand", r"\footrulewidth", extra_arguments="0pt"),
    ]

    # adjust margins based on document type
    if doc_type == "resume":
        doc.preamble += [
            UnsafeCommand(
                "addtolength",
                r"\oddsidemargin",
                extra_arguments="-0.5in",
            ),
            UnsafeCommand(
                "addtolength",
                r"\evensidemargin",
                extra_arguments="0in",
            ),
            UnsafeCommand(
                "addtolength",
                r"\textwidth",
                extra_arguments="1in",
            ),
        ]
    elif doc_type == "letter":
        doc.preamble += [
            UnsafeCommand(
                "addtolength",
                r"\oddsidemargin",
                extra_arguments="-0.5in",
            ),
            UnsafeCommand(
                "addtolength",
                r"\evensidemargin",
                extra_arguments="0.05in",
            ),
            UnsafeCommand(
                "addtolength",
                r"\textwidth",
                extra_arguments="5in",
            ),
        ]

    # adjust vertical spacing
    doc.preamble += [
        UnsafeCommand("addtolength", r"\topmargin", extra_arguments="-.5in"),
        UnsafeCommand("addtolength", r"\textheight", extra_arguments="1.0in"),
    ]

    # set url style and text alignment
    doc.preamble += [
        Command("urlstyle", "same"),
        Command("raggedbottom"),
        Command("raggedright"),
    ]

    # remove padding in tables
    doc.preamble.append(
        UnsafeCommand("setlength", r"\tabcolsep", extra_arguments="0in")
    )

    # define custom fonts
    doc.preamble.extend(
        [
            NoEscape(
                r"\newfontfamily{\timesnewroman}{TimesNewRoman}[Path = fonts/, Extension = .ttf]"
            ),
            NoEscape(
                r"\newfontfamily{\avenirnext}{AvenirNext}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=7}]"
            ),
            NoEscape(
                r"\newfontfamily{\avenirnextmedium}{AvenirNext}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=5}]"
            ),
            NoEscape(
                r"\newfontfamily{\avenir}{Avenir}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=0}]"
            ),
            NoEscape(
                r"\newfontfamily{\avenirheavy}{Avenir}[Path = fonts/, Extension = .ttc, UprightFeatures = {FontIndex=4}]"
            ),
        ]
    )

    # customize section title format
    doc.preamble.append(NoEscape(CUSTOM_SECTION_FORMAT))

    # define custom commands for resume formatting
    doc.preamble += [
        UnsafeCommand(
            "newcommand",
            r"\resumeItem",
            options=1,
            extra_arguments=NoEscape(RESUME_ITEM_EXTRA_ARGUMENT),
        ),
        UnsafeCommand(
            "renewcommand",
            r"\labelitemii",
            extra_arguments=NoEscape(r"$\vcenter{\hbox{\small$\bullet$}}$"),
        ),
        UnsafeCommand(
            "newcommand",
            r"\resumeSubHeadingListStart",
            extra_arguments=NoEscape(r"\begin{itemize}[leftmargin=0in, label={}]"),
        ),
        UnsafeCommand(
            "newcommand",
            r"\resumeSubHeadingListEnd",
            extra_arguments=NoEscape(r"\end{itemize}"),
        ),
        UnsafeCommand(
            "newcommand",
            r"\resumeItemListStart",
            extra_arguments=NoEscape(r"\begin{itemize}"),
        ),
        UnsafeCommand(
            "newcommand",
            r"\resumeItemListEnd",
            extra_arguments=NoEscape(r"\end{itemize}\vspace{0pt}"),
        ),
    ]

    # set default text color
    doc.preamble.append(Command("color", arguments="TextBlack"))
