from api.ai.llms import get_gemni_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_messages(query:str) -> EmailMessageSchema:
    llm_base = get_gemni_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails.",
        ),
        (
            "human",
            f"{query}.",
        ),
        ]
    return llm.invoke(messages)