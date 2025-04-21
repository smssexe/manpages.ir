PAM_ROOTOK(8)							       Linux-PAM Manual								 PAM_ROOTOK(8)

NAME
       pam_rootok - Gain only root access

SYNOPSIS

       pam_rootok.so [debug]

DESCRIPTION
       pam_rootok is a PAM module that authenticates the user if their UID is 0. Applications that are created setuid-root generally retain the UID of the
       user but run with the authority of an enhanced effective-UID. It is the real UID that is checked.

OPTIONS
       debug
	   Print debug information.

MODULE TYPES PROVIDED
       The auth, account and password module types are provided.

RETURN VALUES
       PAM_SUCCESS
	   The UID is 0.

       PAM_AUTH_ERR
	   The UID is not 0.

EXAMPLES
       In the case of the su(1) application the historical usage is to permit the superuser to adopt the identity of a lesser user without the use of a
       password. To obtain this behavior with PAM the following pair of lines are needed for the corresponding entry in the /etc/pam.d/su configuration file:

	   # su authentication. Root is granted access by default.
	   auth	 sufficient   pam_rootok.so
	   auth	 required     pam_unix.so

SEE ALSO
       su(1), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_rootok was written by Andrew G. Morgan, <morgan@kernel.org>.

Linux-PAM								  05/07/2023								 PAM_ROOTOK(8)
