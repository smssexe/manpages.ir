GETCAP(8)							    System Manager's Manual							     GETCAP(8)

NAME
       getcap - examine file capabilities

SYNOPSIS
       getcap [-v] [-n] [-r] [-h] filename [ ... ]

DESCRIPTION
       getcap displays the name and capabilities of each specified file.

OPTIONS
       -h  prints quick usage.

       -n  prints any non-zero user namespace root user ID value found to be associated with a file's capabilities.

       -r  enables recursive search.

       -v  display all searched entries, even if the have no file-capabilities.

       filename
	   One file per line.

REPORTING BUGS
       Please report bugs via:

       https://bugzilla.kernel.org/buglist.cgi?component=libcap&list_id=1090757

SEE ALSO
       capsh(1), cap_get_file(3), cap_to_text(3), capabilities(7), user_namespaces(7), captree(8), getpcaps(8) and setcap(8).

									  2021-08-29								     GETCAP(8)
