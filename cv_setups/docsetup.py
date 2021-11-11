from pylatex import Command, NoEscape, UnsafeCommand

def setup_document(doc):
    doc.preamble.append(Command("setlength", arguments=NoEscape("\\parindent"), extra_arguments="0in"))

    doc.preamble.append(Command("makeatletter"))
    doc.preamble.append(Command("newlength", arguments=NoEscape("\\bibhang")))
    doc.preamble.append(Command("setlength", arguments=NoEscape("\\bibhang"), extra_arguments="0em"))
    doc.preamble.append(Command("newlength", arguments=NoEscape("\\bibsep")))

    doc.preamble.append(NoEscape("{\\@listi \\global\\bibsep\\itemsep \\global\\advance\\bibsep by\\parsep}"))

    doc.preamble.append(Command("newlist", arguments="bibsection", extra_arguments=["itemize", "3"]))
    doc.preamble.append(Command("setlist", options="bibsection", arguments=NoEscape("""
        label=,
        leftmargin=\\bibhang,
        itemindent=-\\bibhang,
        itemsep=\\bibsep,
        parsep=\\z@,
        partopsep=0pt,
        topsep=0pt
    """)))
    doc.preamble.append(Command("newlist", arguments="bibenum", extra_arguments=["enumerate", "3"]))
    doc.preamble.append(Command("setlist", options="bibenum", arguments=NoEscape("""
        label=[\\arabic*], resume
        leftmargin={\\bibhang + \\widthof{[999]}},
        itemindent=-\\bibhang,
        itemsep=0.05in,
        parsep=\\z@,
        partopsep=0pt,
        topsep=0pt
    """)))

    doc.preamble.append(NoEscape("\\let\\oldendbibenum\\endbibenum"))
    doc.preamble.append(NoEscape("\\def\\endbibenum{\\oldendbibenum\\vspace{-.6\\baselineskip}}"))
    doc.preamble.append(NoEscape("\\let\\oldendbibsection\\endbibsection"))
    doc.preamble.append(NoEscape("\\def\\endbibsection{\\oldendbibsection\\vspace{-.6\\baselineskip}}"))
    doc.preamble.append(Command("makeatother"))

    doc.preamble.append(Command("pagestyle", arguments="fancy"))
    doc.preamble.append(Command("pagestyle", arguments="empty"))
    doc.preamble.append(NoEscape("\\fancyhf{}\\renewcommand{\\headrulewidth}{0pt}"))
    doc.preamble.append(NoEscape("\\fancyfootoffset{\\marginparsep+\\marginparwidth}"))
    doc.preamble.append(Command("newlength", arguments=NoEscape("\\footpageshift")))
    doc.preamble.append(Command("setlength", arguments=NoEscape("\\footpageshift"), extra_arguments=NoEscape("0.5\\textwidth+0.5\\marginparsep+0.5\\marginparwidth-2in")))
    doc.preamble.append(NoEscape("""\\lfoot{
        \\hspace{\\footpageshift}
        \\parbox{4in}{
            \\, \\hfill
            \\arabic{page} of
            \\protect\\pageref*{LastPage}
            \\hfill \\,
        }
    }"""))

    doc.preamble.append(Command("hypersetup", arguments="colorlinks,breaklinks,linkcolor=DarkBlue,urlcolor=DarkBlue,anchorcolor=DarkBlue,citecolor=DarkBlue"))

    doc.preamble.append(UnsafeCommand("renewcommand", "\\section", options=1, extra_arguments=NoEscape("""\\pagebreak[3]
        \\vspace{1.3\\baselineskip}
        \\phantomsection\\addcontentsline{toc}{section}{#1}
        \\noindent\\llap{\\scshape\\smash{\\parbox[t]{\\marginparwidth}{\\hyphenpenalty=10000\\raggedright #1}}}
        \\vspace{-\\baselineskip}\\par
    """)))
    doc.preamble.append(Command("newcommand*\\fixendlist", options=1, arguments=NoEscape("""
        \\expandafter\\let\\csname
        preFixEndListend#1\\expandafter\\endcsname\\csname end#1\\endcsname
        \\expandafter\\def\\csname end#1\\endcsname{\\csname preFixEndListend#1\\endcsname\\vspace{-0.6\\baselineskip}}
    """)))

    doc.preamble.append(NoEscape("\\let\\originalItem\\item"))
    doc.preamble.append(Command("newcommand*\\fixouterlist", options=1, arguments=NoEscape("""
        \\expandafter\\let\\csname preFixOuterList#1\\expandafter\\endcsname\\csname #1\\endcsname
        \\expandafter\\def\\csname #1\\endcsname{\\let\\oldItem\\item\\def\\item{\\pagebreak[2]\\oldItem}\\csname preFixOuterList#1\\endcsname}
        \\expandafter\\let\\csname preFixOuterListend#1\\expandafter\\endcsname\\csname end#1\\endcsname
        \\expandafter\\def\\csname end#1\\endcsname{\\let\\item\\oldItem\\csname preFixOuterListend#1\\endcsname}
    """)))
    doc.preamble.append(Command("newcommand*\\fixinnerlist", options=1, arguments=NoEscape("""
        \\expandafter\\let\\csname preFixInnerList#1\\expandafter\\endcsname\\csname #1\\endcsname
        \\expandafter\\def\\csname #1\\endcsname{\\let\\oldItem\\item\\let\\item\\originalItem\\csname preFixInnerList#1\\endcsname}
        \\expandafter\\let\\csname preFixInnerListend#1\\expandafter\\endcsname\\csname end#1\\endcsname
        \\expandafter\\def\\csname end#1\\endcsname{\\csname preFixInnerListend#1\\endcsname\\let\\item\\oldItem}
    """)))

    doc.preamble.append(NoEscape("""\\newlist{outerlist}{itemize}{3}
        \\setlist[outerlist]{label=\\enskip\\textbullet,leftmargin=*}
        \\fixendlist{outerlist}
        \\fixouterlist{outerlist}
    """))
    doc.preamble.append(NoEscape("""\\newlist{lonelist}{itemize}{3}
        \\setlist[lonelist]{label=\\enskip\\textbullet,leftmargin=*,partopsep=0pt,topsep=0pt}
        \\fixendlist{lonelist}
        \\fixouterlist{lonelist}
    """))
    doc.preamble.append(NoEscape("""\\newlist{innerlist}{itemize}{3}
        \\setlist[innerlist]{label=\\enskip\\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
        \\fixinnerlist{innerlist}
    """))
    doc.preamble.append(NoEscape("""\\newlist{loneinnerlist}{itemize}{3}
        \\setlist[loneinnerlist]{label=\\enskip\\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
        \\fixendlist{loneinnerlist}
        \\fixinnerlist{loneinnerlist}
    """))

    doc.preamble.append(Command("newcommand", arguments=NoEscape("\\blankline"), extra_arguments=NoEscape("\\quad\\pagebreak[3]")))
    doc.preamble.append(Command("newcommand", arguments=NoEscape("\\halfblankline"), extra_arguments=NoEscape("\\quad\\vspace{-0.5\\baselineskip}\\pagebreak[3]")))

    doc.preamble.append(Command("urlstyle", arguments="same"))
