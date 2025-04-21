PAM_FAILDELAY(8)						       Linux-PAM Manual							      PAM_FAILDELAY(8)

NAME
       pam_faildelay - Change the delay on failure per-application

SYNOPSIS

       pam_faildelay.so [debug] [delay=microseconds]

DESCRIPTION
       pam_faildelay is a PAM module that can be used to set the delay on failure per-application.

       If no delay is given, pam_faildelay will use the value of FAIL_DELAY from /etc/login.defs.

OPTIONS
       debug
	   Turns on debugging messages sent to syslog.

       delay=N
	   Set the delay on failure to N microseconds.

MODULE TYPES PROVIDED
       Only the auth module type is provided.

RETURN VALUES
       PAM_IGNORE
	   Delay was successful adjusted.

       PAM_SYSTEM_ERR
	   The specified delay was not valid.

EXAMPLES
       The following example will set the delay on failure to 10 seconds:

	   auth	 optional  pam_faildelay.so  delay=10000000

SEE ALSO
       pam_fail_delay(3), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_faildelay was written by Darren Tucker <dtucker@zip.com.au>.

Linux-PAM								  05/07/2023							      PAM_FAILDELAY(8)
