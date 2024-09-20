from abc import ABC, abstractmethod


class FileBase(ABC):
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def edit(self):
        pass


class Json(FileBase):
    def edit(self):
        pass


class Xml(FileBase):
    def edit(self):
        pass


xml_file = Xml('xml')
json_file = Json('json')
files = [xml_file, json_file]
for file in files:
    file.edit()

