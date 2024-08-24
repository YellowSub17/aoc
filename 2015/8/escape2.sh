

inputf='./input.prod'

nlines=$(cat ${inputf} |wc -l)

printf "number of lines ${nlines}\n"

ncharswnl=$(cat ${inputf} |wc --chars)

###part 1!!!
nchars=$(echo ${ncharswnl}-${nlines} | bc)
printf "number of chars ${nchars}\n"




#cat ${inputf}
#echo
#echo
#sed -E 's/\\x[0-9a-f]{2}/j/g' ${inputf} >output_nohex
#sed -E 's/\\"/j/g' output_nohex  > output_noquotes
#sed -E 's/\\\\/j/g' output_noquotes  > output_noslash
#sed -E 's/"//g' output_noslash  > output_noouter
#cat output_noouter


#sed -E 's/^"/"\"/' ${inputf}  > output_lhsq
#sed -E 's/"$/\""/' output_lhsq  > output_rhsq

sed -E 's/\\x[0-9a-f]{2}/\\\\xjj/g' ${inputf} >output_hex
#sed -E 's/\\"/j/g' output_nohex  > output_noquotes
#sed -E 's/\\\\/j/g' output_noquotes  > output_noslash




nmemwnl=$(cat output_noslash| wc --chars)
nmem=$(echo ${nmemwnl}-${nlines} | bc)

echo ${nmem}


p1ans=$(echo ${nchars}-${nmem}-2 | bc)

echo P1 ANSWER
echo ${p1ans}







