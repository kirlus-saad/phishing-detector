import re

def is_phishing_email(email_text):

	phishing_keywords = ["urgent", "account verification", "update payment", "click here"]

	for keyword in phishing_keywords:
		if keyword.lower() in email_text.lower():
			return True
	return False

email_content = "Dear user, your account needs urgent verification. Click here to update your payment details."
if is_phishing_email(email_content):
    print("⚠️ Warning: This email looks like a phishing attempt!")
else:
    print("✅ This email seems safe.")	
