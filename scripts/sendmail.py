#!/usr/bin/env python3
"""
Email notification script for Claude Code.
Sends task completion notifications via SMTP.
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Configuration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "xujialiuphd@gmail.com"
SMTP_PASSWORD = "fkoo cgab azuw ymwm"
RECIPIENT = "xujialiu@link.cuhk.edu.hk"


def send_email(subject: str, body: str) -> bool:
    """Send an email notification."""
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = RECIPIENT
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, RECIPIENT, msg.as_string())
        print(f"Email sent successfully to {RECIPIENT}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: sendmail.py <subject> [body]")
        print('Example: sendmail.py "Task Complete" "Your task has finished."')
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2] if len(sys.argv) > 2 else "Claude Code task completed."

    success = send_email(subject, body)
    sys.exit(0 if success else 1)
