#!/bin/bash
# replacements in tex file

tex_file="$1"

# pandoc seems to have issues with german quotation marks in certain situations:
sed -i -e 's/?``/?{``}/g' "$tex_file" # closing german quotation mark after '?'
sed -i -e 's/!``/!{``}/g' "$tex_file" # closing german quotation mark after '!'

# adding thin spaces in-between abbreviations:
sed -i -e 's/i\. d\. R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/I\. d\. R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/z\. B\./z\.\\thinspace{}B\./g' "$tex_file"
sed -i -e 's/Z\. B\./Z\.\\thinspace{}B\./g' "$tex_file"
sed -i -e 's/d\. h\./d\.\\thinspace{}h\./g' "$tex_file"
sed -i -e 's/D\. h\./D\.\\thinspace{}h\./g' "$tex_file"

# adding thin spaces in-between abbreviations (pandoc inserts a '~' in some cases):
sed -i -e 's/i\.~d\.~R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/I\.~d\.~R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/i\. d\.~R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/I\. d\.~R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i -e 's/z\.~B\./z\.\\thinspace{}B\./g' "$tex_file"
sed -i -e 's/Z\.~B\./Z\.\\thinspace{}B\./g' "$tex_file"
sed -i -e 's/d\.~h\./d\.\\thinspace{}h\./g' "$tex_file"
sed -i -e 's/D\.~h\./D\.\\thinspace{}h\./g' "$tex_file"
