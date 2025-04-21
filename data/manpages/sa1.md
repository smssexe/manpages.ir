SA1(8)								      Linux User's Manual								SA1(8)

NAME
       sa1 - Collect and store binary data in the system activity daily data file.

SYNOPSIS
       /usr/lib/sysstat/sa1 [ --boot | --rotate [ iso ] | --sleep | interval count ]

DESCRIPTION
       The  sa1 command is a shell procedure variant of the sadc command and handles all of the flags and parameters of that command. The sa1 command collects
       and stores binary data in the current standard system activity daily data file.

       The standard system activity daily data file is named saDD unless sadc's option -D is used, in which case its name is saYYYYMMDD, where YYYY stands for
       the current year, MM for the current month and DD for the current day. By default it is located in the /var/log/sysstat directory.

       The interval and count parameters specify that the record should be written count times at interval seconds. If no arguments are given to  sa1  then  a
       single record is written.

       The sa1 command is designed to be started automatically by the cron command.

OPTIONS
       --boot This  option  tells  sa1	that the sadc command should be called without specifying the interval and count parameters in order to insert a dummy
	      record, marking the time when the counters restart from 0.

       --rotate [ iso ]
	      Use this option to tell sa1 to insert a record of statistics to the standard saDD system activity daily data file of  the	 previous  day.	  This
	      should  be  done shortly after midnight (on day DD+1) in order to make sure that the data file covers the whole day, including the last interval
	      of time just before midnight.  Adding the iso keyword tells sa1 to use saYYYYMMDD instead of saDD as the standard	 system	 activity  daily  data
	      file name.

       --sleep
	      This  option  tells  sa1 that the sadc command should insert a comment indicating that the system is entering or leaving sleep mode (i.e. system
	      suspend or hibernation).

EXAMPLE
       To collect data (including those from disks) every 10 minutes, place the following entry in your root crontab file:

       0,10,20,30,40,50 * * * * /usr/lib/sysstat/sa1 1 1 -S DISK

       To rotate current system activity daily data file, ensuring it is complete, place the following entry in your root crontab file:

       0 0 * * * /usr/lib/sysstat/sa1 --rotate

   Debian note
       The Debian sysstat package has already placed such an entry in your system crontab.  Please refer to the /usr/share/doc/sysstat/README.Debian file  for
       details.

FILES
       /var/log/sysstat/saDD
       /var/log/sysstat/saYYYYMMDD
	      The standard system activity daily data files and their default location.	 YYYY stands for the current year, MM for the current month and DD for
	      the current day.

AUTHOR
       Sebastien Godard (sysstat <at> orange.fr)

SEE ALSO
       sar(1), sadc(8), sa2(8), sadf(1), sysstat(5)

       https://github.com/sysstat/sysstat
       http://pagesperso-orange.fr/sebastien.godard/

Linux									 NOVEMBER 2020									SA1(8)
