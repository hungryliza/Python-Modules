from abc import ABC, abstractmethod
from typing import Any, Protocol


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
        return ((self.total - len(self.storage)) - 1, first_item)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processorslst:
            res = []
            print(f"{type(plugin).__name__} Output:")
            for i in range(0, nb):
                if len(proc.storage) > 0:
                    res.append(proc.output())
            plugin.process_output(res)



class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSV:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        lstval = []
        for el in data:
            val = str(el[1])
            lstval.append(val)
        formatted = ",".join(lstval)
        print(formatted)


class JSON:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        dictval = {}
        lst= []
        for el in data:
            key = "item_" + str(el[0])
            val = el[1]
            dictval[key] = val
        for key, val in dictval.items():
            lst.append(f'"{key}" : "{val}"')
        print("{" + ", ".join(lst) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    print("== DataStream statistics ==")
    streamy = DataStream()
    numeric_check = NumericProcessor()
    text_check = TextProcessor()
    log_check = LogProcessor()
    streamy.print_processors_stats()
    streamy.register_processor(numeric_check)
    streamy.register_processor(text_check)
    streamy.register_processor(log_check)
    print(f"\nRegistering Processors")
    data = ['Hello world', [3.14, -1, 2.71], 
            [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    print("\n== DataStream statistics ==")
    streamy.process_stream(data)
    streamy.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv = CSV()
    json = JSON()
    streamy.output_pipeline(3, csv)

    print("\n== DataStream statistics ==")
    streamy.print_processors_stats()
    data = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
             {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
             [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data: {data}")
    print("\n== DataStream statistics ==")
    streamy.process_stream(data)
    streamy.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    streamy.output_pipeline(5, json)
    print("\n== DataStream statistics ==")
    streamy.print_processors_stats()