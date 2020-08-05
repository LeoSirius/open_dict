from django.core.mail import send_mail

def send_emails(to_emails):
    send_mail(
        subject='黄文杨的个人网站，谢谢使用！',
        message='Here is the message.',
        from_email='',
        # 接受者
        recipient_list=to_emails,
    )
