SUBGID(5)							File Formats and Configuration							     SUBGID(5)

NAME
       subgid - the configuration for subordinate group ids

DESCRIPTION
       Subgid authorizes a group id to map ranges of group ids from its namespace into child namespaces.

       The delegation of the subordinate gids can be configured via the subid field in /etc/nsswitch.conf file. Only one value can be set as the delegation
       source. Setting this field to files configures the delegation of gids to /etc/subgid. Setting any other value treats the delegation as a plugin
       following with a name of the form libsubid_$value.so. If the value or plugin is missing, then the subordinate gid delegation falls back to files.

       Note, that groupadd will only create entries in /etc/subgid if subid delegation is managed via subid files.

LOCAL SUBORDINATE DELEGATION
       Each line in /etc/subgid contains a user name and a range of subordinate group ids that user is allowed to use. This is specified with three fields
       delimited by colons (“:”). These fields are:

       •   login name or UID

       •   numerical subordinate group ID

       •   numerical subordinate group ID count

       This file specifies the group IDs that ordinary users can use, with the newgidmap command, to configure gid mapping in a user namespace.

       Multiple ranges may be specified per user.

       When large number of entries (10000-100000 or more) are defined in /etc/subgid, parsing performance penalty will become noticeable. In this case it is
       recommended to use UIDs instead of login names. Benchmarks have shown speed-ups up to 20x.

FILES
       /etc/subgid
	   Per user subordinate group IDs.

       /etc/subgid-
	   Backup file for /etc/subgid.

SEE ALSO
       login.defs(5), newgidmap(1), newuidmap(1), newusers(8), subuid(5), useradd(8), userdel(8), usermod(8), user_namespaces(7).

shadow-utils 4.13							  05/30/2024								     SUBGID(5)
