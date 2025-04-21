LSLOGINS(1)								 User Commands								   LSLOGINS(1)

NAME
       lslogins - display information about known users in the system

SYNOPSIS
       lslogins [options] [-s|-u[=UID]] [-g groups] [-l logins] [username]

DESCRIPTION
       Examine the wtmp and btmp logs, /etc/shadow (if necessary) and /passwd and output the desired data.

       The optional argument username forces lslogins to print all available details about the specified user only. In this case the output format is
       different than in case of -l or -g and unknown is username reported as an error.

       The default action is to list info about all the users in the system.

OPTIONS
       Mandatory arguments to long options are mandatory for short options too.

       -a, --acc-expiration
	   Display data about the date of last password change and the account expiration date (see shadow(5) for more info). (Requires root privileges.)

       --btmp-file path
	   Alternate path for btmp.

       -c, --colon-separate
	   Separate info about each user with a colon instead of a newline.

       -e, --export
	   Output data in the format of NAME=VALUE. See also option --shell.

       -f, --failed
	   Display data about the users' last failed login attempts.

       -G, --supp-groups
	   Show information about supplementary groups.

       -g, --groups=groups
	   Only show data of users belonging to groups. More than one group may be specified; the list has to be comma-separated. Unknown group names are
	   ignored.

	   Note that the relation between user and group may be invisible for the primary group if the user is not explicitly specified as group member (e.g.,
	   in /etc/group). If the command lslogins scans for groups then it uses the groups database only, and the user database with primary GID is not used
	   at all.

       -L, --last
	   Display data containing information about the users' last login sessions.

       -l, --logins=logins
	   Only show data of users with a login specified in logins (user names or user IDs). More than one login may be specified; the list has to be
	   comma-separated. Unknown login names are ignored.

       -n, --newline
	   Display each piece of information on a separate line.

       --noheadings
	   Do not print a header line.

       --notruncate
	   Don’t truncate output.

       -o, --output list
	   Specify which output columns to print. The default list of columns may be extended if list is specified in the format +list.

       --output-all
	   Output all available columns. --help to get a list of all supported columns.

       -p, --pwd
	   Display information related to login by password (see also -afL).

       -r, --raw
	   Raw output (no columnation).

       -s, --system-accs
	   Show system accounts. These are by default all accounts with a UID between 101 and 999 (inclusive), with the exception of either nobody or
	   nfsnobody (UID 65534). This hardcoded default may be overwritten by parameters SYS_UID_MIN and SYS_UID_MAX in the file /etc/login.defs.

       --time-format type
	   Display dates in short, full or iso format. The default is short, this time format is designed to be space efficient and human readable.

       -u, --user-accs
	   Show user accounts. These are by default all accounts with UID above 1000 (inclusive), with the exception of either nobody or nfsnobody (UID
	   65534). This hardcoded default maybe overwritten by parameters UID_MIN and UID_MAX in the file /etc/login.defs.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

       --wtmp-file path
	   Alternate path for wtmp.

       --lastlog path
	   Alternate path for lastlog(8).

       -y, --shell
	   The column name will be modified to contain only characters allowed for shell variable identifiers. This is usable, for example, with --export.
	   Note that this feature has been automatically enabled for --export in version 2.37, but due to compatibility issues, now it’s necessary to request
	   this behavior by --shell.

       -Z, --context
	   Display the users' security context.

       -z, --print0
	   Delimit user entries with a nul character, instead of a newline.

EXIT STATUS
       0
	   if OK,

       1
	   if incorrect arguments specified,

       2
	   if a serious error occurs (e.g., a corrupt log).

NOTES
       The default UID thresholds are read from /etc/login.defs.

   Password status
       Multiple fields describe password status.

       "Password is locked"
	   The password is prefixed by '!!', and the user cannot login although the password is set or empty. This is common for new accounts without a set
	   password.

       "Password not required (empty)"
	   The password is not set (hash is missing); this is common for locked system accounts. Not requiring a password does not mean the user can log-in
	   without a password. It depends on the password "lock" status.

       "Login by password disabled"
	   'yes' means that there is no valid password. The password hash is missing, or the hash method is unknown or contains invalid chars.

HISTORY
       The lslogins utility is inspired by the logins utility, which first appeared in FreeBSD 4.10.

AUTHORS
       Ondrej Oprala <ooprala@redhat.com>, Karel Zak <kzak@redhat.com>

SEE ALSO
       group(5), passwd(5), shadow(5), utmp(5)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The lslogins command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-30								   LSLOGINS(1)
