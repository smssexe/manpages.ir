SYSTEMD.INDEX(7)							 systemd.index							      SYSTEMD.INDEX(7)

NAME
       systemd.index - List all manpages from the systemd project

3
       30-systemd-environment-d-generator(8) — Load variables specified by environment.d

B
       binfmt.d(5) — Configure additional binary formats for executables at boot
       bootctl(1) — Control EFI firmware boot settings and manage boot loader
       bootup(7) — System bootup process
       busctl(1) — Introspect the bus

C
       coredump.conf(5) — Core dump storage configuration files
       coredump.conf.d(5) — Core dump storage configuration files
       coredumpctl(1) — Retrieve and process saved core dumps and metadata
       crypttab(5) — Configuration for encrypted block devices

D
       daemon(7) — Writing and packaging system daemons
       dnssec-trust-anchors.d(5) — DNSSEC trust anchor configuration files

E
       environment.d(5) — Definition of user service environment
       extension-release(5) — Operating system identification

F
       file-hierarchy(7) — File system hierarchy overview

H
       halt(8) — Power off, reboot, or halt the machine
       homectl(1) — Create, remove, change or inspect home directories
       homed.conf(5) — Home area/user account manager configuration files
       homed.conf.d(5) — Home area/user account manager configuration files
       hostname(5) — Local hostname configuration file
       hostnamectl(1) — Control the system hostname
       hwdb(7) — Hardware Database

I
       init(1) — systemd system and service manager
       initrd-release(5) — Operating system identification
       integritytab(5) — Configuration for integrity block devices
       iocost.conf(5) — Configuration files for the iocost solution manager

J
       journal-remote.conf(5) — Configuration files for the service accepting remote journal uploads
       journal-remote.conf.d(5) — Configuration files for the service accepting remote journal uploads
       journal-upload.conf(5) — Configuration files for the journal upload service
       journal-upload.conf.d(5) — Configuration files for the journal upload service
       journalctl(1) — Print log entries from the systemd journal
       journald.conf(5) — Journal service configuration files
       journald.conf.d(5) — Journal service configuration files
       journald@.conf(5) — Journal service configuration files

K
       kernel-command-line(7) — Kernel command line parameters
       kernel-install(8) — Add and remove kernel and initrd images to and from /boot

L
       libnss_myhostname.so.2(8) — Hostname resolution for the locally configured system hostname
       libnss_mymachines.so.2(8) — Hostname resolution for local container instances
       libnss_resolve.so.2(8) — Hostname resolution via systemd-resolved.service
       libnss_systemd.so.2(8) — UNIX user and group name resolution for user/group lookup via Varlink
       libsystemd(3) — Functions for implementing services and interacting with systemd
       libudev(3) — API for enumerating and introspecting local devices
       linuxaa64.efi.stub(7) — A simple UEFI kernel boot stub
       linuxia32.efi.stub(7) — A simple UEFI kernel boot stub
       linuxx64.efi.stub(7) — A simple UEFI kernel boot stub
       loader.conf(5) — Configuration file for systemd-boot
       locale.conf(5) — Configuration file for locale settings
       localectl(1) — Control the system locale and keyboard layout settings
       localtime(5) — Local timezone configuration file
       loginctl(1) — Control the systemd login manager
       logind.conf(5) — Login manager configuration files
       logind.conf.d(5) — Login manager configuration files

M
       machine-id(5) — Local machine ID configuration file
       machine-info(5) — Local machine information file
       machinectl(1) — Control the systemd machine manager
       modules-load.d(5) — Configure kernel modules to load at boot
       mount.ddi(1) — Dissect Discoverable Disk Images (DDIs)

N
       networkctl(1) — Query or modify the status of network links
       networkd.conf(5) — Global Network configuration files
       networkd.conf.d(5) — Global Network configuration files
       nss-myhostname(8) — Hostname resolution for the locally configured system hostname
       nss-mymachines(8) — Hostname resolution for local container instances
       nss-resolve(8) — Hostname resolution via systemd-resolved.service
       nss-systemd(8) — UNIX user and group name resolution for user/group lookup via Varlink

O
       oomctl(1) — Analyze the state stored in systemd-oomd
       oomd.conf(5) — Global systemd-oomd configuration files
       oomd.conf.d(5) — Global systemd-oomd configuration files
       org.freedesktop.home1(5) — The D-Bus interface of systemd-homed
       org.freedesktop.hostname1(5) — The D-Bus interface of systemd-hostnamed
       org.freedesktop.import1(5) — The D-Bus interface of systemd-importd
       org.freedesktop.locale1(5) — The D-Bus interface of systemd-localed
       org.freedesktop.LogControl1(5) — D-Bus interface to query and set logging configuration
       org.freedesktop.login1(5) — The D-Bus interface of systemd-logind
       org.freedesktop.machine1(5) — The D-Bus interface of systemd-machined
       org.freedesktop.network1(5) — The D-Bus interface of systemd-networkd
       org.freedesktop.oom1(5) — The D-Bus interface of systemd-oomd
       org.freedesktop.portable1(5) — The D-Bus interface of systemd-portabled
       org.freedesktop.resolve1(5) — The D-Bus interface of systemd-resolved
       org.freedesktop.systemd1(5) — The D-Bus interface of systemd
       org.freedesktop.timedate1(5) — The D-Bus interface of systemd-timedated
       os-release(5) — Operating system identification

P
       pam_systemd(8) — Register user sessions in the systemd login manager
       pam_systemd_home(8) — Authenticate users and mount home directories via systemd-homed.service
       pam_systemd_loadkey(8) — Read password from kernel keyring and set it as PAM authtok
       portablectl(1) — Attach, detach or inspect portable service images
       poweroff(8) — Power off, reboot, or halt the machine
       pstore.conf(5) — PStore configuration file
       pstore.conf.d(5) — PStore configuration file

R
       rc-local.service(8) — Compatibility generator and service to start /etc/rc.local during boot
       reboot(8) — Power off, reboot, or halt the machine
       repart.d(5) — Partition Definition Files for Automatic Boot-Time Repartitioning
       resolvconf(1) — Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver
       resolvectl(1) — Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver
       resolved.conf(5) — Network Name Resolution configuration files
       resolved.conf.d(5) — Network Name Resolution configuration files
       runlevel(8) — Print previous and current SysV runlevel

S
       sd-boot(7) — A simple UEFI boot manager
       sd-bus(3) — A lightweight D-Bus IPC client library
       sd-bus-errors(3) — Standard D-Bus error names
       sd-daemon(3) — APIs for new-style daemons
       sd-device(3) — API for enumerating and introspecting local devices
       sd-event(3) — A generic event loop implementation
       sd-hwdb(3) — Read-only access to the hardware description database
       sd-id128(3) — APIs for processing 128-bit IDs
       sd-journal(3) — APIs for submitting and querying log entries to and from the journal
       sd-login(3) — APIs for tracking logins
       sd-stub(7) — A simple UEFI kernel boot stub
       SD_ALERT(3) — APIs for new-style daemons
       sd_booted(3) — Test whether the system is running the systemd init system
       sd_bus_add_fallback(3) — Declare properties and methods for a D-Bus path
       sd_bus_add_fallback_vtable(3) — Declare properties and methods for a D-Bus path
       sd_bus_add_filter(3) — Declare properties and methods for a D-Bus path
       sd_bus_add_match(3) — Add a match rule for incoming message dispatching
       sd_bus_add_match_async(3) — Add a match rule for incoming message dispatching
       sd_bus_add_node_enumerator(3) — Add a node enumerator for a D-Bus object path prefix
       sd_bus_add_object(3) — Declare properties and methods for a D-Bus path
       sd_bus_add_object_manager(3) — Add a D-Bus object manager for a D-Bus object sub-tree
       sd_bus_add_object_vtable(3) — Declare properties and methods for a D-Bus path
       sd_bus_attach_event(3) — Attach a bus connection object to an event loop
       sd_bus_call(3) — Invoke a D-Bus method call
       sd_bus_call_async(3) — Invoke a D-Bus method call
       sd_bus_call_method(3) — Initialize a bus message object and invoke the corresponding D-Bus method call
       sd_bus_call_method_async(3) — Initialize a bus message object and invoke the corresponding D-Bus method call
       sd_bus_call_method_asyncv(3) — Initialize a bus message object and invoke the corresponding D-Bus method call
       sd_bus_call_methodv(3) — Initialize a bus message object and invoke the corresponding D-Bus method call
       sd_bus_can_send(3) — Check which types can be sent over a bus object
       sd_bus_close(3) — Close and flush a bus connection
       sd_bus_close_unref(3) — Create a new bus object and create or destroy references to it
       sd_bus_close_unrefp(3) — Create a new bus object and create or destroy references to it
       sd_bus_creds_get_audit_login_uid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_audit_session_id(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_augmented_mask(3) — Retrieve credentials object for the specified PID
       sd_bus_creds_get_cgroup(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_cmdline(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_comm(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_description(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_egid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_euid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_exe(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_fsgid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_fsuid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_gid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_mask(3) — Retrieve credentials object for the specified PID
       sd_bus_creds_get_owner_uid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_pid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_ppid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_selinux_context(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_session(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_sgid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_slice(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_suid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_supplementary_gids(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_tid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_tid_comm(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_tty(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_uid(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_unique_name(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_unit(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_user_slice(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_user_unit(3) — Retrieve fields from a credentials object
       sd_bus_creds_get_well_known_names(3) — Retrieve fields from a credentials object
       sd_bus_creds_has_bounding_cap(3) — Retrieve fields from a credentials object
       sd_bus_creds_has_effective_cap(3) — Retrieve fields from a credentials object
       sd_bus_creds_has_inheritable_cap(3) — Retrieve fields from a credentials object
       sd_bus_creds_has_permitted_cap(3) — Retrieve fields from a credentials object
       sd_bus_creds_new_from_pid(3) — Retrieve credentials object for the specified PID
       sd_bus_creds_ref(3) — Retrieve credentials object for the specified PID
       sd_bus_creds_unref(3) — Retrieve credentials object for the specified PID
       sd_bus_creds_unrefp(3) — Retrieve credentials object for the specified PID
       sd_bus_default(3) — Acquire a connection to a system or user bus
       sd_bus_default_flush_close(3) — Close and flush a bus connection
       sd_bus_default_system(3) — Acquire a connection to a system or user bus
       sd_bus_default_user(3) — Acquire a connection to a system or user bus
       sd_bus_destroy_t(3) — Define the callback function for resource cleanup
       sd_bus_detach_event(3) — Attach a bus connection object to an event loop
       sd_bus_emit_interfaces_added(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_interfaces_added_strv(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_interfaces_removed(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_interfaces_removed_strv(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_object_added(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_object_removed(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_properties_changed(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_properties_changed_strv(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_signal(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_signal_to(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_signal_tov(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_emit_signalv(3) — Convenience functions for emitting (standard) D-Bus signals
       sd_bus_enqueue_for_read(3) — Re-enqueue a bus message on a bus connection, for reading
       sd_bus_error(3) — sd-bus error handling
       SD_BUS_ERROR_ACCESS_DENIED(3) — Standard D-Bus error names
       sd_bus_error_add_map(3) — Additional sd-dbus error mappings
       SD_BUS_ERROR_ADDRESS_IN_USE(3) — Standard D-Bus error names
       SD_BUS_ERROR_AUTH_FAILED(3) — Standard D-Bus error names
       SD_BUS_ERROR_BAD_ADDRESS(3) — Standard D-Bus error names
       sd_bus_error_copy(3) — sd-bus error handling
       SD_BUS_ERROR_DISCONNECTED(3) — Standard D-Bus error names
       SD_BUS_ERROR_END(3) — Additional sd-dbus error mappings
       SD_BUS_ERROR_FAILED(3) — Standard D-Bus error names
       SD_BUS_ERROR_FILE_EXISTS(3) — Standard D-Bus error names
       SD_BUS_ERROR_FILE_NOT_FOUND(3) — Standard D-Bus error names
       sd_bus_error_free(3) — sd-bus error handling
       sd_bus_error_get_errno(3) — sd-bus error handling
       sd_bus_error_has_name(3) — sd-bus error handling
       sd_bus_error_has_names(3) — sd-bus error handling
       sd_bus_error_has_names_sentinel(3) — sd-bus error handling
       SD_BUS_ERROR_INCONSISTENT_MESSAGE(3) — Standard D-Bus error names
       SD_BUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED(3) — Standard D-Bus error names
       SD_BUS_ERROR_INVALID_ARGS(3) — Standard D-Bus error names
       SD_BUS_ERROR_INVALID_FILE_CONTENT(3) — Standard D-Bus error names
       SD_BUS_ERROR_INVALID_SIGNATURE(3) — Standard D-Bus error names
       SD_BUS_ERROR_IO_ERROR(3) — Standard D-Bus error names
       sd_bus_error_is_set(3) — sd-bus error handling
       SD_BUS_ERROR_LIMITS_EXCEEDED(3) — Standard D-Bus error names
       SD_BUS_ERROR_MAKE_CONST(3) — sd-bus error handling
       sd_bus_error_map(3) — Additional sd-dbus error mappings
       SD_BUS_ERROR_MAP(3) — Additional sd-dbus error mappings
       SD_BUS_ERROR_MATCH_RULE_INVALID(3) — Standard D-Bus error names
       SD_BUS_ERROR_MATCH_RULE_NOT_FOUND(3) — Standard D-Bus error names
       sd_bus_error_move(3) — sd-bus error handling
       SD_BUS_ERROR_NAME_HAS_NO_OWNER(3) — Standard D-Bus error names
       SD_BUS_ERROR_NO_MEMORY(3) — Standard D-Bus error names
       SD_BUS_ERROR_NO_NETWORK(3) — Standard D-Bus error names
       SD_BUS_ERROR_NO_REPLY(3) — Standard D-Bus error names
       SD_BUS_ERROR_NO_SERVER(3) — Standard D-Bus error names
       SD_BUS_ERROR_NOT_SUPPORTED(3) — Standard D-Bus error names
       SD_BUS_ERROR_NULL(3) — sd-bus error handling
       SD_BUS_ERROR_OBJECT_PATH_IN_USE(3) — Standard D-Bus error names
       SD_BUS_ERROR_PROPERTY_READ_ONLY(3) — Standard D-Bus error names
       SD_BUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN(3) — Standard D-Bus error names
       SD_BUS_ERROR_SERVICE_UNKNOWN(3) — Standard D-Bus error names
       sd_bus_error_set(3) — sd-bus error handling
       sd_bus_error_set_const(3) — sd-bus error handling
       sd_bus_error_set_errno(3) — sd-bus error handling
       sd_bus_error_set_errnof(3) — sd-bus error handling
       sd_bus_error_set_errnofv(3) — sd-bus error handling
       sd_bus_error_setf(3) — sd-bus error handling
       sd_bus_error_setfv(3) — sd-bus error handling
       SD_BUS_ERROR_TIMED_OUT(3) — Standard D-Bus error names
       SD_BUS_ERROR_TIMEOUT(3) — Standard D-Bus error names
       SD_BUS_ERROR_UNIX_PROCESS_ID_UNKNOWN(3) — Standard D-Bus error names
       SD_BUS_ERROR_UNKNOWN_INTERFACE(3) — Standard D-Bus error names
       SD_BUS_ERROR_UNKNOWN_METHOD(3) — Standard D-Bus error names
       SD_BUS_ERROR_UNKNOWN_OBJECT(3) — Standard D-Bus error names
       SD_BUS_ERROR_UNKNOWN_PROPERTY(3) — Standard D-Bus error names
       sd_bus_flush(3) — Close and flush a bus connection
       sd_bus_flush_close_unref(3) — Create a new bus object and create or destroy references to it
       sd_bus_flush_close_unrefp(3) — Create a new bus object and create or destroy references to it
       sd_bus_get_address(3) — Set or query the address of the bus connection
       sd_bus_get_allow_interactive_authorization(3) — Set or query properties of a bus object
       sd_bus_get_bus_id(3) — Configure connection mode for a bus object
       sd_bus_get_close_on_exit(3) — Control whether to close the bus connection during the event loop exit phase
       sd_bus_get_connected_signal(3) — Control emission of local connection establishment signal on bus connections
       sd_bus_get_creds_mask(3) — Control feature negotiation on bus connections
       sd_bus_get_current_handler(3) — Query information of the callback a bus object is currently running
       sd_bus_get_current_message(3) — Query information of the callback a bus object is currently running
       sd_bus_get_current_slot(3) — Query information of the callback a bus object is currently running
       sd_bus_get_current_userdata(3) — Query information of the callback a bus object is currently running
       sd_bus_get_description(3) — Set or query properties of a bus object
       sd_bus_get_event(3) — Attach a bus connection object to an event loop
       sd_bus_get_events(3) — Get the file descriptor, I/O events and timeout to wait for from a message bus object
       sd_bus_get_exit_on_disconnect(3) — Control the exit behavior when the bus object disconnects
       sd_bus_get_fd(3) — Get the file descriptor, I/O events and timeout to wait for from a message bus object
       sd_bus_get_method_call_timeout(3) — Set or query the default D-Bus method call timeout of a bus object
       sd_bus_get_n_queued_read(3) — Get the number of pending bus messages in the read and write queues of a bus connection object
       sd_bus_get_n_queued_write(3) — Get the number of pending bus messages in the read and write queues of a bus connection object
       sd_bus_get_name_creds(3) — Query bus client credentials
       sd_bus_get_name_machine_id(3) — Retrieve a bus client's machine identity
       sd_bus_get_owner_creds(3) — Query bus client credentials
       sd_bus_get_property(3) — Set or query D-Bus service properties
       sd_bus_get_property_string(3) — Set or query D-Bus service properties
       sd_bus_get_property_strv(3) — Set or query D-Bus service properties
       sd_bus_get_property_trivial(3) — Set or query D-Bus service properties
       sd_bus_get_scope(3) — Set or query properties of a bus object
       sd_bus_get_sender(3) — Configure default sender for outgoing messages
       sd_bus_get_tid(3) — Set or query properties of a bus object
       sd_bus_get_timeout(3) — Get the file descriptor, I/O events and timeout to wait for from a message bus object
       sd_bus_get_unique_name(3) — Set or query properties of a bus object
       sd_bus_get_watch_bind(3) — Control socket binding watching on bus connections
       sd_bus_interface_name_is_valid(3) — Check if a string is a valid bus name or object path
       sd_bus_is_anonymous(3) — Set or query properties of a bus object
       sd_bus_is_bus_client(3) — Configure connection mode for a bus object
       sd_bus_is_monitor(3) — Configure connection mode for a bus object
       sd_bus_is_open(3) — Check whether the bus connection is open or ready
       sd_bus_is_ready(3) — Check whether the bus connection is open or ready
       sd_bus_is_server(3) — Configure connection mode for a bus object
       sd_bus_is_trusted(3) — Set or query properties of a bus object
       sd_bus_list_names(3) — Retrieve information about registered names on a bus
       sd_bus_match_signal(3) — Add a match rule for incoming message dispatching
       sd_bus_match_signal_async(3) — Add a match rule for incoming message dispatching
       sd_bus_member_name_is_valid(3) — Check if a string is a valid bus name or object path
       sd_bus_message_append(3) — Attach fields to a D-Bus message based on a type string
       sd_bus_message_append_array(3) — Append an array of fields to a D-Bus message
       sd_bus_message_append_array_iovec(3) — Append an array of fields to a D-Bus message
       sd_bus_message_append_array_memfd(3) — Append an array of fields to a D-Bus message
       sd_bus_message_append_array_space(3) — Append an array of fields to a D-Bus message
       sd_bus_message_append_basic(3) — Attach a single field to a message
       sd_bus_message_append_string_iovec(3) — Attach a string to a message
       sd_bus_message_append_string_memfd(3) — Attach a string to a message
       sd_bus_message_append_string_space(3) — Attach a string to a message
       sd_bus_message_append_strv(3) — Attach an array of strings to a message
       sd_bus_message_appendv(3) — Attach fields to a D-Bus message based on a type string
       sd_bus_message_at_end(3) — Check if a message has been fully read
       sd_bus_message_close_container(3) — Create and move between containers in D-Bus messages
       sd_bus_message_copy(3) — Copy the contents of one message to another
       sd_bus_message_dump(3) — Produce a string representation of a message for debugging purposes
       sd_bus_message_enter_container(3) — Create and move between containers in D-Bus messages
       sd_bus_message_exit_container(3) — Create and move between containers in D-Bus messages
       sd_bus_message_get_allow_interactive_authorization(3) — Set and query bus message metadata
       sd_bus_message_get_auto_start(3) — Set and query bus message metadata
       sd_bus_message_get_bus(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_get_cookie(3) — Returns the transaction cookie of a message
       sd_bus_message_get_creds(3) — Query bus message addressing/credentials metadata
       sd_bus_message_get_destination(3) — Set and query bus message addressing information
       sd_bus_message_get_errno(3) — Query bus message addressing/credentials metadata
       sd_bus_message_get_error(3) — Query bus message addressing/credentials metadata
       sd_bus_message_get_expect_reply(3) — Set and query bus message metadata
       sd_bus_message_get_interface(3) — Set and query bus message addressing information
       sd_bus_message_get_member(3) — Set and query bus message addressing information
       sd_bus_message_get_monotonic_usec(3) — Retrieve the sender timestamps and sequence number of a message
       sd_bus_message_get_path(3) — Set and query bus message addressing information
       sd_bus_message_get_realtime_usec(3) — Retrieve the sender timestamps and sequence number of a message
       sd_bus_message_get_reply_cookie(3) — Returns the transaction cookie of a message
       sd_bus_message_get_sender(3) — Set and query bus message addressing information
       sd_bus_message_get_seqnum(3) — Retrieve the sender timestamps and sequence number of a message
       sd_bus_message_get_signature(3) — Query bus message signature
       sd_bus_message_get_type(3) — Query bus message addressing/credentials metadata
       sd_bus_message_has_signature(3) — Query bus message signature
       sd_bus_message_is_empty(3) — Query bus message signature
       sd_bus_message_is_method_call(3) — Query bus message addressing/credentials metadata
       sd_bus_message_is_method_error(3) — Query bus message addressing/credentials metadata
       sd_bus_message_is_signal(3) — Query bus message addressing/credentials metadata
       SD_BUS_MESSAGE_METHOD_CALL(3) — Create a new bus message object and create or destroy references to it
       SD_BUS_MESSAGE_METHOD_ERROR(3) — Create a new bus message object and create or destroy references to it
       SD_BUS_MESSAGE_METHOD_RETURN(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_new(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_new_method_call(3) — Create a method call message
       sd_bus_message_new_method_errno(3) — Create an error reply for a method call
       sd_bus_message_new_method_errnof(3) — Create an error reply for a method call
       sd_bus_message_new_method_error(3) — Create an error reply for a method call
       sd_bus_message_new_method_errorf(3) — Create an error reply for a method call
       sd_bus_message_new_method_return(3) — Create a method call message
       sd_bus_message_new_signal(3) — Create a signal message
       sd_bus_message_new_signal_to(3) — Create a signal message
       sd_bus_message_open_container(3) — Create and move between containers in D-Bus messages
       sd_bus_message_peek_type(3) — Read a sequence of values from a message
       sd_bus_message_read(3) — Read a sequence of values from a message
       sd_bus_message_read_array(3) — Access an array of elements in a message
       sd_bus_message_read_basic(3) — Read a basic type from a message
       sd_bus_message_read_strv(3) — Access an array of strings in a message
       sd_bus_message_read_strv_extend(3) — Access an array of strings in a message
       sd_bus_message_readv(3) — Read a sequence of values from a message
       sd_bus_message_ref(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_rewind(3) — Return to beginning of message or current container
       sd_bus_message_seal(3) — Prepare a D-Bus message for transmission
       sd_bus_message_send(3) — Queue a D-Bus message for transfer
       sd_bus_message_sensitive(3) — Mark a message object as containing sensitive data
       sd_bus_message_set_allow_interactive_authorization(3) — Set and query bus message metadata
       sd_bus_message_set_auto_start(3) — Set and query bus message metadata
       sd_bus_message_set_destination(3) — Set and query bus message addressing information
       sd_bus_message_set_expect_reply(3) — Set and query bus message metadata
       sd_bus_message_set_sender(3) — Set and query bus message addressing information
       SD_BUS_MESSAGE_SIGNAL(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_skip(3) — Skip elements in a bus message
       sd_bus_message_unref(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_unrefp(3) — Create a new bus message object and create or destroy references to it
       sd_bus_message_verify_type(3) — Check if the message has specified type at the current location
       SD_BUS_METHOD(3) — Declare properties and methods for a D-Bus path
       SD_BUS_METHOD_WITH_NAMES(3) — Declare properties and methods for a D-Bus path
       SD_BUS_METHOD_WITH_NAMES_OFFSET(3) — Declare properties and methods for a D-Bus path
       SD_BUS_METHOD_WITH_OFFSET(3) — Declare properties and methods for a D-Bus path
       sd_bus_negotiate_creds(3) — Control feature negotiation on bus connections
       sd_bus_negotiate_fds(3) — Control feature negotiation on bus connections
       sd_bus_negotiate_timestamp(3) — Control feature negotiation on bus connections
       sd_bus_new(3) — Create a new bus object and create or destroy references to it
       sd_bus_object_path_is_valid(3) — Check if a string is a valid bus name or object path
       sd_bus_open(3) — Acquire a connection to a system or user bus
       sd_bus_open_system(3) — Acquire a connection to a system or user bus
       sd_bus_open_system_machine(3) — Acquire a connection to a system or user bus
       sd_bus_open_system_remote(3) — Acquire a connection to a system or user bus
       sd_bus_open_system_with_description(3) — Acquire a connection to a system or user bus
       sd_bus_open_user(3) — Acquire a connection to a system or user bus
       sd_bus_open_user_machine(3) — Acquire a connection to a system or user bus
       sd_bus_open_user_with_description(3) — Acquire a connection to a system or user bus
       sd_bus_open_with_description(3) — Acquire a connection to a system or user bus
       SD_BUS_PARAM(3) — Declare properties and methods for a D-Bus path
       sd_bus_path_decode(3) — Convert an external identifier into an object path and back
       sd_bus_path_decode_many(3) — Convert an external identifier into an object path and back
       sd_bus_path_encode(3) — Convert an external identifier into an object path and back
       sd_bus_path_encode_many(3) — Convert an external identifier into an object path and back
       sd_bus_process(3) — Drive the connection
       SD_BUS_PROPERTY(3) — Declare properties and methods for a D-Bus path
       sd_bus_query_sender_creds(3) — Query bus message sender credentials/privileges
       sd_bus_query_sender_privilege(3) — Query bus message sender credentials/privileges
       sd_bus_ref(3) — Create a new bus object and create or destroy references to it
       sd_bus_release_name(3) — Request or release a well-known service name on a bus
       sd_bus_release_name_async(3) — Request or release a well-known service name on a bus
       sd_bus_reply_method_errno(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_errnof(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_errnofv(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_error(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_errorf(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_errorfv(3) — Reply with an error to a D-Bus method call
       sd_bus_reply_method_return(3) — Reply to a D-Bus method call
       sd_bus_reply_method_returnv(3) — Reply to a D-Bus method call
       sd_bus_request_name(3) — Request or release a well-known service name on a bus
       sd_bus_request_name_async(3) — Request or release a well-known service name on a bus
       sd_bus_send(3) — Queue a D-Bus message for transfer
       sd_bus_send_to(3) — Queue a D-Bus message for transfer
       sd_bus_service_name_is_valid(3) — Check if a string is a valid bus name or object path
       sd_bus_set_address(3) — Set or query the address of the bus connection
       sd_bus_set_allow_interactive_authorization(3) — Set or query properties of a bus object
       sd_bus_set_anonymous(3) — Set or query properties of a bus object
       sd_bus_set_bus_client(3) — Configure connection mode for a bus object
       sd_bus_set_close_on_exit(3) — Control whether to close the bus connection during the event loop exit phase
       sd_bus_set_connected_signal(3) — Control emission of local connection establishment signal on bus connections
       sd_bus_set_description(3) — Set or query properties of a bus object
       sd_bus_set_exec(3) — Set or query the address of the bus connection
       sd_bus_set_exit_on_disconnect(3) — Control the exit behavior when the bus object disconnects
       sd_bus_set_fd(3) — Set the file descriptors to use for bus communication
       sd_bus_set_method_call_timeout(3) — Set or query the default D-Bus method call timeout of a bus object
       sd_bus_set_monitor(3) — Configure connection mode for a bus object
       sd_bus_set_property(3) — Set or query D-Bus service properties
       sd_bus_set_propertyv(3) — Set or query D-Bus service properties
       sd_bus_set_sender(3) — Configure default sender for outgoing messages
       sd_bus_set_server(3) — Configure connection mode for a bus object
       sd_bus_set_trusted(3) — Set or query properties of a bus object
       sd_bus_set_watch_bind(3) — Control socket binding watching on bus connections
       SD_BUS_SIGNAL(3) — Declare properties and methods for a D-Bus path
       SD_BUS_SIGNAL_WITH_NAMES(3) — Declare properties and methods for a D-Bus path
       sd_bus_slot_get_bus(3) — Query information attached to a bus slot object
       sd_bus_slot_get_current_handler(3) — Query information attached to a bus slot object
       sd_bus_slot_get_current_message(3) — Query information attached to a bus slot object
       sd_bus_slot_get_current_userdata(3) — Query information attached to a bus slot object
       sd_bus_slot_get_description(3) — Set or query the description of bus slot objects
       sd_bus_slot_get_destroy_callback(3) — Define the callback function for resource cleanup
       sd_bus_slot_get_floating(3) — Control whether a bus slot object is "floating"
       sd_bus_slot_get_userdata(3) — Set and query the value in the "userdata" field
       sd_bus_slot_ref(3) — Create and destroy references to a bus slot object
       sd_bus_slot_set_description(3) — Set or query the description of bus slot objects
       sd_bus_slot_set_destroy_callback(3) — Define the callback function for resource cleanup
       sd_bus_slot_set_floating(3) — Control whether a bus slot object is "floating"
       sd_bus_slot_set_userdata(3) — Set and query the value in the "userdata" field
       sd_bus_slot_unref(3) — Create and destroy references to a bus slot object
       sd_bus_slot_unrefp(3) — Create and destroy references to a bus slot object
       sd_bus_start(3) — Initiate a bus connection to the D-bus broker daemon
       sd_bus_track_add_name(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_add_sender(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_contains(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_count(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_count_name(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_count_sender(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_first(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_get_bus(3) — Track bus peers
       sd_bus_track_get_destroy_callback(3) — Define the callback function for resource cleanup
       sd_bus_track_get_recursive(3) — Track bus peers
       sd_bus_track_get_userdata(3) — Track bus peers
       sd_bus_track_new(3) — Track bus peers
       sd_bus_track_next(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_ref(3) — Track bus peers
       sd_bus_track_remove_name(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_remove_sender(3) — Add, remove and retrieve bus peers tracked in a bus peer tracking object
       sd_bus_track_set_destroy_callback(3) — Define the callback function for resource cleanup
       sd_bus_track_set_recursive(3) — Track bus peers
       sd_bus_track_set_userdata(3) — Track bus peers
       sd_bus_track_unref(3) — Track bus peers
       sd_bus_track_unrefp(3) — Track bus peers
       sd_bus_unref(3) — Create a new bus object and create or destroy references to it
       sd_bus_unrefp(3) — Create a new bus object and create or destroy references to it
       SD_BUS_VTABLE_CAPABILITY(3) — Declare properties and methods for a D-Bus path
       SD_BUS_VTABLE_END(3) — Declare properties and methods for a D-Bus path
       SD_BUS_VTABLE_START(3) — Declare properties and methods for a D-Bus path
       sd_bus_wait(3) — Wait for I/O on a bus connection
       SD_BUS_WRITABLE_PROPERTY(3) — Declare properties and methods for a D-Bus path
       SD_CRIT(3) — APIs for new-style daemons
       SD_DEBUG(3) — APIs for new-style daemons
       sd_device_get_devname(3) — Returns various fields of device objects
       sd_device_get_devnum(3) — Returns various fields of device objects
       sd_device_get_devpath(3) — Returns various fields of device objects
       sd_device_get_devtype(3) — Returns various fields of device objects
       sd_device_get_diskseq(3) — Returns various fields of device objects
       sd_device_get_driver(3) — Returns various fields of device objects
       sd_device_get_ifindex(3) — Returns various fields of device objects
       sd_device_get_subsystem(3) — Returns various fields of device objects
       sd_device_get_sysname(3) — Returns various fields of device objects
       sd_device_get_sysnum(3) — Returns various fields of device objects
       sd_device_get_syspath(3) — Returns various fields of device objects
       sd_device_ref(3) — Create or destroy references to a device object
       sd_device_unref(3) — Create or destroy references to a device object
       sd_device_unrefp(3) — Create or destroy references to a device object
       SD_EMERG(3) — APIs for new-style daemons
       SD_ERR(3) — APIs for new-style daemons
       sd_event(3) — Acquire and release an event loop object
       sd_event_add_child(3) — Add a child process state change event source to an event loop
       sd_event_add_child_pidfd(3) — Add a child process state change event source to an event loop
       sd_event_add_defer(3) — Add static event sources to an event loop
       sd_event_add_exit(3) — Add static event sources to an event loop
       sd_event_add_inotify(3) — Add an "inotify" file system inode event source to an event loop
       sd_event_add_inotify_fd(3) — Add an "inotify" file system inode event source to an event loop
       sd_event_add_io(3) — Add an I/O event source to an event loop
       sd_event_add_memory_pressure(3) — Add and configure an event source run as result of memory pressure
       sd_event_add_post(3) — Add static event sources to an event loop
       sd_event_add_signal(3) — Add a UNIX process signal event source to an event loop
       sd_event_add_time(3) — Add a timer event source to an event loop
       sd_event_add_time_relative(3) — Add a timer event source to an event loop
       SD_EVENT_ARMED(3) — Low-level event loop operations
       sd_event_child_handler_t(3) — Add a child process state change event source to an event loop
       sd_event_default(3) — Acquire and release an event loop object
       sd_event_destroy_t(3) — Define the callback function for resource cleanup
       sd_event_dispatch(3) — Low-level event loop operations
       sd_event_exit(3) — Ask the event loop to exit
       SD_EVENT_EXITING(3) — Low-level event loop operations
       SD_EVENT_FINISHED(3) — Low-level event loop operations
       sd_event_get_exit_code(3) — Ask the event loop to exit
       sd_event_get_fd(3) — Obtain a file descriptor to poll for event loop events
       sd_event_get_iteration(3) — Low-level event loop operations
       sd_event_get_state(3) — Low-level event loop operations
       sd_event_get_tid(3) — Acquire and release an event loop object
       sd_event_get_watchdog(3) — Enable event loop watchdog support
       sd_event_handler_t(3) — Add static event sources to an event loop
       SD_EVENT_INITIAL(3) — Low-level event loop operations
       sd_event_inotify_handler_t(3) — Add an "inotify" file system inode event source to an event loop
       sd_event_io_handler_t(3) — Add an I/O event source to an event loop
       sd_event_loop(3) — Run an event loop
       sd_event_new(3) — Acquire and release an event loop object
       sd_event_now(3) — Retrieve current event loop iteration timestamp
       SD_EVENT_OFF(3) — Enable or disable event sources
       SD_EVENT_ON(3) — Enable or disable event sources
       SD_EVENT_ONESHOT(3) — Enable or disable event sources
       SD_EVENT_PENDING(3) — Low-level event loop operations
       sd_event_prepare(3) — Low-level event loop operations
       SD_EVENT_PREPARING(3) — Low-level event loop operations
       SD_EVENT_PRIORITY_IDLE(3) — Set or retrieve the priority of event sources
       SD_EVENT_PRIORITY_IMPORTANT(3) — Set or retrieve the priority of event sources
       SD_EVENT_PRIORITY_NORMAL(3) — Set or retrieve the priority of event sources
       sd_event_ref(3) — Acquire and release an event loop object
       sd_event_run(3) — Run an event loop
       SD_EVENT_RUNNING(3) — Low-level event loop operations
       sd_event_set_signal_exit(3) — Automatically leave event loop on SIGINT and SIGTERM
       sd_event_set_watchdog(3) — Enable event loop watchdog support
       sd_event_signal_handler_t(3) — Add a UNIX process signal event source to an event loop
       SD_EVENT_SIGNAL_PROCMASK(3) — Add a UNIX process signal event source to an event loop
       sd_event_source(3) — Add an I/O event source to an event loop
       sd_event_source_disable_unref(3) — Increase or decrease event source reference counters
       sd_event_source_disable_unrefp(3) — Increase or decrease event source reference counters
       sd_event_source_get_child_pid(3) — Add a child process state change event source to an event loop
       sd_event_source_get_child_pidfd(3) — Add a child process state change event source to an event loop
       sd_event_source_get_child_pidfd_own(3) — Add a child process state change event source to an event loop
       sd_event_source_get_child_process_own(3) — Add a child process state change event source to an event loop
       sd_event_source_get_description(3) — Set or retrieve descriptive names of event sources
       sd_event_source_get_destroy_callback(3) — Define the callback function for resource cleanup
       sd_event_source_get_enabled(3) — Enable or disable event sources
       sd_event_source_get_event(3) — Retrieve the event loop of an event source
       sd_event_source_get_exit_on_failure(3) — Set or retrieve the exit-on-failure feature of event sources
       sd_event_source_get_floating(3) — Set or retrieve 'floating' state of event sources
       sd_event_source_get_inotify_mask(3) — Add an "inotify" file system inode event source to an event loop
       sd_event_source_get_io_events(3) — Add an I/O event source to an event loop
       sd_event_source_get_io_fd(3) — Add an I/O event source to an event loop
       sd_event_source_get_io_fd_own(3) — Add an I/O event source to an event loop
       sd_event_source_get_io_revents(3) — Add an I/O event source to an event loop
       sd_event_source_get_pending(3) — Determine pending state of event sources
       sd_event_source_get_priority(3) — Set or retrieve the priority of event sources
       sd_event_source_get_ratelimit(3) — Configure rate limiting on event sources
       sd_event_source_get_signal(3) — Add a UNIX process signal event source to an event loop
       sd_event_source_get_time(3) — Add a timer event source to an event loop
       sd_event_source_get_time_accuracy(3) — Add a timer event source to an event loop
       sd_event_source_get_time_clock(3) — Add a timer event source to an event loop
       sd_event_source_get_userdata(3) — Set or retrieve user data pointer of event sources
       sd_event_source_is_ratelimited(3) — Configure rate limiting on event sources
       sd_event_source_leave_ratelimit(3) — Configure rate limiting on event sources
       sd_event_source_ref(3) — Increase or decrease event source reference counters
       sd_event_source_send_child_signal(3) — Add a child process state change event source to an event loop
       sd_event_source_set_child_pidfd_own(3) — Add a child process state change event source to an event loop
       sd_event_source_set_child_process_own(3) — Add a child process state change event source to an event loop
       sd_event_source_set_description(3) — Set or retrieve descriptive names of event sources
       sd_event_source_set_destroy_callback(3) — Define the callback function for resource cleanup
       sd_event_source_set_enabled(3) — Enable or disable event sources
       sd_event_source_set_exit_on_failure(3) — Set or retrieve the exit-on-failure feature of event sources
       sd_event_source_set_floating(3) — Set or retrieve 'floating' state of event sources
       sd_event_source_set_io_events(3) — Add an I/O event source to an event loop
       sd_event_source_set_io_fd(3) — Add an I/O event source to an event loop
       sd_event_source_set_io_fd_own(3) — Add an I/O event source to an event loop
       sd_event_source_set_memory_pressure_period(3) — Add and configure an event source run as result of memory pressure
       sd_event_source_set_memory_pressure_type(3) — Add and configure an event source run as result of memory pressure
       sd_event_source_set_prepare(3) — Set a preparation callback for event sources
       sd_event_source_set_priority(3) — Set or retrieve the priority of event sources
       sd_event_source_set_ratelimit(3) — Configure rate limiting on event sources
       sd_event_source_set_ratelimit_expire_callback(3) — Configure rate limiting on event sources
       sd_event_source_set_time(3) — Add a timer event source to an event loop
       sd_event_source_set_time_accuracy(3) — Add a timer event source to an event loop
       sd_event_source_set_time_relative(3) — Add a timer event source to an event loop
       sd_event_source_set_userdata(3) — Set or retrieve user data pointer of event sources
       sd_event_source_unref(3) — Increase or decrease event source reference counters
       sd_event_source_unrefp(3) — Increase or decrease event source reference counters
       sd_event_time_handler_t(3) — Add a timer event source to an event loop
       sd_event_trim_memory(3) — Add and configure an event source run as result of memory pressure
       sd_event_unref(3) — Acquire and release an event loop object
       sd_event_unrefp(3) — Acquire and release an event loop object
       sd_event_wait(3) — Low-level event loop operations
       sd_get_machine_names(3) — Determine available seats, sessions, logged in users and virtual machines/containers
       sd_get_seats(3) — Determine available seats, sessions, logged in users and virtual machines/containers
       sd_get_sessions(3) — Determine available seats, sessions, logged in users and virtual machines/containers
       sd_get_uids(3) — Determine available seats, sessions, logged in users and virtual machines/containers
       sd_hwdb_enumerate(3) — Seek to a location in hwdb or access entries
       SD_HWDB_FOREACH_PROPERTY(3) — Seek to a location in hwdb or access entries
       sd_hwdb_get(3) — Seek to a location in hwdb or access entries
       sd_hwdb_new(3) — Create a new hwdb object and create or destroy references to it
       sd_hwdb_new_from_path(3) — Create a new hwdb object and create or destroy references to it
       sd_hwdb_ref(3) — Create a new hwdb object and create or destroy references to it
       sd_hwdb_seek(3) — Seek to a location in hwdb or access entries
       sd_hwdb_unref(3) — Create a new hwdb object and create or destroy references to it
       SD_ID128_ALLF(3) — APIs for processing 128-bit IDs
       SD_ID128_CONST_STR(3) — APIs for processing 128-bit IDs
       sd_id128_equal(3) — APIs for processing 128-bit IDs
       SD_ID128_FORMAT_STR(3) — APIs for processing 128-bit IDs
       SD_ID128_FORMAT_VAL(3) — APIs for processing 128-bit IDs
       sd_id128_from_string(3) — Format or parse 128-bit IDs as strings
       sd_id128_get_app_specific(3) — Retrieve 128-bit IDs
       sd_id128_get_boot(3) — Retrieve 128-bit IDs
       sd_id128_get_boot_app_specific(3) — Retrieve 128-bit IDs
       sd_id128_get_invocation(3) — Retrieve 128-bit IDs
       sd_id128_get_machine(3) — Retrieve 128-bit IDs
       sd_id128_get_machine_app_specific(3) — Retrieve 128-bit IDs
       sd_id128_in_set(3) — APIs for processing 128-bit IDs
       sd_id128_in_set_sentinel(3) — APIs for processing 128-bit IDs
       sd_id128_in_setv(3) — APIs for processing 128-bit IDs
       sd_id128_is_allf(3) — APIs for processing 128-bit IDs
       sd_id128_is_null(3) — APIs for processing 128-bit IDs
       SD_ID128_MAKE(3) — APIs for processing 128-bit IDs
       SD_ID128_MAKE_STR(3) — APIs for processing 128-bit IDs
       SD_ID128_MAKE_UUID_STR(3) — APIs for processing 128-bit IDs
       SD_ID128_NULL(3) — APIs for processing 128-bit IDs
       sd_id128_randomize(3) — Generate 128-bit IDs
       sd_id128_string_equal(3) — APIs for processing 128-bit IDs
       SD_ID128_STRING_MAX(3) — Format or parse 128-bit IDs as strings
       sd_id128_t(3) — APIs for processing 128-bit IDs
       sd_id128_to_string(3) — Format or parse 128-bit IDs as strings
       SD_ID128_TO_STRING(3) — Format or parse 128-bit IDs as strings
       sd_id128_to_uuid_string(3) — Format or parse 128-bit IDs as strings
       SD_ID128_TO_UUID_STRING(3) — Format or parse 128-bit IDs as strings
       SD_ID128_UUID_FORMAT_STR(3) — APIs for processing 128-bit IDs
       SD_ID128_UUID_STRING_MAX(3) — Format or parse 128-bit IDs as strings
       SD_INFO(3) — APIs for new-style daemons
       sd_is_fifo(3) — Check the type of a file descriptor
       sd_is_mq(3) — Check the type of a file descriptor
       sd_is_socket(3) — Check the type of a file descriptor
       sd_is_socket_inet(3) — Check the type of a file descriptor
       sd_is_socket_sockaddr(3) — Check the type of a file descriptor
       sd_is_socket_unix(3) — Check the type of a file descriptor
       sd_is_special(3) — Check the type of a file descriptor
       sd_journal(3) — Open the system journal for reading
       sd_journal_add_conjunction(3) — Add or remove entry matches
       sd_journal_add_disjunction(3) — Add or remove entry matches
       sd_journal_add_match(3) — Add or remove entry matches
       SD_JOURNAL_ALL_NAMESPACES(3) — Open the system journal for reading
       SD_JOURNAL_APPEND(3) — Journal change notification interface
       sd_journal_close(3) — Open the system journal for reading
       SD_JOURNAL_CURRENT_USER(3) — Open the system journal for reading
       sd_journal_enumerate_available_data(3) — Read data fields from the current journal entry
       sd_journal_enumerate_available_unique(3) — Read unique data fields from the journal
       sd_journal_enumerate_data(3) — Read data fields from the current journal entry
       sd_journal_enumerate_fields(3) — Read used field names from the journal
       sd_journal_enumerate_unique(3) — Read unique data fields from the journal
       sd_journal_flush_matches(3) — Add or remove entry matches
       SD_JOURNAL_FOREACH(3) — Advance or set back the read pointer in the journal
       SD_JOURNAL_FOREACH_BACKWARDS(3) — Advance or set back the read pointer in the journal
       SD_JOURNAL_FOREACH_DATA(3) — Read data fields from the current journal entry
       SD_JOURNAL_FOREACH_FIELD(3) — Read used field names from the journal
       SD_JOURNAL_FOREACH_UNIQUE(3) — Read unique data fields from the journal
       sd_journal_get_catalog(3) — Retrieve message catalog entry
       sd_journal_get_catalog_for_message_id(3) — Retrieve message catalog entry
       sd_journal_get_cursor(3) — Get cursor string for or test cursor string against the current journal entry
       sd_journal_get_cutoff_monotonic_usec(3) — Read cut-off timestamps from the current journal entry
       sd_journal_get_cutoff_realtime_usec(3) — Read cut-off timestamps from the current journal entry
       sd_journal_get_data(3) — Read data fields from the current journal entry
       sd_journal_get_data_threshold(3) — Read data fields from the current journal entry
       sd_journal_get_events(3) — Journal change notification interface
       sd_journal_get_fd(3) — Journal change notification interface
       sd_journal_get_monotonic_usec(3) — Read timestamps from the current journal entry
       sd_journal_get_realtime_usec(3) — Read timestamps from the current journal entry
       sd_journal_get_seqnum(3) — Read sequence number from the current journal entry
       sd_journal_get_timeout(3) — Journal change notification interface
       sd_journal_get_usage(3) — Journal disk usage
       sd_journal_has_persistent_files(3) — Query availability of runtime or persistent journal files
       sd_journal_has_runtime_files(3) — Query availability of runtime or persistent journal files
       SD_JOURNAL_INCLUDE_DEFAULT_NAMESPACE(3) — Open the system journal for reading
       SD_JOURNAL_INVALIDATE(3) — Journal change notification interface
       SD_JOURNAL_LOCAL_ONLY(3) — Open the system journal for reading
       sd_journal_next(3) — Advance or set back the read pointer in the journal
       sd_journal_next_skip(3) — Advance or set back the read pointer in the journal
       SD_JOURNAL_NOP(3) — Journal change notification interface
       sd_journal_open(3) — Open the system journal for reading
       sd_journal_open_directory(3) — Open the system journal for reading
       sd_journal_open_directory_fd(3) — Open the system journal for reading
       sd_journal_open_files(3) — Open the system journal for reading
       sd_journal_open_files_fd(3) — Open the system journal for reading
       sd_journal_open_namespace(3) — Open the system journal for reading
       SD_JOURNAL_OS_ROOT(3) — Open the system journal for reading
       sd_journal_perror(3) — Submit log entries to the journal
       sd_journal_perror_with_location(3) — Submit log entries to the journal
       sd_journal_previous(3) — Advance or set back the read pointer in the journal
       sd_journal_previous_skip(3) — Advance or set back the read pointer in the journal
       sd_journal_print(3) — Submit log entries to the journal
       sd_journal_print_with_location(3) — Submit log entries to the journal
       sd_journal_printv(3) — Submit log entries to the journal
       sd_journal_printv_with_location(3) — Submit log entries to the journal
       sd_journal_process(3) — Journal change notification interface
       sd_journal_query_unique(3) — Read unique data fields from the journal
       sd_journal_reliable_fd(3) — Journal change notification interface
       sd_journal_restart_data(3) — Read data fields from the current journal entry
       sd_journal_restart_fields(3) — Read used field names from the journal
       sd_journal_restart_unique(3) — Read unique data fields from the journal
       SD_JOURNAL_RUNTIME_ONLY(3) — Open the system journal for reading
       sd_journal_seek_cursor(3) — Seek to a position in the journal
       sd_journal_seek_head(3) — Seek to a position in the journal
       sd_journal_seek_monotonic_usec(3) — Seek to a position in the journal
       sd_journal_seek_realtime_usec(3) — Seek to a position in the journal
       sd_journal_seek_tail(3) — Seek to a position in the journal
       sd_journal_send(3) — Submit log entries to the journal
       sd_journal_send_with_location(3) — Submit log entries to the journal
       sd_journal_sendv(3) — Submit log entries to the journal
       sd_journal_sendv_with_location(3) — Submit log entries to the journal
       sd_journal_set_data_threshold(3) — Read data fields from the current journal entry
       sd_journal_step_one(3) — Advance or set back the read pointer in the journal
       sd_journal_stream_fd(3) — Create log stream file descriptor to the journal
       SD_JOURNAL_SUPPRESS_LOCATION(3) — Submit log entries to the journal
       SD_JOURNAL_SYSTEM(3) — Open the system journal for reading
       SD_JOURNAL_TAKE_DIRECTORY_FD(3) — Open the system journal for reading
       sd_journal_test_cursor(3) — Get cursor string for or test cursor string against the current journal entry
       sd_journal_wait(3) — Journal change notification interface
       sd_listen_fds(3) — Check for file descriptors passed by the system manager
       SD_LISTEN_FDS_START(3) — Check for file descriptors passed by the system manager
       sd_listen_fds_with_names(3) — Check for file descriptors passed by the system manager
       sd_login_monitor(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_flush(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_get_events(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_get_fd(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_get_timeout(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_new(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_unref(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_login_monitor_unrefp(3) — Monitor login sessions, seats, users and virtual machines/containers
       sd_machine_get_class(3) — Determine the class and network interface indices of a locally running virtual machine or container
       sd_machine_get_ifindices(3) — Determine the class and network interface indices of a locally running virtual machine or container
       SD_NOTICE(3) — APIs for new-style daemons
       sd_notify(3) — Notify service manager about start-up completion and other service status changes
       sd_notify_barrier(3) — Notify service manager about start-up completion and other service status changes
       sd_notifyf(3) — Notify service manager about start-up completion and other service status changes
       sd_path_lookup(3) — Query well-known file system paths
       sd_path_lookup_strv(3) — Query well-known file system paths
       sd_peer_get_cgroup(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_machine_name(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_owner_uid(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_session(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_user_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_peer_get_user_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_cgroup(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_machine_name(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_owner_uid(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_session(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a specific
       PID or socket peer belongs to
       sd_pid_get_user_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_get_user_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pid_notify(3) — Notify service manager about start-up completion and other service status changes
       sd_pid_notify_barrier(3) — Notify service manager about start-up completion and other service status changes
       sd_pid_notify_with_fds(3) — Notify service manager about start-up completion and other service status changes
       sd_pid_notifyf(3) — Notify service manager about start-up completion and other service status changes
       sd_pid_notifyf_with_fds(3) — Notify service manager about start-up completion and other service status changes
       sd_pidfd_get_cgroup(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_machine_name(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that
       a specific PID or socket peer belongs to
       sd_pidfd_get_owner_uid(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_session(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_user_slice(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_pidfd_get_user_unit(3) — Determine the owner uid of the user unit or session, or the session, user unit, system unit, container/VM or slice that a
       specific PID or socket peer belongs to
       sd_seat_can_graphical(3) — Determine state of a specific seat
       sd_seat_can_tty(3) — Determine state of a specific seat
       sd_seat_get_active(3) — Determine state of a specific seat
       sd_seat_get_sessions(3) — Determine state of a specific seat
       sd_session_get_class(3) — Determine state of a specific session
       sd_session_get_desktop(3) — Determine state of a specific session
       sd_session_get_display(3) — Determine state of a specific session
       sd_session_get_leader(3) — Determine state of a specific session
       sd_session_get_remote_host(3) — Determine state of a specific session
       sd_session_get_remote_user(3) — Determine state of a specific session
       sd_session_get_seat(3) — Determine state of a specific session
       sd_session_get_service(3) — Determine state of a specific session
       sd_session_get_start_time(3) — Determine state of a specific session
       sd_session_get_state(3) — Determine state of a specific session
       sd_session_get_tty(3) — Determine state of a specific session
       sd_session_get_type(3) — Determine state of a specific session
       sd_session_get_uid(3) — Determine state of a specific session
       sd_session_get_username(3) — Determine state of a specific session
       sd_session_get_vt(3) — Determine state of a specific session
       sd_session_is_active(3) — Determine state of a specific session
       sd_session_is_remote(3) — Determine state of a specific session
       sd_uid_get_display(3) — Determine login state of a specific Unix user ID
       sd_uid_get_login_time(3) — Determine login state of a specific Unix user ID
       sd_uid_get_seats(3) — Determine login state of a specific Unix user ID
       sd_uid_get_sessions(3) — Determine login state of a specific Unix user ID
       sd_uid_get_state(3) — Determine login state of a specific Unix user ID
       sd_uid_is_on_seat(3) — Determine login state of a specific Unix user ID
       SD_WARNING(3) — APIs for new-style daemons
       sd_watchdog_enabled(3) — Check whether the service manager expects watchdog keep-alive notifications from a service
       shutdown(8) — Halt, power off or reboot the machine
       sleep.conf.d(5) — Suspend and hibernation configuration file
       smbios-type-11(7) — SMBIOS Type 11 strings
       sysctl.d(5) — Configure kernel parameters at boot
       system.conf.d(5) — System and session service manager configuration files
       systemctl(1) — Control the systemd system and service manager
       systemd(1) — systemd system and service manager
       systemd-ac-power(1) — Report whether we are connected to an external power source
       systemd-analyze(1) — Analyze and debug system manager
       systemd-ask-password(1) — Query the user for a system password
       systemd-ask-password-console.path(8) — Query the user for system passwords on the console and via wall
       systemd-ask-password-console.service(8) — Query the user for system passwords on the console and via wall
       systemd-ask-password-wall.path(8) — Query the user for system passwords on the console and via wall
       systemd-ask-password-wall.service(8) — Query the user for system passwords on the console and via wall
       systemd-backlight(8) — Load and save the display backlight brightness at boot and shutdown
       systemd-backlight@.service(8) — Load and save the display backlight brightness at boot and shutdown
       systemd-battery-check(8) — Check battery level whether there's enough charge, and power off if not
       systemd-battery-check.service(8) — Check battery level whether there's enough charge, and power off if not
       systemd-binfmt(8) — Configure additional binary formats for executables at boot
       systemd-binfmt.service(8) — Configure additional binary formats for executables at boot
       systemd-bless-boot(8) — Mark current boot process as successful
       systemd-bless-boot-generator(8) — Pull systemd-bless-boot.service into the initial boot transaction when boot counting is in effect
       systemd-bless-boot.service(8) — Mark current boot process as successful
       systemd-boot(7) — A simple UEFI boot manager
       systemd-boot-check-no-failures(8) — verify that the system booted up cleanly
       systemd-boot-check-no-failures.service(8) — verify that the system booted up cleanly
       systemd-boot-random-seed.service(8) — Refresh boot loader random seed at boot
       systemd-bsod(8) — Displays boot-time emergency log message in full screen.
       systemd-bsod.service(8) — Displays boot-time emergency log message in full screen.
       systemd-cat(1) — Connect a pipeline or program's output with the journal
       systemd-cgls(1) — Recursively show control group contents
       systemd-cgtop(1) — Show top control groups by their resource usage
       systemd-confext(8) — Activates System Extension Images
       systemd-confext.service(8) — Activates System Extension Images
       systemd-coredump(8) — Acquire, save and process core dumps
       systemd-coredump.socket(8) — Acquire, save and process core dumps
       systemd-coredump@.service(8) — Acquire, save and process core dumps
       systemd-creds(1) — Lists, shows, encrypts and decrypts service credentials
       systemd-cryptenroll(1) — Enroll PKCS#11, FIDO2, TPM2 token/devices to LUKS2 encrypted volumes
       systemd-cryptsetup(8) — Full disk decryption logic
       systemd-cryptsetup-generator(8) — Unit generator for /etc/crypttab
       systemd-cryptsetup@.service(8) — Full disk decryption logic
       systemd-debug-generator(8) — Generator for enabling a runtime debug shell and masking specific units at boot
       systemd-delta(1) — Find overridden configuration files
       systemd-detect-virt(1) — Detect execution in a virtualized environment
       systemd-dissect(1) — Dissect Discoverable Disk Images (DDIs)
       systemd-environment-d-generator(8) — Load variables specified by environment.d
       systemd-escape(1) — Escape strings for usage in systemd unit names
       systemd-firstboot(1) — Initialize basic system settings on or before the first boot-up of a system
       systemd-firstboot.service(1) — Initialize basic system settings on or before the first boot-up of a system
       systemd-fsck(8) — File system checker logic
       systemd-fsck-root.service(8) — File system checker logic
       systemd-fsck-usr.service(8) — File system checker logic
       systemd-fsck@.service(8) — File system checker logic
       systemd-fsckd(8) — File system check progress reporting
       systemd-fsckd.service(8) — File system check progress reporting
       systemd-fsckd.socket(8) — File system check progress reporting
       systemd-fstab-generator(8) — Unit generator for /etc/fstab
       systemd-getty-generator(8) — Generator for enabling getty instances on the console
       systemd-gpt-auto-generator(8) — Generator for automatically discovering and mounting root, /home/ , /srv/ , /var/ and /var/tmp/ partitions, as well as
       discovering and enabling swap partitions, based on GPT partition type GUIDs
       systemd-growfs(8) — Creating and growing file systems on demand
       systemd-growfs-root.service(8) — Creating and growing file systems on demand
       systemd-growfs@.service(8) — Creating and growing file systems on demand
       systemd-halt.service(8) — System shutdown logic
       systemd-hibernate-resume(8) — Resume from hibernation
       systemd-hibernate-resume-generator(8) — Unit generator for resume= kernel parameter
       systemd-hibernate-resume.service(8) — Resume from hibernation
       systemd-hibernate.service(8) — System sleep state logic
       systemd-homed(8) — Home Area/User Account Manager
       systemd-homed.service(8) — Home Area/User Account Manager
       systemd-hostnamed(8) — Daemon to control system hostname from programs
       systemd-hostnamed.service(8) — Daemon to control system hostname from programs
       systemd-hwdb(8) — hardware database management tool
       systemd-hybrid-sleep.service(8) — System sleep state logic
       systemd-id128(1) — Generate and print sd-128 identifiers
       systemd-importd(8) — VM and container image import and export service
       systemd-importd.service(8) — VM and container image import and export service
       systemd-inhibit(1) — Execute a program with an inhibition lock taken
       systemd-initctl(8) — /dev/initctl compatibility
       systemd-initctl.service(8) — /dev/initctl compatibility
       systemd-initctl.socket(8) — /dev/initctl compatibility
       systemd-integritysetup(8) — Disk integrity protection logic
       systemd-integritysetup-generator(8) — Unit generator for integrity protected block devices
       systemd-integritysetup@.service(8) — Disk integrity protection logic
       systemd-journal-gatewayd(8) — HTTP server for journal events
       systemd-journal-gatewayd.service(8) — HTTP server for journal events
       systemd-journal-gatewayd.socket(8) — HTTP server for journal events
       systemd-journal-remote(8) — Receive journal messages over the network
       systemd-journal-remote.service(8) — Receive journal messages over the network
       systemd-journal-remote.socket(8) — Receive journal messages over the network
       systemd-journal-upload(8) — Send journal messages over the network
       systemd-journal-upload.service(8) — Send journal messages over the network
       systemd-journald(8) — Journal service
       systemd-journald-audit.socket(8) — Journal service
       systemd-journald-dev-log.socket(8) — Journal service
       systemd-journald-varlink@.socket(8) — Journal service
       systemd-journald.service(8) — Journal service
       systemd-journald.socket(8) — Journal service
       systemd-journald@.service(8) — Journal service
       systemd-journald@.socket(8) — Journal service
       systemd-kexec.service(8) — System shutdown logic
       systemd-localed(8) — Locale bus mechanism
       systemd-localed.service(8) — Locale bus mechanism
       systemd-logind(8) — Login manager
       systemd-logind.service(8) — Login manager
       systemd-machine-id-commit.service(8) — Commit a transient machine ID to disk
       systemd-machine-id-setup(1) — Initialize the machine ID in /etc/machine-id
       systemd-machined(8) — Virtual machine and container registration manager
       systemd-machined.service(8) — Virtual machine and container registration manager
       systemd-makefs(8) — Creating and growing file systems on demand
       systemd-makefs@.service(8) — Creating and growing file systems on demand
       systemd-measure(1) — Pre-calculate and sign expected TPM2 PCR values for booted unified kernel images
       systemd-mkswap@.service(8) — Creating and growing file systems on demand
       systemd-modules-load(8) — Load kernel modules at boot
       systemd-modules-load.service(8) — Load kernel modules at boot
       systemd-mount(1) — Establish and destroy transient mount or auto-mount points
       systemd-network-generator(8) — Generate network configuration from the kernel command line
       systemd-network-generator.service(8) — Generate network configuration from the kernel command line
       systemd-networkd(8) — Network manager
       systemd-networkd-wait-online(8) — Wait for network to come online
       systemd-networkd-wait-online.service(8) — Wait for network to come online
       systemd-networkd-wait-online@.service(8) — Wait for network to come online
       systemd-networkd.service(8) — Network manager
       systemd-notify(1) — Notify service manager about start-up completion and other daemon status changes
       systemd-nspawn(1) — Spawn a command or OS in a light-weight container
       systemd-oomd(8) — A userspace out-of-memory (OOM) killer
       systemd-oomd.service(8) — A userspace out-of-memory (OOM) killer
       systemd-path(1) — List and query system and user paths
       systemd-pcrextend(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrfs-root.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrfs@.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrlock(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-file-system.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-firmware-code.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-firmware-config.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-machine-id.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-make-policy.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-secureboot-authority.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrlock-secureboot-policy.service(8) — Analyze and predict TPM2 PCR states and generate an access policy from the prediction
       systemd-pcrmachine.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrphase-initrd.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrphase-sysinit.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-pcrphase.service(8) — Measure boot phase into TPM2 PCR 11, machine ID and file system identity into PCR 15
       systemd-portabled(8) — Portable service manager
       systemd-portabled.service(8) — Portable service manager
       systemd-poweroff.service(8) — System shutdown logic
       systemd-pstore(8) — A service to archive contents of pstore
       systemd-pstore.service(8) — A service to archive contents of pstore
       systemd-quotacheck(8) — File system quota checker logic
       systemd-quotacheck.service(8) — File system quota checker logic
       systemd-random-seed(8) — Load and save the OS system random seed at boot and shutdown
       systemd-random-seed.service(8) — Load and save the OS system random seed at boot and shutdown
       systemd-rc-local-generator(8) — Compatibility generator and service to start /etc/rc.local during boot
       systemd-reboot.service(8) — System shutdown logic
       systemd-remount-fs(8) — Remount root and kernel file systems
       systemd-remount-fs.service(8) — Remount root and kernel file systems
       systemd-repart(8) — Automatically grow and add partitions
       systemd-repart.service(8) — Automatically grow and add partitions
       systemd-resolved(8) — Network Name Resolution manager
       systemd-resolved.service(8) — Network Name Resolution manager
       systemd-rfkill(8) — Load and save the RF kill switch state at boot and change
       systemd-rfkill.service(8) — Load and save the RF kill switch state at boot and change
       systemd-rfkill.socket(8) — Load and save the RF kill switch state at boot and change
       systemd-run(1) — Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units
       systemd-run-generator(8) — Generator for invoking commands specified on the kernel command line as system service
       systemd-shutdown(8) — System shutdown logic
       systemd-sleep(8) — System sleep state logic
       systemd-sleep.conf(5) — Suspend and hibernation configuration file
       systemd-socket-activate(1) — Test socket activation of daemons
       systemd-socket-proxyd(8) — Bidirectionally proxy local sockets to another (possibly remote) socket
       systemd-soft-reboot.service(8) — Userspace reboot operation
       systemd-stdio-bridge(1) — D-Bus proxy
       systemd-storagetm(8) — Exposes all local block devices as NVMe-TCP mass storage devices
       systemd-storagetm.service(8) — Exposes all local block devices as NVMe-TCP mass storage devices
       systemd-stub(7) — A simple UEFI kernel boot stub
       systemd-suspend-then-hibernate.service(8) — System sleep state logic
       systemd-suspend.service(8) — System sleep state logic
       systemd-sysctl(8) — Configure kernel parameters at boot
       systemd-sysctl.service(8) — Configure kernel parameters at boot
       systemd-sysext(8) — Activates System Extension Images
       systemd-sysext.service(8) — Activates System Extension Images
       systemd-system-update-generator(8) — Generator for redirecting boot to offline update mode
       systemd-system.conf(5) — System and session service manager configuration files
       systemd-sysupdate(8) — Automatically Update OS or Other Resources
       systemd-sysupdate-reboot.service(8) — Automatically Update OS or Other Resources
       systemd-sysupdate-reboot.timer(8) — Automatically Update OS or Other Resources
       systemd-sysupdate.service(8) — Automatically Update OS or Other Resources
       systemd-sysupdate.timer(8) — Automatically Update OS or Other Resources
       systemd-sysusers(8) — Allocate system users and groups
       systemd-sysusers.service(8) — Allocate system users and groups
       systemd-sysv-generator(8) — Unit generator for SysV init scripts
       systemd-time-wait-sync(8) — Wait until kernel time is synchronized
       systemd-time-wait-sync.service(8) — Wait until kernel time is synchronized
       systemd-timedated(8) — Time and date bus mechanism
       systemd-timedated.service(8) — Time and date bus mechanism
       systemd-timesyncd(8) — Network Time Synchronization
       systemd-timesyncd.service(8) — Network Time Synchronization
       systemd-tmpfiles(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tmpfiles-clean.service(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tmpfiles-clean.timer(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tmpfiles-setup-dev-early.service(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tmpfiles-setup-dev.service(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tmpfiles-setup.service(8) — Creates, deletes and cleans up volatile and temporary files and directories
       systemd-tpm2-setup(8) — Set up the TPM2 Storage Root Key (SRK) at boot
       systemd-tpm2-setup-early.service(8) — Set up the TPM2 Storage Root Key (SRK) at boot
       systemd-tpm2-setup.service(8) — Set up the TPM2 Storage Root Key (SRK) at boot
       systemd-tty-ask-password-agent(1) — List or process pending systemd password requests
       systemd-udev-settle.service(8) — Wait for all pending udev events to be handled
       systemd-udevd(8) — Device event managing daemon
       systemd-udevd-control.socket(8) — Device event managing daemon
       systemd-udevd-kernel.socket(8) — Device event managing daemon
       systemd-udevd.service(8) — Device event managing daemon
       systemd-umount(1) — Establish and destroy transient mount or auto-mount points
       systemd-update-done(8) — Mark /etc/ and /var/ fully updated
       systemd-update-done.service(8) — Mark /etc/ and /var/ fully updated
       systemd-update-utmp(8) — Write audit and utmp updates at bootup, runlevel changes and shutdown
       systemd-update-utmp-runlevel.service(8) — Write audit and utmp updates at bootup, runlevel changes and shutdown
       systemd-update-utmp.service(8) — Write audit and utmp updates at bootup, runlevel changes and shutdown
       systemd-user-runtime-dir(5) — System units to start the user manager
       systemd-user-sessions(8) — Permit user logins after boot, prohibit user logins at shutdown
       systemd-user-sessions.service(8) — Permit user logins after boot, prohibit user logins at shutdown
       systemd-user.conf(5) — System and session service manager configuration files
       systemd-userdbd(8) — JSON User/Group Record Query Multiplexer/NSS Compatibility
       systemd-userdbd.service(8) — JSON User/Group Record Query Multiplexer/NSS Compatibility
       systemd-veritysetup(8) — Disk verity protection logic
       systemd-veritysetup-generator(8) — Unit generator for verity protected block devices
       systemd-veritysetup@.service(8) — Disk verity protection logic
       systemd-volatile-root(8) — Make the root file system volatile
       systemd-volatile-root.service(8) — Make the root file system volatile
       systemd-xdg-autostart-generator(8) — User unit generator for XDG autostart files
       systemd.automount(5) — Automount unit configuration
       systemd.device(5) — Device unit configuration
       systemd.directives(7) — Index of configuration directives
       systemd.dnssd(5) — DNS-SD configuration
       systemd.environment-generator(7) — systemd environment file generators
       systemd.exec(5) — Execution environment configuration
       systemd.generator(7) — systemd unit generators
       systemd.image-policy(7) — Disk Image Dissection Policy
       systemd.journal-fields(7) — Special journal fields
       systemd.kill(5) — Process killing procedure configuration
       systemd.link(5) — Network device configuration
       systemd.mount(5) — Mount unit configuration
       systemd.negative(5) — DNSSEC trust anchor configuration files
       systemd.net-naming-scheme(7) — Network device naming schemes
       systemd.netdev(5) — Virtual Network Device configuration
       systemd.network(5) — Network configuration
       systemd.nspawn(5) — Container settings
       systemd.offline-updates(7) — Implementation of offline updates in systemd
       systemd.path(5) — Path unit configuration
       systemd.pcrlock(5) — PCR measurement prediction files
       systemd.pcrlock.d(5) — PCR measurement prediction files
       systemd.positive(5) — DNSSEC trust anchor configuration files
       systemd.preset(5) — Service enablement presets
       systemd.resource-control(5) — Resource control unit settings
       systemd.scope(5) — Scope unit configuration
       systemd.service(5) — Service unit configuration
       systemd.slice(5) — Slice unit configuration
       systemd.socket(5) — Socket unit configuration
       systemd.special(7) — Special systemd units
       systemd.swap(5) — Swap unit configuration
       systemd.syntax(7) — General syntax of systemd configuration files
       systemd.system-credentials(7) — System Credentials
       systemd.target(5) — Target unit configuration
       systemd.time(7) — Time and date specifications
       systemd.timer(5) — Timer unit configuration
       systemd.unit(5) — Unit configuration
       sysupdate.d(5) — Transfer Definition Files for Automatic Updates
       sysusers.d(5) — Declarative allocation of system users and groups

T
       telinit(8) — Change SysV runlevel
       timedatectl(1) — Control the system time and date
       timesyncd.conf(5) — Network Time Synchronization configuration files
       timesyncd.conf.d(5) — Network Time Synchronization configuration files
       tmpfiles.d(5) — Configuration for creation, deletion and cleaning of volatile and temporary files

U
       udev(7) — Dynamic device management
       udev.conf(5) — Configuration for device event managing daemon
       udev_device_get_action(3) — Query device properties
       udev_device_get_current_tags_list_entry(3) — Retrieve or set device attributes
       udev_device_get_devlinks_list_entry(3) — Retrieve or set device attributes
       udev_device_get_devnode(3) — Query device properties
       udev_device_get_devnum(3) — Query device properties
       udev_device_get_devpath(3) — Query device properties
       udev_device_get_devtype(3) — Query device properties
       udev_device_get_driver(3) — Query device properties
       udev_device_get_is_initialized(3) — Query device properties
       udev_device_get_parent(3) — Query device properties
       udev_device_get_parent_with_subsystem_devtype(3) — Query device properties
       udev_device_get_properties_list_entry(3) — Retrieve or set device attributes
       udev_device_get_property_value(3) — Retrieve or set device attributes
       udev_device_get_subsystem(3) — Query device properties
       udev_device_get_sysattr_list_entry(3) — Retrieve or set device attributes
       udev_device_get_sysattr_value(3) — Retrieve or set device attributes
       udev_device_get_sysname(3) — Query device properties
       udev_device_get_sysnum(3) — Query device properties
       udev_device_get_syspath(3) — Query device properties
       udev_device_get_tags_list_entry(3) — Retrieve or set device attributes
       udev_device_get_udev(3) — Query device properties
       udev_device_has_current_tag(3) — Retrieve or set device attributes
       udev_device_has_tag(3) — Retrieve or set device attributes
       udev_device_new_from_device_id(3) — Create, acquire and release a udev device object
       udev_device_new_from_devnum(3) — Create, acquire and release a udev device object
       udev_device_new_from_environment(3) — Create, acquire and release a udev device object
       udev_device_new_from_subsystem_sysname(3) — Create, acquire and release a udev device object
       udev_device_new_from_syspath(3) — Create, acquire and release a udev device object
       udev_device_ref(3) — Create, acquire and release a udev device object
       udev_device_set_sysattr_value(3) — Retrieve or set device attributes
       udev_device_unref(3) — Create, acquire and release a udev device object
       udev_enumerate_add_match_is_initialized(3) — Modify filters
       udev_enumerate_add_match_parent(3) — Modify filters
       udev_enumerate_add_match_property(3) — Modify filters
       udev_enumerate_add_match_subsystem(3) — Modify filters
       udev_enumerate_add_match_sysattr(3) — Modify filters
       udev_enumerate_add_match_sysname(3) — Modify filters
       udev_enumerate_add_match_tag(3) — Modify filters
       udev_enumerate_add_nomatch_subsystem(3) — Modify filters
       udev_enumerate_add_nomatch_sysattr(3) — Modify filters
       udev_enumerate_add_syspath(3) — Query or modify a udev enumerate object
       udev_enumerate_get_list_entry(3) — Query or modify a udev enumerate object
       udev_enumerate_get_udev(3) — Query or modify a udev enumerate object
       udev_enumerate_new(3) — Create, acquire and release a udev enumerate object
       udev_enumerate_ref(3) — Create, acquire and release a udev enumerate object
       udev_enumerate_scan_devices(3) — Query or modify a udev enumerate object
       udev_enumerate_scan_subsystems(3) — Query or modify a udev enumerate object
       udev_enumerate_unref(3) — Create, acquire and release a udev enumerate object
       udev_list_entry(3) — Iterate and access udev lists
       udev_list_entry_get_by_name(3) — Iterate and access udev lists
       udev_list_entry_get_name(3) — Iterate and access udev lists
       udev_list_entry_get_next(3) — Iterate and access udev lists
       udev_list_entry_get_value(3) — Iterate and access udev lists
       udev_monitor_enable_receiving(3) — Query and modify device monitor
       udev_monitor_filter_add_match_subsystem_devtype(3) — Modify filters
       udev_monitor_filter_add_match_tag(3) — Modify filters
       udev_monitor_filter_remove(3) — Modify filters
       udev_monitor_filter_update(3) — Modify filters
       udev_monitor_get_fd(3) — Query and modify device monitor
       udev_monitor_get_udev(3) — Query and modify device monitor
       udev_monitor_new_from_netlink(3) — Create, acquire and release a udev monitor object
       udev_monitor_receive_device(3) — Query and modify device monitor
       udev_monitor_ref(3) — Create, acquire and release a udev monitor object
       udev_monitor_set_receive_buffer_size(3) — Query and modify device monitor
       udev_monitor_unref(3) — Create, acquire and release a udev monitor object
       udev_new(3) — Create, acquire and release a udev context object
       udev_ref(3) — Create, acquire and release a udev context object
       udev_unref(3) — Create, acquire and release a udev context object
       udevadm(8) — udev management tool
       ukify(1) — Combine components into a signed Unified Kernel Image for UEFI systems
       user-runtime-dir@.service(5) — System units to start the user manager
       user.conf.d(5) — System and session service manager configuration files
       user@.service(5) — System units to start the user manager
       userdbctl(1) — Inspect users, groups and group memberships

V
       varlinkctl(1) — Introspect with and invoke Varlink services
       veritytab(5) — Configuration for verity block devices

SEE ALSO
       systemd.directives(7)

       This index contains 1156 entries, referring to 395 individual manual pages.

systemd 255																      SYSTEMD.INDEX(7)
