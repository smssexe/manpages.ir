SYSTEMD-PCRLOCK(8)							systemd-pcrlock							    SYSTEMD-PCRLOCK(8)

NAME
       systemd-pcrlock, systemd-pcrlock-file-system.service, systemd-pcrlock-firmware-code.service, systemd-pcrlock-firmware-config.service, systemd-pcrlock-
       machine-id.service, systemd-pcrlock-make-policy.service, systemd-pcrlock-secureboot-authority.service, systemd-pcrlock-secureboot-policy.service -
       Analyze and predict TPM2 PCR states and generate an access policy from the prediction

SYNOPSIS

       /usr/lib/systemd/systemd-pcrlock [OPTIONS...]

DESCRIPTION
       Note: this command is experimental for now. While it is likely to become a regular component of systemd, it might still change in behaviour and
       interface.

       systemd-pcrlock is a tool that may be used to analyze and predict TPM2 PCR measurements, and generate TPM2 access policies from the prediction which it
       stores in a TPM2 NV index (i.e. in the TPM2 non-volatile memory). This may then be used to restrict access to TPM2 objects (such as disk encryption
       keys) to system boot-ups in which only specific, trusted components are used.

       systemd-pcrlock uses as input for its analysis and prediction:

       •   The UEFI firmware TPM2 event log (i.e.  /sys/kernel/security/tpm0/binary_bios_measurements) of the current boot.

       •   The userspace TPM2 event log (i.e.  /run/log/systemd/tpm2-measure.log) of the current boot.

       •   The current PCR state of the TPM2 chip.

       •   Boot component definition files (*.pcrlock and *.pcrlock.d/*.pcrlock, see systemd.pcrlock(5)) that each define expected measurements for one
	   component of the boot process, permitting alternative variants for each. (Variants may be used used to bless multiple kernel versions or boot
	   loader versions at the same time.)

       It uses these inputs to generate a combined event log, validating it against the PCR states. It then attempts to recognize event log records and
       matches them against the defined components. For each PCR where this can be done comprehensively (i.e. where all listed records and all defined
       components have been matched) this may then be used to predict future PCR measurements, taking the alternative variants defined for each component into
       account. This prediction may then be converted into a TPM2 access policy (consisting of TPM2 PolicyPCR and PolicyOR items), which is then stored in an
       NV index in the TPM2. This may be used to then lock secrets (such as disk encryption keys) to these policies (via a TPM2 PolicyAuthorizeNV policy).

       Use tools such as systemd-cryptenroll(1) or systemd-repart(8) to bind disk encryption to such a systemd-pcrlock TPM2 policy. Specifically, see the
       --tpm2-pcrlock= switches of these tools.

       The access policy logic requires a TPM2 device that implements the "PolicyAuthorizeNV" command, i.e. implements TPM 2.0 version 1.38 or newer.

COMMANDS
       The following commands are understood:

       log
	   This reads the combined TPM2 event log, validates it, matches it against the current PCR values, and outputs both in tabular form. Combine with
	   --json= to generate output in JSON format.

	   Added in version 255.

       cel
	   This reads the combined TPM2 event log and writes it to STDOUT in TCG Common Event Log Format (CEL-JSON)[1] format.

	   Added in version 255.

       list-components
	   Shows a list of component definitions and their variants, i.e. the *.pcrlock files discovered in /var/lib/pcrlock.d/, /usr/lib/pcrlock.d/, and the
	   other supported directories. See systemd.pcrlock(5) for details on these files and the full list of directories searched.

	   Added in version 255.

       predict
	   Predicts the PCR state on future boots. This will analyze the TPM2 event log as described above, recognize components, and then generate all
	   possible resulting PCR values for all combinations of component variants. Note that no prediction is made for PCRs whose value does not match the
	   event log records, for which unrecognized measurements are discovered or for which components are defined that cannot be found in the event log.
	   This is a safety measure to ensure that any generated access policy can be fulfilled correctly on current and future boots.

	   Added in version 255.

       make-policy
	   This predicts the PCR state for future boots, much like the predict command above. It then uses this data to generate a TPM2 access policy which it
	   stores in a TPM2 NV index. The prediction and information about the used TPM2 and its NV index are written to /var/lib/systemd/pcrlock.json.

	   The NV index is allocated on first invocation, and updated on subsequent invocations.

	   The NV index contents may be changed (and thus the policy stored in it updated) by providing an access PIN. This PIN is normally generated
	   automatically and stored in encrypted form (with an access policy binding it to the NV index itself) in the aforementioned JSON policy file. This
	   PIN may be chosen by the user, via the --recovery-pin= switch. If specified it may be used as alternative path of access to update the policy.

	   If the new prediction matches the old this command terminates quickly and executes no further operation. (Unless --force is specified, see below.)

	   Added in version 255.

       remove-policy
	   Removes a previously generated policy. Deletes the /var/lib/systemd/pcrlock.json file, and deallocates the NV index.

	   Added in version 255.

       lock-firmware-code, unlock-firmware-code
	   Generates/removes .pcrlock files based on the TPM2 event log of the current boot covering all records for PCRs 0 ("platform-code") and 2
	   ("external-code").

	   This operation allows locking the boot process to the current version of the firmware of the system and its extension cards. This operation should
	   only be used if the system vendor does not provide suitable pcrlock data ahead of time.

	   Note that this data only matches the current version of the firmware. If a firmware update is applied this data will be out-of-date and any access
	   policy generated from it will no longer pass. It is thus recommended to invoke unlock-firmware-code before doing a firmware update, followed by
	   make-policy to refresh the policy.

	   systemd-pcrlock lock-firmware-code is invoked automatically at boot via the systemd-pcrlock-firmware-code.service unit, if enabled. This ensures
	   that an access policy managed by systemd-pcrlock is automatically locked to the new firmware version whenever the policy has been relaxed
	   temporarily, in order to cover for firmware updates, as described above.

	   The files are only generated from the event log if the event log matches the current TPM2 PCR state.

	   This writes/removes the files /var/lib/pcrlock.d/250-firmware-code-early.pcrlock.d/generated.pcrlock and
	   /var/lib/pcrlock.d/550-firmware-code-late.pcrlock.d/generated.pcrlock.

	   Added in version 255.

       lock-firmware-config, unlock-firmware-config
	   This is similar to lock-firmware-code/unlock-firmware-code but locks down the firmware configuration, i.e. PCRs 1 ("platform-config") and 3
	   ("external-config").

	   This functionality should be used with care as in most scenarios a minor firmware configuration change should not invalidate access policies to
	   TPM2 objects. Also note that some systems measure unstable and unpredictable information (e.g. current CPU voltages, temperatures, as part of
	   SMBIOS data) to these PCRs, which means this form of lockdown cannot be used reliably on such systems. Use this functionality only if the system
	   and hardware is well known and does not suffer by these limitations, for example in virtualized environments.

	   Use unlock-firmware-config before making firmware configuration changes. If the systemd-pcrlock-firmware-config.service unit is enabled it will
	   automatically generate a pcrlock file from the new measurements.

	   This writes/removes the files /var/lib/pcrlock.d/250-firmware-config-early.pcrlock.d/generated.pcrlock and
	   /var/lib/pcrlock.d/550-firmware-config-late.pcrlock.d/generated.pcrlock.

	   Added in version 255.

       lock-secureboot-policy, unlock-secureboot-policy
	   Generates/removes a .pcrlock file based on the SecureBoot policy currently enforced. This looks at the SecureBoot, PK, KEK, db, dbx, dbt, dbr EFI
	   variables and predicts their measurements to PCR 7 ("secure-boot-policy") on the next boot.

	   Use unlock-firmware-config before applying SecureBoot policy updates. If the systemd-pcrlock-secureboot-policy.service unit is enabled it will
	   automatically generate a pcrlock file from the policy discovered.

	   This writes/removes the file /var/lib/pcrlock.d/230-secureboot-policy.pcrlock.d/generated.pcrlock.

	   Added in version 255.

       lock-secureboot-authority, unlock-secureboot-authority
	   Generates/removes a .pcrlock file based on the SecureBoot authorities used to validate the boot path. SecureBoot authorities are the specific
	   SecureBoot database entries that where used to validate the UEFI PE binaries executed at boot. This looks at the event log of the current boot, and
	   uses relevant measurements on PCR 7 ("secure-boot-policy").

	   This writes/removes the file /var/lib/pcrlock.d/620-secureboot-authority.pcrlock.d/generated.pcrlock.

	   Added in version 255.

       lock-gpt [DEVICE], unlock-gpt
	   Generates/removes a .pcrlock file based on the GPT partition table of the specified disk. If no disk is specified automatically determines the
	   block device backing the root file system. This locks the state of the disk partitioning of the booted medium, which firmware measures to PCR 5
	   ("boot-loader-config").

	   This writes/removes the file /var/lib/pcrlock.d/600-gpt.pcrlock.d/generated.pcrlock.

	   Added in version 255.

       lock-pe [BINARY], unlock-pe
	   Generates/removes a .pcrlock file based on the specified PE binary. This is useful for predicting measurements the firmware makes to PCR 4
	   ("boot-loader-code") if the specified binary is part of the UEFI boot process. Use this on boot loader binaries and suchlike. Use lock-uki (see
	   below) for PE binaries that are unified kernel images (UKIs).

	   Expects a path to the PE binary as argument. If not specified, reads the binary from STDIN instead.

	   The pcrlock file to write must be specified via the --pcrlock= switch.

	   Added in version 255.

       lock-uki [UKI], unlock-uki
	   Generates/removes a .pcrlock file based on the specified UKI PE binary. This is useful for predicting measurements the firmware makes to PCR 4
	   ("boot-loader-code"), and systemd-stub(7) makes to PCR 11 ("kernel-boot"), if the specified UKI is booted. This is a superset of lock-pe.

	   Expects a path to the UKI PE binary as argument. If not specified, reads the binary from STDIN instead.

	   The pcrlock file to write must be specified via the --pcrlock= switch.

	   Added in version 255.

       lock-machine-id, unlock-machine-id
	   Generates/removes a .pcrlock file based on /etc/machine-id. This is useful for predicting measurements systemd-pcrmachine.service(8) makes to PCR
	   15 ("system-identity").

	   This writes/removes the file /var/lib/pcrlock.d/820-machine-id.pcrlock.

	   Added in version 255.

       lock-file-system [PATH], unlock-file-system [PATH]
	   Generates/removes a .pcrlock file based on file system identity. This is useful for predicting measurements systemd-pcrfs@.service(8) makes to PCR
	   15 ("system-identity") for the root and /var/ file systems.

	   This writes/removes the files /var/lib/pcrlock.d/830-root-file-system.pcrlock and /var/lib/pcrlock.d/840-file-system-path.pcrlock.

	   Added in version 255.

       lock-kernel-cmdline [FILE], unlock-kernel-cmdline
	   Generates/removes a .pcrlock file based on /proc/cmdline (or the specified file if given). This is useful for predicting measurements the Linux
	   kernel makes to PCR 9 ("kernel-initrd").

	   This writes/removes the file /var/lib/pcrlock.d/710-kernel-cmdline.pcrlock/generated.pcrlock.

	   Added in version 255.

       lock-kernel-initrd FILE, unlock-kernel-initrd
	   Generates/removes a .pcrlock file based on a kernel initrd cpio archive. This is useful for predicting measurements the Linux kernel makes to PCR 9
	   ("kernel-initrd"). Do not use for systemd-stub UKIs, as the initrd is combined dynamically from various sources and hence does not take a single
	   input, like this command.

	   This writes/removes the file /var/lib/pcrlock.d/720-kernel-initrd.pcrlock/generated.pcrlock.

	   Added in version 255.

       lock-raw [FILE], unlock-raw
	   Generates/removes a .pcrlock file based on raw binary data. The data is either read from the specified file or from STDIN (if none is specified).
	   This requires that --pcrs= is specified. The generated pcrlock file is written to the file specified via --pcrlock= or to STDOUT (if none is
	   specified).

	   Added in version 255.

OPTIONS
       The following options are understood:

       --raw-description
	   When displaying the TPM2 event log do not attempt to decode the records to provide a friendly event log description string. Instead, show the
	   binary payload data in escaped form.

	   Added in version 255.

       --pcr=
	   Specifies the PCR number to use. May be specified more than once to select multiple PCRs.

	   This is used by lock-raw and lock-pe to select the PCR to lock against.

	   If used with predict and make-policy this will override which PCRs to include in the prediction and policy. If unspecified this defaults to PCRs
	   0-5, 7, 11-15. Note that these commands will not include any PCRs in the prediction/policy (even if specified explicitly) if there are measurements
	   in the event log that do not match the current PCR value, or there are unrecognized measurements in the event log, or components define
	   measurements not seen in the event log.

	   Added in version 255.

       --nv-index=
	   Specifies to NV index to store the policy in. Honoured by make-policy. If not specified the command will automatically pick a free NV index.

	   Added in version 255.

       --components=
	   Takes a path to read *.pcrlock and *.pcrlock.d/*.pcrlock files from. May be used more than once to specify multiple such directories. If not
	   specified defaults to /etc/pcrlock.d/, /run/pcrlock.d/, /var/lib/pcrlock.d/, /usr/local/pcrlock.d/, /usr/lib/pcrlock.d/.

	   Added in version 255.

       --location=
	   Takes either a string or a colon-separated pair of strings. Configures up to which point in the sorted list of defined components to
	   analyze/predict PCRs to. Typically, the systemd-pcrlock tool is invoked from a fully booted system after boot-up and before shutdown. This means
	   various components that are defined for shutdown have not been measured yet, and should not be searched for. This option allows one to restrict
	   which components are considered for analysis (taking only components before some point into account, ignoring components after them). The expected
	   string is ordered against the filenames of the components defined. Any components with a lexicographically later name are ignored. This logic
	   applies to the log, predict, and make-policy verbs. If a colon-separated pair of strings are specified then they select which phases of the boot to
	   include in the prediction/policy. The first string defines where the first prediction shall be made, and the second string defines where the last
	   prediction shall be made. All such predictions are then combined into one set.

	   If used with list-components the selected location range will be highlighted in the component list.

	   Defaults to "760-:940-", which means the policies generated by default will basically cover the whole runtime of the OS userspace, from the initrd
	   (as "760-" closely follows 750-enter-initrd.pcrlock) until (and including) the main runtime of the system (as "940-" is closely followed by
	   950-shutdown.pcrlock). See systemd.pcrlock(5) for a full list of well-known components, that illustrate where this range is placed by default.

	   Added in version 255.

       --recovery-pin=
	   Takes a boolean. Defaults to false. Honoured by make-policy. If true, will query the user for a PIN to unlock the TPM2 NV index with. If no policy
	   was created before this PIN is used to protect the newly allocated NV index. If a policy has been created before the PIN is used to unlock write
	   access to the NV index. If this option is not used a PIN is automatically generated. Regardless if user supplied or automatically generated, it is
	   stored in encrypted form in the policy metadata file. The recovery PIN may be used to regain write access to an NV index in case the access policy
	   became out of date.

	   Added in version 255.

       --pcrlock=
	   Takes a file system path as argument. If specified overrides where to write the generated pcrlock data to. Honoured by the various lock-* commands.
	   If not specified, a default path is generally used, as documented above.

	   Added in version 255.

       --policy=
	   Takes a file system path as argument. If specified overrides where to write pcrlock policy metadata to. If not specified defaults to
	   /var/lib/systemd/pcrlock.json.

	   Added in version 255.

       --force
	   If specified with make-policy, the predicted policy will be written to the NV index even if it is detected to be the same as the previously stored
	   one.

	   Added in version 255.

       --json=MODE
	   Shows output formatted as JSON. Expects one of "short" (for the shortest possible output without any redundant whitespace or line breaks), "pretty"
	   (for a pretty version of the same, with indentation and line breaks) or "off" (to turn off JSON output, the default).

       --no-pager
	   Do not pipe output into a pager.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise.

SEE ALSO
       systemd(1), systemd.pcrlock(5), systemd-cryptenroll(1), systemd-cryptsetup@.service(8), systemd-repart(8), systemd-pcrmachine.service(8)

NOTES
	1. TCG Common Event Log Format (CEL-JSON)
	   https://trustedcomputinggroup.org/resource/canonical-event-log-format/

systemd 255																    SYSTEMD-PCRLOCK(8)
