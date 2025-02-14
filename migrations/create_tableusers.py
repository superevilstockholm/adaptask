import aiomysql
import os
from dotenv import load_dotenv

load_dotenv()

async def create_table_users():
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
            db=db_name
        ) as conn:
            async with conn.cursor() as cur:
                await cur.execute("SHOW TABLES LIKE 'users'")
                if not await cur.fetchone():
                    await cur.execute("""
                        CREATE TABLE users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            fullname VARCHAR(255) NOT NULL,
                            username VARCHAR(64) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL UNIQUE,
                            phone VARCHAR(20) DEFAULT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                else:
                    await cur.execute("""
                        ALTER TABLE users
                        MODIFY fullname VARCHAR(255) NOT NULL,
                        MODIFY username VARCHAR(64) NOT NULL UNIQUE,
                        MODIFY password VARCHAR(255) NOT NULL,
                        MODIFY email VARCHAR(255) NOT NULL UNIQUE,
                        MODIFY phone VARCHAR(20) DEFAULT NULL,
                        MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    """)
                await conn.commit()
                print("Table users created/updated successfully")
    except aiomysql.Error as e:
        print(e)
