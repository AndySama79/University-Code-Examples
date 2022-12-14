#! /usr/bin/bash

x=0
x=x+1
echo $x
x=$x+1
echo $x
x=1
(( x=x+1 ))
echo $x
(expr $x + 1)
echo $x
for (( i=0; i<10; i++ ))
do
    echo $i
done

for i in *
do
    echo $i
done

n=0
for i in `ls`
do
    (( n++ ))
done
echo "no. of files is $n"
