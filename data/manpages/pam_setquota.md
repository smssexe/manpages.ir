PAM_SETQUOTA(8)							       Linux-PAM Manual							       PAM_SETQUOTA(8)

NAME
       pam_setquota - PAM module to set or modify disk quotas on session start

SYNOPSIS

       pam_setquota.so [fs=/home] [overwrite=0] [debug=0] [startuid=1000] [enduid=0] [bsoftlimit=19000] [bhardlimit=20000] [isoftlimit=3000] [ihardlimit=4000]

DESCRIPTION
       pam_setquota is a PAM module to set or modify a disk quota at session start

       This makes quotas usable with central user databases, such as MySQL or LDAP.

OPTIONS
       fs=/home
	   The device file or mountpoint the policy applies to. Defaults to the filesystem containing the users home directory.

       overwrite=0
	   Overwrite an existing quota. Note: Enabling this will remove the ability for the admin to manually configure different quotas for users for a
	   filesystem with edquota(8). (Defaults to 0)

       debug=0
	   Enable debugging. A value of 1 outputs the old and new quota on a device. A value of 2 also prints out the matched and found filesystems should fs
	   be unset. (Defaults to 0)

       startuid=1000
	   Describe the start of the UID range the policy is applied to. (Defaults to UID_MIN from login.defs or the uidmin value defined at compile-time if
	   UID_MIN is undefined.)

       enduid=0
	   Describe the end of the UID range the policy is applied to. Setting enduid=0 results in an open-ended UID range (i.e. all uids greater than
	   startuid are included). (Defaults to 0)

       bsoftlimit=19000
	   Soft limit for disk quota blocks, as defined by quotactl(2). Note: bsoftlimit and bhardlimit must be set at the same time!

       bhardlimit=20000
	   Hard limit for disk quota blocks, as defined by quotactl(2). Note: bsoftlimit and bhardlimit must be set at the same time!

       isoftlimit=3000
	   Soft limit for inodes, as defined by
	    quotactl(2). Note: isoftlimit and ihardlimit must be set at the same time!

       ihardlimit=4000
	   Hard limit for inodes, as defined by
	    quotactl(2). Note: isoftlimit and ihardlimit must be set at the same time!

MODULE TYPES PROVIDED
       Only the session module type is provided.

RETURN VALUES
       PAM_SUCCESS
	   The quota was set successfully.

       PAM_IGNORE
	   No action was taken because either the UID of the user was outside of the specified range, a quota already existed and overwrite=1 was not
	   configured or no limits were configured at all.

       PAM_USER_UNKNOWN
	   The user was not found.

       PAM_PERM_DENIED
	   /proc/mounts could not be opened.

	   The filesystem or device specified was not found.

	   The limits for the user could not be retrieved. See syslog for more information.

	   The limits for the user could not be set. See syslog for more information.

	   Either isoftlimit/ihardlimit or bsoftlimit/bhardlimit were not set at the same time.

EXAMPLES
       A single invocation of `pam_setquota` applies a specific policy to a UID range. Applying different policies to specific UID ranges is done by invoking
       pam_setquota more than once. The last matching entry defines the resulting quota.

		 session  required   pam_setquota.so bsoftlimit=1000 bhardlimit=2000 isoftlimit=1000 ihardlimit=2000 startuid=1000 enduid=0 fs=/home
		 session  required   pam_setquota.so bsoftlimit=19000 bhardlimit=20000 isoftlimit=3000 ihardlimit=4000 startuid=2001 enduid=3000 fs=/dev/sda1
		 session  required   pam_setquota.so bsoftlimit=19000 bhardlimit=20000 isoftlimit=3000 ihardlimit=4000 startuid=3001 enduid=4000 fs=/dev/sda1 overwrite=1

SEE ALSO
       pam.conf(5), pam.d(5), pam(8)

AUTHOR
       pam_setquota was originally written by Ruslan Savchenko <savrus@mexmat.net>.

       Further modifications were made by Shane Tzen <shane@ict.usc.edu>, Sven Hartge <sven@svenhartge.de> and Keller Fuchs <kellerfuchs@hashbang.sh>.

Linux-PAM								  05/07/2023							       PAM_SETQUOTA(8)
