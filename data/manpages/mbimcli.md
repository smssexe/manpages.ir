MBIMCLI(1)								 User Commands								    MBIMCLI(1)

NAME
       mbimcli - Control MBIM devices

DESCRIPTION
   Usage:
	      mbimcli [OPTION?] - Control MBIM devices

   Help Options:
       -h, --help
	      Show help options

       --help-all
	      Show all help options

       --help-basic-connect
	      Show Basic Connect Service options

       --help-phonebook
	      Show Phonebook Service options

       --help-dss
	      Show Device Service Stream options

       --help-ms-firmware-id
	      Show Microsoft Firmware ID Service options

       --help-ms-host-shutdown
	      Show Microsoft Host Shutdown Service options

       --help-ms-sar
	      Show Microsoft SAR Service options

       --help-atds
	      Show AT&T Device Service options

       --help-intel-firmware-update
	      Show Intel Firmware Update Service options

       --help-ms-basic-connect-extensions
	      Show Microsoft Basic Connect Extensions Service options

       --help-quectel
	      Show Quectel Service options

       --help-link-management
	      Show link management specific options

       --help-intel-thermal-rf
	      Show Intel Thermal RF Service options

       --help-ms-voice-extensions
	      Show Microsoft Voice Extensions Service options

       --help-ms-uicc-low-level-access
	      Show Microsoft UICC Low Level Access Service options

       --help-intel-mutual-authentication
	      Show Intel mutual authentication Service options

       --help-intel-tools
	      Show Intel 5G tools options

       --help-google
	      Show Google Service options

       --help-fibocom
	      Show Fibocom Service options

       --help-sms
	      Show SMS service options

   Basic Connect options:
       --query-device-caps
	      Query device capabilities

       --query-subscriber-ready-status
	      Query subscriber ready status

       --query-radio-state
	      Query radio state

       --set-radio-state=[(on|off)]
	      Set radio state

       --query-device-services
	      Query device services

       --query-pin-state
	      Query PIN state

       --enter-pin=[(PIN type),(current PIN)]
	      Enter PIN (PIN type is optional, defaults to PIN1, allowed options: (pin1,network-pin,network-subset-pin,service-provider-pin,corporate-pin)

       --change-pin=[(current PIN),(new PIN)]
	      Change PIN

       --enable-pin=[(current PIN)]
	      Enable PIN

       --disable-pin=[(PIN type),(current PIN)]
	      Disable PIN (PIN type is optional, see enter-pin for details)

       --enter-puk=[(PUK type),(PUK),(new PIN)]
	      Enter PUK (PUK type is optional, defaults to PUK1, allowed options: (puk1,network-puk,network-subset-puk,service-provider-puk,corporate-puk)

       --query-pin-list
	      Query PIN list

       --query-home-provider
	      Query home provider

       --query-preferred-providers
	      Query preferred providers

       --query-visible-providers
	      Query visible providers

       --query-registration-state
	      Query registration state

       --register-automatic
	      Launch automatic registration

       --query-signal-state
	      Query signal state

       --query-packet-service-state
	      Query packet service state

       --attach-packet-service
	      Attach to the packet service

       --detach-packet-service
	      Detach from the packet service

       --query-connection-state=[SessionID]
	      Query connection state (SessionID is optional, defaults to 0)

       --connect=["key=value,..."]
	      Connect (allowed keys: session-id, access-string, ip-type, auth, username, password, compression, context-type)

       --query-ip-configuration=[SessionID]
	      Query IP configuration (SessionID is optional, defaults to 0)

       --disconnect=[SessionID]
	      Disconnect (SessionID is optional, defaults to 0)

       --query-packet-statistics
	      Query packet statistics

       --query-ip-packet-filters=[SessionID]
	      Query IP packet filters (SessionID is optional, defaults to 0)

       --set-ip-packet-filters=["key=value,..."]
	      Set IP packet filters (allowed keys: session-id, packet-filter, packet-mask, filter-id)

       --query-provisioned-contexts
	      Query provisioned contexts

       --set-provisioned-contexts=["key=value,..."]
	      Set provisioned contexts (allowed keys: context-id, context-type, auth, compression, username, password, access-string, provider-id)

       --set-signal-state=["key=value,..."]
	      Set signal state (allowed keys: signal-strength-interval, rssi-threshold, error-rate-threshold)

       --set-network-idle-hint=[(enabled|disabled)]
	      Set network idle hint

       --query-network-idle-hint
	      Query network idle hint

       --set-emergency-mode=[(on|off)]
	      Set emergency mode

       --query-emergency-mode
	      Query emergency mode

       --set-service-activation=[Data]
	      Set service activation

   Phonebook options:
       --phonebook-query-configuration
	      Query the phonebook configuration

       --phonebook-read=[(Phonebook index)]
	      Read phonebook entry with given index

       --phonebook-read-all
	      Read all phonebook entries

       --phonebook-write=[(Name),(Number)[,(Index)]]
	      Add new phonebook entry or update an existing one

       --phonebook-delete=[(Phonebook index)]
	      Delete phonebook entry with given index

       --phonebook-delete-all
	      Delete all phonebook entries

   Device Service Stream options:
       --dss-connect=[(UUID),(Session ID)]
	      Connect DSS session

       --dss-disconnect=[(UUID),(Session ID)]
	      Disconnect DSS session

   Microsoft Firmware ID options:
       --ms-query-firmware-id
	      Query firmware ID

   Microsoft Host Shutdown options:
       --ms-notify-host-shutdown
	      Notify that host is shutting down

   Microsoft SAR options:
       --ms-set-sar-config=[(device|os),(enabled|disabled)[,[{antenna_index,backoff_index}...]]]
	      Set SAR config

       --ms-query-sar-config
	      Query SAR config

       --ms-set-transmission-status=[(enabled|disabled),(timer)]
	      Set transmission status and hysteresis timer (in seconds)

       --ms-query-transmission-status
	      Query transmission status

   AT&T Device Service options:
       --atds-query-signal
	      Query signal info

       --atds-query-location
	      Query cell location

   Intel Firmware Update Service options:
       --intel-modem-reboot=[(Boot Mode),(Timeout)]
	      Reboot modem. Boot mode and timeout arguments only required if MBIMEx >= 2.0.

   Microsoft Basic Connect Extensions options:
       --ms-query-pco=[SessionID]
	      Query PCO value (SessionID is optional, defaults to 0)

       --ms-query-lte-attach-configuration
	      Query LTE attach configuration

       --ms-query-lte-attach-info
	      Query LTE attach status information

       --ms-query-sys-caps
	      Query system capabilities

       --ms-query-device-caps
	      Query device capabilities

       --ms-query-slot-info-status=[SlotIndex]
	      Query slot information status

       --ms-set-device-slot-mappings=[(SlotIndex)[,(SlotIndex)[,...]]]
	      Set device slot mappings for each executor

       --ms-query-device-slot-mappings
	      Query device slot mappings

       --ms-query-location-info-status
	      Query location info status

       --ms-set-provisioned-contexts=["key=value,..."]
	      Set  provisioned	contexts (allowed keys: operation, context-type, ip-type, state, roaming-control, media-type, source, auth, compression, user‐
	      name, password, access-string)

       --ms-query-provisioned-contexts
	      Query provisioned contexts

       --ms-query-base-stations-info
	      Query base stations info

       --ms-device-reset
	      Reset device

       --ms-query-version=[(MBIM version),(MBIM extended version)]
	      Exchange supported version information. Since MBIMEx v2.0.

       --ms-query-registration-parameters
	      Query registration parameters. Since MBIMEx v3.0.

       --ms-set-registration-parameters=["key=value,..."]
	      Set registration parameters (required keys: mico-mode, drx-cycle, ladn-info, default-pdu-activation-hint, re-register-if-needed).	 Since	MBIMEx
	      v3.0.

       --ms-query-modem-configuration
	      Query modem configuration. Since MBIMEx v3.0.

       --ms-query-wake-reason
	      Query wake reason. Since MBIMEx v3.0.

   Quectel options:
       --quectel-query-radio-state
	      Query radio state

       --quectel-set-radio-state=[(on)]
	      Set radio state

   Link management options:
       --link-list=[IFACE]
	      List links created from a given interface

       --link-add=[iface=IFACE,prefix=PREFIX[,session-id=N]]
	      Create new network interface link

       --link-delete=IFACE
	      Delete a given network interface link

       --link-delete-all=[IFACE]
	      Delete all network interface links from the given interface

   Intel Thermal RF Service options:
       --intel-query-rfim
	      Query RFIM frequency information

       --intel-set-rfim=[(on|off)]
	      Enable or disable RFIM (disabled by default)

   Microsoft Voice Extensions Service options:
       --ms-query-nitz
	      Query network identity and time zone

   Microsoft UICC Low Level Access Service options:
       --ms-query-uicc-application-list
	      Query UICC application list

       --ms-query-uicc-file-status=["key=value,..."]
	      Query UICC file status (allowed keys: application-id, file-path)

       --ms-query-uicc-read-binary=["key=value,..."]
	      Read UICC binary file (allowed keys: application-id, file-path, read-offset, read-size, local-pin and data)

       --ms-query-uicc-read-record=["key=value,..."]
	      Read UICC record file (allowed keys: application-id, file-path, record-number, local-pin and data)

       --ms-set-uicc-open-channel=["key=value,..."]
	      Set UICC open channel (allowed keys: application-id, selectp2arg, channel-group)

       --ms-set-uicc-close-channel=["key=value,..."]
	      Set UICC close channel (allowed keys: channel, channel-group)

       --ms-query-uicc-atr
	      Query UICC atr

       --ms-set-uicc-apdu=["key=value,..."]
	      Set UICC apdu (allowed keys: channel, secure-message, classbyte-type, command)

       --ms-set-uicc-reset=[(Pass Through Action)]
	      Set UICC reset

       --ms-query-uicc-reset
	      Query UICC reset

       --ms-set-uicc-terminal-capability=["key=value,..."]
	      Set UICC terminal capability (allowed keys: terminal-capability)

       --ms-query-uicc-terminal-capability
	      Query UICC terminal capability

   Intel mutual authentication Service options:
       --intel-query-fcc-lock
	      Query FCC lock information

       --intel-set-fcc-lock=[(ResponsePresent),(Response)]
	      Set FCC lock information

       Intel 5G tools options

       --intel-set-trace-config=[(TraceCmd)|(TraceValue)]
	      Set trace configuration

       --intel-query-trace-config=[(TraceCmd)]
	      Query trace configuration

   Google options:
       --google-set-carrier-lock=[(Data)]
	      Set Google Carrier Lock

       --google-query-carrier-lock
	      Query Google Carrier Lock

   FIbocom options:
       --fibocom-set-at-command="<AT command>"
	      send AT command to modem, and receive AT response

   Simple message service options:
       --sms-delete=[(all|new|old|sent|draft|index=N)]
	      Delete all SMS matching a given filter

       --sms-read=[(all|new|old|sent|draft|index=N)]
	      Read all SMS matching a given filter

   Application Options:
       -d, --device=[PATH]
	      Specify device path

       -p, --device-open-proxy
	      Request to use the 'mbim-proxy' proxy

       --device-open-ms-mbimex-v2
	      Request to enable Microsoft MBIMEx v2.0 support

       --device-open-ms-mbimex-v3
	      Request to enable Microsoft MBIMEx v3.0 support

       --no-open=[Transaction ID]
	      Do not explicitly open the MBIM device before running the command

       --no-close
	      Do not close the MBIM device after running the command

       --noop Don't run any command

       -v, --verbose
	      Run action with verbose logs, including the debug ones

       --verbose-full
	      Run action with verbose logs, including the debug ones and personal info

       --silent
	      Run action with no logs; not even the error/warning ones

       --printable=[(Data)]
	      Get the printable info of the given hex encoded MBIM message

       -V, --version
	      Print version

COPYRIGHT
       Copyright © 2013-2023 Aleksander Morgado License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl-2.0.html>
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       The  full  documentation for mbimcli is maintained as a Texinfo manual.	If the info and mbimcli programs are properly installed at your site, the com‐
       mand

	      info mbimcli

       should give you access to the complete manual.

mbimcli 1.31.2								  March 2024								    MBIMCLI(1)
