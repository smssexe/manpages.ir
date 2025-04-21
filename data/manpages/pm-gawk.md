PM-GAWK(1)							       Utility Commands								    PM-GAWK(1)

NAME
       persistent memory gawk - persistent data and functions

SYNOPSIS
       truncate -s size heap.pma
       export GAWK_PERSIST_FILE=heap.pma
       gawk ...

       truncate -s size heap.pma
       GAWK_PERSIST_FILE=heap.pma gawk ...

       truncate -s size heap.pma
       alias pm='GAWK_PERSIST_FILE=heap.pma'
       pm gawk ...			 # succinct

       unset GAWK_PERSIST_FILE	 # disable persistence

       export GAWK_PERSIST_FILE=other_heap.pma	# change heap

       rm heap.pma		 # delete heap

DESCRIPTION
       Gawk  5.2  and  later supports a persistent memory feature that can store script-defined variables and functions in a file for later use.  The feature,
       called pm-gawk, is described in GAWK: Effective AWK Programming and in Persistent Memory gawk User Manual.

       pm-gawk is activated by passing to gawk the name of an initially empty (all-zero-bytes) heap file, via the environment variable GAWK_PERSIST_FILE.  pm-
       gawk retains script-defined variables and functions in the heap file for use in subsequent gawk invocations.

       pm-gawk offers at least two advantages compared with the existing rwarray extension: it offers constant-time (``O(1) time'') access to individual  ele‐
       ments of persistent associative arrays, and it can store script-defined functions in addition to variables.

EXAMPLES
       Demonstrate persistent variables:
	      $ truncate -s 1G heap.pma		   # create heap file
	      $ export GAWK_PERSIST_FILE=heap.pma  # "ambient" env var
	      $ gawk 'BEGIN { print ++i }'
	      1
	      $ gawk 'BEGIN { print ++i }'
	      2
	      $ gawk 'BEGIN { print ++i }'
	      3

       To pass the environment variable on per-command basis:
	      $ unset GAWK_PERSIST_FILE
	      $ GAWK_PERSIST_FILE=heap.pma gawk 'BEGIN { print ++i }'
	      4
	      $ GAWK_PERSIST_FILE=heap.pma gawk 'BEGIN { print ++i }'
	      5
	      $ GAWK_PERSIST_FILE=heap.pma gawk 'BEGIN { print ++i }'
	      6

       To reduce visual clutter of per-command environment variable passing:
	      $ alias pm='GAWK_PERSIST_FILE=heap.pma'
	      $ pm gawk 'BEGIN { print ++i }'
	      7
	      $ pm gawk 'BEGIN { print ++i }'
	      8

       To refrain from activating persistence:
	      $ unset GAWK_PERSIST_FILE
	      $ gawk 'BEGIN { print ++i }'
	      1
	      $ gawk 'BEGIN { print ++i }'
	      1

       To permanently ``forget'' the contents of the heap file:
	      $ rm heap.pma

ENVIRONMENT VARIABLES
       GAWK_PERSIST_FILE  contains the name of a heap file where script-defined variables and functions are stored.  If this environment variable is not visi‐
       ble to gawk, the persistence feature is not activated and gawk behaves in its traditional manner.

VERSION INFORMATION
       Persistent memory gawk was first released in gawk 5.2.

AUTHORS
       Arnold Robbins, the maintainer of gawk, implemented pm-gawk using a persistent memory allocator (pma) provided by Terence Kelly.	 An earlier  proof-of-
       concept prototype of persistent gawk was developed by Haris Volos, Zi Fan Tan, and Jianan Li using a fork of the official gawk sources.

CAVEATS
       The  GNU/Linux  CIFS filesystem is known to cause problems for the persistent memory allocator. Do not use a backing file on such a filesystem with pm-
       gawk.

BUG REPORTS
       Follow the procedures in GAWK: Effective AWK Programming and in Persistent Memory gawk User Manual.  For suspected bugs related to persistence (as  op‐
       posed  to  other	 non-persistence-related  gawk	bugs) please also send e-mail to Terence Kelly at one or more of these addresses: tpkelly@acm.org, tp‐
       kelly@eecs.umich.edu, or tpkelly@cs.princeton.edu.

SEE ALSO
       gawk(1), GAWK: Effective AWK Programming, and Persistent Memory gawk User Manual.  The two manuals should be available in the Info  subsystem  if  Info
       installed on your system.

       See https://web.eecs.umich.edu/~tpkelly/pma/ for the latest source code and manual.

COPYING PERMISSIONS
       Copyright © 2022 Terence Kelly.

       Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved
       on all copies.

       Permission  is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire
       resulting derived work is distributed under the terms of a permission notice identical to this one.

       Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified  versions,
       except that this permission notice may be stated in a translation approved by the Foundation.

Free Software Foundation						  Nov 17 2022								    PM-GAWK(1)
