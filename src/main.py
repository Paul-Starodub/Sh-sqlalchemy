import asyncio
from src.queries.orm import create_tables, insert_data


create_tables()
# insert_data()  # sync version

asyncio.run(insert_data())  # async version
