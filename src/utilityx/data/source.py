from abc import abstractmethod

from utilityx.data.access import Access
from utilityx.data.format.format import Format


class Source(ABC):
    def __init__(self, type:Type, format:Format, access:Access):
        self._type = type
        self._format = format
        self._access = access


    @abstractmethod
    def get_content(self):
        pass
