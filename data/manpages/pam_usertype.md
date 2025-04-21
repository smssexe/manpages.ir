PAM_USERTYPE(8)							       Linux-PAM Manual							       PAM_USERTYPE(8)

NAME
       pam_usertype - check if the authenticated user is a system or regular account

SYNOPSIS

       pam_usertype.so [flag...] {condition}

DESCRIPTION
       pam_usertype.so is designed to succeed or fail authentication based on type of the account of the authenticated user. The type of the account is
       decided with help of SYS_UID_MAX settings in /etc/login.defs. One use is to select whether to load other modules based on this test.

       The module should be given only one condition as module argument. Authentication will succeed only if the condition is met.

OPTIONS
       The following flags are supported:

       use_uid
	   Evaluate conditions using the account of the user whose UID the application is running under instead of the user being authenticated.

       audit
	   Log unknown users to the system log.

       Available conditions are:

       issystem
	   Succeed if the user is a system user.

       isregular
	   Succeed if the user is a regular user.

MODULE TYPES PROVIDED
       All module types (account, auth, password and session) are provided.

RETURN VALUES
       PAM_SUCCESS
	   The condition was true.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_CONV_ERR
	   The conversation method supplied by the application failed to obtain the username.

       PAM_INCOMPLETE
	   The conversation method supplied by the application returned PAM_CONV_AGAIN.

       PAM_AUTH_ERR
	   The condition was false.

       PAM_SERVICE_ERR
	   A service error occurred or the arguments can't be parsed correctly.

       PAM_USER_UNKNOWN
	   User was not found.

EXAMPLES
       Skip remaining modules if the user is a system user:

	   account sufficient pam_usertype.so issystem

SEE ALSO
       login.defs(5), pam(8)

AUTHOR
       Pavel Březina <pbrezina@redhat.com>

Linux-PAM								  05/07/2023							       PAM_USERTYPE(8)
