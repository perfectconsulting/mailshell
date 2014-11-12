mailshell
=========
a python based utility that scans an email account for shell scripts and executes them, sending the result back to the sender.

signature
=========
to ensure only athorised shell scripts are executed the email containing the script must contain the SIGNATUE in the
email subject line.

setup
=====
GMAIL_ADDRESS='elvis@gmail.com'
GMAIL_PASSWORD='letmein'

IMAP_SERVER='imap.gmail.com'
IMAP_PORT=993

SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587

SIGNATURE='elvis has left the buiding'

usage
=====
set a cron job to execute the script at regular intervals (5 minutes)

then email the sever your commands, thus

subject:elvis has left the buiding

ls -al

du -h

free -m
