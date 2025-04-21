PAM_STRESS(8)							       Linux-PAM Manual								 PAM_STRESS(8)

NAME
       pam_stress - The stress-testing PAM module

SYNOPSIS

       pam_stress.so [debug] [no_warn] [use_first_pass] [try_first_pass] [rootok] [expired] [fail_1] [fail_2] [prelim] [required]

DESCRIPTION
       The pam_stress PAM module is mainly intended to give the impression of failing as a fully functioning module might.

OPTIONS
       debug
	   Put lots of information in syslog. *NOTE* this option writes passwords to syslog, so don't use anything sensitive when testing.

       no_warn
	   Do not give warnings about things (otherwise warnings are issued via the conversation function)

       use_first_pass
	   Do not prompt for a password, for pam_sm_authentication function just use item PAM_AUTHTOK.

       try_first_pass
	   Do not prompt for a password unless there has been no previous authentication token (item PAM_AUTHTOK is NULL)

       rootok
	   This is intended for the pam_sm_chauthtok function and it instructs this function to permit root to change the user's password without entering the
	   old password.

       expired
	   An argument intended for the account and chauthtok module parts. It instructs the module to act as if the user's password has expired

       fail_1
	   This instructs the module to make its first function fail.

       fail_2
	   This instructs the module to make its second function (if there is one) fail.

       prelim
	   For pam_sm_chauthtok, means fail on PAM_PRELIM_CHECK.

       required
	   For pam_sm_chauthtok, means fail if the user hasn't already been authenticated by this module. (See stress_new_pwd data string in the NOTES.)

MODULE TYPES PROVIDED
       All module types (auth, account, password and session) are provided.

RETURN VALUES
       PAM_BUF_ERR
	   Memory buffer error.

       PAM_PERM_DENIED
	   Permission denied.

       PAM_AUTH_ERR
	   Access to the system was denied.

       PAM_CONV_ERR
	   Conversation failure.

       PAM_SUCCESS
	   The function passes all checks.

       PAM_USER_UNKNOWN
	   The user is not known to the system.

       PAM_CRED_ERR
	   Failure involving user credentials.

       PAM_NEW_AUTHTOK_REQD
	   Authentication token is no longer valid; new one required.

       PAM_SESSION_ERR
	   Session failure.

       PAM_TRY_AGAIN
	   Failed preliminary check by service.

       PAM_AUTHTOK_LOCK_BUSY
	   Authentication token lock busy.

       PAM_AUTHTOK_ERR
	   Authentication token manipulation error.

       PAM_SYSTEM_ERR
	   System error.

NOTES
       This module uses the stress_new_pwd data string which tells pam_sm_chauthtok that pam_sm_acct_mgmt says we need a new password. The only possible value
       for this data string is 'yes'.

EXAMPLES
	   #%PAM-1.0
	   #
	   # Any of the following will suffice
	   account  required pam_stress.so
	   auth	    required pam_stress.so
	   password required pam_stress.so
	   session  required pam_stress.so

SEE ALSO
       pam.conf(5), pam.d(5), pam(8).

AUTHORS
       The pam_stress PAM module was developed by Andrew Morgan <morgan@linux.kernel.org>. The man page for pam_stress was written by Lucas Ramage
       <ramage.lucas@protonmail.com>.

Linux-PAM								  05/07/2023								 PAM_STRESS(8)
