PAM_SHELLS(8)							       Linux-PAM Manual								 PAM_SHELLS(8)

NAME
       pam_shells - PAM module to check for valid login shell

SYNOPSIS

       pam_shells.so

DESCRIPTION
       pam_shells is a PAM module that only allows access to the system if the user's shell is listed in /etc/shells.

       It also checks if needed files (e.g.  /etc/shells) are plain files and not world writable.

OPTIONS
       This module does not recognise any options.

MODULE TYPES PROVIDED
       The auth and account module types are provided.

RETURN VALUES
       PAM_AUTH_ERR
	   Access to the system was denied.

       PAM_SUCCESS
	   The user's login shell was listed as valid shell in /etc/shells.

       PAM_SERVICE_ERR
	   The module was not able to get the name of the user.

EXAMPLES
	   auth	 required  pam_shells.so

SEE ALSO
       shells(5), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_shells was written by Erik Troan <ewt@redhat.com>.

Linux-PAM								  05/07/2023								 PAM_SHELLS(8)
