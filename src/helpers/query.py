
from typing import List, TypeVar

KeyName = str
Value = TypeVar('Value')


class Query:
    def __init__(self, query_dict: dict):
        self.table_name: str = query_dict.get('table_name', '')
        self.equals_to: List[List[KeyName, Value]
                             ] = query_dict.get('equals_to', [])
        self.starts_with: List[List[KeyName, Value]
                               ] = query_dict.get('starts_with', [])
