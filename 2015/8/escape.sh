

inputf='./input.prod'


nlines=$(cat ${inputf} |wc -l)

printf "number of lines ${nlines}\n"

ncharswnl=$(cat ${inputf} |wc --chars)

###part 1!!!
nchars=$(echo ${ncharswnl}-${nlines} | bc)
printf "number of chars ${nchars}\n"



sed -E 's/z/j/g' ${inputf} > js2ws
sed -E 's/y/j/g' ${inputf} > js2ws
sed -E 's/w/j/g' ${inputf} > js2ws



#crop the start and end quotes
sed -E 's/^"//' ${inputf} >output_lhs
sed -E 's/"$//' output_lhs > output_rhs


#replace every hex code with a z
sed -E 's/\\x[0-9a-f]{2}/z/g' output_rhs > output_hex

#replace every \" with a y
sed -E 's/\\"/y/g' output_hex  > output_quotes

#replace every \\\\ with a w
sed -E 's/\\\\/w/g' output_quotes  > output_slash






nmemwnl=$(cat output_slash| wc --chars)
nmem=$(echo ${nmemwnl}-${nlines} | bc)

#echo ${nmem}


p1ans=$(echo ${nchars}-${nmem}-2 | bc)

echo P1 ANSWER
echo ${p1ans}













