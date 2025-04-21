regulatory.bin(5)							     Linux							     regulatory.bin(5)

NAME
       regulatory.bin, regulatory.db - The Linux wireless regulatory database

Description
       regulatory.bin and regulatory.db are the files used by the Linux wireless subsystem to keep its regulatory database information.

       regulatory.bin is read by crda upon the Linux kernel's request for regulatory information for a specific ISO / IEC 3166 alpha2 country code.

       regulatory.db is a newer, extensible database format which (since Linux 4.15) is read by the kernel directly as a firmware file.

       The regulatory database is kept in a small binary format for size and code efficiency. The regulatory.bin file can be parsed and read in human format
       by using the regdbdump command. The regulatory database files should be updated upon regulatory changes or corrections.

Upkeeping
       The regulatory database is maintained by the community as such you are encouraged to send any corrections or updates to the linux-wireless and wire‐
       less-regdb mailing lists: linux-wireless@vger.kernel.org and wireless-regdb@lists.infradead.org

SEE ALSO
       regdbdump(8) crda(8) iw(8)

       http://wireless.kernel.org/en/developers/Regulatory/

regulatory.bin							       21 December 2017							     regulatory.bin(5)
