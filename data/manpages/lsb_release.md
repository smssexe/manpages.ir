LSB_RELEASE(1)								 User Commands								LSB_RELEASE(1)

NAME
       lsb_release - print distribution-specific information (minimal implementation).

SYNOPSIS
       lsb_release [options]

DESCRIPTION
       This is a bare-bones version of the lsb_release command, implemented as a tiny POSIX shell script (less than 100 lines of commented code).

       Instead of using LSB packages, this version of lsb_release uses the information in /etc/os-release and /usr/lib/os-release.  Nevertheless, the output
       of this version is byte-for-byte compatible with the Python-based version provided by Debian and its derivatives.

       Using this implementation it is possible to avoid installing Python in a base OS image while still retaining compatibility with older scripts that
       expect lsb_release to exist.

OPTIONS
       The program follows the usual GNU command line syntax, with long options starting with two dashes ("--").  A summary of options are included below.

       -h, --help
	   Show a help message with a list of options and exit.

       -v, --version
	   Show LSB modules this system supports.

       -i, --id
	   Show distributor ID.

       -d, --description
	   Show description of this distribution.

       -r, --release
	   Show release number of this distribution.

       -c, --codename
	   Show code name of this distribution.

       -a, --all
	   Show all of the above information.

       -s, --short
	   Show requested information in short format.

FILES
       /usr/lib/os-release
	   Distribution-provided file with operating system identification data.

       /etc/os-release
	   Machine-specific file with operating system identification data.  If present, /etc/os-release is read instead of /usr/lib/os-release.

SEE ALSO
       os-release(5)

AUTHOR
       Gioele Barabucci <https://gioele.io>

LICENSE
       This implementation of lsb_release is free software released under the terms of the ISC license.

lsb_release 12.0							  2023-07-05								LSB_RELEASE(1)
