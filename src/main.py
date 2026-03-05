from typing import Union
import uvicorn
from fastapi import FastAPI
from routers.v1 import user, attendance, members, services
from config_setting import setting
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.router)
app.include_router(attendance.router)
app.include_router(members.router)
app.include_router(services.router)

origins = setting.CORS_ORIGINS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=[
        'http://localhost:3000',
        'https://murrzzz.xyz',
        'https://api.murrzzz.xyz',
        'https://jiomtc.murrzzz.xyz',
        'jiomtc-attendance-git-master-roger-moore-sangols-projects.vercel.app'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000, reload=False)
