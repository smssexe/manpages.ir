ADDUSER(8)							    System Manager's Manual							    ADDUSER(8)

NAME
       adduser.local, deluser.local - hook for local actions in adduser and deluser

SYNOPSIS
       adduser.local [username] [uid] [gid] [home-directory]
       deluser.local [username] [uid] [gid] [home-directory]

DESCRIPTION
       adduser.local  and  deluser.local can be placed by the local admin into /usr/local/sbin and will be called by adduser and deluser respectively in order
       to do locally relevant setup and cleanup actions.

       The hooks are called while the adduser/deluser lock is active.  They must therefore not call back to adduser/deluser themselves.

RETURN VALUE
       Return values from the hooks are ignored.

ENVIRONMENT
       VERBOSE

       0      if  --quiet is specified

       1      if neither --quiet nor --debug is specified

       2      if --debug is specified

SEE ALSO
       adduser.conf(5), deluser.conf(5), adduser(8), deluser(8), groupadd(8), useradd(8), usermod(8), Debian Policy 9.2.2.

Debian GNU/Linux																    ADDUSER(8)
