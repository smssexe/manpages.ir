PAM_TIME(8)							       Linux-PAM Manual								   PAM_TIME(8)

NAME
       pam_time - PAM module for time control access

SYNOPSIS

       pam_time.so [conffile=conf-file] [debug] [noaudit]

DESCRIPTION
       The pam_time PAM module does not authenticate the user, but instead it restricts access to a system and or specific applications at various times of
       the day and on specific days or over various terminal lines. This module can be configured to deny access to (individual) users based on their name,
       the time of day, the day of week, the service they are applying for and their terminal from which they are making their request.

       By default rules for time/port access are taken from config file /etc/security/time.conf. An alternative file can be specified with the conffile
       option.

       If Linux PAM is compiled with audit support the module will report when it denies access.

OPTIONS
       conffile=/path/to/time.conf
	   Indicate an alternative time.conf style configuration file to override the default.

       debug
	   Some debug information is printed with syslog(3).

       noaudit
	   Do not report logins at disallowed time to the audit subsystem.

MODULE TYPES PROVIDED
       Only the account type is provided.

RETURN VALUES
       PAM_SUCCESS
	   Access was granted.

       PAM_ABORT
	   Not all relevant data could be gotten.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_PERM_DENIED
	   Access was not granted.

       PAM_USER_UNKNOWN
	   The user is not known to the system.

FILES
       /etc/security/time.conf
	   Default configuration file

EXAMPLES
	   #%PAM-1.0
	   #
	   # apply pam_time accounting to login requests
	   #
	   login  account  required  pam_time.so

SEE ALSO
       time.conf(5), pam.d(5), pam(7).

AUTHOR
       pam_time was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								   PAM_TIME(8)
