PAM_PERMIT(8)							       Linux-PAM Manual								 PAM_PERMIT(8)

NAME
       pam_permit - The promiscuous module

SYNOPSIS

       pam_permit.so

DESCRIPTION
       pam_permit is a PAM module that always permit access. It does nothing else.

       In the case of authentication, the user's name will be set to nobody if the application didn't set one. Many applications and PAM modules become
       confused if this name is unknown.

       This module is very dangerous. It should be used with extreme caution.

OPTIONS
       This module does not recognise any options.

MODULE TYPES PROVIDED
       The auth, account, password and session module types are provided.

RETURN VALUES
       PAM_SUCCESS
	   This module always returns this value.

EXAMPLES
       Add this line to your other login entries to disable account management, but continue to permit users to log in.

	   account  required  pam_permit.so

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_permit was written by Andrew G. Morgan, <morgan@kernel.org>.

Linux-PAM								  05/07/2023								 PAM_PERMIT(8)
