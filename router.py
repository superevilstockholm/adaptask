from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from aiomysql.pool import Pool

from models import UserLogin

class Router():
    def __init__(self, app: FastAPI, pool: Pool):
        """
        Params:
        - app: FastAPI application
        - pool: aiomysql pool
        """
        self.app = app
        self.pool = pool
        self.routes()

    def routes(self):
        @self.app.post("/api/login")
        async def get_test(username: str = Form(...), password: str = Form(...)) -> JSONResponse:
            """API DOCUMENTATION
            - name: LOGIN
            - path: /api/login
            - method: POST
            - need auth: false
            - fields:
                - username: str
                - password: str
            - response type: JSONResponse
            - response:
                - status: bool
                - message: str
                - token: str
            """
            try:
                user = UserLogin(username=username, password=password)
                print(user)
                return JSONResponse(content={"message": "Login successful"}, status_code=200)
            except Exception as e:
                return JSONResponse(content={"message": "Login failed"}, status_code=400)