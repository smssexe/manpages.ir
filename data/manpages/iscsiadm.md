ISCSIADM(8)							 Linux Administrator's Manual							   ISCSIADM(8)

NAME
       iscsiadm - open-iscsi administration utility

SYNOPSIS
       iscsiadm	 -m  discoverydb [-hV] [-d debug_level] [-P printlevel] [-I iface -t type -p ip:port [-lD] ] | [ [-p ip:port -t type] [-o operation] [-n name]
       [-v value] [-lD] ]

       iscsiadm -m discovery [-hV] [-d debug_level] [-P printlevel] [-I iface] [-t type] [-p ip:port] [-l]

       iscsiadm -m node [-hV] [-d debug_level] [-P printlevel] [-L all,manual,automatic,onboot] [-W]  [-U  all,manual,automatic,onboot]	 [-S]  [  [-T  target‐
       name -p ip:port -I iface] [-l|-u|-R|-s] ] [ [-o operation] [-n name] [-v value] [-p ip:port] ]

       iscsiadm -m session [-hV] [-d debug_level] [-P printlevel] [-r sessionid|sysfsdir [-R] [-u|-s|-o new] ]

       iscsiadm	 -m  iface [-hV] [-d debug_level] [-P printlevel] [-I ifacename | -H hostno|MAC] [ [-o operation] [-n name] [-v value] ] [ -C ping [-a ip] [-b
       packetsize] [-c count] [-i interval] ]

       iscsiadm -m fw [-d debug_level] [-l] [-W] [-n name] [-v value]

       iscsiadm -m host [-P printlevel] [-H hostno|MAC] [ [-C chap [-x chap_tbl_idx] ] | [-C flashnode [-A portal_type] [-x flashnode_idx] ] | [-C stats] ]  [
       [-o operation] [-n name] [-v value] ]

       iscsiadm -k priority

DESCRIPTION
       The iscsiadm utility is a command-line tool allowing discovery and login to iSCSI targets, as well as access and management of the open-iscsi database.

       Open-iscsi does not use the term node as defined by the iSCSI RFC, where a node is a single iSCSI initiator or target. Open-iscsi uses the term node to
       refer to a portal on a target.

       For  session mode, a session id (sid) is used. The sid of a session can be found by running iscsiadm -m session -P 1. The session id and sysfs path are
       not currently persistent and is partially determined by when the session is setup.

NOTES
       Many of the node and discovery operations require that the iSCSI daemon (iscsid) be running. If running on a system that uses systemd, the  daemon  may
       start up automatically, if enabled, when needed.

       Open-iscsi has two groups of files it needs to store or get access to, while running: the HOMEDIR and the DBROOT. The following describes them:

       Home Directory
	      The home directory for open-iscsi is /etc/iscsi. This is where it keeps it's configuration file (iscsid.conf) and it's initiator name file (ini‐
	      tiatorname.iscsi).

       Database Root Directory
	      The  database  root  directory for open-iscsi is /etc/iscsi. This is where it keeps its flat database files, such as it's list of nodes (see be‐
	      low).

OPTIONS
       -a, --ip=ipaddr
	      ipaddr can be IPv4 or IPv6.

	      This option is only valid for ping submode.

       -A, --portal_type=[ipv4|ipv6]
	      Specify the portal type for the new flash node entry to be created.

	      This option is only valid for flashnode submode of host mode and only with new operation.

       -b, --packetsize=packetsize
	      Specify the ping packetsize.

	      This option is only valid for ping submode.

       -c, --count=count
	      count specifies the number of ping iterations.

	      This option is only valid for ping submode.

       -C, --submode=op
	      Specify the submode for mode. op must be name of submode.

	      Currently iscsiadm supports ping as a submode for iface. For example:

	      iscsiadm -m iface -I ifacename -C ping -a ipaddr -b packetsize -c count -i interval

	      For host, it supports chap, flashnode and stats as submodes. For example:

	      iscsiadm -m host -H hostno -C chap -x chap_tbl_idx -o operation

	      iscsiadm -m host -H hostno -C flashnode -x flashnode_idx -o operation

	      iscsiadm -m host -H hostno -C stats

       -d, --debug=debug_level
	      print debugging information. Valid values for debug_level are 0 to 8.

       -h, --help
	      display help text and exit

       -H, --host=[hostno|MAC]
	      The host argument specifies the SCSI host to use for the operation. It can be the scsi host number assigned to the host  by  the	kernel's  scsi
	      layer, or the MAC address of a scsi host.

       -i, --interval=interval
	      interval specifies the delay between two ping iterations.

	      This option is only valid for ping submode.

       -I, --interface=[iface]
	      The  interface  argument specifies the iSCSI interface to use for the operation.	iSCSI interfaces (iface) are defined in /etc/iscsi/ifaces. For
	      hardware iSCSI (e.g. qla4xxx) the iface configuration must have the hardware address  (iface.hwaddress  =	 port's	 MAC  address)	and  the  dri‐
	      ver/transport_name  (iface.transport_name). The iface's name is then the filename of the iface configuration. For software iSCSI, the iface con‐
	      figuration must have either the hardware address (iface.hwaddress), or the network layer's interface name	 (iface.net_ifacename),	 and  it  must
	      have the driver/transport_name.

	      The  available  drivers/iscsi_transports	are tcp (software iSCSI over TCP/IP), iser (software iSCSI over InfiniBand), qla4xxx (Qlogic 4XXXX and
	      82XXX HBAs), cxgb3i and cxgb4i (Chelsio T3 and T4 adapters), bnx2i (QLogic Netextreme II adapters), be2iscsi (Emulex 10G adapter), qedi  (QLogic
	      QEDI 25/40/100Gb adapter), and ocs (Emulex One Connect storage).	Some of these are considered experimental, as they are not fully tested.

	      The  hwaddress  is the MAC address or for software iSCSI it may be the special value default which directs the initiator to not bind the session
	      to a specific hardware resource and instead allow the network or InfiniBand layer to decide what to do. There is no need to create an iface con‐
	      figuration with the default behavior. If you do not specify an iface, then the default behavior is used.

	      As mentioned above there is a special iface name default. There are others which do not bind the session to a specific card,  but	 instead  bind
	      the session to the transport: iser, cxgb3i, cxgb4i, and bnx2i.

	      In discovery mode multiple interfaces can be specified by passing in multiple -I/--interface instances. For example:

	      sh# iscsiadm -m discoverydb -t st -p ip:port -I iface0 -I iface2 --discover

	      Will direct iscsiadm to setup the node db to create records which will create sessions through the two interfaces passed in.

	      In node mode, only a single interface is supported in each call to iscsiadm.

	      This option is valid for discovery, node and iface modes.

       -k, --killiscsid=[priority]
	      Currently	 priority must be zero. This will immediately stop all iscsid operations and shutdown iscsid. It does not logout any sessions. Running
	      this command is the same as doing killall iscsid. Neither should normally be used, because if iscsid is doing error recovery or if there	is  an
	      error while iscsid is not running, the system may not be able to recover.	 This command and iscsid's SIGTERM handling are experimental.

       -D, --discover
	      Discover targets using the discovery record with the recid matching the the discovery type and portal passed in. If there is no matching record,
	      it will be created using the iscsid.conf discovery settings.  This must be passed in to discoverydb mode to instruct iscsiadm to perform discov‐
	      ery.

	      This option is only valid for SendTargets discovery mode.

       -l, --login
	      For node and fw modes, login to a specified record. For discovery mode, login to all discovered targets.

	      This  option is only valid for discovery, node, and fw modes.  For fw mode only, name and value pairs can optionally be passed in, so that those
	      values get used for the sessions created. In this case, no op is needed, since update is assumed.

       -L, --loginall=[all|manual|automatic|onboot]
	      For node mode, login to all sessions with the node or conn startup values passed in or all running session, except ones marked onboot, if all is
	      passed in.

	      This option is only valid for node mode (it is valid but not functional for session mode).

       -W, ---no_wait
	      In node, discovery, or fw (firmware) mode, do not wait for a response from the target(s).	 This means that success will be returned if the  com‐
	      mand  is	able to send the login requests, whether or not they succeed. In this case, it will be up to the caller to poll for success (i.e. ses‐
	      sion creation).

       -m, --mode op
	      specify the mode. op must be one of discovery, discoverydb, node, fw, host, iface or session.

	      If no other options are specified: for discovery, discoverydb and node mode, all of their respective records are displayed;  for	session	 mode,
	      all  active sessions and connections are displayed; for fw mode, all boot firmware values are displayed; for host mode, all iSCSI hosts are dis‐
	      played; and for iface mode, all interfaces setup in /etc/iscsi/ifaces are displayed.

       -n, --name=name
	      In node mode, specify a field name in a record. In flashnode submode of host mode, specify name of the flash node parameter.

	      For use with the update operator.

       -o, --op=op
	      Specifies a database operator op. op must be one of new, delete, update, show or nonpersistent.

	      For iface mode, apply and applyall are also applicable.

	      For flashnode submode of host mode, login and logout are also applicable.

	      This option is valid for all modes except fw. Delete should not be used on a running session. If it is iscsiadm will stop the session  and  then
	      delete the record.

	      An  op  of new creates a new database record for a given object. In node mode, the recid is the target name and portal (IP:port). In iface mode,
	      the recid is the iface name. In discovery mode, the recid is the portal and discovery type.

	      In session mode, the new operation logs in a new session using the same node database and iface information as the specified session.

	      In discovery mode, if the recid and new operation is passed in, but the --discover argument is not passed in, then iscsiadm will only  create  a
	      discovery record (it will not perform discovery). If the --discover argument is passed in with the portal and discovery type, then iscsiadm will
	      create the discovery record if needed, and it will create records for portals returned by the target that do not yet have a node DB record.

	      Setting  op  to  delete  deletes the specified recid. In discovery mode, if iscsiadm is performing discovery, it will delete records for portals
	      that are no longer returned.

	      Setting op to update will update the recid with name to the specified value. In discovery mode, if iscsiadm is performing discovery  the	recid,
	      name  and	 value	arguments  are	not  needed. The update operation will operate on the portals returned by the target, and will update the node
	      records with information from the configuration file and command line.

	      The op value of show is the default behaviour for node, discovery and iface mode. It is also used when there are no commands passed into session
	      mode and a running sid is passed in.  If name and value are passed in, they are currently ignored in show mode.

	      An op value of nonpersistent instructs iscsiadm to not manipulate the node DB.

	      An op value of apply will cause the network settings to take effect on the specified iface.

	      An op value of applyall will cause the network settings to take effect on all the ifaces whose MAC address or host number matches	 that  of  the
	      specific host.

	      An op value of login will log into the specified flash node entry.

	      An op value of logout does the logout from the given flash node entry.

       -p, --portal=ip[:port]
	      Use target portal with IP address ip and port port. If port is not passed in the default value of 3260 is used.

	      IPv6 addresses can be specified as [ddd.ddd.ddd.ddd]:port or ddd.ddd.ddd.ddd.

	      Hostnames can also be used for the ip argument.

	      This option is only valid for discovery, or for node operations with the new operator.

	      This  should  be	used along with --target in node mode, to specify what the open-iscsi documents refer to as a node or node record. Note: open-
	      iscsi's use of the word node, does not match the iSCSI RFC's iSCSI Node term.

       -P, --print=printlevel
	      If in node mode print nodes in tree format. If in session mode print sessions in tree format. If in discovery mode print the nodes in tree  for‐
	      mat.

       -T, --targetname=targetname
	      Use target targetname.

	      This  should  be	used along with --portal in node mode, to specify what the open-iscsi documents refer to as a node or node record. Note: open-
	      iscsi's use of the word node, does not match the iSCSI RFC's iSCSI Node term.

       -r, --sid=sid | sysfsdir
	      Use session ID sid. The session ID of a session can be found from running iscsiadm in session mode with the --info argument.

	      Instead of a session ID, a sysfs path containing the session  can	 be  used.   For  example  using  one  of  the	following:  /sys/devices/plat‐
	      form/hostH/sessionS/targetH:B:I/H:B:I:L, /sys/devices/platform/hostH/sessionS/targetH:B:I, or /sys/devices/platform/hostH/sessionS, for the sys‐
	      fsdir argument would result in the session with session ID S to be used.

	      sid | sysfsdir is only required for session mode.

       -R, --rescan
	      In session mode, if sid is also passed in, rescan the session.  If no sid has been passed in rescan all running sessions.

	      In node mode, rescan a session running through the target, portal, iface tuple passed in.

       -s, --stats
	      Display session statistics.  This option when used with host mode, displays host statistics.

       -S, --show
	      When displaying records, do not hide masked values, such as the CHAP secret (password).

	      This option is only valid for node and session mode.

       -t, --type=type
	      type must be sendtargets (or abbreviated as st), isns (if enabled), or fw. See the DISCOVERY TYPES section.

	      This option is only valid for discovery mode.

       -u, --logout
	      Logout for the specified record.

	      This option is only valid for node and session mode.

       -U, --logoutall=[all,manual,automatic|onboot]
	      Logout of all sessions with the node or conn startup values passed in or all running sessions, except ones marked onboot, if all is passed in.

	      This option is only valid for node mode (it is valid but not functional for session mode).

       -v, --value=value
	      Specify a value for use with the update operator, or for firmware login mode.

	      This option is only valid for node mode and flashnode submode of host mode.

       -V, --version
	      Display version and exit.

       -x, --index=index
	      Specify the index of the entity to operate on.

	      This option is only valid for chap and flashnode submodes of host mode.

DISCOVERY TYPES
       iSCSI defines 3 discovery types: SendTargets, SLP, and iSNS.  SLP is not widely supported, and not supported by this pacakge.  SNS supported depends on
       build options, but is enabled by default.

       A  special discovery type called fw (for firmware) is also supported, for discovering firmware interfaces, and populating the interface database in the
       process.

       SendTargets
	      A native iSCSI protocol which allows each iSCSI target to send a list of available targets to the initiator.

       iSNS   iSNS (Internet Storage Name Service) records information about storage volumes within a larger network. To utilize iSNS, pass  the  address  and
	      optionally the port of the iSNS server to do discovery to.

       fw     Firmware	mode.	Several NICs and systems contain a mini iSCSI initiator which can be used for boot. To get the values used for boot the fw op‐
	      tion can be used.	 Doing fw discovery does not store persistent records in the node or discovery DB, because the values are stored in  the  sys‐
	      tem's or NIC's resource.

	      Performing  fw  discovery	 will  print the portals, like with other discovery methods. To see other settings like CHAP values and initiator set‐
	      tings, like you would in node mode, run iscsiadm -m fw.

EXIT STATUS
       On success 0 is returned. On error one of the return codes below will be returned.

       Commands that operate on multiple objects (sessions, records, etc), iscsiadm/iscsistart will return the first error that is encountered.	 iscsiadm/isc‐
       sistart will attempt to execute the operation on the objects it can. If no objects are found ISCSI_ERR_NO_OBJS_FOUND is returned.

       0      ISCSI_SUCCESS - command executed successfully.

       1      ISCSI_ERR - generic error code.

       2      ISCSI_ERR_SESS_NOT_FOUND - session could not be found.

       3      ISCSI_ERR_NOMEM - could not allocate resource for operation.

       4      ISCSI_ERR_TRANS - connect problem caused operation to fail.

       5      ISCSI_ERR_LOGIN - generic iSCSI login failure.

       6      ISCSI_ERR_IDBM - error accessing/managing iSCSI DB.

       7      ISCSI_ERR_INVAL - invalid argument.

       8      ISCSI_ERR_TRANS_TIMEOUT - connection timer expired while trying to connect.

       9      ISCSI_ERR_INTERNAL - generic internal iscsid/kernel failure.

       10     ISCSI_ERR_LOGOUT - iSCSI logout failed.

       11     ISCSI_ERR_PDU_TIMEOUT - iSCSI PDU timed out.

       12     ISCSI_ERR_TRANS_NOT_FOUND - iSCSI transport module not loaded in kernel or iscsid.

       13     ISCSI_ERR_ACCESS - did not have proper OS permissions to access iscsid or execute iscsiadm command.

       14     ISCSI_ERR_TRANS_CAPS - transport module did not support operation.

       15     ISCSI_ERR_SESS_EXISTS - session is logged in.

       16     ISCSI_ERR_INVALID_MGMT_REQ - invalid IPC MGMT request.

       17     ISCSI_ERR_ISNS_UNAVAILABLE - iSNS service is not supported.

       18     ISCSI_ERR_ISCSID_COMM_ERR - a read/write to iscsid failed.

       19     ISCSI_ERR_FATAL_LOGIN - fatal iSCSI login error.

       20     ISCSI_ERR_ISCSID_NOTCONN - could not connect to iscsid.

       21     ISCSI_ERR_NO_OBJS_FOUND - no records/targets/sessions/portals found to execute operation on.

       22     ISCSI_ERR_SYSFS_LOOKUP - could not lookup object in sysfs.

       23     ISCSI_ERR_HOST_NOT_FOUND - could not lookup host.

       24     ISCSI_ERR_LOGIN_AUTH_FAILED - login failed due to authorization failure.

       25     ISCSI_ERR_ISNS_QUERY - iSNS query failure.

       26     ISCSI_ERR_ISNS_REG_FAILED - iSNS registration/deregistration failed.

       27     ISCSI_ERR_OP_NOT_SUPP - operation not support

       28     ISCSI_ERR_BUSY - device or resource in use

       29     ISCSI_ERR_AGAIN - operation failed, but retrying later may succeed

       30     ISCSI_ERR_UNKNOWN_DISCOVERY_TYPE - unknown discovery type

       31     ISCSI_ERR_CHILD_TERMINATED - child process terminated

       32     ISCSI_ERR_SESSION_NOT_CONNECTED - session likely not connected

EXAMPLES
       Discover targets at a given IP address:

	      sh# iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.10 --discover

       Login, must use a node record id found by the discovery:

	      sh# iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260 --login

       Logout:

	      sh# iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260 --logout

       List node records:

	      sh# iscsiadm --mode node

       Display all data for a given node record:

	      sh# iscsiadm --mode node --targetname iqn.2001-05.com.doe:test --portal 192.168.1.1:3260

       List all sessions:

	      sh# iscsiadm --mode session

       List all sessions in tree format:

	      sh# iscsiadm --mode session  --print

FILES
       /etc/iscsi/iscsid.conf
	      The configuration file read by iscsid and iscsiadm on startup.

       /etc/iscsi/initiatorname.iscsi
	      The file containing the iSCSI InitiatorName and InitiatorAlias read by iscsid and iscsiadm on startup.

       /etc/iscsi/nodes/
	      This directory contains the nodes with their targets.

       /etc/iscsi/send_targets
	      This directory contains the portals.

SEE ALSO
       iscsid(8)

AUTHORS
       Open-iSCSI project <http://www.open-iscsi.com/>
       Alex Aizman <itn780@yahoo.com>
       Dmitry Yusupov <dmitry_yus@yahoo.com>

									   Mar 2022								   ISCSIADM(8)
