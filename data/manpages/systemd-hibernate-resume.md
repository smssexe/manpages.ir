SYSTEMD-HIBERNATE-RESUME.SERVICE(8)			       systemd-hibernate-resume.service				   SYSTEMD-HIBERNATE-RESUME.SERVICE(8)

NAME
       systemd-hibernate-resume.service, systemd-hibernate-resume - Resume from hibernation

SYNOPSIS
       systemd-hibernate-resume.service

       /usr/lib/systemd/systemd-hibernate-resume

DESCRIPTION
       systemd-hibernate-resume.service initiates the resume from hibernation.

       systemd-hibernate-resume only supports the in-kernel hibernation implementation, see Swap suspend[1]. Internally, it works by writing the major:minor
       of specified device node to /sys/power/resume, along with the offset in memory pages (/sys/power/resume_offset) if supported.

       Failing to initiate a resume is not an error condition. It may mean that there was no resume image (e. g. if the system has been simply powered off and
       not hibernated). In such cases, the boot is ordinarily continued.

SEE ALSO
       systemd(1), systemd-hibernate-resume-generator(8)

NOTES
	1. Swap suspend
	   https://docs.kernel.org/power/swsusp.html

systemd 255														   SYSTEMD-HIBERNATE-RESUME.SERVICE(8)
