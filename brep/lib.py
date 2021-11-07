import os
import pathlib
import gzip


class File():
    def __init__(self, file) -> None:
        if isinstance(file, str):
            self.path = pathlib.Path(file)
        elif isinstance(file, pathlib.Path):
            self.path = file
        else:
            raise Exception("Please prove a str of pathlib.Path file.")

        self.gzip = self.path.suffix == ".gz"

        if self.gzip:
            self.file = gzip.open(self.path, 'rb')
        else:
            self.file = open(file, "r")

    def seek(self, position):
        return self.file.seek(position)

    def tell(self):
        return self.file.tell()

    def readline(self):
        line = self.file.readline()

        if self.gzip:
            line = line.decode()

        return line

    def __iter__(self):
        for line in self.file:
            if self.gzip:
                line = line.decode()
            yield line

    def __exit__(self):
        self.file.close()

    def __len__(self):
        if self.gzip:
            pipe_in = os.popen(f'gzip -l "{self.path}"')
            return int(pipe_in.readlines()[1].split()[1])
        else:
            return os.path.getsize(self.path)


class Search():
    def __init__(self, prefix, filepath) -> None:
        self.file = File(filepath)
        self.prefix = prefix

    def __iter__(self):
        left, right = 0, len(self.file) - 1

        while left <= right:
            mid = int((left + right) / 2)
            self.file.seek(mid)
            self.file.readline()
            value = self.file.readline().strip()

            if self.prefix <= value or value.startswith(self.prefix):
                right = mid - 1
            else:
                left = mid + 1

        self.file.seek(left)
        self.file.readline()

        for line in self.file:
            if not line.startswith(self.prefix):
                break
            yield line.strip()
