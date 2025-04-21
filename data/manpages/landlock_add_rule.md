landlock_add_rule(2)						      System Calls Manual						  landlock_add_rule(2)

NAME
       landlock_add_rule - add a new Landlock rule to a ruleset

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <linux/landlock.h>  /* Definition of LANDLOCK_* constants */
       #include <sys/syscall.h>	    /* Definition of SYS_* constants */

       int syscall(SYS_landlock_add_rule, int ruleset_fd,
		   enum landlock_rule_type rule_type,
		   const void *rule_attr, uint32_t flags);

DESCRIPTION
       A  Landlock  rule describes an action on an object.  An object is currently a file hierarchy, and the related filesystem actions are defined with a set
       of access rights.  This landlock_add_rule() system call enables adding a new Landlock rule to an existing ruleset  created  with	 landlock_create_rule‐
       set(2).	See landlock(7) for a global overview.

       ruleset_fd is a Landlock ruleset file descriptor obtained with landlock_create_ruleset(2).

       rule_type identifies the structure type pointed to by rule_attr.	 Currently, Linux supports the following rule_type value:

       LANDLOCK_RULE_PATH_BENEATH
	      This defines the object type as a file hierarchy.	 In this case, rule_attr points to the following structure:

		  struct landlock_path_beneath_attr {
		      __u64 allowed_access;
		      __s32 parent_fd;
		  } __attribute__((packed));

	      allowed_access contains a bitmask of allowed filesystem actions for this file hierarchy (see Filesystem actions in landlock(7)).

	      parent_fd	 is  an opened file descriptor, preferably with the O_PATH flag, which identifies the parent directory of the file hierarchy or just a
	      file.

       flags must be 0.

RETURN VALUE
       On success, landlock_add_rule() returns 0.

ERRORS
       landlock_add_rule() can fail for the following reasons:

       EOPNOTSUPP
	      Landlock is supported by the kernel but disabled at boot time.

       EINVAL flags is not 0, or the rule accesses are inconsistent (i.e., rule_attr->allowed_access is not a subset of the ruleset handled accesses).

       ENOMSG Empty accesses (i.e., rule_attr->allowed_access is 0).

       EBADF  ruleset_fd is not a file descriptor for the current thread, or a member of rule_attr is not a file descriptor as expected.

       EBADFD ruleset_fd is not a ruleset file descriptor, or a member of rule_attr is not the expected file descriptor type.

       EPERM  ruleset_fd has no write access to the underlying ruleset.

       EFAULT rule_attr was not a valid address.

STANDARDS
       Linux.

HISTORY
       Linux 5.13.

EXAMPLES
       See landlock(7).

SEE ALSO
       landlock_create_ruleset(2), landlock_restrict_self(2), landlock(7)

Linux man-pages 6.7							  2023-10-31							  landlock_add_rule(2)
