SYSTEMD-BOOT-CHECK-NO-FAILURES.SERVICE(8)		    systemd-boot-check-no-failures.service		     SYSTEMD-BOOT-CHECK-NO-FAILURES.SERVICE(8)

NAME
       systemd-boot-check-no-failures.service, systemd-boot-check-no-failures - verify that the system booted up cleanly

SYNOPSIS
       systemd-boot-check-no-failures.service

       /usr/lib/systemd/system-boot-check-no-failures

DESCRIPTION
       systemd-boot-check-no-failures.service is a system service that checks whether the system booted up successfully. This service implements a very
       minimal test only: whether there are any failed units on the system. This service is disabled by default. When enabled, it is ordered before
       boot-complete.target, thus ensuring the target cannot be reached when the system booted up with failed services.

       Note that due the simple nature of this check this service is probably not suitable for deployment in most scenarios. It is primarily useful only as
       example for developing more fine-grained checks to order before boot-complete.target.

SEE ALSO
       systemd(1), systemd.special(7)

systemd 255													     SYSTEMD-BOOT-CHECK-NO-FAILURES.SERVICE(8)
