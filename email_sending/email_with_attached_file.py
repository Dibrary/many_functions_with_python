
import os

from email.mime.multipart import MIMEMultipart

from email import encoders

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio

from email.mime.base import MIMEBase

msg_dict = {
    'text':{'maintype':'text', 'subtype':'plain', 'filename':'res/test.txt'},

}


