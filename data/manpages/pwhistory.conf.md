PWHISTORY.CONF(5)						       Linux-PAM Manual							     PWHISTORY.CONF(5)

NAME
       pwhistory.conf - pam_pwhistory configuration file

DESCRIPTION
       pwhistory.conf provides a way to configure the default settings for saving the last passwords for each user. This file is read by the pam_pwhistory
       module and is the preferred method over configuring pam_pwhistory directly.

       The file has a very simple name = value format with possible comments starting with # character. The whitespace at the beginning of line, end of line,
       and around the = sign is ignored.

OPTIONS
       debug
	   Turns on debugging via syslog(3).

       enforce_for_root
	   If this option is set, the check is enforced for root, too.

       remember=N
	   The last N passwords for each user are saved. The default is 10. Value of 0 makes the module to keep the existing contents of the opasswd file
	   unchanged.

       retry=N
	   Prompt user at most N times before returning with error. The default is 1.

       file=/path/filename
	   Store password history in file /path/filename rather than the default location. The default location is /etc/security/opasswd.

EXAMPLES
       /etc/security/pwhistory.conf file example:

	   debug
	   remember=5
	   file=/tmp/opasswd

FILES
       /etc/security/pwhistory.conf
	   the config file for custom options

SEE ALSO
       pwhistory(8), pam_pwhistory(8), pam.conf(5), pam.d(5), pam(8)

AUTHOR
       pam_pwhistory was written by Thorsten Kukuk. The support for pwhistory.conf was written by Iker Pedrosa.

Linux-PAM								  05/07/2023							     PWHISTORY.CONF(5)
