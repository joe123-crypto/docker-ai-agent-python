from langchain_core.tools import tool
from api.myemailer.sender import send_email
from api.myemailer.inbox_reader import read_inbox

@tool
def send_me_email(subject:str,content:str) -> str:
    """
    Send an email to myself with a subject and content

    Arguments:
        - subject: str - Text subject of the email  
        - content: str - Text body content of the email
    """
    try:
        send_email(subject=subject,content=content)
    except:
        return "Not sent"
    return "Email sent "

@tool
def get_unread_emails(hours_ago:int=48) -> str:
    """
    Read all emails from my inbox within the last N hours 

    Arguments:
        - hours_ago: int = 24 - Number of hours ago to retrieve in the inbox  

    Returns:
    A string of emails seperated by a line  "----"
    """
    try:
        emails = read_inbox(hours_ago=hours_ago,verbose=False)
    except:
        return "Error getting latest emails"
    
    cleaned = []
    for email in emails:
        data = email.copy()
        if "html_body" in data:
            data.pop("html_body")
        msg = ""
        for k,v in data.items():
            msg += f"{k}:\{v}"
        cleaned.append(msg)
    return "\n----\n".join(cleaned)