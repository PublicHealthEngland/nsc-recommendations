from ..celery import app
from .models import Email


@app.task
def send_pending_emails():
    # limit to the first 3000 as a max of 3000 messages can be sent in a minute
    for email in Email.objects.to_send()[:3000]:
        email.send()
