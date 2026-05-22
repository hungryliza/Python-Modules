from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id : str = Field(min_length=3, max_length=10)
    name : str = Field(min_length=1, max_length=50)
    crew_size : int = Field(ge=1, le=20)
    power_level : float = Field(ge=0.0, le=100.0)
    oxygen_level : float = Field(ge=0.0, le=100.0)
    last_maintenance : datetime
    is_operational : bool = Field(default=True)
    notes : Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    space_station = SpaceStation(station_id = "ISS001",
    name = "International Space Station",
    crew_size = 6,
    power_level =  85.5,
    oxygen_level = 92.3,
    last_maintenance = "2026-05-22T16:41:00",
    is_operational = True)
    for el in space_station:
        if el[0] == "station_id":
            print(f"ID: {el[1]}")
        if el[0] == "name":
            print(f"Name: {el[1]}")
        if el[0] == "crew_size":
            print(f"Crew: {el[1]} people")
        if el[0] == "power_level":
            print(f"Power: {el[1]}%")
        if el[0] == "oxygen_level":
            print(f"Oxygen: {el[1]}%")
        if el[0] == "is_operational" and el[1] is True:
            print("Status: Operational")
        if el[0] == "is_operational" and el[1] is False:
            print("Status: Non Operational")
    print("\n========================================")
    print("Expected validation error:")
    try:
        space_station = SpaceStation(station_id = "ISS001",
        name = "International Space Station",
        crew_size = 21,
        power_level =  85.5,
        oxygen_level = 92.3,
        last_maintenance = "2026-05-22T16:41:00",
        is_operational = True)
    except ValidationError as e:
        errordict = e.errors()
        for el in errordict:
            print(el.get("msg"))
