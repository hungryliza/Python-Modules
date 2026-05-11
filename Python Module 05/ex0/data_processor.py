from abc import ABC, abstractmethod
from typing import Any 

class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.total = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    def output(self) -> tuple[int, str]:
        first_item = self.storage.pop(0)
        return (self.total - len(self.storage), first_item)

class NumericProcessor(DataProcessor):
    def validate(self, data:int | float | list[int | float]) -> bool:
        res = (isinstance(data, int) or isinstance(data, float)) and not isinstance(data, bool)
        if isinstance(data, list) and len(data) > 0:
            res = all((isinstance(x, int) or isinstance(x, float)) 
                      and not isinstance(x, bool) for x in data)
        return res
    def ingest(self, data:int | float | list[int | float]) -> None:
        to_check = self.validate(data)
        if to_check is True and (isinstance(data, int) or isinstance(data, float)):
            data = str(data)
            self.storage.append(data)
            self.total += 1
        elif to_check is True and isinstance(data, list):
            for el in data:
                el = str(el)
                self.storage.append(el)
                self.total += 1
        else:
            raise Exception

class TextProcessor(DataProcessor):
    def validate(self, data:str | list[str]) -> bool:
        res = isinstance(data, str)
        if isinstance(data, list) and len(data) > 0:
            res = all(isinstance(x, str) for x in data)
        return res
    def ingest(self, data:str | list[str]) -> None:
        to_check = self.validate(data)
        if to_check is True and isinstance(data, str):
            self.storage.append(data)
            self.total += 1
        elif to_check is True and isinstance(data, list):
            for el in data:
                self.storage.append(el)
                self.total += 1
        else:
            raise Exception

class LogProcessor(DataProcessor):
    def validate(self, data:dict[str,str] | list[dict[str, str]]) -> bool:
        if isinstance(data, dict):
            data_unpacker = data.items()
            res = all(isinstance(key, str) and isinstance(value, str) for key, value in data_unpacker)
            return res
        elif isinstance(data, list) and len(data) > 0:
            res = all(isinstance(x, dict) 
                      and all((isinstance(key, str) 
                               and isinstance(value, str) for key, value in x.items())) for x in data)
            return res
        else:
            return False
    def ingest(self, data:dict[str,str] | list[dict[str, str]]) -> None:
        to_check = self.validate(data)
        if to_check is True and isinstance(data, dict):
            tuptostr = ": ".join(data.values())
            self.storage.append(tuptostr)
            self.total += 1
        elif to_check is True and isinstance(data, list):
            for el in data:
                tuptostr = ": ".join(el.values())
                self.storage.append(tuptostr)
                self.total += 1
        else:
            raise Exception

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric_check = NumericProcessor()
    print(f"Trying to validate input '42': {numeric_check.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric_check.validate("Hello")}")
    print(f"Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_check.ingest("foo")
    except:
        print("Got exception: Improper numeric data")
    lst = [1, 2, 3, 4, 5]
    try:
        numeric_check.ingest(lst)
        print(f"Processing data: [1, 2, 3, 4, 5]")
        print("Extracting 3 values...")
        for i in range(0, 3):
            rank, value = numeric_check.output()
            print(f"Numeric value {i}: {value}")
    except:
        print("Got exception: Improper numeric data")

    print("\nTesting Text Processor...")
    text_check = TextProcessor()
    print(f"Trying to validate input '42': {text_check.validate(42)}")
    lststr = ['Hello', 'Nexus', 'World']
    try:
        text_check.ingest(lststr)
        print(f"Processing data: ['Hello', 'Nexus', 'World']")
        print("Extracting 1 value...")
        rank, value = text_check.output()
        print(f"Text value 0: {value}")
    except:
        print("Got exception: Improper text data")

    print("\nTesting Log Processor...")
    log_check = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_check.validate("Hello")}")
    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {data}")
    print("Extracting 2 values...")
    log_check.ingest(data)
    rank, value = log_check.output()
    print(f"Log entry 0: {value}")
    rank, value = log_check.output()
    print(f"Log entry 1: {value}")
