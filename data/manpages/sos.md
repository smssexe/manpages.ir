sos(1)								    General Commands Manual								sos(1)

NAME
       sos - A unified tool for collecting system logs and other debug information

SYNOPSIS
       sos component [options]

DESCRIPTION
       sos  is	a diagnostic data collection utility, used by system administrators, support representatives, and the like to assist in troubleshooting issues
       with a system or group of systems.

       The most well known function is	sos report or sos report as it was previously known.

       An sos archive is typically requested by support organizations to collect baseline configuration and system data from which to begin the	 troubleshoot‐
       ing process.

COMPONENTS
       sos supports several subcommands or components. Each provides a different set of information for the user. Supported components are as follows

       report Report  generates an archive of system information including configuration files and command output. Information included in the report is based
	      upon plugins that are activated automatically when certain criteria, such as installed packages, files, services, or system architecture is  de‐
	      tected.

	      See sos report --help and man sos-report for more information.

	      May also be invoked via the alias rep or the deprecated command sos report.

       collect
	      Collect  is  used	 to  capture  reports  on multiple systems simultaneously. These systems can either be defined by the user at the command line
	      and/or defined by clustering software that exists either on the local system or on a "primary" system that is able to inform about  other	 nodes
	      in the cluster.

	      When  running  collect, sos report will be run on the remote nodes, and then the resulting archives will be copied from those nodes to the local
	      system running sos collect. Archives are then removed from the remote systems.

	      See sos collect --help and man sos-collect for more information.

	      May also be invoked via the alias sos collector or the deprecated command sos-collector.

       clean|cleaner|mask
	      This subcommand takes input of either 1) an sos report tarball, 2) a collection of sos report tarballs such as from collect, or 3)  the  unpack‐
	      aged  directory  of  an sos report and obfuscates potentially sensitive system information that is not covered by the standard postprocessing of
	      sos report.

	      Such data includes IP addresses, networks, MAC addresses, and more. Data obfuscated by this command will remain consistent throughout the report
	      and across reports provided in the same invocation. Additionally, care is taken to maintain network topology relationships between matched  data
	      items.

	      See  sos clean --help and man sos-clean for more information.

	      May be invoked via either sos clean, sos cleaner, sos mask, or via the --clean, --cleaner or  --mask options for report and collect.

       help   This  subcommand	is  used to retrieve more detailed information on the various SoS commands and components than is directly available in either
	      other manpages or --help output.

	      See  sos help --help and	man sos-help for more information.

GLOBAL OPTIONS
       sos components provide their own set of options, however the following are available to be set across all components.

       --batch Do not prompt interactively, user will not be prompted for any data

       --encrypt
	      Encrypt the resulting archive, and determine the method by which that encryption is done by either a user prompt or environment variables.

	      When run with --batch, using this option will cause sos to look for either the SOSENCRYPTKEY or SOSENCRYPTPASS environment  variables.  If  set,
	      this  will  implicitly enable the --encrypt-key or --encrypt-pass options, respectively, to the values set by the environment variable. This en‐
	      ables the use of these options without directly setting those options in a config file or command line string. Note that use  of	an  encryption
	      key has precedence over a passphrase.

	      Otherwise,  using	 this option will cause sos to prompt the user to choose the method of encryption to use. Choices will be [P]assphrase, [K]ey,
	      [E]nv vars, or [N]o encryption.  If passphrase or key the user will then be prompted for the respective value, env vars will cause sos to source
	      the information in the manner stated above, and choosing no encryption will disable encryption.

	      See the sections on --encrypt-key and --encrypt-pass below for more information.

       --encrypt-key KEY
	      Encrypts the resulting archive that sos report produces using GPG. KEY must be an existing key in the user's keyring as GPG does not  allow  for
	      keyfiles.	 KEY can be any value accepted by gpg's 'recipient' option.

	      Note  that the user running sos report must match the user owning the keyring from which keys will be obtained. In particular this means that if
	      sudo is used to run sos report, the keyring must also be set up using sudo (or direct shell access to the account).

	      Users should be aware that encrypting the final archive will result in sos using double the amount of  temporary	disk  space  -	the  encrypted
	      archive  must  be	 written as a separate, rather than replacement, file within the temp directory that sos writes the archive to. However, since
	      the encrypted archive will be the same size as the original archive, there is no additional space consumption once the  temporary	 directory  is
	      removed at the end of execution.

	      This means that only the encrypted archive is present on disk after sos finishes running.

	      If encryption fails for any reason, the original unencrypted archive is preserved instead.

       --encrypt-pass PASS
	      The same as --encrypt-key, but use the provided PASS for symmetric encryption rather than key-pair encryption.

       --config-file CONFIG
	      Specify alternate configuration file.

       -s, --sysroot SYSROOT
	      Specify an alternate root file system path.

       --tmp-dir DIRECTORY
	      Specify alternate temporary directory to copy data during execution.

       --threads THREADS
	      Specify the number of threads sos report will use for concurrency. Defaults to 4.

       -v, --verbose
	      Increase logging verbosity. May be specified multiple times to enable additional debugging messages.

	      The following table summarizes the effects of different verbosity levels:

		  1 (-v)   :  Enable debug messages for sos.log. Show individual plugins starting.
		  2 (-vv)  :  Also print debug messages to console.
		  3 (-vvv) :  Enable debug messages for archive file operations. Note this will dramatically
			      increase the amount of logging.

       -q, --quiet
	      Only log fatal errors to stderr.

       -z, --compression-type {auto|xz|gzip}
	      Compression type to use when compression the final archive output

       --help Display usage message.

SEE ALSO
       sos.conf(5)

MAINTAINER
       Maintained on GitHub at https://github.com/sos report/sos

AUTHORS & CONTRIBUTORS
       See AUTHORS file in the package documentation.

									  April 2020									sos(1)
