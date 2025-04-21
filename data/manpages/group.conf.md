GROUP.CONF(5)							       Linux-PAM Manual								 GROUP.CONF(5)

NAME
       group.conf - configuration file for the pam_group module

DESCRIPTION
       The pam_group PAM module does not authenticate the user, but instead it grants group memberships (in the credential setting phase of the authentication
       module) to the user. Such memberships are based on the service they are applying for.

       For this module to function correctly there must be a correctly formatted /etc/security/group.conf file present. White spaces are ignored and lines
       maybe extended with '\' (escaped newlines). Text following a '#' is ignored to the end of the line.

       The syntax of the lines is as follows:

       services;ttys;users;times;groups

       The first field, the services field, is a logic list of PAM service names that the rule applies to.

       The second field, the tty field, is a logic list of terminal names that this rule applies to.

       The third field, the users field, is a logic list of users, or a UNIX group, or a netgroup of users to whom this rule applies. Group names are preceded
       by a '%' symbol, while netgroup names are preceded by a '@' symbol.

       A logic list namely means individual tokens that are optionally prefixed with '!' (logical not) and separated with '&' (logical and) and '|' (logical
       or).

       For these items the simple wildcard '*' may be used only once. With UNIX groups or netgroups no wildcards or logic operators are allowed.

       The times field is used to indicate "when" these groups are to be given to the user. The format here is a logic list of day/time-range entries. The
       days are specified by a sequence of two character entries, MoTuSa for example is Monday Tuesday and Saturday. Note that repeated days are unset MoMo =
       no day, and MoWk = all weekdays bar Monday. The two character combinations accepted are Mo Tu We Th Fr Sa Su Wk Wd Al, the last two being week-end days
       and all 7 days of the week respectively. As a final example, AlFr means all days except Friday.

       Each day/time-range can be prefixed with a '!' to indicate "anything but". The time-range part is two 24-hour times HHMM, separated by a hyphen,
       indicating the start and finish time (if the finish time is smaller than the start time it is deemed to apply on the following day).

       The groups field is a comma or space separated list of groups that the user inherits membership of. These groups are added if the previous fields are
       satisfied by the user's request.

       For a rule to be active, ALL of service+ttys+users must be satisfied by the applying process.

EXAMPLES
       These are some example lines which might be specified in /etc/security/group.conf.

       Running 'xsh' on tty* (any ttyXXX device), the user 'us' is given access to the floppy (through membership of the floppy group)

	   xsh;tty*&!ttyp*;us;Al0000-2400;floppy

       Running 'xsh' on tty* (any ttyXXX device), the users 'sword', 'pike' and 'shield' are given access to games (through membership of the floppy group)
       after work hours.

	   xsh; tty* ;sword|pike|shield;!Wk0900-1800;games, sound
	   xsh; tty* ;*;Al0900-1800;floppy

       Any member of the group 'admin' running 'xsh' on tty*, is granted access (at any time) to the group 'plugdev'

	   xsh; tty* ;%admin;Al0000-2400;plugdev

SEE ALSO
       pam_group(8), pam.d(5), pam(7)

AUTHOR
       pam_group was written by Andrew G. Morgan <morgan@kernel.org>.

Linux-PAM								  05/07/2023								 GROUP.CONF(5)
