from .celery import app

@app.task
def send_email(subject, html_content, to, cc=None):
    return 'Email sented to %s' % to
