#!/bin/bash

# german-specific replacements in tex file, because pandoc messes up some things

tex_file="$1"

sed -i -e 's/?``/?{``}/g' "$tex_file" # closing german quotation mark after '?'
sed -i -e 's/!``/!{``}/g' "$tex_file" # closing german quotation mark after '!'
