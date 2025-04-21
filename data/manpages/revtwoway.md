REVTWOWAY(3am)							   GNU Awk Extension Modules							REVTWOWAY(3am)

NAME
       revtwoway - Reverse strings sample two-way processor extension

SYNOPSIS
       @load "revtwoway"

       BEGIN {
	   cmd = "/magic/mirror"
	   print "hello, world" |& cmd
	   cmd |& getline result
	   print result
	   close(cmd)
       }

DESCRIPTION
       The revtwoway extension adds a simple two-way processor that reverses the characters in each line sent to it for reading back by the AWK program.  It's
       main purpose is to show how to write a two-way extension, although it may also be mildly amusing.

SEE ALSO
       GAWK: Effective AWK Programming, filefuncs(3am), fnmatch(3am), fork(3am), inplace(3am), ordchr(3am), readdir(3am), readfile(3am), revoutput(3am), rwar‐
       ray(3am), time(3am).

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

Free Software Foundation						  Feb 21 2018								REVTWOWAY(3am)
