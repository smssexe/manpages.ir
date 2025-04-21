REVOUTPUT(3am)							   GNU Awk Extension Modules							REVOUTPUT(3am)

NAME
       revoutput - Reverse output strings sample extension

SYNOPSIS
       @load "revoutput"

       BEGIN { REVOUT = 1 }    # Reverse all output strings

DESCRIPTION
       The  revoutput  extension  adds a simple output wrapper that reverses the characters in each output line.  It's main purpose is to show how to write an
       output wrapper, although it may be mildly amusing for the unwary.

EXAMPLE
       @load "revoutput"

       BEGIN {
	   REVOUT = 1
	   print "hello, world" > "/dev/stdout"
       }

       The output from this program is:

       dlrow ,olleh

BUGS
       This extension does not affect the default standard output.

SEE ALSO
       GAWK: Effective AWK Programming,	 filefuncs(3am),  fnmatch(3am),	 fork(3am),  inplace(3am),  ordchr(3am),  readdir(3am),	 readfile(3am),	 rwarray(3am),
       time(3am).

AUTHOR
       Arnold Robbins, arnold@skeeve.com.

COPYING PERMISSIONS
       Copyright © 2012, 2013, 2018, Free Software Foundation, Inc.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission  is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified  versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Feb 21 2018								REVOUTPUT(3am)
