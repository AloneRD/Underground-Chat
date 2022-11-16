import argparse


class CLI():
    """Интерфейс командной строки"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Chat',
            description='Underground chat'
        )

        self.parser.add_argument('--host', required=True, help="Chat Ip address")
        self.parser.add_argument('--port', required=True, help="Chat port")

        self.parser.add_argument('--username', help="Registrational of new user")
        self.parser.add_argument('--token', help="User token")
