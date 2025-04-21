BTRFS(8)								     BTRFS								      BTRFS(8)

NAME
       btrfs - a toolbox to manage btrfs filesystems

SYNOPSIS
       btrfs [global] <group> [<group>...] <command> [<args>]

DESCRIPTION
       The  btrfs  utility  is	a  toolbox for managing btrfs filesystems.  There are command groups to work with subvolumes, devices, for whole filesystem or
       other specific actions. See section COMMANDS.

       There are also standalone tools for some tasks like btrfs-convert(8) or btrfstune(8) that were separate historically and/or haven't been merged to  the
       main utility. See section STANDALONE TOOLS for more details.

       For other topics (mount options, etc) please refer to the separate manual page btrfs(5).

COMMAND SYNTAX
       Any  command  name can be shortened so long as the shortened form is unambiguous, however, it is recommended to use full command names in scripts.  All
       command groups have their manual page named btrfs-<group>.

       For example: it is possible to run btrfs sub snaps instead of btrfs subvolume snapshot.	But btrfs file s is not allowed, because file s may be	inter‐
       preted both as filesystem show and as filesystem sync.

       If the command name is ambiguous, the list of conflicting options is printed.

       Sizes,  both  upon input and output, can be expressed in either SI or IEC-I units (see numfmt(1)) with the suffix B appended.  All numbers will be for‐
       matted according to the rules of the C locale (ignoring the shell locale, see locale(7)).

       For an overview of a given command use btrfs command --help or btrfs [command...] --help --full to print all available options.

       There are global options that are passed between btrfs and the group name and affect behaviour not specific to the command, e.g. verbosity or the  type
       of the output.

       --format <format>
	      if supported by the command, print subcommand output in that format (text, json)

       -v|--verbose
	      increase verbosity of the subcommand

       -q|--quiet
	      print only errors

       --log <level>
	      set log level (default, info, verbose, debug, quiet)

       The remaining options are relevant only for the main tool:

       --help print condensed help for all subcommands

       --version
	      print version string

COMMANDS
       balance
	      Balance btrfs filesystem chunks across single or several devices.	 See btrfs-balance(8) for details.

       check  Do off-line check on a btrfs filesystem.	See btrfs-check(8) for details.

       device Manage devices managed by btrfs, including add/delete/scan and so on.  See btrfs-device(8) for details.

       filesystem
	      Manage a btrfs filesystem, including label setting/sync and so on.  See btrfs-filesystem(8) for details.

       inspect-internal
	      Debug tools for developers/hackers.  See btrfs-inspect-internal(8) for details.

       property
	      Get/set a property from/to a btrfs object.  See btrfs-property(8) for details.

       qgroup Manage quota group(qgroup) for btrfs filesystem.	See btrfs-qgroup(8) for details.

       quota  Manage quota on btrfs filesystem like enabling/rescan and etc.  See btrfs-quota(8) and btrfs-qgroup(8) for details.

       receive
	      Receive subvolume data from stdin/file for restore and etc.  See btrfs-receive(8) for details.

       replace
	      Replace btrfs devices.  See btrfs-replace(8) for details.

       rescue Try to rescue damaged btrfs filesystem.  See btrfs-rescue(8) for details.

       restore
	      Try to restore files from a damaged btrfs filesystem.  See btrfs-restore(8) for details.

       scrub  Scrub a btrfs filesystem.	 See btrfs-scrub(8) for details.

       send   Send subvolume data to stdout/file for backup and etc.  See btrfs-send(8) for details.

       subvolume
	      Create/delete/list/manage btrfs subvolume.  See btrfs-subvolume(8) for details.

STANDALONE TOOLS
       New  functionality  could  be provided using a standalone tool. If the functionality proves to be useful, then the standalone tool is declared obsolete
       and its functionality is copied to the main tool. Obsolete tools are removed after a long (years) depreciation period.

       Tools that are still in active use without an equivalent in btrfs:

       btrfs-convert
	      in-place conversion from ext2/3/4 filesystems to btrfs

       btrfstune
	      tweak some filesystem properties on a unmounted filesystem

       btrfs-select-super
	      rescue tool to overwrite primary superblock from a spare copy

       btrfs-find-root
	      rescue helper to find tree roots in a filesystem

       For space-constrained environments, it's possible to build a single binary with functionality of several standalone tools. This is following  the  con‐
       cept of busybox where the file name selects the functionality. This works for symlinks or hardlinks. The full list can be obtained by btrfs help --box.

EXIT STATUS
       btrfs returns a zero exit status if it succeeds. Non zero is returned in case of failure.

AVAILABILITY
       btrfs is part of btrfs-progs.  Please refer to the documentation at https://btrfs.readthedocs.io.

SEE ALSO
       btrfs(5),  btrfs-balance(8),  btrfs-check(8),  btrfs-convert(8),	 btrfs-device(8),  btrfs-filesystem(8),	 btrfs-inspect-internal(8), btrfs-property(8),
       btrfs-qgroup(8),	  btrfs-quota(8),   btrfs-receive(8),	btrfs-replace(8),   btrfs-rescue(8),	btrfs-restore(8),    btrfs-scrub(8),	btrfs-send(8),
       btrfs-subvolume(8), btrfstune(8), mkfs.btrfs(8)

6.6.3									 Mar 31, 2024								      BTRFS(8)
