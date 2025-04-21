PAM_SECURETTY(8)						       Linux-PAM Manual							      PAM_SECURETTY(8)

NAME
       pam_securetty - Limit root login to special devices

SYNOPSIS

       pam_securetty.so [debug]

DESCRIPTION
       pam_securetty is a PAM module that allows root logins only if the user is logging in on a "secure" tty, as defined by the listing in the securetty
       file. pam_securetty checks at first, if /etc/securetty exists. If not and it was built with vendordir support, it will use /securetty. pam_securetty
       also checks that the securetty files are plain files and not world writable. It will also allow root logins on the tty specified with console= switch
       on the kernel command line and on ttys from the /sys/class/tty/console/active.

       This module has no effect on non-root users and requires that the application fills in the PAM_TTY item correctly.

       For canonical usage, should be listed as a required authentication method before any sufficient authentication methods.

OPTIONS
       debug
	   Print debug information.

       noconsole
	   Do not automatically allow root logins on the kernel console device, as specified on the kernel command line or by the sys file, if it is not also
	   specified in the securetty file.

MODULE TYPES PROVIDED
       Only the auth module type is provided.

RETURN VALUES
       PAM_SUCCESS
	   The user is allowed to continue authentication. Either the user is not root, or the root user is trying to log in on an acceptable device.

       PAM_AUTH_ERR
	   Authentication is rejected. Either root is attempting to log in via an unacceptable device, or the securetty file is world writable or not a normal
	   file.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_CONV_ERR
	   The conversation method supplied by the application failed to obtain the username.

       PAM_INCOMPLETE
	   The conversation method supplied by the application returned PAM_CONV_AGAIN.

       PAM_SERVICE_ERR
	   An error occurred while the module was determining the user's name or tty, or the module could not open the securetty file.

       PAM_USER_UNKNOWN
	   The module could not find the user name in the /etc/passwd file to verify whether the user had a UID of 0. Therefore, the results of running this
	   module are ignored.

EXAMPLES
	   auth	 required  pam_securetty.so
	   auth	 required  pam_unix.so

SEE ALSO
       securetty(5), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_securetty was written by Elliot Lee <sopwith@cuc.edu>.

Linux-PAM								  05/07/2023							      PAM_SECURETTY(8)
