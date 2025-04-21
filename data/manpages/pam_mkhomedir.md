PAM_MKHOMEDIR(8)						       Linux-PAM Manual							      PAM_MKHOMEDIR(8)

NAME
       pam_mkhomedir - PAM module to create users home directory

SYNOPSIS

       pam_mkhomedir.so [silent] [debug] [umask=mode] [skel=skeldir]

DESCRIPTION
       The pam_mkhomedir PAM module will create a users home directory if it does not exist when the session begins. This allows users to be present in
       central database (such as NIS, kerberos or LDAP) without using a distributed file system or pre-creating a large number of directories. The skeleton
       directory (usually /etc/skel/) is used to copy default files and also sets a umask for the creation.

       The new users home directory will not be removed after logout of the user.

OPTIONS
       silent
	   Don't print informative messages.

       debug
	   Turns on debugging via syslog(3).

       umask=mask
	   The file mode creation mask is set to mask. The default value of mask is 0022. If this option is not specified, then the permissions of created
	   user home directory is set to the value of HOME_MODE configuration item from /etc/login.defs. If there is no such configuration item then the value
	   is computed from the value of UMASK in the same file. If there is no such configuration option either the default value of 0755 is used for the
	   mode.

       skel=/path/to/skel/directory
	   Indicate an alternative skel directory to override the default /etc/skel.

MODULE TYPES PROVIDED
       Only the session module type is provided.

RETURN VALUES
       PAM_BUF_ERR
	   Memory buffer error.

       PAM_PERM_DENIED
	   Not enough permissions to create the new directory or read the skel directory.

       PAM_USER_UNKNOWN
	   User not known to the underlying authentication module.

       PAM_SUCCESS
	   Environment variables were set.

FILES
       /etc/skel
	   Default skel directory

EXAMPLES
       A sample /etc/pam.d/login file:

	     auth	requisite   pam_securetty.so
	     auth	sufficient  pam_ldap.so
	     auth	required    pam_unix.so
	     auth	required    pam_nologin.so
	     account	sufficient  pam_ldap.so
	     account	required    pam_unix.so
	     password	required    pam_unix.so
	     session	required    pam_mkhomedir.so skel=/etc/skel/ umask=0022
	     session	required    pam_unix.so
	     session	optional    pam_lastlog.so
	     session	optional    pam_mail.so standard

SEE ALSO
       pam.d(5), pam(7).

AUTHOR
       pam_mkhomedir was written by Jason Gunthorpe <jgg@debian.org>.

Linux-PAM								  05/07/2023							      PAM_MKHOMEDIR(8)
