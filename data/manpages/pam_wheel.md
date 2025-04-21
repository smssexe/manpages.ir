PAM_WHEEL(8)							       Linux-PAM Manual								  PAM_WHEEL(8)

NAME
       pam_wheel - Only permit root access to members of group wheel

SYNOPSIS

       pam_wheel.so [debug] [deny] [group=name] [root_only] [trust]

DESCRIPTION
       The pam_wheel PAM module is used to enforce the so-called wheel group. By default it permits access to the target user if the applicant user is a
       member of the wheel group. If no group with this name exist, the module is using the group with the group-ID 0.

OPTIONS
       debug
	   Print debug information.

       deny
	   Reverse the sense of the auth operation: if the user is trying to get UID 0 access and is a member of the wheel group (or the group of the group
	   option), deny access. Conversely, if the user is not in the group, return PAM_IGNORE (unless trust was also specified, in which case we return
	   PAM_SUCCESS).

       group=name
	   Instead of checking the wheel or GID 0 groups, use the name group to perform the authentication.

       root_only
	   The check for wheel membership is done only when the target user UID is 0.

       trust
	   The pam_wheel module will return PAM_SUCCESS instead of PAM_IGNORE if the user is a member of the wheel group (thus with a little play stacking the
	   modules the wheel members may be able to su to root without being prompted for a passwd).

MODULE TYPES PROVIDED
       The auth and account module types are provided.

RETURN VALUES
       PAM_AUTH_ERR
	   Authentication failure.

       PAM_BUF_ERR
	   Memory buffer error.

       PAM_IGNORE
	   The return value should be ignored by PAM dispatch.

       PAM_PERM_DENY
	   Permission denied.

       PAM_SERVICE_ERR
	   Cannot determine the user name.

       PAM_SUCCESS
	   Success.

       PAM_USER_UNKNOWN
	   User not known.

EXAMPLES
       The root account gains access by default (rootok), only wheel members can become root (wheel) but Unix authenticate non-root applicants.

	   su	   auth	    sufficient	   pam_rootok.so
	   su	   auth	    required	   pam_wheel.so
	   su	   auth	    required	   pam_unix.so

SEE ALSO
       pam.conf(5), pam.d(5), pam(7)

AUTHOR
       pam_wheel was written by Cristian Gafton <gafton@redhat.com>.

Linux-PAM								  09/13/2023								  PAM_WHEEL(8)
