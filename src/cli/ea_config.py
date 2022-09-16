from dataclasses import dataclass

from dataclasses_json import dataclass_json, Undefined, LetterCase


@dataclass_json(undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL)
@dataclass
class EAConfig:
    sources: []
    destination: str
