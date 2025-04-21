GIT-HOOK(1)								  Git Manual								   GIT-HOOK(1)

NAME
       git-hook - Run git hooks

SYNOPSIS
       git hook run [--ignore-missing] [--to-stdin=<path>] <hook-name> [-- <hook-args>]

DESCRIPTION
       A command interface for running git hooks (see githooks(5)), for use by other scripted git commands.

SUBCOMMANDS
       run
	   Run the <hook-name> hook. See githooks(5) for supported hook names.

	   Any positional arguments to the hook should be passed after a mandatory -- (or --end-of-options, see gitcli(7)). See githooks(5) for arguments
	   hooks might expect (if any).

OPTIONS
       --to-stdin
	   For "run"; specify a file which will be streamed into the hook’s stdin. The hook will receive the entire file from beginning to EOF.

       --ignore-missing
	   Ignore any missing hook by quietly returning zero. Used for tools that want to do a blind one-shot run of a hook that may or may not be present.

SEE ALSO
       githooks(5)

GIT
       Part of the git(1) suite

Git 2.43.0								  01/13/2025								   GIT-HOOK(1)
