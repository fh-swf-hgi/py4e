#!/bin/bash

rm tmp.* *.tmp *.aux
pandoc A0-preface.mkd -o tmp.prefacex.tex
sed < tmp.prefacex.tex 's/section{/section*{/' > tmp.preface.tex
#cat [0-9]*.mkd | python verbatim.py | tee tmp.verbatim | pandoc -s -N -f markdown+definition_lists -t latex --toc --default-image-extension=eps -V lang:ngerman -V highlighting-macros:'\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},fontsize=\small}' -V fontsize:10pt -V documentclass:book --template=template.latex -o tmp.tex
cat [0-9]*.mkd | python verbatim.py | tee tmp.verbatim | pandoc -s -N -f markdown+definition_lists -t latex --toc --default-image-extension=eps -V lang:ngerman -V fontsize:10pt -V documentclass:book -V title-meta="Python für alle" --template=template.latex -o tmp.tex
pandoc [A-Z][A-Z]*.mkd -o tmp.app.tex

sed < tmp.app.tex -e 's/subsubsection{/xyzzy{/' -e 's/subsection{/plugh{/' -e 's/section{/chapter{/' -e 's/xyzzy{/subsection{/' -e 's/plugh{/section{/'  > tmp.appendix.tex

sed < tmp.tex '/includegraphics/s/jpg/eps/' | sed 's"includegraphics{../photos"includegraphics[height=3.0in]{../photos"' | sed 's/\(\\DefineVerbatimEnvironment.*}\)}/\1,fontsize=\\small}/g' > tmp.sed

diff tmp.sed tmp.tex
python texpatch.py < tmp.sed > tmp.patch

mv tmp.patch tmp.tex
./german.sh tmp.tex

pdflatex -shell-escape tmp.tex
pdflatex -shell-escape tmp.tex
mv tmp.pdf x.pdf

echo "Output on x.pdf"
