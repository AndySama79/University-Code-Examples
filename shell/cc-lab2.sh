#!/bin/bash

# output the contents of a file on the terminal.
# no. of arguments: 1
# Argument1: filename

mycat()
{	
	cat $1
	# echo "not implemented"
}

# 
# print the following exactly as is from the lscpu output.
# CPU(s):                          8
# On-line CPU(s) list:             0-7
# Thread(s) per core:              2
# Core(s) per socket:              4
# Socket(s):                       1
#
# you could use any temporary file you want.
# just name it as prefixed with temp.lscpu.

lscpuinfo()
{	
	cat temp.lscpu | grep "CPU(s):" | head -1
	cat temp.lscpu | grep "On-line CPU(s) list:" | head -1
	cat temp.lscpu | grep "Thread(s) per core:" | head -1
	cat temp.lscpu | grep "Core(s) per socket:" | head -1
	cat temp.lscpu | grep "Socket(s):" | head -1
	# echo "not implemented"
}

# given a file in argument 1, return '0' if
# the file is an C program executable else 1

is_exe()
{
	out=`file $1 | awk -F"," '{print $1}'`
	ext=`echo $1 | awk -F"." '{print $NF}'`
	if [[ $out =~ "executable" ]]; then
		echo 0
	else
		echo 1
	fi
}

# given a file in argument 1, return 0 if
# the file is an C program object file else 1

is_object()
{
	out=`file $1`
	ext=`echo $1 | awk -F"." '{print $NF}'`
	if [[ $out =~ "ELF 64-bit LSB relocatable" ]]; then
		echo 0
	else
		echo 1
	fi
}

# given a file in argument 1, return 0 if
# the file is an C program source file else 1

is_C()
{
	out=`file $1`
	ext=`echo $1 | awk -F"." '{print $NF}'`
	if [[ $1 =~ ".c" ]]; then
		echo 0
	else
		echo 1
	fi
}

# given a file in argument 1, return 0 if
# the file is a text  file else 1

is_text()
{
	out=`file $1`
	ext=`echo $1 | awk -F"." '{print $NF}'`
	if [[ $1 =~ ".txt" ]]; then
		echo 0
	else
		echo 1
	fi
}

# given a file in argument 1, return 0 if
# the file is an assembler source file 1 false

is_assembler()
{
	out=`file $1`
	ext=`echo $1 | awk -F"." '{print $NF}'`
	if [[ $out =~ "assembler source" ]]; then
		echo 0
	else
		echo 1
	fi
}

# Output the file names:type of file 
# Total no. of arguments: 5
# Arguments 1-5 : All arguments are file names.
# output the file types of each of that file.
# Output should be of the following format.
# file1:assembler
# file2:executable
# file3:object
# file4:C
# file5:text
# Note the lack of any space inbetween. 
# In the above , replace file1, file2.. etc to be
# the name given in the arguments.
# print "none" in the right column if you cannot find
# which kind of file it is or it is in a format that
# is other than what is listed above.

filetypes()
{
	for file in "$@"
	do
		type="none"
		if [[ `is_exe $file` -eq 0 ]]; then
			type="executable"
		elif [[ `is_object $file` -eq 0 ]]; then
			type="object"
		elif [[ `is_text $file` -eq 0 ]]; then
			type="text"
		elif [[ `is_C $file` -eq 0 ]]; then
			type="C"
		elif [[ `is_assembler $file` -eq 0 ]]; then
			type="assembler"
		fi
		echo "$file:$type"
	done
}
#!/bin/bash
 
# output the contents of a file on the terminal.
# no. of arguments: 1
# Argument1: filename
 
mycat()
{	
	cat $1
	# echo "not implemented"
}
 
# 
# print the following exactly as is from the lscpu output.
# CPU(s):                          8
# On-line CPU(s) list:             0-7
# Thread(s) per core:              2
# Core(s) per socket:              4
# Socket(s):                       1
#
# you could use any temporary file you want.
# just name it as prefixed with temp.lscpu.
 
lscpuinfo()
{	
	cat temp.lscpu | grep "CPU(s):" | head -1
	cat temp.lscpu | grep "On-line CPU(s) list:" | head -1
	cat temp.lscpu | grep "Thread(s) per core:" | head -1
	cat temp.lscpu | grep "Core(s) per socket:" | head -1
	cat temp.lscpu | grep "Socket(s):" | head -1
	# echo "not implemented"
}
 
# given a file in argument 1, return '0' if
# the file is an C program executable else 1
 
is_exe()
{
	out=`file $1 | awk -F"," '{print $1}'`
	if [[ $out =~ "executable" ]]; then
		echo 0
	else
		echo 1
	fi
}
 
# given a file in argument 1, return 0 if
# the file is an C program object file else 1
 
is_object()
{
	out=`file $1`
	if [[ $out =~ "ELF 64-bit LSB relocatable" ]]; then
		echo 0
	else
		echo 1
	fi
}
 
# given a file in argument 1, return 0 if
# the file is an C program source file else 1
 
is_C()
{
	out=`file $1`
	if [[ $1 =~ ".c" ]]; then
		echo 0
	else
		echo 1
	fi
}
 
# given a file in argument 1, return 0 if
# the file is a text  file else 1
 
is_text()
{
	out=`file $1`
	if [[ $1 =~ ".txt" ]]; then
		echo 0
	else
		echo 1
	fi
}
 
# given a file in argument 1, return 0 if
# the file is an assembler source file 1 false
 
is_assembler()
{
	out=`file $1`
	if [[ $out =~ "assembler source" ]]; then
		echo 0
	else
		echo 1
	fi
}
 
# Output the file names:type of file 
# Total no. of arguments: 5
# Arguments 1-5 : All arguments are file names.
# output the file types of each of that file.
# Output should be of the following format.
# file1:assembler
# file2:executable
# file3:object
# file4:C
# file5:text
# Note the lack of any space inbetween. 
# In the above , replace file1, file2.. etc to be
# the name given in the arguments.
# print "none" in the right column if you cannot find
# which kind of file it is or it is in a format that
# is other than what is listed above.
 
filetypes()
{
	for file in "$@"
	do
		type="none"
		if [[ `is_exe $file` -eq 0 ]]; then
			type="executable"
		elif [[ `is_object $file` -eq 0 ]]; then
			type="object"
		elif [[ `is_text $file` -eq 0 ]]; then
			type="text"
		elif [[ `is_C $file` -eq 0 ]]; then
			type="C"
		elif [[ `is_assembler $file` -eq 0 ]]; then
			type="assembler"
		fi
		echo "$file:$type"
	done
}