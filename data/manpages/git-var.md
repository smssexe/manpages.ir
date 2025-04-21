GIT-VAR(1)								  Git Manual								    GIT-VAR(1)

NAME
       git-var - Show a Git logical variable

SYNOPSIS
       git var (-l | <variable>)

DESCRIPTION
       Prints a Git logical variable. Exits with code 1 if the variable has no value.

OPTIONS
       -l
	   Display the logical variables. In addition, all the variables of the Git configuration file .git/config are listed as well. (However, the
	   configuration variables listing functionality is deprecated in favor of git config -l.)

EXAMPLES
	   $ git var GIT_AUTHOR_IDENT
	   Eric W. Biederman <ebiederm@lnxi.com> 1121223278 -0600

VARIABLES
       GIT_AUTHOR_IDENT
	   The author of a piece of code.

       GIT_COMMITTER_IDENT
	   The person who put a piece of code into Git.

       GIT_EDITOR
	   Text editor for use by Git commands. The value is meant to be interpreted by the shell when it is used. Examples: ~/bin/vi,
	   $SOME_ENVIRONMENT_VARIABLE, "C:\Program Files\Vim\gvim.exe" --nofork. The order of preference is the $GIT_EDITOR environment variable, then
	   core.editor configuration, then $VISUAL, then $EDITOR, and then the default chosen at compile time, which is usually vi. The build you are using
	   chose editor as the default.

       GIT_SEQUENCE_EDITOR
	   Text editor used to edit the todo file while running git rebase -i. Like GIT_EDITOR, the value is meant to be interpreted by the shell when it is
	   used. The order of preference is the $GIT_SEQUENCE_EDITOR environment variable, then sequence.editor configuration, and then the value of git var
	   GIT_EDITOR.

       GIT_PAGER
	   Text viewer for use by Git commands (e.g., less). The value is meant to be interpreted by the shell. The order of preference is the $GIT_PAGER
	   environment variable, then core.pager configuration, then $PAGER, and then the default chosen at compile time (usually less). The build you are
	   using chose pager as the default.

       GIT_DEFAULT_BRANCH
	   The name of the first branch created in newly initialized repositories.

       GIT_SHELL_PATH
	   The path of the binary providing the POSIX shell for commands which use the shell.

       GIT_ATTR_SYSTEM
	   The path to the system gitattributes(5) file, if one is enabled.

       GIT_ATTR_GLOBAL
	   The path to the global (per-user) gitattributes(5) file.

       GIT_CONFIG_SYSTEM
	   The path to the system configuration file, if one is enabled.

       GIT_CONFIG_GLOBAL
	   The path to the global (per-user) configuration files, if any.

       Most path values contain only one value. However, some can contain multiple values, which are separated by newlines, and are listed in order from
       highest to lowest priority. Callers should be prepared for any such path value to contain multiple items.

       Note that paths are printed even if they do not exist, but not if they are disabled by other environment variables.

SEE ALSO
       git-commit-tree(1) git-tag(1) git-config(1)

GIT
       Part of the git(1) suite

Git 2.43.0								  01/13/2025								    GIT-VAR(1)
