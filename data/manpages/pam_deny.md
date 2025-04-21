PAM_DENY(8)							       Linux-PAM Manual								   PAM_DENY(8)

NAME
       pam_deny - The locking-out PAM module

SYNOPSIS

       pam_deny.so

DESCRIPTION
       This module can be used to deny access. It always indicates a failure to the application through the PAM framework. It might be suitable for using for
       default (the OTHER) entries.

OPTIONS
       This module does not recognise any options.

MODULE TYPES PROVIDED
       All module types (account, auth, password and session) are provided.

RETURN VALUES
       PAM_AUTH_ERR
	   This is returned by the account and auth services.

       PAM_CRED_ERR
	   This is returned by the setcred function.

       PAM_AUTHTOK_ERR
	   This is returned by the password service.

       PAM_SESSION_ERR
	   This is returned by the session service.

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
       pam_deny was written by Andrew G. Morgan <morgan@kernel.org>

Linux-PAM								  05/07/2023								   PAM_DENY(8)
