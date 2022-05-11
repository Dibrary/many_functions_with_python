
from email.mime.text import MIMEText
from email_sending.smtp_practice import send_email


smtp_info= dict({'smtp_server':'smtp.gmail.com',
                 'smtp_user_id':'송신자 계정',
                 'smtp_user_pw' :'송신자 비밀번호', # 2차 비밀번호까지 사용해서 안 되는 듯. gmail로 하니까 됨.
                 'smtp_port':587})

title = "기본 이메일 입니다."
content = "메일 내용입니다."

sender = smtp_info['smtp_user_id']
receiver = '수신자 메일주소' # 수신자 메일 주소

msg = MIMEText(_text = content, _charset='utf-8') # 본문 텍스트

msg['Subject'] = title # 텍스트 제목
msg['From'] = sender # 송신자
msg['To'] = receiver # 수신자

send_email(smtp_info, msg)

