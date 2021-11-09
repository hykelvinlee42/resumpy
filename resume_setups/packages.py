from pylatex.package import Package

packages = {
    "fontspec": None,
    "latexsym": None,
    "fullpage": "empty",
    "titlesec": None,
    "color": None,
    "transparent": None,
    "enumitem": None,
    "hyperref": "hidelinks",
    "fancyhdr": None,
    "tabularx": None,
    "ulem": "normalem"
}


def add_packages(doc):
    for package in packages.keys():
        doc.packages.append(Package(package, packages[package]))
