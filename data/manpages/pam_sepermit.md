PAM_SEPERMIT(8)							       Linux-PAM Manual							       PAM_SEPERMIT(8)

NAME
       pam_sepermit - PAM module to allow/deny login depending on SELinux enforcement state

SYNOPSIS

       pam_sepermit.so [debug] [conf=/path/to/config/file]

DESCRIPTION
       The pam_sepermit module allows or denies login depending on SELinux enforcement state.

       When the user which is logging in matches an entry in the config file he is allowed access only when the SELinux is in enforcing mode. Otherwise he is
       denied access. For users not matching any entry in the config file the pam_sepermit module returns PAM_IGNORE return value.

       The config file contains a list of user names one per line with optional arguments. If the name is prefixed with @ character it means that all users in
       the group name match. If it is prefixed with a % character the SELinux user is used to match against the name instead of the account name. Note that
       when SELinux is disabled the SELinux user assigned to the account cannot be determined. This means that such entries are never matched when SELinux is
       disabled and pam_sepermit will return PAM_IGNORE.

       See sepermit.conf(5) for details.

OPTIONS
       debug
	   Turns on debugging via syslog(3).

       conf=/path/to/config/file
	   Path to alternative config file overriding the default.

MODULE TYPES PROVIDED
       The auth and account module types are provided.

RETURN VALUES
       PAM_AUTH_ERR
	   SELinux is disabled or in the permissive mode and the user matches.

       PAM_SUCCESS
	   SELinux is in the enforcing mode and the user matches.

       PAM_IGNORE
	   The user does not match any entry in the config file.

       PAM_USER_UNKNOWN
	   The module was unable to determine the user's name.

       PAM_SERVICE_ERR
	   Error during reading or parsing the config file.

FILES
       /etc/security/sepermit.conf
	   Default configuration file

EXAMPLES
	   auth	    [success=done ignore=ignore default=bad] pam_sepermit.so
	   auth	    required  pam_unix.so
	   account  required  pam_unix.so
	   session  required  pam_permit.so

SEE ALSO
       sepermit.conf(5), pam.conf(5), pam.d(5), pam(7) selinux(8)

AUTHOR
       pam_sepermit and this manual page were written by Tomas Mraz <tmraz@redhat.com>.

Linux-PAM								  05/07/2023							       PAM_SEPERMIT(8)
