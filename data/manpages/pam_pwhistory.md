PAM_PWHISTORY(8)						       Linux-PAM Manual							      PAM_PWHISTORY(8)

NAME
       pam_pwhistory - PAM module to remember last passwords

SYNOPSIS

       pam_pwhistory.so [debug] [use_authtok] [enforce_for_root] [remember=N] [retry=N] [authtok_type=STRING] [file=/path/filename]
			[conf=/path/to/config-file]

DESCRIPTION
       This module saves the last passwords for each user in order to force password change history and keep the user from alternating between the same
       password too frequently.

       This module does not work together with kerberos. In general, it does not make much sense to use this module in conjunction with NIS or LDAP, since the
       old passwords are stored on the local machine and are not available on another machine for password history checking.

OPTIONS
       debug
	   Turns on debugging via syslog(3).

       use_authtok
	   When password changing enforce the module to use the new password provided by a previously stacked password module (this is used in the example of
	   the stacking of the pam_passwdqc module documented below).

       enforce_for_root
	   If this option is set, the check is enforced for root, too.

       remember=N
	   The last N passwords for each user are saved. The default is 10. Value of 0 makes the module to keep the existing contents of the opasswd file
	   unchanged.

       retry=N
	   Prompt user at most N times before returning with error. The default is 1.

       authtok_type=STRING
	   See pam_get_authtok(3) for more details.

       file=/path/filename
	   Store password history in file /path/filename rather than the default location. The default location is /etc/security/opasswd.

       conf=/path/to/config-file
	   Use another configuration file instead of the default /etc/security/pwhistory.conf.

       The options for configuring the module behavior are described in the pwhistory.conf(5) manual page. The options specified on the module command line
       override the values from the configuration file.

MODULE TYPES PROVIDED
       Only the password module type is provided.

RETURN VALUES
       PAM_AUTHTOK_ERR
	   No new password was entered, the user aborted password change or new password couldn't be set.

       PAM_IGNORE
	   Password history was disabled.

       PAM_MAXTRIES
	   Password was rejected too often.

       PAM_USER_UNKNOWN
	   User is not known to system.

EXAMPLES
       An example password section would be:

	   #%PAM-1.0
	   password	required       pam_pwhistory.so
	   password	required       pam_unix.so	  use_authtok

       In combination with pam_passwdqc:

	   #%PAM-1.0
	   password	required       pam_passwdqc.so	  config=/etc/passwdqc.conf
	   password	required       pam_pwhistory.so	  use_authtok
	   password	required       pam_unix.so	  use_authtok

FILES
       /etc/security/opasswd
	   Default file with password history

       /etc/security/pwhistory.conf
	   Config file for pam_pwhistory options

SEE ALSO
       pwhistory.conf(5), pam.conf(5), pam.d(5), pam(7) pam_get_authtok(3)

AUTHOR
       pam_pwhistory was written by Thorsten Kukuk <kukuk@thkukuk.de>

Linux-PAM								  05/07/2023							      PAM_PWHISTORY(8)
