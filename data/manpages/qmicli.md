QMICLI(1)								 User Commands								     QMICLI(1)

NAME
       qmicli - Control QMI devices

DESCRIPTION
   Usage:
	      qmicli [OPTION?] - Control QMI devices

   Help Options:
       -h, --help
	      Show help options

       --help-all
	      Show all help options

       --help-dms
	      Show Device Management Service options

       --help-nas
	      Show Network Access Service options

       --help-wds
	      Show Wireless Data Service options

       --help-pbm
	      Show Phonebook Management options

       --help-pdc
	      Show platform device configurations options

       --help-uim
	      Show User Identity Module options

       --help-sar
	      Show Specific Absorption Rate options

       --help-wms
	      Show Wireless Messaging Service options

       --help-wda
	      Show Wireless Data Administrative options

       --help-voice
	      Show Voice Service options

       --help-loc
	      Show location options

       --help-qos
	      Show Quality of Service options

       --help-gas
	      Show General Application Service options

       --help-gms
	      Show General Modem Service options

       --help-dsd
	      Show Data System Determination options

       --help-dpm
	      Show Data Port Mapper Service options

       --help-fox
	      Show Foxconn Modem Service options

       --help-atr
	      Show AT Relay Service options

       --help-imsp
	      Show IP Multimedia Subsystem Presence Service options

       --help-imsa
	      Show IP Multimedia Subsystem Application Service options

       --help-ims
	      Show IP Multimedia Subsystem Settings Service options

       --help-link-management
	      Show link management specific options

       --help-qmiwwan
	      Show qmi_wwan driver specific options

   DMS options:
       --dms-get-ids
	      Get IDs

       --dms-get-capabilities
	      Get capabilities

       --dms-get-manufacturer
	      Get manufacturer

       --dms-get-model
	      Get model

       --dms-get-revision
	      Get revision

       --dms-get-msisdn
	      Get MSISDN

       --dms-get-power-state
	      Get power state

       --dms-uim-set-pin-protection=[(PIN|PIN2),(disable|enable),(current PIN)]
	      Set PIN protection in the UIM

       --dms-uim-verify-pin=[(PIN|PIN2),(current PIN)]
	      Verify PIN

       --dms-uim-unblock-pin=[(PIN|PIN2),(PUK),(new PIN)]
	      Unblock PIN

       --dms-uim-change-pin=[(PIN|PIN2),(old PIN),(new PIN)]
	      Change PIN

       --dms-uim-get-pin-status
	      Get PIN status

       --dms-uim-get-iccid
	      Get ICCID

       --dms-uim-get-imsi
	      Get IMSI

       --dms-uim-get-state
	      Get UIM State

       --dms-uim-get-ck-status=[(pn|pu|pp|pc|pf)]
	      Get CK Status

       --dms-uim-set-ck-protection=[(pn|pu|pp|pc|pf),(disable),(key)]
	      Disable CK protection

       --dms-uim-unblock-ck=[(pn|pu|pp|pc|pf),(key)]
	      Unblock CK

       --dms-get-hardware-revision
	      Get the HW revision

       --dms-get-operating-mode
	      Get the device operating mode

       --dms-set-operating-mode=[(Operating mode)]
	      Set the device operating mode

       --dms-get-time
	      Get the device time

       --dms-get-prl-version
	      Get the PRL version

       --dms-get-activation-state
	      Get the state of the service activation

       --dms-activate-automatic=[Activation Code]
	      Request automatic service activation

       --dms-activate-manual=[SPC,SID,MDN,MIN]
	      Request manual service activation

       --dms-get-user-lock-state
	      Get the state of the user lock

       --dms-set-user-lock-state=[(disable|enable),(current lock code)]
	      Set the state of the user lock

       --dms-set-user-lock-code=[(old lock code),(new lock code)]
	      Change the user lock code

       --dms-read-user-data
	      Read user data

       --dms-write-user-data=[(User data)]
	      Write user data

       --dms-read-eri-file
	      Read ERI file

       --dms-restore-factory-defaults=[(Service Programming Code)]
	      Restore factory defaults

       --dms-validate-service-programming-code=[(Service Programming Code)]
	      Validate the Service Programming Code

       --dms-set-firmware-id
	      Set firmware id

       --dms-get-band-capabilities
	      Get band capabilities

       --dms-get-factory-sku
	      Get factory stock keeping unit

       --dms-list-stored-images
	      List stored images

       --dms-select-stored-image=[modem#,pri#] where # is the index
	      Select stored image

       --dms-delete-stored-image=[modem#|pri#] where # is the index
	      Delete stored image

       --dms-get-firmware-preference
	      Get firmware preference

       --dms-set-firmware-preference=["key=value,..."]
	      Set firmware preference (required keys: firmware-version, config-version, carrier; optional keys: modem-storage-index, override-download=yes)

       --dms-get-boot-image-download-mode
	      Get boot image download mode

       --dms-set-boot-image-download-mode=[normal|boot-and-recovery]
	      Set boot image download mode

       --dms-get-software-version
	      Get software version

       --dms-set-fcc-authentication
	      Set FCC authentication

       --dms-get-supported-messages
	      Get supported messages

       --dms-hp-change-device-mode=[fastboot]
	      Change device mode (HP specific)

       --dms-swi-get-current-firmware
	      Get Current Firmware (Sierra Wireless specific)

       --dms-swi-get-usb-composition
	      Get current and supported USB compositions (Sierra Wireless specific)

       --dms-swi-set-usb-composition=[#]
	      Set USB composition (Sierra Wireless specific)

       --dms-foxconn-change-device-mode=[fastboot-ota|fastboot-online]
	      Change device mode (Foxconn specific)

       --dms-foxconn-get-firmware-version=[firmware-mcfg-apps|firmware-mcfg|apps]
	      Get firmware version (Foxconn specific)

       --dms-foxconn-set-fcc-authentication=[magic]
	      Set FCC authentication (Foxconn specific)

       --dms-foxconn-set-fcc-authentication-v2=[magic-string,magic-number]
	      Set FCC authentication (Foxconn specific, v2)

       --dms-get-mac-address=[wlan|bt]
	      Get default MAC address

       --dms-reset
	      Reset the service state

       --dms-noop
	      Just allocate or release a DMS client. Use with `--client-no-release-cid' and/or `--client-cid'

   NAS options:
       --nas-get-signal-strength
	      Get signal strength

       --nas-get-signal-info
	      Get signal info

       --nas-get-tx-rx-info=[(Radio Interface)]
	      Get TX/RX info

       --nas-get-home-network
	      Get home network

       --nas-get-serving-system
	      Get serving system

       --nas-get-system-info
	      Get system info

       --nas-get-technology-preference
	      Get technology preference

       --nas-get-preferred-networks
	      Get preferred networks

       --nas-set-preferred-networks=[[MCCMNC,access_tech],...]
	      Set preferred networks list

       --nas-get-system-selection-preference
	      Get system selection preference

       --nas-set-system-selection-preference=[cdma-1x|cdma-1xevdo|gsm|umts|lte|td-scdma][,[automatic|manual=MCCMNC]]
	      Set system selection preference

       --nas-network-scan
	      Scan networks

       --nas-get-cell-location-info
	      Get Cell Location Info

       --nas-force-network-search
	      Force network search

       --nas-get-operator-name
	      Get operator name data

       --nas-get-plmn-name=[mccmnc]
	      Get plmn name data

       --nas-get-lte-cphy-ca-info
	      Get LTE Cphy CA Info

       --nas-get-rf-band-info
	      Get RF Band Info

       --nas-get-drx
	      Get DRX

       --nas-get-supported-messages
	      Get supported messages

       --nas-swi-get-status
	      Get status ((Sierra Wireless specific)

       --nas-reset
	      Reset the service state

       --nas-noop
	      Just allocate or release a NAS client. Use with `--client-no-release-cid' and/or `--client-cid'

   WDS options:
       --wds-start-network=["key=value,..."]
	      Start network (allowed keys: apn, 3gpp-profile, 3gpp2-profile, auth (PAP|CHAP|BOTH), username, password, autoconnect=yes, ip-type (4|6))

       --wds-follow-network
	      Follow the network status until disconnected. Use with `--wds-start-network'

       --wds-stop-network=[Packet data handle] OR [disable-autoconnect]
	      Stop network

       --wds-get-current-settings
	      Get current settings

       --wds-get-packet-service-status
	      Get packet service status

       --wds-get-packet-statistics
	      Get packet statistics

       --wds-get-data-bearer-technology
	      Get data bearer technology

       --wds-get-current-data-bearer-technology
	      Get current data bearer technology

       --wds-go-dormant
	      Make the active data connection go dormant

       --wds-go-active
	      Make the active data connection go active

       --wds-get-dormancy-status
	      Get the dormancy status of the active data connection

       --wds-create-profile=["(3gpp|3gpp2)[,key=value,...]"]
	      Create  new  profile  using  first  available profile index (optional keys: name, apn, pdp-type (IP|PPP|IPV6|IPV4V6), auth (NONE|PAP|CHAP|BOTH),
	      username, password, context-num, no-roaming=yes, disabled=yes)

       --wds-swi-create-profile-indexed=["(3gpp|3gpp2),#[,key=value,...]"]
	      Create new profile at specified profile index [Sierra  Wireless  specific]  (optional  keys:  name,  apn,	 pdp-type  (IP|PPP|IPV6|IPV4V6),  auth
	      (NONE|PAP|CHAP|BOTH), username, password, context-num, no-roaming=yes, disabled=yes)

       --wds-modify-profile=["(3gpp|3gpp2),#,key=value,..."]
	      Modify  existing	profile	 (optional keys: name, apn, pdp-type (IP|PPP|IPV6|IPV4V6), auth (NONE|PAP|CHAP|BOTH), username, password, context-num,
	      no-roaming=yes, disabled=yes)

       --wds-delete-profile=[(3gpp|3gpp2),#]
	      Delete existing profile

       --wds-get-profile-list=[3gpp|3gpp2]
	      Get profile list

       --wds-get-default-profile-number=[3gpp|3gpp2]
	      Get default profile number

       --wds-set-default-profile-number=[(3gpp|3gpp2),#]
	      Set default profile number

       --wds-get-default-settings=[3gpp|3gpp2]
	      Get default settings

       --wds-get-autoconnect-settings
	      Get autoconnect settings

       --wds-set-autoconnect-settings=[(enabled|disabled|paused)[,(roaming-allowed|home-only)]]
	      Set autoconnect settings (roaming settings optional)

       --wds-get-supported-messages
	      Get supported messages

       --wds-reset
	      Reset the service state

       --wds-bind-data-port=[a2-mux-rmnet0-7|#]
	      Bind data port to controller device to be used with `--client-no-release-cid'

       --wds-bind-mux-data-port=["key=value,..."]
	      Bind qmux data port to controller device (allowed keys: mux-id, ep-type (undefined|hsusb|pcie|embedded|bam-dmux), ep-iface-number)  to  be  used
	      with `--client-no-release-cid'

       --wds-set-ip-family=[4|6]
	      Set IP family

       --wds-get-channel-rates
	      Get channel data rates

       --wds-get-lte-attach-parameters
	      Get LTE attach parameters

       --wds-get-max-lte-attach-pdn-num
	      Get the maximum number of LTE attach PDN

       --wds-get-lte-attach-pdn-list
	      Get the list of LTE attach PDN

       --wds-set-lte-attach-pdn-list=[#,#,...]
	      Set the list of LTE attach PDN

       --wds-noop
	      Just allocate or release a WDS client. Use with `--client-no-release-cid' and/or `--client-cid'

   PBM options:
       --pbm-get-all-capabilities
	      Get all phonebook capabilities

       --pbm-noop
	      Just allocate or release a PBM client. Use with `--client-no-release-cid' and/or `--client-cid'

   PDC options:
       --pdc-list-configs=[(platform|software)]
	      List all configs

       --pdc-delete-config=[(platform|software),ConfigId]
	      Delete config

       --pdc-activate-config=[(platform|software),ConfigId]
	      Activate config

       --pdc-deactivate-config=[(platform|software),ConfigId]
	      Deactivate config

       --pdc-load-config=[Path to config]
	      Load config to device

       --pdc-monitor-refresh
	      Watch for refresh indications

       --pdc-noop
	      Just allocate or release a PDC client. Use with `--client-no-release-cid' and/or `--client-cid'

   UIM options:
       --uim-set-pin-protection=[(PIN1|PIN2|UPIN),(disable|enable),(current PIN)]
	      Set PIN protection

       --uim-verify-pin=[(PIN1|PIN2|UPIN),(current PIN)]
	      Verify PIN

       --uim-unblock-pin=[(PIN1|PIN2|UPIN),(PUK),(new PIN)]
	      Unblock PIN

       --uim-change-pin=[(PIN1|PIN2|UPIN),(old PIN),(new PIN)]
	      Change PIN

       --uim-read-transparent=[0xNNNN,0xNNNN,...]
	      Read a transparent file given the file path

       --uim-get-file-attributes=[0xNNNN,0xNNNN,...]
	      Get the attributes of a given file

       --uim-read-record=["key=value,..."]
	      Read a record from given file (allowed keys: record-number, record-length, file ([0xNNNN-0xNNNN,...])

       --uim-get-card-status
	      Get card status

       --uim-get-supported-messages
	      Get supported messages

       --uim-sim-power-on=[(slot number)]
	      Power on SIM card

       --uim-sim-power-off=[(slot number)]
	      Power off SIM card

       --uim-change-provisioning-session=["key=value,..."]
	      Change provisioning session (allowed keys: session-type, activate, slot, aid)

       --uim-get-slot-status
	      Get slot status

       --uim-switch-slot=[(slot number)]
	      Switch active physical slot

       --uim-monitor-slot-status
	      Watch for slot status indications

       --uim-reset
	      Reset the service state

       --uim-monitor-refresh-file=[0xNNNN,0xNNNN,...]
	      Watch for REFRESH events for given file paths

       --uim-monitor-refresh-all
	      Watch for REFRESH events for any file

       --uim-get-configuration
	      Get personalization status of the modem

       --uim-depersonalization=[(feature),(operation),(control key)[,(slot number)]]
	      Deactivates or unblocks personalization feature

       --uim-remote-unlock=[XX:XX:...]
	      Updates the SimLock configuration data

       --uim-noop
	      Just allocate or release a UIM client. Use with `--client-no-release-cid' and/or `--client-cid'

   SAR options:
       --sar-rf-get-state
	      Get RF state

       --sar-rf-set-state=[(state number)]
	      Set RF state.

       --sar-noop
	      Just allocate or release a SAR client. Use with `--client-no-release-cid' and/or `--client-cid'

   WMS options:
       --wms-get-supported-messages
	      Get supported messages

       --wms-get-routes
	      Get SMS route information

       --wms-set-routes=["key=value,..."]
	      Set SMS route information (keys: type, class, storage, receipt-action)

       --wms-reset
	      Reset the service state

       --wms-noop
	      Just allocate or release a WMS client. Use with `--client-no-release-cid' and/or `--client-cid'

   WDA options:
       --wda-set-data-format=["key=value,..."]
	      Set  data	 format (allowed keys: link-layer-protocol (802-3|raw-ip), ul-protocol (disabled|tlp|qc-ncm|mbim|rndis|qmap|qmapv5), dl-protocol (dis‐
	      abled|tlp|qc-ncm|mbim|rndis|qmap|qmapv5),	 dl-datagram-max-size,	dl-max-datagrams,  ep-type  (undefined|hsusb|pcie|embedded),  ep-iface-number,
	      ul-datagram-max-size, ul-max-datagrams)

       --wda-get-data-format=["key=value,..."]
	      Get data format (allowed keys: ep-type (undefined|hsusb|pcie|embedded), ep-iface-number); also allows empty key list

       --wda-get-supported-messages
	      Get supported messages

       --wda-noop
	      Just allocate or release a WDA client. Use with `--client-no-release-cid' and/or `--client-cid'

   VOICE options:
       --voice-get-config
	      Get Voice service configuration

       --voice-get-supported-messages
	      Get supported messages

       --voice-noop
	      Just allocate or release a VOICE client. Use with `--client-no-release-cid' and/or `--client-cid'

   LOC options:
       --loc-session-id=[ID]
	      Session ID for the LOC session

       --loc-start
	      Start location gathering

       --loc-stop
	      Stop location gathering

       --loc-get-position-report
	      Get position reported by the location module

       --loc-get-gnss-sv-info
	      Show GNSS space vehicle info

       --loc-timeout=[SECS]
	      Maximum time to wait for information in `--loc-get-position-report' and `--loc-get-gnss-sv-info' (default 30s)

       --loc-follow-position-report
	      Follow all position updates reported by the location module indefinitely

       --loc-follow-gnss-sv-info
	      Follow all GNSS space vehicle info updates reported by the location module indefinitely

       --loc-follow-nmea
	      Follow all NMEA trace updates reported by the location module indefinitely

       --loc-delete-assistance-data
	      Delete positioning assistance data

       --loc-get-nmea-types
	      Get list of enabled NMEA traces

       --loc-set-nmea-types=[type1|type2|type3...]
	      Set list of enabled NMEA traces

       --loc-get-operation-mode
	      Get operation mode

       --loc-set-operation-mode=[default|msb|msa|standalone|cellid|wwan]
	      Set operation mode

       --loc-get-engine-lock
	      Get engine lock status

       --loc-set-engine-lock=[none|mi|mt|all]
	      Set engine lock status

       --loc-noop
	      Just allocate or release a LOC client. Use with `--client-no-release-cid' and/or `--client-cid'

   QoS options:
       --qos-get-flow-status=[QoS ID]
	      Get QoS flow status

       --qos-get-network-status
	      Gets the network status

       --qos-swi-read-data-stats=[APN ID]
	      Read data stats (Sierra Wireless specific)

       --qos-reset
	      Reset the service state

       --qos-noop
	      Just allocate or release a QOS client. Use with `--client-no-release-cid' and/or `--client-cid'

   GAS options:
       --gas-dms-set-usb-composition=[pid]
	      Sets the USB composition

       --gas-dms-get-usb-composition
	      Gets the current USB composition

       --gas-dms-get-firmware-list
	      Gets the list of stored firmware

       --gas-dms-get-active-firmware
	      Gets the currently active firmware

       --gas-dms-set-active-firmware=[index]
	      Sets the active firmware index

       --gas-noop
	      Just allocate or release a GAS client. Use with `--client-no-release-cid' and/or `--client-cid'

   GMS options:
       --gms-test-get-value
	      Gets test value

       --gms-test-set-value=[mandatory-value][,[optional-value]]
	      Sets test value

       --gms-noop
	      Just allocate or release a GMS client. Use with `--client-no-release-cid' and/or `--client-cid'

   DSD options:
       --dsd-get-apn-info=[(type)]
	      Gets the settings associated to a given APN type

       --dsd-set-apn-type=[(name), (type1|type2|type3...)]
	      Sets the types associated to a given APN name

       --dsd-get-system-status
	      Gets system status

       --dsd-noop
	      Just allocate or release a DSD client. Use with `--client-no-release-cid' and/or `--client-cid'

   DPM options:
       --dpm-open-port=["key=value,..."]
	      Open   port   (allowed-keys:   ctrl-ep-type,  ctrl-ep-iface-number,  ctrl-port-name,  hw-data-ep-type,  hw-data-ep-iface-number,	hw-data-rx-id,
	      hw-data-tx-id, sw-data-ep-type, sw-data-ep-iface-number, sw-data-port-name)

       --dpm-close-port
	      Close port

       --dpm-noop
	      Just allocate or release a DPM client. Use with `--client-no-release-cid' and/or `--client-cid'

   FOX options:
       --fox-get-firmware-version=[firmware-mcfg-apps|firmware-mcfg|apps]
	      Get firmware version

       --fox-noop
	      Just allocate or release a FOX client. Use with `--client-no-release-cid' and/or `--client-cid'

   ATR options:
       --atr-send=[AT command]
	      Send an AT command and wait for the reply

       --atr-send-only=[AT command]
	      Send an AT command without waiting for the reply

       --atr-monitor
	      Watch for unsolicited indications

       --atr-noop
	      Just allocate or release an ATR client. Use with `--client-no-release-cid' and/or `--client-cid'

   IMSP options:
       --imsp-get-enabler-state
	      Get IMSP enabler state

       --imsp-noop
	      Just allocate or release a IMSP client. Use with `--client-no-release-cid' and/or `--client-cid'

   IMSA options:
       --imsa-get-ims-registration-status
	      Get IMS registration status

       --imsa-get-ims-services-status
	      Get IMS services status

       --imsa-noop
	      Just allocate or release a IMSA client. Use with `--client-no-release-cid' and/or `--client-cid'

   IMS options:
       --ims-get-ims-services-enabled-setting
	      Get IMS Services Enabled Setting

       --ims-noop
	      Just allocate or release a IMS client. Use with `--client-no-release-cid' and/or `--client-cid'

   Link management options:
       --link-list=[IFACE]
	      List links created from a given interface

       --link-add=[iface=IFACE,prefix=PREFIX[,mux-id=N][,flags=FLAGS]]
	      Create new network interface link

       --link-delete=[link-iface=IFACE][,[mux-id=N]]
	      Delete a given network interface link

       --link-delete-all=[IFACE]
	      Delete all network interface links from the given interface

   qmi_wwan specific options:
       -w, --get-wwan-iface
	      Get the associated WWAN iface name

       -e, --get-expected-data-format
	      Get the expected data format in the WWAN iface

       -E, --set-expected-data-format=[802-3|raw-ip|qmap-pass-through]
	      Set the expected data format in the WWAN iface

   Application Options:
       -d, --device=[PATH|URI]
	      Specify device path or QRTR URI (e.g. qrtr://0)

       --get-service-version-info
	      Get service version info

       --device-set-instance-id=[Instance ID]
	      Set instance ID

       --device-open-version-info
	      Run version info check when opening device

       --device-open-sync
	      Run sync operation when opening device

       -p, --device-open-proxy
	      Request to use the 'qmi-proxy' proxy

       --device-open-qmi
	      Open a cdc-wdm device explicitly in QMI mode

       --device-open-mbim
	      Open a cdc-wdm device explicitly in MBIM mode

       --device-open-auto
	      Open a cdc-wdm device in either QMI or MBIM mode (default)

       --device-open-net=[net-802-3|net-raw-ip|net-qos-header|net-no-qos-header]
	      Open device with specific link protocol and QoS flags

       --client-cid=[CID]
	      Use the given CID, don't allocate a new one

       --client-no-release-cid
	      Do not release the CID when exiting

       -v, --verbose
	      Run action with verbose logs, including the debug ones

       --verbose-full
	      Run action with verbose logs, including the debug ones and personal info

       --silent
	      Run action with no logs; not even the error/warning ones

       -V, --version
	      Print version

COPYRIGHT
       Copyright © 2012-2023 Aleksander Morgado License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl-2.0.html>
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       The full documentation for qmicli is maintained as a Texinfo manual.  If the info and qmicli programs are properly installed at your site, the command

	      info qmicli

       should give you access to the complete manual.

qmicli 1.35.2								  March 2024								     QMICLI(1)
