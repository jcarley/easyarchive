class FakeFileSystem(list):

    def __init__(self, read_result=None):
        super().__init__()
        self.read_result = read_result

    def copy(self, src, dest):
        self.append(('COPY', src, dest))

    def move(self, src, dest):
        self.append(('MOVE', src, dest))

    def delete(self, dest):
        self.append(('DELETE', dest))

    def write_text(self, source, data):
        self.append(('WRITE', source, data))

    def read_text(self, source):
        self.append(('READ', source))
        return self.read_result
