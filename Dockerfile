FROM python:3.11-bookworm
WORKDIR /runtime
COPY requirements.txt /runtime/
RUN pip install -r requirements.txt
RUN apt update && apt install -y \
    texlive-latex-recommended texlive-latex-extra texlive-luatex
COPY cv.py /runtime/
COPY resume.py /runtime/
COPY letter.py /runtime/
COPY Signature.png /runtime/
CMD python cv.py && python resume.py && python letter.py
