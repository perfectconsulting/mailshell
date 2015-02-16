# Copyright 2011-2013 S J Consulting Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0.html
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import imaplib
import smtplib
import email
import pprint
import subprocess
from time import gmtime, strftime

GMAIL_ADDRESS='<email addres to which you will send the shell commands>'
GMAIL_PASSWORD='<password>'

IMAP_SERVER='<email server imap addrss>'
IMAP_PORT=993
SMTP_SERVER='<email server smtp address>'
SMTP_PORT=587
SIGNATURE='<secret subject signature to identify a email message containing the shell commands>'

def get_next_shell_email(purge = True):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(GMAIL_ADDRESS,GMAIL_PASSWORD)
    mail.select('INBOX')

    filter = "(HEADER Subject \"%s\")" % SIGNATURE
    result, data = mail.uid('search', None, filter)

    uids = data[0].split()

    if len(uids) == 0:
        return ('','')

    first_id = uids[0]

    result, data = mail.uid('fetch', first_id, '(RFC822)')
    email_message = email.message_from_string(data[0][1])
    from_address = email_message['FROM']

    type = email_message.get_content_maintype()
    if type == 'multipart':
        for part in email_message.get_payload():
            if part.get_content_maintype() == 'text':
                text = part.get_payload()
                break

    elif type == 'text':
        text = email_message.get_payload()

    if purge:
        mail.uid('STORE', first_id , '+FLAGS', '(\Deleted)')
        mail.expunge()

    mail.logout()

    return (from_address, text)

def execute_shell_email(script):
    result = ''
    
    pad = script.replace("\n","")
    pad = pad.replace("\r\r","\r")
    pad = pad.replace("\r",";")
    pad = pad.replace("\r",";")
    pad = pad.rstrip(';')

    p = subprocess.Popen(pad, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        result = result + line
        retval = p.wait()

    return result

def send_email(from_addr, to_addr_list, cc_addr_list, subject, message,login, password, smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % to_addr_list
    header += 'Cc: %s\n' % cc_addr_list
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

reply_address, script = get_next_shell_email(False)

if reply_address <> '' and script <> '':
    print("executing script for %s" % reply_address)
    result = execute_shell_email(script)
    send_email(GMAIL_ADDRESS,reply_address,'',"shell executed @ %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime()), result,GMAIL_ADDRESS,GMAIL_PASSWORD)
