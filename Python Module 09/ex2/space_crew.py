from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import List

class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id : str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id : str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)
    
    @model_validator(mode='after')
    def verif(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(member.rank in (Rank.captain, Rank.commander) for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")
        inexperienced = 0
        for member in self.crew:
            if member.years_experience < 5:
                inexperienced += 1
        if self.duration_days > 365 and ((len(self.crew) / 2) < inexperienced):
            raise ValueError(r"Long missions (> 365 days) need 50% experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("========================================")
    print("Valid mission created:")
    space_mission = SpaceMission(mission_id="M2024_MARS",
    mission_name="Mars Colony Establishment",
    destination="Mars",
    launch_date="2026-05-22T16:41:00",
    duration_days=900,
    crew=[CrewMember(member_id="IDSarah",
    name="Sarah Connor",
    age=33,
    rank=Rank.commander,
    specialization="Mission Command",
    years_experience=30),
    CrewMember(member_id="IDJohn",
    name="John Smith",
    age=33,
    rank=Rank.lieutenant,
    specialization="Navigation",
    years_experience=30),
    CrewMember(member_id="IDAlice",
    name="Alice Johnson",
    age=33,
    rank=Rank.officer,
    specialization="Engineering",
    years_experience=30)],
    budget_millions=2500.0)
    for el in space_mission:
        if el[0] == "mission_name":
            print(f"Mission: {el[1]}")
        if el[0] == "mission_id":
            print(f"ID: {el[1]}")
        if el[0] == "destination":
            print(f"Destination: {el[1]}")
        if el[0] == "duration_days":
            print(f"Duration: {el[1]} days")
        if el[0] == "budget_millions":
            print(f"Budget: ${el[1]}M")
        if el[0] == "crew":
            print(f"Crew size: {len(el[1])}")
            for ele in el[1]:
                print(f"- {ele.name} "
                      f"({str(ele.rank).removeprefix("Rank.")}) - {ele.specialization}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        space_mission = SpaceMission(mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-05-22T16:41:00",
        duration_days=900,
        crew=[CrewMember(member_id="IDSarah",
        name="Sarah Connor",
        age=33,
        rank=Rank.cadet,
        specialization="Mission Command",
        years_experience=30),
        CrewMember(member_id="IDJohn",
        name="John Smith",
        age=33,
        rank=Rank.cadet,
        specialization="Navigation",
        years_experience=30),
        CrewMember(member_id="IDAlice",
        name="Alice Johnson",
        age=33,
        rank=Rank.cadet,
        specialization="Engineering",
        years_experience=30)],
        budget_millions=2500.0)
    except ValidationError as e:
        errordict = e.errors()
        for el in errordict:
            print(el.get("msg").removeprefix("Value error, "))
