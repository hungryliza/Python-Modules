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
    def __init__(self):
        super().__init__()
        self.name = "Numeric Processor"

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
    def __init__(self):
        super().__init__()
        self.name = "Text Processor"

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
    def __init__(self):
        super().__init__()
        self.name = "Log Processor"

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

class DataStream:
    def __init__(self):
        self.processorslst = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processorslst.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for el in stream:
            checked = False
            for proc in self.processorslst:
                    if proc.validate(el):
                        proc.ingest(el)
                        checked = True
                        break
            if checked == False:
                print(f"DataStream error - Can't process element in stream: {el}")

    def print_processors_stats(self) -> None:
        if len(self.processorslst) != 0:
            for proc in self.processorslst:
                if proc:
                    print(f"{proc.name} : "
                        f"total {proc.total}"
                        f" items processed, remaining {len(proc.storage)} on processor")
                else:
                    print("No processor found, no data")
        else:
            print("No processor found, no data")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    print("== DataStream statistics ==")
    streamy = DataStream()
    numeric_check = NumericProcessor()
    text_check = TextProcessor()
    log_check = LogProcessor()
    streamy.print_processors_stats()
    streamy.register_processor(numeric_check)
    print(f"\nRegistering {numeric_check.name}")
    data = ['Hello world', [3.14, -1, 2.71], 
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {data}")
    streamy.process_stream(data)

    print("== DataStream statistics ==")
    streamy.print_processors_stats()
    print(f"\nRegistering other data processors")
    print(f"Send the same batch again")
    print("== DataStream statistics ==")
    streamy.register_processor(text_check)
    streamy.register_processor(log_check)
    streamy.process_stream(data)
    streamy.print_processors_stats()
    for j in range(0, 3):
        numeric_check.output()
    for i in range(0, 2):
        text_check.output()
    rank, value = log_check.output()
    print(f"\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")

    print("== DataStream statistics ==")
    streamy.print_processors_stats()