import asyncio
from typing import Tuple
from contextlib import asynccontextmanager

@asynccontextmanager
async def connect_to_chat(ip: str, port: int):
    conn = await asyncio.open_connection(ip, port)
    try:
        reader, writer = conn
        yield reader, writer
    finally:
        writer.close()

