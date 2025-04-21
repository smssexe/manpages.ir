SETCAP(8)							    System Manager's Manual							     SETCAP(8)

NAME
       setcap - set file capabilities

SYNOPSIS
       setcap [-q] [-n <rootuid>] [-v] {capabilities|-|-r} filename [ ... capabilitiesN fileN ]

DESCRIPTION
       In  the absence of the -v (verify) option setcap sets the capabilities of each specified filename to the capabilities specified.	 The optional -n <roo‐
       tuid> argument can be used to set the file capability for use only in a user namespace with this root user ID owner. The -v option is  used  to	verify
       that the specified capabilities are currently associated with the file. If -v and -n are supplied, the -n <rootuid> argument is also verified.

       The capabilities are specified in the form described in cap_from_text(3).

       The  special  capability	 string, '-', can be used to indicate that capabilities are read from the standard input. In such cases, the capability set is
       terminated with a blank line.

       The special capability string, '-r', is used to remove a capability set from a file. Note, setting an empty capability set is not the same as  removing
       it. An empty set can be used to guarantee a file is not executed with privilege in spite of the fact that the prevailing ambient+inheritable sets would
       otherwise bestow capabilities on executed binaries.

       The -q flag is used to make the program less verbose in its output.

EXIT CODE
       The setcap program will exit with a 0 exit code if successful. On failure, the exit code is 1.

REPORTING BUGS
       Please report bugs via:

       https://bugzilla.kernel.org/buglist.cgi?component=libcap&list_id=1090757

SEE ALSO
       capsh(1), cap_from_text(3), cap_get_file(3), capabilities(7), user_namespaces(7), captree(8), getcap(8) and getpcaps(8).

									  2020-08-29								     SETCAP(8)
