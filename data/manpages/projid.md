projid(5)							      File Formats Manual							     projid(5)

NAME
       projid - the project name mapping file

DESCRIPTION
       The  /etc/projid file provides a mapping between numeric project identifiers and a simple human readable name (similar relationship to the one that ex‐
       ists between usernames and uids).  Its format is simply:

	    # comments are hash-prefixed
	    # ...
	    cage:10
	    logfiles:42

       This file is optional, if a project identifier cannot be mapped to a name, it will be parsed and displayed as a numeric value.

SEE ALSO
       xfs_quota(8), xfsctl(3), projects(5).

																		     projid(5)
