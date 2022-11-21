import asyncio
from typing import Tuple


async def connect_to_chat(ip: str, port: int) -> Tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    """Установка соединения с чатом"""
    reader, writer = await asyncio.open_connection(ip, port)
    return reader, writer
