SYSTEMD-QUOTACHECK.SERVICE(8)					  systemd-quotacheck.service					 SYSTEMD-QUOTACHECK.SERVICE(8)

NAME
       systemd-quotacheck.service, systemd-quotacheck - File system quota checker logic

SYNOPSIS
       systemd-quotacheck.service

       /usr/lib/systemd/systemd-quotacheck

DESCRIPTION
       systemd-quotacheck.service is a service responsible for file system quota checks. It is run once at boot after all necessary file systems are mounted.
       It is pulled in only if at least one file system has quotas enabled.

KERNEL COMMAND LINE
       systemd-quotacheck understands one kernel command line parameter:

       quotacheck.mode=
	   One of "auto", "force", "skip". Controls the mode of operation. The default is "auto", and ensures that file system quota checks are done when the
	   file system quota checker deems them necessary.  "force" unconditionally results in full file system quota checks.  "skip" skips any file system
	   quota checks.

	   Added in version 186.

SEE ALSO
       systemd(1), quotacheck(8), systemd-fsck@.service(8)

systemd 255															 SYSTEMD-QUOTACHECK.SERVICE(8)
