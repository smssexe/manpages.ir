CRYPTSETUP-ERASE(8)						     Maintenance Commands						   CRYPTSETUP-ERASE(8)

NAME
       cryptsetup-erase, cryptsetup-luksErase - erase all keyslots

SYNOPSIS
       cryptsetup  erase [<options>] <device>
       cryptsetup luksErase [<options>] <device>

DESCRIPTION
       Erase all keyslots and make the LUKS container permanently inaccessible. Unless the device is configured with HW OPAL support you do not need to
       provide any password for this operation.

       WARNING: This operation is irreversible.

       WARNING: with --hw-opal-factory-reset ALL data is lost on the device, regardless of the partition it is ran on, if any, and regardless of any LUKS2
       header backup, and does not require a valid LUKS2 header to be present on the device to run.

       <options> can be [--header, --disable-locks, --hw-opal-factory-reset, --key-file].

OPTIONS
       --key-file, -d name (LUKS2 with HW OPAL only)
	   Read the Admin PIN or PSID (with --hw-opal-factory-reset) from file depending on options used.

	   If the name given is "-", then the secret will be read from stdin. In this case, reading will not stop at newline characters.

       --header <device or file storing the LUKS header>
	   Use to specify detached LUKS2 header when erasing HW OPAL enabled data device.

       --disable-locks
	   Disable lock protection for metadata on disk. This option is valid only for LUKS2 and ignored for other formats.

	   WARNING: Do not use this option unless you run cryptsetup in a restricted environment where locking is impossible to perform (where /run directory
	   cannot be used).

       --batch-mode, -q
	   Suppresses all confirmation questions. Use with care!

	   If the --verify-passphrase option is not specified, this option also switches off the passphrase verification.

       --debug or --debug-json
	   Run in debug mode with full diagnostic logs. Debug output lines are always prefixed by #.

	   If --debug-json is used, additional LUKS2 JSON data structures are printed.

       --version, -V
	   Show the program version.

       --usage
	   Show short option help.

       --help, -?
	   Show help text and default parameters.

REPORTING BUGS
       Report bugs at cryptsetup mailing list <cryptsetup@lists.linux.dev> or in Issues project section
       <https://gitlab.com/cryptsetup/cryptsetup/-/issues/new>.

       Please attach output of the failed command with --debug option added.

SEE ALSO
       Cryptsetup FAQ <https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions>

       cryptsetup(8), integritysetup(8) and veritysetup(8)

CRYPTSETUP
       Part of cryptsetup project <https://gitlab.com/cryptsetup/cryptsetup/>.

cryptsetup 2.7.0							  2024-11-14							   CRYPTSETUP-ERASE(8)
