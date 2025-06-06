from ipaddress import IPv4Address

from fastapi import APIRouter, Request

from ..schemas import EventCreate, EventSchema, Response

router = APIRouter(tags=["events"])


@router.get(
    "/",
    response_model_by_alias=True,
    response_model_exclude_none=True,
    response_model=Response[EventSchema],
)
def read_events(req: Request):
    return Response[EventSchema](
        data=[
            EventSchema(
                id=1,
                path="/dummy/path",
                agent="dummy-agent",
                ip_address=IPv4Address("127.0.0.1"),
                session_id="dummy-session",
            ),
            EventSchema(
                id=2,
                path="/dummy/path/2",
                agent="dummy-agent-2",
                ip_address=IPv4Address("172.0.0.1"),
                session_id="dummy-session-2",
            ),
        ],
        req=req,
    )


@router.post("/", response_model=Response[EventSchema], response_model_by_alias=True)
def create_event(req: Request, payload: EventCreate):
    return Response[EventSchema](**{"req": req, "data": EventSchema(**payload.model_dump(), id=1)})
