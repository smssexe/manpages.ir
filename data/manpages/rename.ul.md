RENAME(1)								 User Commands								     RENAME(1)

NAME
       rename - rename files

SYNOPSIS
       rename [options] expression replacement file...

DESCRIPTION
       rename will rename the specified files by replacing the first occurrence of expression in their name by replacement.

OPTIONS
       -s, --symlink
	   Do not rename a symlink but change where it points.

       -v, --verbose
	   Show which files were renamed, if any.

       -n, --no-act
	   Do not make any changes; add --verbose to see what would be made.

       -a, --all
	   Replace all occurrences of expression rather than only the first one.

       -l, --last
	   Replace the last occurrence of expression rather than the first one.

       -o, --no-overwrite
	   Do not overwrite existing files. When --symlink is active, do not overwrite symlinks pointing to existing targets.

       -i, --interactive
	   Ask before overwriting existing files.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

WARNING
       The renaming has no safeguards by default or without any one of the options --no-overwrite, --interactive or --no-act. If the user has permission to
       rewrite file names, the command will perform the action without any questions. For example, the result can be quite drastic when the command is run as
       root in the /lib directory. Always make a backup before running the command, unless you truly know what you are doing.

EDGE CASES
       If the expression is empty, then by default replacement will be added to the start of the filename. With --all, replacement will be inserted in between
       every two characters of the filename, as well as at the start and end.

       Normally, only the final path component of a filename is updated. (Or with --symlink, only the final path component of the link.) But if either
       expression or replacement contains a /, the full path is updated. This can cause a file to be moved between folders. Creating folders, and moving files
       between filesystems, is not supported.

INTERACTIVE MODE
       As most standard utilities rename can be used with a terminal device (tty in short) in canonical mode, where the line is buffered by the tty and you
       press ENTER to validate the user input. If you put your tty in cbreak mode however, rename requires only a single key press to answer the prompt. To
       set cbreak mode, run for example:

	   sh -c 'stty -icanon min 1; "$0" "$@"; stty icanon' rename -i from to files

EXIT STATUS
       0
	   all requested rename operations were successful

       1
	   all rename operations failed

       2
	   some rename operations failed

       4
	   nothing was renamed

       64
	   unanticipated error occurred

EXAMPLES
       Given the files foo1, ..., foo9, foo10, ..., foo278, the commands

	   rename foo foo00 foo?
	   rename foo foo0 foo??

       will turn them into foo001, ..., foo009, foo010, ..., foo278. And

	   rename .htm .html *.htm

       will fix the extension of your html files. Provide an empty string for shortening:

	   rename '_with_long_name' '' file_with_long_name.*

       will remove the substring in the filenames.

SEE ALSO
       mv(1)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The rename command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								     RENAME(1)
