mailshell
=========
a pythion based utility that scans an email account for shell scripts and executes them, sending the result back to the sender.

signature
=========
to ensure only athorised shell scripts are executed the email conataining the script must contain the SIGNATUE in the
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






Usage
=====
-k ,--awsaccesskeyid , AWS Access Key ID
-s, --awssecretaccesskey , AWS Secret Access Key  
-b, --bucketname, AWS Bucket Name  
-c, --cloudpath, AWS cloud path  
-l,--localpath, local path  
-d, --direction, transfer direction (upload, download)  
--logfile , log file name  
--maxactions, maximum number of actions  
--md5, enable md5 hash file checking  
--dryrun, enable dryrun'  
--delete, enable file deletion'  

Example
=======
s3sync.py -k AFIAKP0IQFWOEFCYAYEA -s JusNeBKWC/K6lUEeQiXg+nTPnnwxCXUT+CuIQ9C -b testbucket -c Backup -l /media/Backup -d upload --logfile /media/Backup/s3.log --maxactions 100

