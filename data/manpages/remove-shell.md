REMOVE-SHELL(8)							    System Manager's Manual						       REMOVE-SHELL(8)

NAME
       remove-shell - remove shells from the list of valid login shells

SYNOPSIS
       remove-shell shellname [shellname...]

DESCRIPTION
       remove-shell  operates  on the temporary files /etc/shells.tmp and /etc/shells.tmp2 to remove the given shells from the list of valid login shells, and
       copy the result back to /etc/shells.

ENVIRONMENT
       DPKG_ROOT
	      specifies the base path under which /etc/shells resides.

SEE ALSO
       shells(5)

									  23 Sep 2021							       REMOVE-SHELL(8)
