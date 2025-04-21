PAM_CAP(8)							       Linux-PAM Manual								    PAM_CAP(8)

NAME
       pam_cap - PAM module to set inheritable capabilities

SYNOPSIS

       pam_cap.so [config=/path/to/capability.conf] [debug]

DESCRIPTION
       The pam_cap PAM module sets the current process' inheritable capabilities.

       Capabilities are read from the /etc/security/capability.conf config file, or alternate file specified with the config= option.

       The module must not be called by a multithreaded application.

OPTIONS
       config=/path/to/capability.conf
	   Indicate an alternative capability.conf style configuration file to override the default.

       debug
	   Print debug information.

MODULE TYPES PROVIDED
       Only the authentication module type is provided.

RETURN VALUES
       PAM_AUTH_ERR
	   The user is not known to the system.

       PAM_IGNORE
	   No capabilities found for this user.

       PAM_INCOMPLETE
	   Indicates a PAM-Conversation failure.

       PAM_SUCCESS
	   Capabilities were set.

FILES
       /etc/security/capability.conf
	   Default configuration file

EXAMPLES
       Nearly all applications/daemons which use PAM for authentication contain a configuration line: @include common-auth.  Thus, to set inheritable
       capabilities in all of these applications, add the following as the last line to /etc/pam.d/common-auth

	   auth	     optional	     pam_cap.so

       To set inheritable capabilities for a user in a specific application, or in application(s) which do not @include common-auth, add the line below to the
       application-specific file; e.g. /etc/pam.d/myapp

	   auth	     optional	     pam_cap.so

SEE ALSO
       capability.conf(5), pam.d(5), pam(7).

AUTHORS
       pam_cap was initially written by Andrew G. Morgan <morgan@kernel.org>

Linux-PAM Manual							  09/23/2011								    PAM_CAP(8)
