#!/usr/bin/env python3
"""
Send email notification using SMTP.

Usage:
    python send_email.py --to <recipient> --subject <subject> --body <body>
    python send_email.py --to <recipient> --subject <subject> --body-file <file>

Environment variables (or use .credentials.json in ~/.claude):
    SMTP_HOST: SMTP server host
    SMTP_PORT: SMTP server port
    SMTP_USER: SMTP username/email
    SMTP_PASSWORD: SMTP password
"""

import argparse
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


def load_credentials():
    """Load SMTP credentials and settings from environment or .credentials.json"""
    # Try environment variables first
    if all(os.environ.get(k) for k in ['SMTP_HOST', 'SMTP_PORT', 'SMTP_USER', 'SMTP_PASSWORD']):
        return {
            'host': os.environ['SMTP_HOST'],
            'port': int(os.environ['SMTP_PORT']),
            'user': os.environ['SMTP_USER'],
            'password': os.environ['SMTP_PASSWORD'],
            'to': os.environ.get('SMTP_TO')
        }

    # Try .credentials.json in ~/.claude
    creds_file = Path.home() / '.claude' / '.credentials.json'
    if creds_file.exists():
        with open(creds_file) as f:
            creds = json.load(f)
            smtp = creds.get('smtp', {})
            if smtp:
                return {
                    'host': smtp.get('host'),
                    'port': int(smtp.get('port', 587)),
                    'user': smtp.get('user'),
                    'password': smtp.get('password'),
                    'to': smtp.get('to')
                }

    raise ValueError("SMTP credentials not found. Set environment variables or configure .credentials.json")


def send_email(to: str, subject: str, body: str, html: bool = False):
    """Send an email using SMTP."""
    creds = load_credentials()

    msg = MIMEMultipart('alternative')
    msg['From'] = creds['user']
    msg['To'] = to
    msg['Subject'] = subject

    if html:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(creds['host'], creds['port']) as server:
        server.starttls()
        server.login(creds['user'], creds['password'])
        server.send_message(msg)

    print(f"Email sent successfully to {to}")


def main():
    parser = argparse.ArgumentParser(description='Send email notification')
    parser.add_argument('--to', help='Recipient email address (uses default from .credentials.json if not specified)')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', help='Email body text')
    parser.add_argument('--body-file', help='File containing email body')
    parser.add_argument('--html', action='store_true', help='Send as HTML email')

    args = parser.parse_args()

    if args.body_file:
        with open(args.body_file) as f:
            body = f.read()
    elif args.body:
        body = args.body
    else:
        parser.error("Either --body or --body-file is required")

    # Determine recipient: command line arg takes precedence over credentials default
    creds = load_credentials()
    recipient = args.to or creds.get('to')
    if not recipient:
        parser.error("No recipient specified. Use --to or set 'to' in .credentials.json smtp config")

    send_email(recipient, args.subject, body, args.html)


if __name__ == '__main__':
    main()
