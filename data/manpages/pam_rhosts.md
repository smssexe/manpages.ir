PAM_RHOSTS(8)							       Linux-PAM Manual								 PAM_RHOSTS(8)

NAME
       pam_rhosts - The rhosts PAM module

SYNOPSIS

       pam_rhosts.so

DESCRIPTION
       This module performs the standard network authentication for services, as used by traditional implementations of rlogin and rsh etc.

       The authentication mechanism of this module is based on the contents of two files; /etc/hosts.equiv (or and ~/.rhosts. Firstly, hosts listed in the
       former file are treated as equivalent to the localhost. Secondly, entries in the user's own copy of the latter file is used to map "remote-host
       remote-user" pairs to that user's account on the current host. Access is granted to the user if their host is present in /etc/hosts.equiv and their
       remote account is identical to their local one, or if their remote account has an entry in their personal configuration file.

       The module authenticates a remote user (internally specified by the item PAM_RUSER connecting from the remote host (internally specified by the item
       PAM_RHOST). Accordingly, for applications to be compatible this authentication module they must set these items prior to calling pam_authenticate().
       The module is not capable of independently probing the network connection for such information.

OPTIONS
       debug
	   Print debug information.

       silent
	   Don't print informative messages.

       superuser=account
	   Handle account as root.

MODULE TYPES PROVIDED
       Only the auth module type is provided.

RETURN VALUES
       PAM_AUTH_ERR
	   The remote host, remote user name or the local user name couldn't be determined or access was denied by .rhosts file.

       PAM_USER_UNKNOWN
	   User is not known to system.

EXAMPLES
       To grant a remote user access by /etc/hosts.equiv or .rhosts for rsh add the following lines to /etc/pam.d/rsh:

	   #%PAM-1.0
	   #
	   auth	    required	   pam_rhosts.so
	   auth	    required	   pam_nologin.so
	   auth	    required	   pam_env.so
	   auth	    required	   pam_unix.so

SEE ALSO
       rootok(3), hosts.equiv(5), rhosts(5), pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_rhosts was written by Thorsten Kukuk <kukuk@thkukuk.de>

Linux-PAM								  05/07/2023								 PAM_RHOSTS(8)
