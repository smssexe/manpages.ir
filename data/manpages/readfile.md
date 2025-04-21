READFILE(3am)							   GNU Awk Extension Modules							 READFILE(3am)

NAME
       readfile - return the entire contents of a file as a string

SYNOPSIS
       @load "readfile"

       result = readfile("/some/path")

       For making whole files be single records:

       @load "readfile"
       BEGIN { PROCINFO["readfile"] = 1 }

DESCRIPTION
       The readfile extension adds a single function named readfile().	The argument is the name of the file to read.  The return value is a string containing
       the entire contents of the requested file.

       Upon error, the function returns the empty string and sets ERRNO.

       In  addition, it adds an input parser that is activated if PROCINFO["readfile"] exists.	When activated, each input file is returned in its entirety as
       $0.  RT is set to the null string.

EXAMPLE
       @load "readfile"
       ...
       contents = readfile("/path/to/file");
       if (contents == "" && ERRNO != "") {
	   print("problem reading file", ERRNO) > "/dev/stderr"
	   ...
       }

SEE ALSO
       GAWK: Effective AWK Programming, filefuncs(3am),	 fnmatch(3am),	fork(3am),  inplace(3am),  ordchr(3am),	 readdir(3am),	revoutput(3am),	 rwarray(3am),
       time(3am).

AUTHOR
       Arnold Robbins, arnold@skeeve.com.

COPYING PERMISSIONS
       Copyright © 2012, 2013, 2014, 2018, Free Software Foundation, Inc.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission  is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified  versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Feb 02 2018								 READFILE(3am)
