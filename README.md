# halo-firewall-report
=====================

Generate HTML, PDF reports for CSM and SVA Halo modules

###Required Modules:
* xhtml2pdf or pdfkit for PDF output
* markdown

###Caveats:
* If configured to output to PDF, will attempt to load xhtml2pdf and pdfkit.  At least one required.  If both are loadable, pdfkit is preferred.  If pdfkit is installed and wkhtml2pdf is not installed, it will error out.
* If configured to use a proxy and output to PDF, you must use a local logo file.

###Files:
* **README.md**   The one you're reading now...
* **api.py**   The last stop before crossing the interwebs
* **assets/**   This is where we put logo files...
* **config.conf**   This is the default configuration file.
* **cruncher.py**   This contains functions related to data crunching.
* **dumper.py**   This handles output formatting
* **fn.py**   Misc functions here
* **license.txt**   The cure for insomnia
* **outfiles/**   Output files get dropped here
* **repgen.py**   RUN THIS ONE.  Accepts -s SearchString or -a for all.  Optionally declare another config file with -c
* **server.py**   Server object definition

###Usage:


>repgen.py (-s SEARCHPREFIX|-a) [-c CONFIGFILE]

>This script generates a report for all servers if -a is used, or just the servers with SEARCHPREFIX in the server label if -s is used.

>Make sure you correctly configure config.conf.  You can use -c to specify a different configuration file.  Otherwise, ./config.conf is assumed.  In config.conf: search_field will determine the metadata field that SEARCHPREFIX is applied to
to create the list of servers that will be reported on.

>The output configuration value  will determine the output format for the information.

>Text is mainly for debugging and may not produce as much meaningful information as html or pdf.

>HTML and PDF files are placed in the ./outfile folder.  If it doesn't exist, the script will fail.
