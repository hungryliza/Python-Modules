from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional

class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def verif(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and self.is_verified is False:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and len(self.message_received) == 0:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self

if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("========================================")
    print("Valid contact report:")
    alien_contact = AlienContact(contact_id="AC_2024_001",
    timestamp="2026-05-22T16:41:00",
    location="Area 51, Nevada",
    contact_type ="radio",
    signal_strength=8.5,
    duration_minutes=45,
    witness_count=5,
    message_received="'Greetings from Zeta Reticuli'")
    for el in alien_contact:
        if el[0] == "contact_id":
            print(f"ID: {el[1]}")
        if el[0] == "contact_type":
            splitted = str(el[1]).split(".")
            print(f"Type: {splitted[1]}")
        if el[0] == "location":
            print(f"Location: {el[1]}")
        if el[0] == "signal_strength":
            print(f"Signal: {el[1]}/10")
        if el[0] == "duration_minutes":
            print(f"Oxygen: {el[1]} minutes")
        if el[0] == "witness_count":
            print(el[1])
        if el[0] == "message_received":
            print(el[1])
    print("\n========================================")
    print("Expected validation error:")
    try:
        alien_contact = AlienContact(contact_id="AC_2024_001",
        timestamp="2026-05-22T16:41:00",
        location="Area 51, Nevada",
        contact_type ="telepathic",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=1,
        message_received="'Greetings from Zeta Reticuli'")
    except ValidationError as e:
        errordict = e.errors()
        for el in errordict:
            print(el.get("msg").removeprefix("Value error, "))
