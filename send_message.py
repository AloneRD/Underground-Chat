import asyncio
import logging
import logging.config
from typing import NoReturn

from cli import CLI
from connect import connection_chat

logging.config.fileConfig(fname='logging.ini', disable_existing_loggers=False)
logger = logging.getLogger('sender')


async def authentication(reader:asyncio.StreamReader, writer:asyncio.StreamWriter, user_token:str) -> str:
    """Аутентификация пользователя по токену"""
    
    await reader.readline()
    writer.write(f'{user_token}\n'.encode())
    await writer.drain()
    data = await reader.readline()
    print(f"Welcome to chat! \n{data.decode()}")
    return data.decode()
    

async def send_message(writer:asyncio.StreamWriter, reader:asyncio.StreamReader)-> NoReturn:
    """Отправка нового сообщения"""

    await reader.readline()
    while True:
        message = input('Enter your message: ')
        logger.info("Hello")
        writer.write(f'{message}\n\n'.encode())
        await writer.drain()

        data = await reader.readline()
        print(data.decode())


async def main():
    cli = CLI()
    args = cli.parser.parse_args()

    user_token = args.token
    reader, writer = await connection_chat(args.host, args.port)

    if user_token is not None:
        await authentication(reader, writer, user_token)
    await send_message(writer,reader)
    

if __name__ == "__main__":
    asyncio.run(main())
