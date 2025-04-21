QMI-FIRMWARE-UPDATE(1)							 User Commands							QMI-FIRMWARE-UPDATE(1)

NAME
       qmi-firmware-update - Update firmware in QMI devices

DESCRIPTION
   Usage:
	      qmi-firmware-update [OPTION?] FILE1 FILE2... - Update firmware in QMI devices

   Generic device selection options:
       -s, --busnum-devnum=[BUS:]DEV
	      Select device by bus and device number (in decimal).

       -d, --vid-pid=VID[:PID]
	      Select device by device vendor and product id (in hexadecimal).

       -w, --cdc-wdm=[PATH]
	      Select device by QMI/MBIM cdc-wdm device path (e.g. /dev/cdc-wdm0).

       -t, --tty=[PATH]
	      Select device by serial device path (e.g. /dev/ttyUSB2).

   Update options (normal mode):
       -u, --update
	      Launch firmware update process.

       -f, --firmware-version=[VERSION]
	      Firmware version (e.g. '05.05.58.00').

       -c, --config-version=[VERSION]
	      Config version (e.g. '005.025_002').

       -C, --carrier=[CARRIER]
	      Carrier name (e.g. 'Generic').

       --ignore-version-errors
	      Run update operation even with version string errors.

       --override-download
	      Download images even if module says it already has them.

       --modem-storage-index=[INDEX]
	      Index storage for the modem image.

       --skip-validation
	      Don't wait to validate the running firmware after update.

   Reset options (normal mode):
       -b, --reset
	      Reset device into download mode.

   Update options (download mode):
       -U, --update-download
	      Launch firmware update process while in download (boot & hold) mode.

   Verify options:
       -z, --verify
	      Analyze and verify firmware images.

   Application Options:
       -p, --device-open-proxy
	      Request to use the 'qmi-proxy' proxy.

       --device-open-qmi
	      Open a cdc-wdm device explicitly in QMI mode

       --device-open-mbim
	      Open a cdc-wdm device explicitly in MBIM mode

       --device-open-auto
	      Open a cdc-wdm device in either QMI or MBIM mode (default)

       --ignore-mm-runtime-check
	      Ignore ModemManager runtime check

       -v, --verbose
	      Run action with verbose messages in standard output, including the debug ones.

       -S, --silent
	      Run action with no messages in standard output; not even the error ones.

       -L, --verbose-log=[PATH]
	      Write verbose messages to an output file.

       -V, --version
	      Print version.

       -h, --help
	      Show help.

       -H, --help-examples
	      Show help examples.

       ***************************************************************************
	      Warning!

	      ***************************************************************************

	      Use this program with caution. The authors take *no* responsibility if any device gets broken as a result of using this program.

	      Please report issues to the libqmi mailing list at:

	      libqmi-devel@lists.freedesktop.org

       qmi-firmware-update 1.35.2

	      Copyright	 (C)  2016-2022	 Aleksander Morgado Copyright (C) 2022 VMware, Inc.  Copyright (C) 2016-2019 Bj?rn Mork Copyright (C) 2016-2018 Zodiac
	      Inflight Innovations

       License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl-2.0.html> This is free software: you are free to change	and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       The  full documentation for qmi-firmware-update is maintained as a Texinfo manual.  If the info and qmi-firmware-update programs are properly installed
       at your site, the command

	      info qmi-firmware-update

       should give you access to the complete manual.

qmi-firmware-update							  March 2024							QMI-FIRMWARE-UPDATE(1)
