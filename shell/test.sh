#! /usr/bin/bash

f1()
{
    echo $1 $2 $3
    mkdir $1 $2 $3
    return 1
}
f1 lab1 lab2 lab3
