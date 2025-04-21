group_member(3)							   Library Functions Manual						       group_member(3)

NAME
       group_member - test whether a process is in a group

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       int group_member(gid_t gid);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       group_member():
	   _GNU_SOURCE

DESCRIPTION
       The group_member() function tests whether any of the caller's supplementary group IDs (as returned by getgroups(2)) matches gid.

RETURN VALUE
       The group_member() function returns nonzero if any of the caller's supplementary group IDs matches gid, and zero otherwise.

STANDARDS
       GNU.

SEE ALSO
       getgid(2), getgroups(2), getgrouplist(3), group(5)

Linux man-pages 6.7							  2023-10-31							       group_member(3)
