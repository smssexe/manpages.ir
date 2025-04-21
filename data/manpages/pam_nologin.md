PAM_NOLOGIN(8)							       Linux-PAM Manual								PAM_NOLOGIN(8)

NAME
       pam_nologin - Prevent non-root users from login

SYNOPSIS

       pam_nologin.so [file=/path/nologin] [successok]

DESCRIPTION
       pam_nologin is a PAM module that prevents users from logging into the system when /var/run/nologin or /etc/nologin exists. The contents of the file are
       displayed to the user. The pam_nologin module has no effect on the root user's ability to log in.

OPTIONS
       file=/path/nologin
	   Use this file instead the default /var/run/nologin or /etc/nologin.

       successok
	   Return PAM_SUCCESS if no file exists, the default is PAM_IGNORE.

MODULE TYPES PROVIDED
       The auth and account module types are provided.

RETURN VALUES
       PAM_AUTH_ERR
	   The user is not root and /etc/nologin exists, so the user is not permitted to log in.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_IGNORE
	   This is the default return value.

       PAM_SUCCESS
	   Success: either the user is root or the nologin file does not exist.

       PAM_USER_UNKNOWN
	   User not known to the underlying authentication module.

EXAMPLES
       The suggested usage for /etc/pam.d/login is:

	   auth	 required  pam_nologin.so

NOTES
       In order to make this module effective, all login methods should be secured by it. It should be used as a required method listed before any sufficient
       methods in order to get standard Unix nologin semantics. Note, the use of successok module argument causes the module to return PAM_SUCCESS and as such
       would break such a configuration - failing sufficient modules would lead to a successful login because the nologin module succeeded.

SEE ALSO
       nologin(5), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_nologin was written by Michael K. Johnson <johnsonm@redhat.com>.

Linux-PAM								  05/07/2023								PAM_NOLOGIN(8)
