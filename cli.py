import argparse


class CLI():
    """Интерфейс командной строки"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Chat',
            description='Underground chat'
        )

        self.parser.add_argument('--host', help="Chat Ip address")
        self.parser.add_argument('--port', help="Chat port")
        self.parser.add_argument('--token', help="User token")
