PAM_DEBUG(8)							       Linux-PAM Manual								  PAM_DEBUG(8)

NAME
       pam_debug - PAM module to debug the PAM stack

SYNOPSIS

       pam_debug.so [auth=value] [cred=value] [acct=value] [prechauthtok=value] [chauthtok=value] [auth=value] [open_session=value] [close_session=value]

DESCRIPTION
       The pam_debug PAM module is intended as a debugging aide for determining how the PAM stack is operating. This module returns what its module arguments
       tell it to return.

OPTIONS
       auth=value
	   The pam_sm_authenticate(3) function will return value.

       cred=value
	   The pam_sm_setcred(3) function will return value.

       acct=value
	   The pam_sm_acct_mgmt(3) function will return value.

       prechauthtok=value
	   The pam_sm_chauthtok(3) function will return value if the PAM_PRELIM_CHECK flag is set.

       chauthtok=value
	   The pam_sm_chauthtok(3) function will return value if the PAM_PRELIM_CHECK flag is not set.

       open_session=value
	   The pam_sm_open_session(3) function will return value.

       close_session=value
	   The pam_sm_close_session(3) function will return value.

       Where value can be one of: success, open_err, symbol_err, service_err, system_err, buf_err, perm_denied, auth_err, cred_insufficient, authinfo_unavail,
       user_unknown, maxtries, new_authtok_reqd, acct_expired, session_err, cred_unavail, cred_expired, cred_err, no_module_data, conv_err, authtok_err,
       authtok_recover_err, authtok_lock_busy, authtok_disable_aging, try_again, ignore, abort, authtok_expired, module_unknown, bad_item, conv_again,
       incomplete.

MODULE TYPES PROVIDED
       All module types (auth, account, password and session) are provided.

RETURN VALUES
       PAM_SUCCESS
	   Default return code if no other value was specified, else specified return value.

EXAMPLES
	   auth	   requisite	   pam_permit.so
	   auth	   [success=2 default=ok]  pam_debug.so auth=perm_denied cred=success
	   auth	   [default=reset]	   pam_debug.so auth=success cred=perm_denied
	   auth	   [success=done default=die] pam_debug.so
	   auth	   optional	   pam_debug.so auth=perm_denied cred=perm_denied
	   auth	   sufficient	   pam_debug.so auth=success cred=success

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_debug was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								  PAM_DEBUG(8)
