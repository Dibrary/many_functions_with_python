from smtp_practice import *
from email_with_attached_file import *

smtp_info= dict({'smtp_server':'smtp.gmail.com',
                 'smtp_user_id':'송신자 계정',
                 'smtp_user_pw' :'송신자 비밀번호', # 2차 비밀번호까지 사용해서 안 되는 듯. gmail로 하니까 됨.
                 'smtp_port':587})

title = "첨부파일이 이씀"
content = "메일 내용"
sender = "송신자 메일 주소"
receiver = "수신자 메일 주소"

msg = MIMEText(_text=content, _charset="utf-8")

multi = make_multimsg(msg_dict)
multi['Subject'] = title
multi['From'] = sender
multi['To'] = receiver
multi.attach(msg)

send_email(smtp_info, multi)
