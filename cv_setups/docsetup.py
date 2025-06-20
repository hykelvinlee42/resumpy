from pylatex import Command, NoEscape, UnsafeCommand

# list formatting for bibliography section (itemize environment)
SETLIST_BIBSECTION_ARGUMENTS = r"""
    label=,
    leftmargin=\bibhang,
    itemindent=-\bibhang,
    itemsep=\bibsep,
    parsep=\z@,
    partopsep=0pt,
    topsep=0pt
"""


# list formatting for numbered bibliography entries (enumerate environment)
SETLIST_BIBNUM_ARGUMENTS = r"""
    label=[\arabic*], resume,
    leftmargin={\bibhang + \widthof{[999]}},
    itemindent=-\bibhang,
    itemsep=0.05in,
    parsep=\z@,
    partopsep=0pt,
    topsep=0pt
"""

# custom layout for the left footer showing page number and total pages
CUSTOM_LFOOT_LAYOUT = r"""
\lfoot{
    \hspace{\footpageshift}
    \parbox{4in}{
        \, \hfill
        \arabic{page} of
        \protect\pageref*{LastPage}
        \hfill \,
    }
}
"""

# custom section heading format with margin-aligned titles
CUSTOM_SECTION_FORMAT = r"""
\pagebreak[3]
\vspace{1.3\baselineskip}
\phantomsection\addcontentsline{toc}{section}{#1}
\noindent\llap{\scshape\smash{\parbox[t]{\marginparwidth}{\hyphenpenalty=10000\raggedright #1}}}
\vspace{-\baselineskip}\par
"""


def setup_document(doc):
    # disable paragraph indentation
    doc.preamble.append(
        Command("setlength", arguments=NoEscape("\\parindent"), extra_arguments="0in")
    )

    # bibliography spacing setup
    doc.preamble += [
        Command("makeatletter"),
        Command("newlength", arguments=NoEscape("\\bibhang")),
        Command("setlength", arguments=NoEscape("\\bibhang"), extra_arguments="0em"),
        Command("newlength", arguments=NoEscape("\\bibsep")),
        NoEscape(r"{\@listi \global\bibsep\itemsep \global\advance\bibsep by\parsep}"),
    ]

    # define bibliography list environments
    doc.preamble += [
        Command("newlist", arguments="bibsection", extra_arguments=["itemize", "3"]),
        Command(
            "setlist",
            options="bibsection",
            arguments=NoEscape(SETLIST_BIBSECTION_ARGUMENTS),
        ),
        Command("newlist", arguments="bibenum", extra_arguments=["enumerate", "3"]),
        Command(
            "setlist",
            options="bibenum",
            arguments=NoEscape(SETLIST_BIBNUM_ARGUMENTS),
        ),
    ]

    # reduce spacing after bibliography lists
    doc.preamble += [
        NoEscape(r"\let\oldendbibenum\endbibenum"),
        NoEscape(r"\def\endbibenum{\oldendbibenum\vspace{-.6\baselineskip}}"),
        NoEscape(r"\let\oldendbibsection\endbibsection"),
        NoEscape(r"\def\endbibsection{\oldendbibsection\vspace{-.6\baselineskip}}"),
        Command("makeatother"),
    ]

    # page style and footer formatting
    doc.preamble += [
        Command("pagestyle", arguments="fancy"),
        Command("pagestyle", arguments="empty"),
        NoEscape(r"\fancyhf{}\renewcommand{\headrulewidth}{0pt}"),
        NoEscape(r"\fancyfootoffset{\marginparsep+\marginparwidth}"),
        Command("newlength", arguments=NoEscape(r"\footpageshift")),
        Command(
            "setlength",
            arguments=NoEscape(r"\footpageshift"),
            extra_arguments=NoEscape(
                r"0.5\textwidth+0.5\marginparsep+0.5\marginparwidth-2in"
            ),
        ),
        NoEscape(CUSTOM_LFOOT_LAYOUT),
    ]

    # hyperlink color setup
    doc.preamble.append(
        Command(
            "hypersetup",
            arguments="colorlinks,breaklinks,linkcolor=DarkBlue,urlcolor=DarkBlue,anchorcolor=DarkBlue,citecolor=DarkBlue",
        )
    )

    # custom section formatting
    doc.preamble.append(
        UnsafeCommand(
            "renewcommand",
            r"\section",
            options=1,
            extra_arguments=NoEscape(CUSTOM_SECTION_FORMAT),
        )
    )

    # list formatting helpers
    doc.preamble.append(NoEscape(r"\let\originalItem\item"))

    # define list fix macros
    list_macros = {
        "fixendlist": r"""
            \expandafter\let\csname preFixEndListend#1\expandafter\endcsname\csname end#1\endcsname
            \expandafter\def\csname end#1\endcsname{\csname preFixEndListend#1\endcsname\vspace{-0.6\baselineskip}}
        """,
        "fixouterlist": r"""
            \expandafter\let\csname preFixOuterList#1\expandafter\endcsname\csname #1\endcsname
            \expandafter\def\csname #1\endcsname{\let\oldItem\item\def\item{\pagebreak[2]\oldItem}\csname preFixOuterList#1\endcsname}
            \expandafter\let\csname preFixOuterListend#1\expandafter\endcsname\csname end#1\endcsname
            \expandafter\def\csname end#1\endcsname{\let\item\oldItem\csname preFixOuterListend#1\endcsname}
        """,
        "fixinnerlist": r"""
            \expandafter\let\csname preFixInnerList#1\expandafter\endcsname\csname #1\endcsname
            \expandafter\def\csname #1\endcsname{\let\oldItem\item\let\item\originalItem\csname preFixInnerList#1\endcsname}
            \expandafter\let\csname preFixInnerListend#1\expandafter\endcsname\csname end#1\endcsname
            \expandafter\def\csname end#1\endcsname{\csname preFixInnerListend#1\endcsname\let\item\oldItem}
        """,
    }

    for name, body in list_macros.items():
        doc.preamble.append(
            Command(
                "newcommand*",
                arguments=NoEscape(f"\\{name}"),
                options=1,
                extra_arguments=NoEscape(body),
            )
        )

    # define custom list environments
    custom_lists = {
        "outerlist": r"""
            \newlist{outerlist}{itemize}{3}
            \setlist[outerlist]{label=\enskip\textbullet,leftmargin=*}
            \fixendlist{outerlist}
            \fixouterlist{outerlist}
        """,
        "lonelist": r"""
            \newlist{lonelist}{itemize}{3}
            \setlist[lonelist]{label=\enskip\textbullet,leftmargin=*,partopsep=0pt,topsep=0pt}
            \fixendlist{lonelist}
            \fixouterlist{lonelist}
        """,
        "innerlist": r"""
            \newlist{innerlist}{itemize}{3}
            \setlist[innerlist]{label=\enskip\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
            \fixinnerlist{innerlist}
        """,
        "loneinnerlist": r"""
            \newlist{loneinnerlist}{itemize}{3}
            \setlist[loneinnerlist]{label=\enskip\textbullet,leftmargin=*,parsep=0pt,itemsep=0pt,topsep=0pt,partopsep=0pt}
            \fixendlist{loneinnerlist}
            \fixinnerlist{loneinnerlist}
        """,
    }

    for name, body in custom_lists.items():
        doc.preamble.append(NoEscape(body))

    # spacing helpers
    doc.preamble += [
        Command(
            "newcommand",
            arguments=NoEscape(r"\blankline"),
            extra_arguments=NoEscape(r"\quad\pagebreak[3]"),
        ),
        Command(
            "newcommand",
            arguments=NoEscape(r"\halfblankline"),
            extra_arguments=NoEscape(r"\quad\vspace{-0.5\baselineskip}\pagebreak[3]"),
        ),
    ]

    # url formatting
    doc.preamble.append(Command("urlstyle", arguments="same"))
