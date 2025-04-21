landlock_create_ruleset(2)					      System Calls Manual					    landlock_create_ruleset(2)

NAME
       landlock_create_ruleset - create a new Landlock ruleset

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <linux/landlock.h>  /* Definition of LANDLOCK_* constants */
       #include <sys/syscall.h>	    /* Definition of SYS_* constants */

       int syscall(SYS_landlock_create_ruleset,
		   const struct landlock_ruleset_attr *attr,
		   size_t size , uint32_t flags);

DESCRIPTION
       A  Landlock  ruleset  identifies a set of rules (i.e., actions on objects).  This landlock_create_ruleset() system call enables creating a new file de‐
       scriptor identifying a ruleset.	This file descriptor can then be used by landlock_add_rule(2) and landlock_restrict_self(2).  See  landlock(7)	for  a
       global overview.

       attr specifies the properties of the new ruleset.  It points to the following structure:

		  struct landlock_ruleset_attr {
		      __u64 handled_access_fs;
		  };

	      handled_access_fs	 is  a	bitmask of actions that is handled by this ruleset and should then be forbidden if no rule explicitly allows them (see
	      Filesystem actions in landlock(7)).  This enables simply restricting ambient rights (e.g., global filesystem access) and is needed for  compati‐
	      bility reasons.

       size must be specified as sizeof(struct landlock_ruleset_attr) for compatibility reasons.

       flags must be 0 if attr is used.	 Otherwise, flags can be set to:

       LANDLOCK_CREATE_RULESET_VERSION
	      If  attr is NULL and size is 0, then the returned value is the highest supported Landlock ABI version (starting at 1).  This version can be used
	      for a best-effort security approach, which is encouraged when user space is not pinned to a specific kernel version.  All features documented in
	      these man pages are available with the version 1.

RETURN VALUE
       On success, landlock_create_ruleset() returns a new Landlock ruleset file descriptor, or a Landlock ABI version, according to flags.

ERRORS
       landlock_create_ruleset() can fail for the following reasons:

       EOPNOTSUPP
	      Landlock is supported by the kernel but disabled at boot time.

       EINVAL Unknown flags, or unknown access, or too small size.

       E2BIG  size is too big.

       EFAULT attr was not a valid address.

       ENOMSG Empty accesses (i.e., attr->handled_access_fs is 0).

STANDARDS
       Linux.

HISTORY
       Linux 5.13.

EXAMPLES
       See landlock(7).

SEE ALSO
       landlock_add_rule(2), landlock_restrict_self(2), landlock(7)

Linux man-pages 6.7							  2023-10-31						    landlock_create_ruleset(2)
