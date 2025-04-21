PAM_GROUP(8)							       Linux-PAM Manual								  PAM_GROUP(8)

NAME
       pam_group - PAM module for group access

SYNOPSIS

       pam_group.so

DESCRIPTION
       The pam_group PAM module does not authenticate the user, but instead it grants group memberships (in the credential setting phase of the authentication
       module) to the user. Such memberships are based on the service they are applying for.

       By default rules for group memberships are taken from config file /etc/security/group.conf.

       This module's usefulness relies on the file-systems accessible to the user. The point being that once granted the membership of a group, the user may
       attempt to create a setgid binary with a restricted group ownership. Later, when the user is not given membership to this group, they can recover group
       membership with the precompiled binary. The reason that the file-systems that the user has access to are so significant, is the fact that when a system
       is mounted nosuid the user is unable to create or execute such a binary file. For this module to provide any level of security, all file-systems that
       the user has write access to should be mounted nosuid.

       The pam_group module functions in parallel with the /etc/group file. If the user is granted any groups based on the behavior of this module, they are
       granted in addition to those entries /etc/group (or equivalent).

OPTIONS
       This module does not recognise any options.

MODULE TYPES PROVIDED
       Only the auth module type is provided.

RETURN VALUES
       PAM_SUCCESS
	   group membership was granted.

       PAM_ABORT
	   Not all relevant data could be gotten.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_CRED_ERR
	   Group membership was not granted.

       PAM_IGNORE
	   pam_sm_authenticate was called which does nothing.

       PAM_USER_UNKNOWN
	   The user is not known to the system.

FILES
       /etc/security/group.conf
	   Default configuration file

SEE ALSO
       group.conf(5), pam.d(5), pam(7).

AUTHORS
       pam_group was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								  PAM_GROUP(8)
