SOS_REPORT(1)							    General Commands Manual							 SOS_REPORT(1)

NAME
       sos_report - Collect and package diagnostic and support data

SYNOPSIS
       sos report
		 [-l|--list-plugins]
		 [-n|--skip-plugins plugin-names]
		 [-e|--enable-plugins plugin-names]
		 [-o|--only-plugins plugin-names]
		 [-a|--alloptions] [-v|--verbose]
		 [-k plug.opt|--plugin-option plug.opt]|--plugopts plug.opt
		 [--no-report] [--config-file conf]
		 [--no-postproc]
		 [--preset preset] [--add-preset add_preset]
		 [--del-preset del_preset] [--desc description]
		 [--batch] [--build] [--debug] [--dry-run]
		 [--estimate-only] [--label label] [--case-id id]
		 [--threads threads]
		 [--plugin-timeout TIMEOUT]
		 [--cmd-timeout TIMEOUT]
		 [--namespaces NAMESPACES]
		 [--container-runtime RUNTIME]
		 [-s|--sysroot SYSROOT]
		 [-c|--chroot {auto|always|never}
		 [--tmp-dir directory]
		 [-p|--profile profile-name]
		 [--list-profiles]
		 [--verify]
		 [--log-size]
		 [--journal-size]
		 [--all-logs]
		 [--since YYYYMMDD[HHMMSS]]
		 [--skip-commands commands]
		 [--skip-files files]
		 [--allow-system-changes]
		 [--low-priority]
		 [-z|--compression-type method]
		 [--encrypt]
		 [--encrypt-key KEY]
		 [--encrypt-pass PASS]
		 [--upload] [--upload-url url] [--upload-user user]
		 [--upload-directory dir] [--upload-pass pass]
		 [--upload-no-ssl-verify] [--upload-method]
		 [--upload-protocol protocol]
		 [--experimental]
		 [-h|--help]

DESCRIPTION
       report  is  an sos subcommand that generates an archive of configuration and diagnostic information from the running system.  The archive may be stored
       locally or centrally for recording or tracking purposes or may be sent to technical support representatives, developers or system administrators to as‐
       sist with technical fault-finding and debugging.

       Sos is modular in design and is able to collect data from a wide range of subsystems and packages that may be installed. An HTML report summarizing the
       collected information is optionally generated and stored within the archive.

       Note: the sosreport command has been deprecated and will be removed in sos-4.9. Use the new sos report syntax instead.

OPTIONS
       -l, --list-plugins
	      List all available plugins and their options. Plug-ins that would not be enabled by the current configuration are listed separately.

       -n, --skip-plugins PLUGNAME[,PLUGNAME]
	      Disable the specified plugin(s). Multiple plug-ins may be specified by repeating the option or as a comma-separated list.

       -e, --enable-plugins PLUGNAME[,PLUGNAME]
	      Enable the specified plugin(s) that would otherwise be disabled. Multiple plugins may be specified by repeating the option or as	a  comma-sepa‐
	      rated list.

	      Note  that  if  using -p, --profile this option will not enable further plugins. Use -o, --only-plugins to extend the list of plugins enabled by
	      profiles.

       -o, --only-plugins PLUGNAME[,PLUGNAME]
	      Enable the specified plugin(s) only (all other plugins should be disabled). Multiple plugins may be specified by repeating the option  or	 as  a
	      comma-separated list.

       -k PLUGNAME.PLUGOPT[=VALUE], --plugin-option=PLUGNAME.PLUGOPT[=VALUE], --plugopts=PLUGNAME.PLUGOPT[=VALUE]
	      Specify plug-in options. The option PLUGOPT is enabled, or set to the specified value in the plug-in PLUGNAME.

       -a, --alloptions
	      Set all boolean options to True for all enabled plug-ins.

       -v, --verbose
	      Increase logging verbosity. May be specified multiple times to enable additional debugging messages.

       -q, --quiet
	      Only log fatal errors to stderr.

       --no-report
	      Disable HTML report writing.

       --config-file CONFIG
	      Specify alternate configuration file.

       --no-postproc
	      Disable postprocessing globally for all plugins. This will mean data is not obfuscated/sanitized from the archive during collection.

	      Note that this means data such as password, SSH keys, certificates, etc...  will be collected in plain text.

	      To  selectively  disable	postprocessing on a per-plugin basis, use the 'postproc' plugin option available to all plugins, e.g. '-k podman.post‐
	      proc=off'.

       --preset PRESET
	      Specify an existing preset to use for sos options.

	      Presets are pre-configured sets of options for both sos and sos plugins. For example a preset may enable a certain set of plugins, disable  oth‐
	      ers, or enable specific plugin options. They may also specify sos options such as log-size or package verification.

	      User defined presets are saved under /etc/sos/presets.d as JSON-formatted files.

       --add-preset ADD_PRESET [options]
	      Add a preset with name ADD_PRESET that enables [options] when called.

	      For  example,  'sos  report  --add-preset mypreset --log-size=50 -n logs' will enable a user to run 'sos report --preset mypreset' that sets the
	      maximum log size to 50 and disables the logs plugin.

	      Note: to set a description for the preset that is displayed with --list-presets, use the --desc option.

	      Note: to set a behaviour note of the preset, use --note option.

	      Note: The root filesystem, as seen by sos if running within a container, must be writable to save presets using this option.

       --del-preset DEL_PRESET
	      Deletes the preset with name DEL_PRESET from the filesystem so that it can no longer be used.

       --list-presets
	      Display a list of available presets and what options they carry.

       --desc DESCRIPTION
	      When using --add-preset use this option to add a description of the preset that will be displayed when using --list-presets.

       -s, --sysroot SYSROOT
	      Specify an alternate root file system path. Useful for collecting reports from containers and images.

       -c, --chroot {auto|always|never}
	      Set the chroot mode. When --sysroot is used commands default to executing with SYSROOT as the root directory (unless disabled by a specific plu‐
	      gin). This can be overridden by setting --chroot to "always" (always chroot) or "never" (always run in the host namespace).

       --tmp-dir DIRECTORY
	      Specify alternate temporary directory to copy data as well as the compressed report.

       --list-profiles
	      Display a list of available profiles and the plugins that they enable.

       -p, --profile, --profiles NAME
	      Only run plugins that correspond to the given profile. Multiple profiles may be specified as a comma-separated list; the set of plugins executed
	      is the union of each of the profile's plugin sets.

	      Note that if there are specific plugins outside of the profile(s) passed to this option that you would also want to enable, use -o, --only-plug‐
	      ins to add those plugins to the list.

	      See sos report --list-profiles for a list of currently supported profiles.

       --verify
	      Instructs plugins to perform plugin-specific verification during data collection. This may include package manager verification,	log  integrity
	      testing or other plugin defined behaviour. Use of --verify may cause the time taken to generate a report to be considerably longer.

       --log-size
	      Places  a	 limit	on the size of collected logs and output in MiB. Note that this causes sos to capture the last X amount of the file or command
	      output collected.

	      By default, this is set to 25 MiB and applies to all files and command output collected with the exception of  journal  collections,  which  are
	      limited by the --journal-size option instead.

	      Setting this value to 0 removes all size limitations, and any files or commands collected will be collected in their entirety, which may drasti‐
	      cally increase the size of the final sos report tarball and the memory usage of sos during collection of commands.

       --journal-size
	      Places a limit on the size of journals collected in MiB. Note that this causes sos to capture the last X amount of the journal.

	      By  default,  this  is  set to 100 MiB. Setting this value to 0 removes all size limitations, as does the use of the --all-logs option. This may
	      drastically increase the size of the final sos report tarball.

       --all-logs
	      Tell plugins to collect all possible log data ignoring any size limits and including logs in non-default locations.  This	 option	 may  signifi‐
	      cantly increase the size of reports.

       --since YYYYMMDD[HHMMSS]
	      Limits the collection of log archives to those newer than this date. A log archive is any file not found in /etc, that has either a numeric or a
	      compression-type	file extension for example ".zip". ".1", ".gz" etc.).  This also affects --all-logs. The date string will be padded with zeros
	      if HHMMSS is not specified.

       --skip-commands COMMANDS
	      A comma delimited list of commands to skip execution of, but still allowing the rest of the plugin that calls the command to run. This will gen‐
	      erally need to be some form of UNIX shell-style wildcard matching. For example, using a value of hostname will skip only	that  single  command,
	      while using hostname* will skip all commands with names that begin with the string "hostname".

       --skip-files FILES
	      A	 comma	delimited  list	 of files or filepath wildcard matches to skip collection of. Values may either be exact filepaths or paths using UNIX
	      shell-style wildcards, for example /etc/sos/*.

       --allow-system-changes
	      Run commands even if they can change the system (e.g. load kernel modules).

       --low-priority
	      Set sos to execute as a low priority process so that is does not interfere with other processes running on the  system.  Specific	 distributions
	      may  set their own constraints, but by default this involves setting process niceness to 19 and, if available, setting an idle IO class via ion‐
	      ice.  -z, --compression-type METHOD Override the default compression type specified by the active policy.

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

       --batch
	      Generate archive without prompting for interactive input.

       --name NAME
	      Deprecated. See --label

       --label LABEL
	      Specify  an  arbitrary  identifier to associate with the archive.	 Labels will be appended after the system's short hostname and may contain al‐
	      phanumeric characters.

       --threads THREADS
	      Specify the number of threads sos report will use for concurrency. Defaults to 4.

       --plugin-timeout TIMEOUT
	      Specify a timeout in seconds to allow each plugin to run for. A value of 0 means no timeout will be set. A value of -1 is used to	 indicate  the
	      default timeout of 300 seconds.

	      Note  that  this	option	sets  the timeout for all plugins. If you want to set a timeout for a specific plugin, use the 'timeout' plugin option
	      available to all plugins - e.g. '-k logs.timeout=600'.

	      The plugin-specific timeout option will override this option. For example, using '--plugin-timeout=60 -k logs.timeout=600' will set a timeout of
	      600 seconds for the logs plugin and 60 seconds for all other enabled plugins.

       --cmd-timeout TIMEOUT
	      Specify a timeout limit in seconds for a command execution. Same defaults logic from --plugin-timeout applies here.

	      This option sets the command timeout for all plugins. If you want to set a cmd timeout for a specific plugin, use the 'cmd-timeout'  plugin  op‐
	      tion available to all plugins - e.g. '-k logs.cmd-timeout=600'.

	      Again, the same plugin/global precedence logic as for --plugin-timeout applies here.

	      Note  that  setting  --cmd-timeout (or -k logs.cmd-timeout) high should be followed by increasing the --plugin-timeout equivalent, otherwise the
	      plugin can easily timeout on slow commands execution.

       --namespaces NAMESPACES
	      For plugins that iterate collections over namespaces that exist on the system, for example the networking plugin collecting `ip` command	output
	      for each network namespace, use this option to limit the number of namespaces that will be collected.

	      Use '0' (default) for no limit - all namespaces will be used for collections.

	      Note that specific plugins may provide a similar `namespaces` plugin option. If the plugin option is used, it will override this option.

       --container-runtime RUNTIME
	      Force  the use of the specified RUNTIME as the default runtime that plugins will use to collect data from and about containers and container im‐
	      ages. By default, the setting of auto results in the local policy determining what runtime will be the default runtime (in configurations	 where
	      multiple runtimes are installed and active).

	      If  no  container	 runtimes are active, this option is ignored. If there are runtimes active, but not one with a name matching RUNTIME, sos will
	      abort.

	      Setting this to none, off, or disabled will cause plugins to NOT leverage any active runtimes for collections. Note that	if  disabled,  plugins
	      specifically  for	 runtimes (e.g. the podman or docker plugins) will still collect general data about the runtime, but will not inspect existing
	      containers or images.

	      Default: 'auto' (policy determined)

       --case-id NUMBER
	      Specify a case identifier to associate with the archive.	Identifiers may include alphanumeric characters, commas and periods ('.').

       --build
	      Do not archive copied data. Causes sos report to leave an uncompressed archive as a temporary file or directory tree.

       --debug
	      Enable interactive debugging using the python debugger. Exceptions in sos or plug-in code will cause a trap to the pdb shell.

       --dry-run
	      Execute plugins as normal, but do not collect any file content, command output, or string data from the system. The resulting logs may  be  used
	      to understand the actions that sos would have taken without the dry run option.

       --estimate-only
	      Estimate disk space requirements when running sos report. This can be valuable to prevent sos report working dir to consume all free disk space.
	      No plugin data is available at the end.

	      Plugins will be collected sequentially, size of collected files and commands outputs will be calculated and the plugin files will be immediately
	      deleted prior execution of the next plugin. This still can consume whole free disk space, though.

	      Please note, size estimations may not be accurate for highly utilized systems due to changes between an estimate and a real execution. Also some
	      difference between estimation (using `stat` command) and other commands used (i.e. `du`).

	      A rule of thumb is to reserve at least double the estimation.

       --upload
	      If specified, attempt to upload the resulting archive to a vendor defined location.

	      This option is implied if --upload-url is used.

	      You  may be prompted for a username and password if these are not defined by the vendor as well. If these credentials are not provided, sos will
	      still run and create an archive but will not attempt an automatic upload, instead relying on the end user to upload it as needed.

	      The sos report archive will still remain on the local filesystem even after a successful upload.

	      Note that depending on the distribution sos is being run on, or the vendor policy detected during execution, there may be dependencies that  are
	      not strictly required by the package at installation time.

	      For  example,  for  HTTPS uploads the python-requests library must be available. If this library is not available, HTTPS uploads will not be at‐
	      tempted.

       --upload-url URL
	      If a vendor does not provide a default upload location, or if you would like to upload the archive to a different location, specify the  address
	      here.

	      A support protocol MUST be specified in this URL. Currently uploading is supported for HTTPS, SFTP, and FTP protocols.

	      If your destination server listens on a non-standard port, specify the listening port in the URL.

       --upload-user USER
	      If a vendor does not provide a default user for uploading, specify the username here.

	      If  this	option is unused and upload is request, and a vendor default is not set, you will be prompted for one. If --batch is used and this op‐
	      tion is omitted, no username will be collected and thus uploads will fail if no vendor default is set.

	      You also have the option of providing this value via the SOSUPLOADUSER environment variable. If this variable is set, then  no  username	prompt
	      will occur and --batch may be used provided all other required values (case number, upload password) are provided.

	      This option is ignored when uploading to the Red Customer Portal or Red Hat Secure FTP server in favour of web token authentication.

       --upload-pass PASS
	      Specify the password to use for authentication with the destination server.

	      If this option is omitted and upload is requested, you will be prompted for one.

	      If --batch is used, this prompt will not occur, so any uploads are likely to fail unless this option is used.

	      Note  that  this	may  result in the plaintext string appearing in `ps` output that may be collected by sos and be in the archive. If a password
	      must be provided by you for uploading, it is strongly recommended to not use --batch and enter the password when prompted rather than using this
	      option.

	      You also have the option of providing this value via the SOSUPLOADPASSWORD environment variable. If this	variable  is  set,  then  no  password
	      prompt will occur and --batch may be used provided all other required values (case number, upload user) are provided.

	      This option is ignored when uploading to the Red Customer Portal or Red Hat Secure FTP server in favour of web token authentication.

       --upload-directory DIR
	      Specify  a  directory  to upload to, if one is not specified by a vendor default location or if your destination server does not allow writes to
	      '/'.

       --upload-method METHOD
	      Specify the HTTP method to use for uploading to the provided --upload-url. Valid values are 'auto' (default),  'put',  or	 'post'.  The  use  of
	      'auto' will default to the method required by the policy-default upload location, if one exists.

	      This option has no effect on upload protocols other than HTTPS.

       --upload-no-ssl-verify
	      Disable SSL verification for HTTPS uploads. This may be used to allow uploading to locations that have self-signed certificates, or certificates
	      that are otherwise untrusted by the local system.

	      Default behavior is to perform SSL verification against all upload locations.

       --upload-protocol PROTO
	      Manually specify the protocol to use for uploading to the target upload-url.

	      Normally	this  is determined via the upload address, assuming that the protocol is part of the address provided, e.g. 'https://example.com'. By
	      using this option, sos will skip the protocol check and use the method defined for the specified PROTO.

	      For RHEL systems, setting this option to sftp will skip the initial attempt to upload to the Red Hat Customer Portal, and only attempt an upload
	      to Red Hat's SFTP server, which is typically used as a fallback target.

	      Valid values for PROTO are: 'auto' (default), 'https', 'ftp', 'sftp'.

       --experimental
	      Enable plugins marked as experimental. Experimental plugins may not have been tested for this port or may still be under active development.

       --help Display usage message.

SEE ALSO
       sos(1) sos-clean(1) sos-collect(1) sos.conf(5)

MAINTAINER
       Maintained on GitHub at https://github.com/sosreport/sos

AUTHORS & CONTRIBUTORS
       See AUTHORS file in the package documentation.

									Mon Mar 25 2013								 SOS_REPORT(1)
