import asyncio
from typing import NoReturn
from datetime import datetime

import aiofiles


async def read_chat(ip: str, port: int) -> NoReturn:
    """Чтения переписки чата"""
    
    reader, writer = await asyncio.open_connection(ip, port)
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


def main():
    ip = 'minechat.dvmn.org'
    port = 5000
    asyncio.run(read_chat(ip, port))


if __name__ == "__main__":
    main()