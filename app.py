from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
app = FastAPI(
    title="My FastAPI Application with MongoDB",
    description="My FastAPI Application with MongoDB",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.include_router(user)
