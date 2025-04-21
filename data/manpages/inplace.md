INPLACE(3am)							   GNU Awk Extension Modules							  INPLACE(3am)

NAME
       inplace - emulate sed/perl/ruby in-place editing

SYNOPSIS
       gawk -i inplace ...

DESCRIPTION
       The inplace extension adds two functions named inplace_begin() and inplace_end().  These functions are meant to be invoked from the inplace.awk wrapper
       which is installed when gawk is.

       By default, each named file on the command line is replaced with a new file of the same name whose contents are the results of running the AWK program.
       If  the user supplies an AWK variable named inplace::suffix in a BEGIN rule or on the command line, then the inplace extension concatenates that suffix
       onto the original filename and uses the result as a filename for renaming the original.

       For backwards compatibility, the variable will also check INPLACE_SUFFIX (in the awk namespace) for the suffix to use if inplace::suffix is not set.

       One can disable inplace editing selectively by placing inplace::enable=0 on the command line prior to files that should be processed normally.  One can
       reenable inplace editing by placing inplace::enable=1 prior to files that should be subject to inplace editing.

BUGS
       While the extension does attempt to preserve ownership and permissions, it makes no attempt to copy the ACLs from the original file.

       If the program dies prematurely, as might happen if an unhandled signal is received, a temporary file may be left behind.

EXAMPLE
       gawk -i inplace 'script' files ...
       gawk -i inplace -f scriptfile files ...

SEE ALSO
       GAWK: Effective AWK Programming, filefuncs(3am), fnmatch(3am), fork(3am), ordchr(3am), readdir(3am), readfile(3am), revoutput(3am), rwarray(3am).

AUTHOR
       Andrew Schorr, schorr@telemetry-investments.com.

COPYING PERMISSIONS
       Copyright © 2012, 2013, 2015, 2018, 2019, Free Software Foundation, Inc.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the	entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission  is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Jun 26 2018								  INPLACE(3am)
