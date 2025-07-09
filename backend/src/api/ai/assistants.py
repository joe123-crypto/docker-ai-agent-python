from api.ai.llms import get_gemni_llm
#from api.ai.schemas import EmailMessageSchema

from api.ai.tools import (
    send_me_email,
    get_unread_emails,
)

EMAIL_TOOLS = {
    "send_me_email":send_me_email,
    "get_unread_emails":get_unread_emails,
}
def email_assistant(query:str):
    llm_base = get_gemni_llm()
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails. Do not use markdown in your response only plaintext.",
        ),
        (
            "human",
            f"{query}. Do not use markdown in your response only plaintext",
        ),
        ]
    response = llm.invoke(messages)
    return response