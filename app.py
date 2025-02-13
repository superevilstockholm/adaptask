from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from dotenv import load_dotenv
import os
import aiomysql

from router import Router

class AdapTask:
    """Color codes for terminal"""
    colors = {
        'RESET': '\033[0m', # Default
        'GREEN': '\033[92m', # Debug
        'YELLOW': '\033[93m', # Warning
        'RED': '\033[91m' # Error
    }
    def __init__(self):
        """Initialize app"""
        load_dotenv()
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app.add_middleware(GZipMiddleware, minimum_size=1000)
        self.pool = None
        self.app.add_event_handler("startup", self.connect_db)
        self.app.add_event_handler("shutdown", self.close_db)

    async def connect_db(self):
        """Connect to database"""
        self.pool = await aiomysql.create_pool(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            db=os.getenv("DB_NAME")
        )
        print(f"{self.colors['GREEN']}DEBUG{self.colors['RESET']}:\tConnected to database")
        Router(self.app, self.pool)

    async def close_db(self):
        """Close database connection"""
        if not self.pool:
            return
        self.pool.close()
        await self.pool.wait_closed()
        print(f"{self.colors['YELLOW']}DEBUG{self.colors['RESET']}:\tDisconnected from database")

    @staticmethod
    def run(host: str = "127.0.0.1", port: int = 23237, reload: bool = True, reload_includes: list = ["*.py"], loop: str = "asyncio", **kwargs):
        """Run app"""
        import uvicorn
        uvicorn.run(
            "app:app",
            host=host,
            port=port,
            reload=reload,
            reload_includes=reload_includes,
            loop=loop,
            **kwargs
        )

webapp = AdapTask()
app = webapp.app

if __name__ == '__main__':
    AdapTask.run(
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_includes=["*.py"],
        loop="asyncio"
    )