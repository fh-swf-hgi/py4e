#!/bin/bash
# replacements in tex file

tex_file="$1"

# pandoc seems to have issues with german quotation marks in certain situations:
sed -i -e 's/?``/?{``}/g' "$tex_file" # closing german quotation mark after '?'
sed -i -e 's/!``/!{``}/g' "$tex_file" # closing german quotation mark after '!'
