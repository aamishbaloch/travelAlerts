import smtplib


class Email:

    def __init__(self, username, password, smtp):
        self.username = username
        self.password = password
        self.server = smtplib.SMTP(smtp)

    def send_email(self, from_address, to_address, subject, message):
        message = "\r\n".join([
            f'Subject: {subject}',
            '',
            message,
        ])

        self.server.starttls()
        self.server.login(self.username, self.password)
        self.server.sendmail(from_address, to_address, message)
        self.server.quit()
