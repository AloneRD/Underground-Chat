import asyncio
from typing import NoReturn


async def echo_client(ip: str, port: int) -> NoReturn:
    """Установка соединения с чатом"""
    reader, writer = await asyncio.open_connection(ip, port)
    while True:
        message = await reader.readline()
        print(message.decode())


def main():
    ip = 'minechat.dvmn.org'
    port = 5000
    asyncio.run(echo_client(ip, port))


if __name__ == "__main__":
    main()