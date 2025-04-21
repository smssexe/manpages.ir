RWARRAY(3am)							   GNU Awk Extension Modules							  RWARRAY(3am)

NAME
       writea, reada, writeall, readall - write and read gawk arrays to/from files

SYNOPSIS
       @load "rwarray"

       ret = writea(file, array)
       ret = reada(file, array)
       ret = writeall(file)
       ret = readall(file)

DESCRIPTION
       The rwarray extension adds functions named writea(), reada(), writeall(), and readall(), as follows.

       writea()
	      This  function  takes  a	string	argument,  which is the name of the file to which dump the array, and the array itself as the second argument.
	      writea() understands multidimensional arrays.  It returns one on success, or zero upon failure.

       reada()
	      is the inverse of writea(); it reads the file named as its first argument, filling in the array named as the second argument. It clears the  ar‐
	      ray first.  Here too, the return value is one on success and zero upon failure.

       writeall()
	      This  function  takes  a	string argument, which is the name of the file to which dump the state of all variables. Calling this function is com‐
	      pletely equivalent to calling writea() with the second argument equal to SYMTAB.	It returns one on success, or zero upon failure.

       readall()
	      This function takes a string argument, which is the name of the file from which to read the contents of  various	global	variables.   For  each
	      variable	in  the file, the data is loaded unless the variable already exists. If the variable already exists, the data for that variable in the
	      file is ignored.	It returns one on success, or zero upon failure.

NOTES
       The array created by reada() is identical to that written by writea() in the sense that the contents are the same. However, due to  implementation  is‐
       sues, the array traversal order of the recreated array will likely be different from that of the original array.	 As array traversal order in AWK is by
       default	undefined, this is not (technically) a problem.	 If you need to guarantee a particular traversal order, use the array sorting features in gawk
       to do so.

       The file contains binary data.  All integral values are written in network byte order.  However, double precision floating-point values are written  as
       native binary data.  Thus, arrays containing only string data can theoretically be dumped on systems with one byte order and restored on systems with a
       different one, but this has not been tried.

EXAMPLE
       @load "rwarray"
       ...
       ret = writea("arraydump.bin", array)
       ...
       ret = reada("arraydump.bin", array)
       ...
       ret = writeall("globalstate.bin")
       ...
       ret = readall("globalstate.bin")

SEE ALSO
       GAWK:  Effective	 AWK  Programming,  filefuncs(3am),  fnmatch(3am),  fork(3am), inplace(3am), ordchr(3am), readdir(3am), readfile(3am), revoutput(3am),
       time(3am).

AUTHOR
       Arnold Robbins, arnold@skeeve.com.

COPYING PERMISSIONS
       Copyright © 2012, 2013, 2018, 2022 Free Software Foundation, Inc.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the	entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission  is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Mar 11 2022								  RWARRAY(3am)
