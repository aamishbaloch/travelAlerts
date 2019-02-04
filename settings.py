import os

# GeoPy
geocoder_app_name = 'BVGConnect'

# Email
smtp = 'smtp.gmail.com:587'
username = os.environ["smtp_username"]
password = os.environ["smtp_password"]
from_address = 'mytravelalert@no-reply.com'
to_address = os.environ["to_address"]
