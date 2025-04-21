PAM_WARN(8)							       Linux-PAM Manual								   PAM_WARN(8)

NAME
       pam_warn - PAM module which logs all PAM items if called

SYNOPSIS

       pam_warn.so

DESCRIPTION
       pam_warn is a PAM module that logs the service, terminal, user, remote user and remote host to syslog(3). The items are not probed for, but instead
       obtained from the standard PAM items. The module always returns PAM_IGNORE, indicating that it does not want to affect the authentication process.

OPTIONS
       This module does not recognise any options.

MODULE TYPES PROVIDED
       The auth, account, password and session module types are provided.

RETURN VALUES
       PAM_IGNORE
	   This module always returns PAM_IGNORE.

EXAMPLES
	   #%PAM-1.0
	   #
	   # If we don't have config entries for a service, the
	   # OTHER entries are used. To be secure, warn and deny
	   # access to everything.
	   other auth	  required	 pam_warn.so
	   other auth	  required	 pam_deny.so
	   other account  required	 pam_warn.so
	   other account  required	 pam_deny.so
	   other password required	 pam_warn.so
	   other password required	 pam_deny.so
	   other session  required	 pam_warn.so
	   other session  required	 pam_deny.so

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_warn was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								   PAM_WARN(8)
