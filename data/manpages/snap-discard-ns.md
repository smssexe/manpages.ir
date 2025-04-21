SNAP-DISCARD-NS(5)							    snappy							    SNAP-DISCARD-NS(5)

NAME
       snap-discard-ns - internal tool for discarding preserved namespaces of snappy applications

SYNOPSIS
	  snap-discard-ns [--from-snap-confine] SNAP_INSTANCE_NAME

DESCRIPTION
       The snap-discard-ns is a program used internally by snapd to discard a preserved mount namespace of a particular snap.

OPTIONS
       The --from-snap-confine option is used internally by snap-confine to tell snap-discard-ns that it is invoked from snap-confine and can disable locking.

ENVIRONMENT
       snap-discard-ns responds to the following environment variables

       SNAP_CONFINE_DEBUG:
	      When defined the program will print additional diagnostic information about the actions being performed. All the output goes to stderr.

FILES
       snap-discard-ns uses the following files:

       /run/snapd/ns/$SNAP_INSTNACE_NAME.mnt: /run/snapd/ns/$SNAP_INSTNACE_NAME.*.mnt:
	  The preserved mount namespace that is unmounted and removed by snap-discard-ns. The second form is for the per-user mount namespace.

       /run/snapd/ns/snap.$SNAP_INSTNACE_NAME.fstab: /run/snapd/ns/snap.$SNAP_INSTNACE_NAME.*.user-fstab:
	  The current mount profile of a preserved mount namespace that is removed by snap-discard-ns.

BUGS
       Please report all bugs with https://bugs.launchpad.net/snapd/+filebug

AUTHOR
       zygmunt.krynicki@canonical.com

COPYRIGHT
       Canonical Ltd.

2.36									  2018-10-17							    SNAP-DISCARD-NS(5)
