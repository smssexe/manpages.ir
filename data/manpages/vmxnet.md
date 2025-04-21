VMXNET(9)								 Open VM Tools								     VMXNET(9)

NAME
       vmxnet - vmware kernel module

SYNOPSIS
       modprobe vmxnet

DESCRIPTION
       This is a Linux kernel device driver module that drives VMware's fast networking device. As it is backed by real (virtual) hardware, it should be auto‐
       matically loaded by hotplug or udev as needed. For best performance, it is recommended to enable TSO on all interfaces driven by vmxnet using ethtool.

       The shell code to do this might look like this:

       if which ethtool >/dev/null 2>&1; then
	  for ethif in `ifconfig -a | grep ^eth | cut -d' ' -f1`; do
	     ethtool -K $ethif tso on >/dev/null 2>&1
	  done fi

       The VMware backend may present the fast networking device as an AMD vlance device instead of the actual vmxnet device.

SEE ALSO
       vmware-checkvm(1)
       vmware-toolbox(1)
       vmware-toolbox-cmd(1)
       vmware-user(1)
       vmware-xferlogs(1)
       libguestlib(3)
       libvmtools(3)
       vmware-guestd(8)
       vmware-user-suid-wrapper(1)
       vmblock(9)
       vmci(9)
       vmmemctl(9)
       vmsock(9)
       vmsync(9)
       vmxnet3(9)

HOMEPAGE
       More information about vmxnet and the Open VM Tools can be found at <http://open-vm-tools.sourceforge.net/>.

AUTHOR
       Open VM Tools were written by VMware, Inc. <http://www.vmware.com/>.

       This  manual  page was put together from homepage materials by Daniel Baumann <mail@daniel-baumann.ch>, for the Debian project (but may be used by oth‐
       ers).

2010.03.20-243334							  2010-04-08								     VMXNET(9)
