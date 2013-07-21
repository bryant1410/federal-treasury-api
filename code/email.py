import os, imaplib

def login():
    M = imaplib.IMAP4_SSL(os.environ['IMAP_SERVER'])
    M.login(os.environ['IMAP_USER'], os.environ['IMAP_PASSWORD'])
    return M

def new_mail(search_string = '(UNSEEN FROM "fms.treas.gov")'):
    M = login()
    M.select()

    # List the emails
    status, numbers = M.search(None, search_string)

    # Check for new mail
    _new_mail = numbers != ['']

    # Mark new mail as read.
    if _new_mail:
        for number in numbers[0].split():
            M.fetch(number, '(RFC822)')

    # Log out
    M.close()
    M.logout()

    # Return True or False
    return _new_mail
