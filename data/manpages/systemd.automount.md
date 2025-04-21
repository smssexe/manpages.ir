SYSTEMD.AUTOMOUNT(5)						       systemd.automount						  SYSTEMD.AUTOMOUNT(5)

NAME
       systemd.automount - Automount unit configuration

SYNOPSIS
       automount.automount

DESCRIPTION
       A unit configuration file whose name ends in ".automount" encodes information about a file system automount point controlled and supervised by systemd.
       Automount units may be used to implement on-demand mounting as well as parallelized mounting of file systems.

       This man page lists the configuration options specific to this unit type. See systemd.unit(5) for the common options of all unit configuration files.
       The common configuration items are configured in the generic [Unit] and [Install] sections. The automount specific configuration options are configured
       in the [Automount] section.

       Automount units must be named after the automount directories they control. Example: the automount point /home/lennart must be configured in a unit
       file home-lennart.automount. For details about the escaping logic used to convert a file system path to a unit name see systemd.unit(5). Note that
       automount units cannot be templated, nor is it possible to add multiple names to an automount unit by creating symlinks to its unit file.

       For each automount unit file a matching mount unit file (see systemd.mount(5) for details) must exist which is activated when the automount path is
       accessed. Example: if an automount unit home-lennart.automount is active and the user accesses /home/lennart the mount unit home-lennart.mount will be
       activated.

       Note that automount units are separate from the mount itself, so you should not set After= or Requires= for mount dependencies here. For example, you
       should not set After=network-online.target or similar on network filesystems. Doing so may result in an ordering cycle.

       Note that automount support on Linux is privileged, automount units are hence only available in the system service manager (and root's user service
       manager), but not in unprivileged users' service managers.

       Note that automount units should not be nested. (The establishment of the inner automount point would unconditionally pin the outer mount point,
       defeating its purpose.)

AUTOMATIC DEPENDENCIES
   Implicit Dependencies
       The following dependencies are implicitly added:

       •   If an automount unit is beneath another mount unit in the file system hierarchy, a requirement and ordering dependencies are created to the on the
	   unit higher in the hierarchy.

       •   An implicit Before= dependency is created between an automount unit and the mount unit it activates.

   Default Dependencies
       The following dependencies are added unless DefaultDependencies=no is set:

       •   Automount units acquire automatic Before= and Conflicts= on umount.target in order to be stopped during shutdown.

       •   Automount units automatically gain an After= dependency on local-fs-pre.target, and a Before= dependency on local-fs.target.

FSTAB
       Automount units may either be configured via unit files, or via /etc/fstab (see fstab(5) for details).

       For details how systemd parses /etc/fstab see systemd.mount(5).

       If an automount point is configured in both /etc/fstab and a unit file, the configuration in the latter takes precedence.

OPTIONS
       Automount unit files may include [Unit] and [Install] sections, which are described in systemd.unit(5).

       Automount unit files must include an [Automount] section, which carries information about the file system automount points it supervises. The options
       specific to the [Automount] section of automount units are the following:

       Where=
	   Takes an absolute path of a directory of the automount point. If the automount point does not exist at time that the automount point is installed,
	   it is created. This string must be reflected in the unit filename. (See above.) This option is mandatory.

       ExtraOptions=
	   Extra mount options to use when creating the autofs mountpoint. This takes a comma-separated list of options. This setting is optional. Note that
	   the usual specifier expansion is applied to this setting, literal percent characters should hence be written as "%%".

	   Added in version 250.

       DirectoryMode=
	   Directories of automount points (and any parent directories) are automatically created if needed. This option specifies the file system access mode
	   used when creating these directories. Takes an access mode in octal notation. Defaults to 0755.

       TimeoutIdleSec=
	   Configures an idle timeout. Once the mount has been idle for the specified time, systemd will attempt to unmount. Takes a unit-less value in
	   seconds, or a time span value such as "5min 20s". Pass 0 to disable the timeout logic. The timeout is disabled by default.

	   Added in version 220.

       Check systemd.unit(5), systemd.exec(5), and systemd.kill(5) for more settings.

SEE ALSO
       systemd(1), systemctl(1), systemd.unit(5), systemd.mount(5), mount(8), automount(8), systemd.directives(7)

systemd 255																  SYSTEMD.AUTOMOUNT(5)
