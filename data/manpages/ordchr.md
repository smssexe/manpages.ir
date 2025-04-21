ORDCHR(3am)							   GNU Awk Extension Modules							   ORDCHR(3am)

NAME
       ordchr - convert characters to strings and vice versa

SYNOPSIS
       @load "ordchr"

       number = ord("A")
       string = chr(65)

DESCRIPTION
       The ordchr extension adds two functions named ord().  and chr(), as follows.

       ord()  This function takes a string argument, and returns the numeric value of the first character in the string.

       chr()  This function takes a numeric argument and returns a string whose first character is that represented by the number.

       These functions are inspired by the Pascal language functions of the same name.

EXAMPLE
       @load "ordchr"
       ...
       printf("The numeric value of 'A' is %d\n", ord("A"))
       printf("The string value of 65 is %s\n", chr(65))

SEE ALSO
       GAWK:  Effective	 AWK  Programming,  filefuncs(3am),  fnmatch(3am), fork(3am), inplace(3am), readdir(3am), readfile(3am), revoutput(3am), rwarray(3am),
       time(3am).

AUTHOR
       Arnold Robbins, arnold@skeeve.com.

COPYING PERMISSIONS
       Copyright © 2012, 2013, 2018, Free Software Foundation, Inc.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the	entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission  is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Feb 02 2018								   ORDCHR(3am)
