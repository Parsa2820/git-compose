class Service:
    def __init__(self, name: str, url: str, branches: list):
        self.name = name
        self.url = url
        self.branches = branches

    @classmethod
    def from_dict(cls, name: str, data: dict):
        existing_branches = [Branch(x) for x in data["branches"]["existing"]]
        new_branches = [Branch(x["name"], x["from"]) for x in data["branches"]["new"]]
        return cls(name, data["url"], existing_branches + new_branches)


class Branch:
    def __init__(self, name: str, _from: str = None):
        self.name = name
        self.base = _from

