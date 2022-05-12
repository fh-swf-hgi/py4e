#! /bin/bash

rm tmp.* *.tmp *.aux solutions.mkd &>/dev/null

python3 generate_mkd.py

cat solutions.mkd | python verbatim.py | tee tmp.verbatim | pandoc -s -N -f markdown+definition_lists -t latex --toc --default-image-extension=eps -V lang:de-DE -V langbabel:ngerman -V fontsize:10pt -V documentclass:book -V title-meta="Python für alle – Lösungen" -V linestretch:1.0 --template=template.latex -o tmp.tex

sed < tmp.tex '/includegraphics/s/jpg/eps/' | sed 's"includegraphics{../photos"includegraphics[height=3.0in]{../photos"' > tmp.sed
diff tmp.sed tmp.tex
python texpatch.py < tmp.sed > tmp.patch

mv tmp.patch tmp.tex
./german.sh tmp.tex

pdflatex -shell-escape tmp.tex
pdflatex -shell-escape tmp.tex
mv tmp.pdf py4e-de-loesungen.pdf

if [[ "$OSTYPE" == "darwin"* ]]; then
  open py4e-de-loesungen.pdf
elif [[ "$OSTYPE" == "linux-gnu" && -n "$DISPLAY" ]]; then
  xdg-open py4e-de-loesungen.pdf
else
  echo "Output on py4e-de-loesungen.pdf"
fi

rm tmp.* *.tmp *.aux solutions.mkd &>/dev/null
