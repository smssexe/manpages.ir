PAM_LOCALUSER(8)						       Linux-PAM Manual							      PAM_LOCALUSER(8)

NAME
       pam_localuser - require users to be listed in /etc/passwd

SYNOPSIS

       pam_localuser.so [debug] [file=/path/passwd]

DESCRIPTION
       pam_localuser is a PAM module to help implementing site-wide login policies, where they typically include a subset of the network's users and a few
       accounts that are local to a particular workstation. Using pam_localuser and pam_wheel or pam_listfile is an effective way to restrict access to either
       local users and/or a subset of the network's users.

       This could also be implemented using pam_listfile.so and a very short awk script invoked by cron, but it's common enough to have been separated out.

OPTIONS
       debug
	   Print debug information.

       file=/path/passwd
	   Use a file other than /etc/passwd.

MODULE TYPES PROVIDED
       All module types (account, auth, password and session) are provided.

RETURN VALUES
       PAM_SUCCESS
	   The new localuser was set successfully.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_CONV_ERR
	   The conversation method supplied by the application failed to obtain the username.

       PAM_INCOMPLETE
	   The conversation method supplied by the application returned PAM_CONV_AGAIN.

       PAM_SERVICE_ERR
	   The user name is not valid or the passwd file is unavailable.

       PAM_PERM_DENIED
	   The user is not listed in the passwd file.

EXAMPLES
       Add the following lines to /etc/pam.d/su to allow only local users or group wheel to use su.

	   account sufficient pam_localuser.so
	   account required pam_wheel.so

FILES
       /etc/passwd
	   Local user account information.

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_localuser was written by Nalin Dahyabhai <nalin@redhat.com>.

Linux-PAM								  05/07/2023							      PAM_LOCALUSER(8)
