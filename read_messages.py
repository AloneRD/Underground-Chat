import asyncio
import logging
import logging.config
from datetime import datetime
from typing import NoReturn

import aiofiles

from cli import CLI
from connect import connect_to_chat

logger = logging.getLogger('sender')


async def read_chat(reader) -> NoReturn:
    """Чтения переписки чата"""

    async with aiofiles.open('messages_history.log', 'a', encoding='utf-8') as history_file:
        datetime_at = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')
        while True:
            data = await reader.readline()
            message = f'[{datetime_at}] {data.decode()}'
            print(message)
            await history_file.write(message)


async def main():
    logging.config.fileConfig(fname='logging.ini', disable_existing_loggers=False)
    cli = CLI()
    args = cli.parser.parse_args()

    async with connect_to_chat(args.host, args.port) as conn:
        reader, writer = conn
        await read_chat(reader)


if __name__ == "__main__":
    asyncio.run(main())
