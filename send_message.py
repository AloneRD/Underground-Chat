import asyncio
import json
import logging
import logging.config
from typing import NoReturn

import aiofiles

from cli import CLI
from connect import connect_to_chat

logger = logging.getLogger('sender')


async def authentication(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, user_token: str) -> str:
    """Аутентификация пользователя по токену"""

    await reader.readline()
    writer.write(f'{user_token}\n'.encode())
    await writer.drain()
    data = await reader.readline()
    response = json.loads(data.decode())
    if response is None:
        raise ConnectionError('Неизвестный токен. Проверьте его или зарегистрируйтесь заново.')
    print(f"Welcome to chat! \n{response}")
    return data.decode()


async def register_new_user(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, username: str) -> NoReturn:
    """Регистрация нового пользователя"""

    await reader.readline()
    await write_messages(writer, '\n')
    await reader.readline()
    await write_messages(writer, f'{username}\n')
    data = await reader.readline()
    async with aiofiles.open(f'{username}.token', 'w') as token_file:
        await token_file.write(data.decode())


async def send_message(writer: asyncio.StreamWriter, reader: asyncio.StreamReader, message: str) -> NoReturn:
    """Отправка нового сообщения"""

    await reader.readline()
    logger.info("Hello")
    await write_messages(writer, f'{message}\n\n')
    data = await reader.readline()
    print(data.decode())


async def write_messages(writer: asyncio.StreamWriter, message: str) -> None:
    """Запись сообщения в сокет"""
    
    writer.write(message.encode())
    await writer.drain()

async def main():
    logging.config.fileConfig(fname='logging.ini', disable_existing_loggers=False)
    cli = CLI()
    args = cli.parser.parse_args()

    user_token = args.token
    user_name = args.username

    while True:
        async with connect_to_chat(args.host, args.port) as conn:
            reader, writer = conn


            if user_token:
                await authentication(reader, writer, user_token)
            elif user_name:
                await register_new_user(reader, writer, user_name)
            else:
                raise SystemExit("Неверные параметры")
            message = input('Enter your message: ')
            await send_message(writer, reader, message)


if __name__ == "__main__":
    asyncio.run(main())
