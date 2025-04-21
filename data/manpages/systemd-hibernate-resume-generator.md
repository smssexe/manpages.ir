SYSTEMD-HIBERNATE-RESUME-GENERATOR(8)			      systemd-hibernate-resume-generator			 SYSTEMD-HIBERNATE-RESUME-GENERATOR(8)

NAME
       systemd-hibernate-resume-generator - Unit generator for resume= kernel parameter

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator

DESCRIPTION
       systemd-hibernate-resume-generator is a generator that initiates the procedure to resume the system from hibernation. It creates the systemd-hibernate-
       resume.service(8) unit according to the value of resume= parameter specified on the kernel command line, or the value of EFI variable
       HibernateLocation, which will instruct the kernel to resume the system from the hibernation image on that device.

KERNEL COMMAND LINE
       systemd-hibernate-resume-generator understands the following kernel command line parameters:

       resume=
	   Takes a path to the resume device. Both persistent block device paths like /dev/disk/by-foo/bar and fstab(5)-style specifiers like "FOO=bar" are
	   supported.

	   Added in version 217.

       resume_offset=
	   Takes the page offset of the swap space from the resume device. Defaults to "0".

	   Added in version 254.

       resumeflags=
	   Takes the resume device mount options to use. Defaults rootflags= if not specified.

	   Added in version 243.

       noresume
	   Do not try to resume from hibernation. If this parameter is present, resume= is ignored.

	   Added in version 240.

SEE ALSO
       systemd(1), systemd-hibernate-resume.service(8), kernel-command-line(7)

systemd 255														 SYSTEMD-HIBERNATE-RESUME-GENERATOR(8)
