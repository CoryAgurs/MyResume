from flask import Flask, request, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Create a sendgrid client
    client = SendGridAPIClient(api_key='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')

    # Create a new email
    mail = Mail(
        from_email=email,
        to_emails='cory.prints@gmail.com',
        subject='Website Form Submission',
        html_content='<strong>Name:</strong> {}<br><strong>Email:</strong> {}<br><br>{}'.format(name, email, message)
    )

    # Send the email
    response = client.send(mail)
    return redirect('/success')




