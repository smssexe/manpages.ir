SYSTEMD-FIRSTBOOT(1)						       systemd-firstboot						  SYSTEMD-FIRSTBOOT(1)

NAME
       systemd-firstboot, systemd-firstboot.service - Initialize basic system settings on or before the first boot-up of a system

SYNOPSIS

       systemd-firstboot [OPTIONS...]

       systemd-firstboot.service

DESCRIPTION
       systemd-firstboot initializes basic system settings interactively during the first boot, or non-interactively on an offline system image. The service
       is started during boot if ConditionFirstBoot=yes is met, which essentially means that /etc/ is unpopulated, see systemd.unit(5) for details.

       The following settings may be configured:

       •   The machine ID of the system

       •   The system locale, more specifically the two locale variables LANG= and LC_MESSAGES

       •   The system keyboard map

       •   The system time zone

       •   The system hostname

       •   The kernel command line used when installing kernel images

       •   The root user's password and shell

       Each of the fields may either be queried interactively by users, set non-interactively on the tool's command line, or be copied from a host system that
       is used to set up the system image.

       If a setting is already initialized, it will not be overwritten and the user will not be prompted for the setting.

       Note that this tool operates directly on the file system and does not involve any running system services, unlike localectl(1), timedatectl(1) or
       hostnamectl(1). This allows systemd-firstboot to operate on mounted but not booted disk images and in early boot. It is not recommended to use
       systemd-firstboot on the running system after it has been set up.

OPTIONS
       The following options are understood:

       --root=root
	   Takes a directory path as an argument. All paths will be prefixed with the given alternate root path, including config search paths. This is useful
	   to operate on a system image mounted to the specified directory instead of the host system itself.

	   Added in version 216.

       --image=path
	   Takes a path to a disk image file or block device node. If specified all operations are applied to file system in the indicated disk image. This is
	   similar to --root= but operates on file systems stored in disk images or block devices. The disk image should either contain just a file system or
	   a set of file systems within a GPT partition table, following the Discoverable Partitions Specification[1]. For further information on supported
	   disk images, see systemd-nspawn(1)'s switch of the same name.

	   Added in version 246.

       --locale=LOCALE, --locale-messages=LOCALE
	   Sets the system locale, more specifically the LANG= and LC_MESSAGES settings. The argument should be a valid locale identifier, such as
	   "de_DE.UTF-8". This controls the locale.conf(5) configuration file.

	   Added in version 216.

       --keymap=KEYMAP
	   Sets the system keyboard layout. The argument should be a valid keyboard map, such as "de-latin1". This controls the "KEYMAP" entry in the
	   vconsole.conf(5) configuration file.

	   Added in version 236.

       --timezone=TIMEZONE
	   Sets the system time zone. The argument should be a valid time zone identifier, such as "Europe/Berlin". This controls the localtime(5) symlink.

	   Added in version 216.

       --hostname=HOSTNAME
	   Sets the system hostname. The argument should be a hostname, compatible with DNS. This controls the hostname(5) configuration file.

	   Added in version 216.

       --setup-machine-id
	   Initialize the system's machine ID to a random ID. This controls the machine-id(5) file.

	   This option only works in combination with --root= or --image=. On a running system, machine-id is written by the manager with help from systemd-
	   machine-id-commit.service(8).

	   Added in version 216.

       --machine-id=ID
	   Set the system's machine ID to the specified value. The same restrictions apply as to --setup-machine-id.

	   Added in version 216.

       --root-password=PASSWORD, --root-password-file=PATH, --root-password-hashed=HASHED_PASSWORD
	   Sets the password of the system's root user. This creates/modifies the passwd(5) and shadow(5) files. This setting exists in three forms:
	   --root-password= accepts the password to set directly on the command line, --root-password-file= reads it from a file and --root-password-hashed=
	   accepts an already hashed password on the command line. See shadow(5) for more information on the format of the hashed password. Note that it is
	   not recommended to specify plaintext passwords on the command line, as other users might be able to see them simply by invoking ps(1).

	   Added in version 216.

       --root-shell=SHELL
	   Sets the shell of the system's root user. This creates/modifies the passwd(5) file.

	   Added in version 246.

       --kernel-command-line=CMDLINE
	   Sets the system's kernel command line. This controls the /etc/kernel/cmdline file which is used by kernel-install(8).

	   Added in version 246.

       --prompt-locale, --prompt-keymap, --prompt-timezone, --prompt-hostname, --prompt-root-password, --prompt-root-shell
	   Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take
	   precedence, and the user is not prompted for it.

	   Added in version 216.

       --prompt
	   Query the user for locale, keymap, timezone, hostname, root's password, and root's shell. This is equivalent to specifying --prompt-locale,
	   --prompt-keymap, --prompt-timezone, --prompt-hostname, --prompt-root-password, --prompt-root-shell in combination.

	   Added in version 216.

       --copy-locale, --copy-keymap, --copy-timezone, --copy-root-password, --copy-root-shell
	   Copy a specific basic setting from the host. This only works in combination with --root= or --image=.

	   Added in version 216.

       --copy
	   Copy locale, keymap, time zone, root password and shell from the host. This is equivalent to specifying --copy-locale, --copy-keymap,
	   --copy-timezone, --copy-root-password, --copy-root-shell in combination.

	   Added in version 216.

       --force
	   Write configuration even if the relevant files already exist. Without this option, systemd-firstboot doesn't modify or replace existing files. Note
	   that when configuring the root account, even with this option, systemd-firstboot only modifies the entry of the "root" user, leaving other entries
	   in /etc/passwd and /etc/shadow intact.

	   Added in version 246.

       --reset
	   If specified, all existing files that are configured by systemd-firstboot are removed. Note that the files are removed regardless of whether
	   they'll be configured with a new value or not. This operation ensures that the next boot of the image will be considered a first boot, and
	   systemd-firstboot will prompt again to configure each of the removed files.

	   Added in version 254.

       --delete-root-password
	   Removes the password of the system's root user, enabling login as root without a password unless the root account is locked. Note that this is
	   extremely insecure and hence this option should not be used lightly.

	   Added in version 246.

       --welcome=
	   Takes a boolean argument. By default when prompting the user for configuration options a brief welcome text is shown before the first question is
	   asked. Pass false to this option to turn off the welcome text.

	   Added in version 246.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

CREDENTIALS
       systemd-firstboot supports the service credentials logic as implemented by ImportCredential=/LoadCredential=/SetCredential= (see systemd.exec(5) for
       details). The following credentials are used when passed in:

       passwd.hashed-password.root, passwd.plaintext-password.root
	   A hashed or plaintext version of the root password to use, in place of prompting the user. These credentials are equivalent to the same ones
	   defined for the systemd-sysusers.service(8) service.

	   Added in version 249.

       passwd.shell.root
	   Specifies the shell binary to use for the specified account. Equivalent to the credential of the same name defined for the systemd-
	   sysusers.service(8) service.

	   Added in version 249.

       firstboot.locale, firstboot.locale-messages
	   These credentials specify the locale settings to set during first boot, in place of prompting the user.

	   Added in version 249.

       firstboot.keymap
	   This credential specifies the keyboard setting to set during first boot, in place of prompting the user.

	   Note the relationship to the vconsole.keymap credential understood by systemd-vconsole-setup.service(8): both ultimately affect the same setting,
	   but firstboot.keymap is written into /etc/vconsole.conf on first boot (if not already configured), and then read from there by
	   systemd-vconsole-setup, while vconsole.keymap is read on every boot, and is not persisted to disk (but any configuration in vconsole.conf will take
	   precedence if present).

	   Added in version 249.

       firstboot.timezone
	   This credential specifies the system timezone setting to set during first boot, in place of prompting the user.

	   Added in version 249.

       Note that by default the systemd-firstboot.service unit file is set up to inherit the listed credentials from the service manager. Thus, when invoking
       a container with an unpopulated /etc/ for the first time it is possible to configure the root user's password to be "systemd" like this:

	   # systemd-nspawn --image=... --set-credential=firstboot.locale:de_DE.UTF-8 ...

       Note that these credentials are only read and applied during the first boot process. Once they are applied they remain applied for subsequent boots,
       and the credentials are not considered anymore.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise.

KERNEL COMMAND LINE
       systemd.firstboot=
	   Takes a boolean argument, defaults to on. If off, systemd-firstboot.service won't interactively query the user for basic settings at first boot,
	   even if those settings are not initialized yet.

	   Added in version 233.

SEE ALSO
       systemd(1), locale.conf(5), vconsole.conf(5), localtime(5), hostname(5), machine-id(5), shadow(5), systemd-machine-id-setup(1), localectl(1),
       timedatectl(1), hostnamectl(1)

NOTES
	1. Discoverable Partitions Specification
	   https://uapi-group.org/specifications/specs/discoverable_partitions_specification

systemd 255																  SYSTEMD-FIRSTBOOT(1)
