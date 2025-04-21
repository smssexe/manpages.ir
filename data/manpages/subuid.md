SUBUID(5)							File Formats and Configuration							     SUBUID(5)

NAME
       subuid - the configuration for subordinate user ids

DESCRIPTION
       Subuid authorizes a user id to map ranges of user ids from its namespace into child namespaces.

       The delegation of the subordinate uids can be configured via the subid field in /etc/nsswitch.conf file. Only one value can be set as the delegation
       source. Setting this field to files configures the delegation of uids to /etc/subuid. Setting any other value treats the delegation as a plugin
       following with a name of the form libsubid_$value.so. If the value or plugin is missing, then the subordinate uid delegation falls back to files.

       Note, that useradd will only create entries in /etc/subuid if subid delegation is managed via subid files.

LOCAL SUBORDINATE DELEGATION
       Each line in /etc/subuid contains a user name and a range of subordinate user ids that user is allowed to use. This is specified with three fields
       delimited by colons (“:”). These fields are:

       •   login name or UID

       •   numerical subordinate user ID

       •   numerical subordinate user ID count

       This file specifies the user IDs that ordinary users can use, with the newuidmap command, to configure uid mapping in a user namespace.

       Multiple ranges may be specified per user.

       When large number of entries (10000-100000 or more) are defined in /etc/subuid, parsing performance penalty will become noticeable. In this case it is
       recommended to use UIDs instead of login names. Benchmarks have shown speed-ups up to 20x.

FILES
       /etc/subuid
	   Per user subordinate user IDs.

       /etc/subuid-
	   Backup file for /etc/subuid.

SEE ALSO
       login.defs(5), newgidmap(1), newuidmap(1), newusers(1), subgid(5), useradd(8), userdel(8), usermod(8), user_namespaces(7).

shadow-utils 4.13							  05/30/2024								     SUBUID(5)
