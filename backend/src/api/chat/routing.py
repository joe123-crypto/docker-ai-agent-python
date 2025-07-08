from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.db import get_session
from .models import ChatMessagePayload,ChatMessage,ChatMessageListItem

router = APIRouter()

@router.get("/")
def chat_health():
    return {"status":"Ok"}

#curl -Uri "http://localhost:8080/api/chats/recent/" -Method GET -ContentType "application/json"
@router.get("/recent/",response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results
#curl -Uri "http://localhost:8080/api/chats/" -Method POST -Body '{"message":"hello world"}' -ContentType "application/json"
@router.post("/",response_model=ChatMessage)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
