import asyncio
from datetime import datetime
from typing import NoReturn

import aiofiles


async def connection_chat(ip: str, port: int):
    """Установка соединения с чатом"""
    reader, writer = await asyncio.open_connection(ip, port)
    return (reader, writer)


async def read_chat(reader) -> NoReturn:
    """Чтения переписки чата"""

    datetime_at = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
    while True:
        data = await reader.readline()
        message = f'[{datetime_at}] {data.decode()}'
        print(message)
        await save_messages_history(message)


async def save_messages_history(message:str)->NoReturn:
    """Записывает сообщения в файл"""

    async with aiofiles.open('messages_history.log', 'a') as history_file:
        await history_file.write(message)


async def main():
    ip = 'minechat.dvmn.org'
    port = 5000
    reader, writer = await connection_chat(ip, port)

    await read_chat(reader)


if __name__ == "__main__":
    asyncio.run(main())