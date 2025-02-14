import aiomysql
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def create_database():
    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    try:
        async with aiomysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
        ) as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
                await conn.commit()
                print(f"{db_name} Database created successfully")
    except aiomysql.Error as e:
        print(e)