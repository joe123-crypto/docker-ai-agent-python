# pip install -qU "langchain[anthropic]" to call the model

from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from api.ai.llms import get_openai_llm,get_gemni_llm

from api.ai.tools import (
    send_me_email,
    get_unread_emails,
    research_email,
)

EMAIL_TOOLS_LIST = [
    send_me_email,
    get_unread_emails,
    research_email,
]

def get_email_agent():
    model = get_gemni_llm()
    agent = create_react_agent(
        model=model,
        tools=EMAIL_TOOLS_LIST,
        prompt=(
            "You are a helpful assistant for managing my email inbox. "
            "When asked to send an email, if the user does not specify the subject or content, "
            "you should generate appropriate values based on their request."
        ),
        name="emai_agent"
    )
    return agent

def get_research_agent():
    model = get_gemni_llm(model="gemini-2.5-pro")
    agent = create_react_agent(
        model=model,
        tools=[research_email],
        prompt="You are a helpful research assistant for preparing email data",
        name="research_agent"
    )
    return agent
#supe.invoke({"messages":[{"role":"user","content":"Find out how to make a latte and them email me the results"}]})
def get_supervisor():
    llm = get_gemni_llm(model="gemni-2.5-flash")
    email_agent = get_email_agent()
    research_agent = get_research_agent()
    prompt = (
        "You are a supervisor. When a user asks for research to be emailed, "
        "first instruct the research_agent to perform the research and obtain the result. "
        "Then, immediately instruct the email_agent to send the research result to the user, "
        "using the research result as the email content, without asking for further confirmation. "
        "Do not ask the user for confirmation if the original request already includes both actions."
    )
    supe = create_supervisor(
        agents = [email_agent, research_agent],
        model = llm,
        prompt = prompt
    ).compile()
    return supe

