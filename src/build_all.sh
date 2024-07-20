all:
    mkdir out -p
    pdflatex -output-directory out main
    makeglossaries-lite main
    TEXMFOUTPUT="out:" bibtex out/main
    pdflatex -output-directory out main
    pdflatex -output-directory out main
