#!/bin/bash
# replacements in tex file

tex_file="$1"

# pandoc seems to have issues with german quotation marks in certain situations:
sed -i 's/?``/?{``}/g' "$tex_file" # closing german quotation mark after '?'
sed -i 's/!``/!{``}/g' "$tex_file" # closing german quotation mark after '!'

# adding thin spaces in-between abbreviations:
sed -i 's/i\. d\. R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/I\. d\. R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/z\. B\./z\.\\thinspace{}B\./g' "$tex_file"
sed -i 's/Z\. B\./Z\.\\thinspace{}B\./g' "$tex_file"
sed -i 's/d\. h\./d\.\\thinspace{}h\./g' "$tex_file"
sed -i 's/D\. h\./D\.\\thinspace{}h\./g' "$tex_file"

# adding thin spaces in-between abbreviations (pandoc inserts a '~' in some cases):
sed -i 's/i\.~d\.~R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/I\.~d\.~R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/i\. d\.~R\./i\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/I\. d\.~R\./I\.\\thinspace{}d\.\\thinspace{}R\./g' "$tex_file"
sed -i 's/z\.~B\./z\.\\thinspace{}B\./g' "$tex_file"
sed -i 's/Z\.~B\./Z\.\\thinspace{}B\./g' "$tex_file"
sed -i 's/d\.~h\./d\.\\thinspace{}h\./g' "$tex_file"
sed -i 's/D\.~h\./D\.\\thinspace{}h\./g' "$tex_file"
