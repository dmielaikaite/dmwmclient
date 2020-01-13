import asyncio


class Test:
    @classmethod
    def register(cls, subparsers):
        parser = subparsers.add_parser(
            'test',
            help='Test connections'
        )
        parser.set_defaults(command=cls)
        return parser

    def __init__(self, *, client=None, datasvc=None, **_):
        self.client = client
        self.datasvc = datasvc
        asyncio.run(self.go())

    async def go(self):
        res = await self.datasvc.jsonmethod('bounce', asdf='hi there')
        print("DataSvc bounce test:", res)
