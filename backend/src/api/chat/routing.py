from typing import List
from fastapi import APIRouter, Depends,HTTPException
from sqlmodel import Session, select

from api.db import get_session
from api.ai.agents import get_supervisor
from api.ai.schemas import EmailMessageSchema,SupervisorMessageSchema
from api.ai.services import generate_email_messages
from .models import ChatMessagePayload,ChatMessage,ChatMessageListItem

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status":"Ok"}

#curl -Uri "http://localhost:8080/api/chats/recent/" -Method GET -ContentType "application/json"
#curl -Uri "https://docker-ai-agent-python-production-81b8.up.railway.app/api/chats/recent/"

@router.get("/recent/",response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results
#curl -Uri "http://localhost:8080/api/chats/" -Method POST -Body '{"message":"give me a summary of why its good to go outside"}' -ContentType "application/json"

#curl -Uri "https://docker-ai-agent-python-production-81b8.up.railway.app/api/chats/" -Method POST -Body '{"message":"give me a summary of the potential dangers of large language models."}' -ContentType "application/json"
#curl -Uri "https://docker-ai-agent-python-production-81b8.up.railway.app/api/chats/" -Method POST -Body '{"message":"Research why it is good to go outside and email me the results ."}' -ContentType "application/json"
@router.post("/",response_model=SupervisorMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    supe = get_supervisor()
    msg_data = {
        "messages":[
            {
                "role":"user",
                "content":f"{payload.message}"
            }
        ]
    }
    results = supe.invoke(msg_data)
    if not results :
        raise HTTPException(status_code=400,detail="Error with supervisor")
    messages = results.get("messages")
    if not messages:
        raise HTTPException(status_code=400,detail="Error with supervisor")
    return messages[-1]