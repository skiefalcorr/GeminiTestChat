import json

from typing import List
from typing import Any
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Part:
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Part':
        _text = str(obj.get('text'))
        return Part(_text)
    
@dataclass
class Content:
    role: str
    parts: List[Part]

    @staticmethod
    def from_dict(obj: Any) -> 'Content':
        _role = str(obj.get('role'))
        _parts = [Part.from_dict(y) for y in obj.get('parts')]
        return Content(_role, _parts)
    
@dataclass
class SafetySetting:
    category: str
    threshold: str

    @staticmethod
    def from_dict(obj: Any) -> 'SafetySetting':
        _category = str(obj.get('category'))
        _threshold = str(obj.get('threshold'))
        return SafetySetting(_category, _threshold)

@dataclass
class GenerationConfig:
    stopSequences: List[str]
    temperature: float
    maxOutputTokens: int
    topP: float
    topK: int

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationConfig':
        _stopSequences = [str.from_dict(y) for y in obj.get('stopSequences')]
        _temperature = float(obj.get('temperature'))
        _maxOutputTokens = int(obj.get('maxOutputTokens'))
        _topP = float(obj.get('topP'))
        _topK = int(obj.get('topK'))
        return GenerationConfig(_stopSequences, _temperature, _maxOutputTokens, _topP, _topK)

@dataclass
class GeminiRequest:
    contents: List[Content]
    safetySettings: List[SafetySetting]
    generationConfig: GenerationConfig

    @staticmethod
    def from_dict(obj: Any) -> 'GeminiRequest':
        _contents = [Content.from_dict(y) for y in obj.get('contents')]
        _safetySettings = [SafetySetting.from_dict(y) for y in obj.get('safetySettings')]
        _generationConfig = GenerationConfig.from_dict(obj.get('generationConfig'))
        return GeminiRequest(_contents, _safetySettings, _generationConfig)
    
    def to_dict(self):
        data = asdict(self)
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

    def to_json(self):
        # def remove_none(d):
        #     return {k: remove_none(v) for k, v in d.items() if v is not None}
        data = asdict(self)
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return json.dumps(filtered_data)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
