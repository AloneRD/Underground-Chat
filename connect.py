import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def connect_to_chat(ip: str, port: int):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        yield reader, writer
    finally:
        await writer.wait_closed()
