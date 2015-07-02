
class WgetFile:

    """ WgetFile is a File Data Container object """

    def __init__(
        self,
        name,
        content="Test Contents",
        timestamp=None,
        rules=None,
        parent=None,
        isdir=False
	):
        self.name = name
        self.content = content
        self.timestamp = timestamp
        self.rules = rules or {}
        self.parent = parent
        self.isdir = isdir
