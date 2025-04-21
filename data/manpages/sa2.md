SA2(8)								      Linux User's Manual								SA2(8)

NAME
       sa2 - Create a report from the current standard system activity daily data file.

SYNOPSIS
       /usr/lib/sysstat/sa2

DESCRIPTION
       The sa2 command is a shell procedure variant of the sar command which writes a daily report in the sarDD or the sarYYYYMMDD file, where YYYY stands for
       the  current  year, MM for the current month and DD for the current day. By default the report is saved in the /var/log/sysstat directory. The sa2 com‐
       mand will also remove reports more than one week old by default.	 You can however keep reports for a longer (or a shorter) period by setting  the  HIS‐
       TORY environment variable. Read the sysstat(5) manual page for details.

       The sa2 command accepts most of the flags and parameters of the sar command.

       The sa2 command is designed to be started automatically by the cron command.

EXAMPLES
       To run the sa2 command daily, place the following entry in your root crontab file:

       5 19 * * 1-5 /usr/lib/sysstat/sa2 -A

       This will generate by default a daily report called sarDD in the /var/log/sysstat directory, where the DD parameter is a number representing the day of
       the month.

   Debian note
       The  Debian sysstat package has already placed such an entry in your system crontab.  Please refer to the /usr/share/doc/sysstat/README.Debian file for
       details.

FILES
       /var/log/sysstat/sarDD
       /var/log/sysstat/sarYYYYMMDD
	      The standard system activity daily report files and their default location.  YYYY stands for the current year, MM for the current month  and  DD
	      for the current day.

AUTHOR
       Sebastien Godard (sysstat <at> orange.fr)

SEE ALSO
       sar(1), sadc(8), sa1(8), sadf(1), sysstat(5)

       https://github.com/sysstat/sysstat
       http://pagesperso-orange.fr/sebastien.godard/

Linux									   JULY 2020									SA2(8)
