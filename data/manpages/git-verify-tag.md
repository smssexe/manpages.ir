GIT-VERIFY-TAG(1)							  Git Manual							     GIT-VERIFY-TAG(1)

NAME
       git-verify-tag - Check the GPG signature of tags

SYNOPSIS
       git verify-tag [-v | --verbose] [--format=<format>] [--raw] <tag>...

DESCRIPTION
       Validates the gpg signature created by git tag.

OPTIONS
       --raw
	   Print the raw gpg status output to standard error instead of the normal human-readable output.

       -v, --verbose
	   Print the contents of the tag object before validating it.

       <tag>...
	   SHA-1 identifiers of Git tag objects.

GIT
       Part of the git(1) suite

Git 2.43.0								  01/13/2025							     GIT-VERIFY-TAG(1)
