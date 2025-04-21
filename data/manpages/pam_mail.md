PAM_MAIL(8)							       Linux-PAM Manual								   PAM_MAIL(8)

NAME
       pam_mail - Inform about available mail

SYNOPSIS

       pam_mail.so [close] [debug] [dir=maildir] [empty] [hash=count] [noenv] [nopen] [quiet] [standard]

DESCRIPTION
       The pam_mail PAM module provides the "you have new mail" service to the user. It can be plugged into any application that has credential or session
       hooks. It gives a single message indicating the newness of any mail it finds in the user's mail folder. This module also sets the PAM environment
       variable, MAIL, to the user's mail directory.

       If the mail spool file (be it /var/mail/$USER or a pathname given with the dir= parameter) is a directory then pam_mail assumes it is in the Maildir
       format.

OPTIONS
       close
	   Indicate if the user has any mail also on logout.

       debug
	   Print debug information.

       dir=maildir
	   Look for the user's mail in an alternative location defined by maildir/<login>. The default location for mail is /var/mail/<login>. Note, if the
	   supplied maildir is prefixed by a '~', the directory is interpreted as indicating a file in the user's home directory.

       empty
	   Also print message if user has no mail.

       hash=count
	   Mail directory hash depth. For example, a hashcount of 2 would make the mail file be /var/spool/mail/u/s/user.

       noenv
	   Do not set the MAIL environment variable.

       nopen
	   Don't print any mail information on login. This flag is useful to get the MAIL environment variable set, but to not display any information about
	   it.

       quiet
	   Only report when there is new mail.

       standard
	   Old style "You have..." format which doesn't show the mail spool being used. This also implies "empty".

MODULE TYPES PROVIDED
       The session and auth (on establishment and deletion of credentials) module types are provided.

RETURN VALUES
       PAM_BUF_ERR
	   Memory buffer error.

       PAM_SERVICE_ERR
	   Badly formed arguments.

       PAM_SUCCESS
	   Success.

       PAM_USER_UNKNOWN
	   User not known.

EXAMPLES
       Add the following line to /etc/pam.d/login to indicate that the user has new mail when they login to the system.

	   session  optional  pam_mail.so standard

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_mail was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								   PAM_MAIL(8)
