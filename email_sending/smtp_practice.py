
import smtplib

smtp_info= dict({'smpt_server':'smtp.naver.com',
                 'smtp_user_id':'송신자 메일 계정',
                 'smtp_user_pw' :'송신자 메일 비밀번호',
                 'smtp_port':587})

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port']) as server:
        server.starttls()
        server.login(smtp_info['smtp_user_id'], smtp_info['smtp_user_pw'])

        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        
        if not response:
            print("성공으로 보냈습니다.")
        else:
            print(response)