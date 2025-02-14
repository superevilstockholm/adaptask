from migrations.create_database import create_database
from migrations.create_tableusers import create_table_users

import argparse

import asyncio

parser = argparse.ArgumentParser()
parser.add_argument("--create-database", action="store_true")
parser.add_argument("--create-table-users", action="store_true")

parser.add_argument("--migrate-all", action="store_true")
args = parser.parse_args()

if args.create_database:
    asyncio.run(create_database())

if args.create_table_users:
    asyncio.run(create_table_users())

if args.migrate_all:
    asyncio.run(create_database())
    asyncio.run(create_table_users())