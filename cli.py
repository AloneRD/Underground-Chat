import argparse


class CLI():
    """Интерфейс командной строки"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Chat',
            description='Underground chat'
        )

        self.parser.add_argument('--host', required=True, default='chat.org', help="Chat Ip address")
        self.parser.add_argument('--port', default=5000, help="Chat port")

        self.parser.add_argument('--username', help="Registrational of new user")
        self.parser.add_argument('--token', help="User token")
