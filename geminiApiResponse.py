from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Part:
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Part':
        _text = str(obj.get("text"))
        return Part(_text)

@dataclass
class Content:
    parts: List[Part]
    role: str

    @staticmethod
    def from_dict(obj: Any) -> 'Content':
        _parts = [Part.from_dict(y) for y in obj.get("parts")]
        _role = str(obj.get("role"))
        return Content(_parts, _role)

@dataclass
class SafetyRating:
    category: str
    probability: str

    @staticmethod
    def from_dict(obj: Any) -> 'SafetyRating':
        _category = str(obj.get("category"))
        _probability = str(obj.get("probability"))
        return SafetyRating(_category, _probability)
    
@dataclass
class PromptFeedback:
    safetyRatings: List[SafetyRating]

    @staticmethod
    def from_dict(obj: Any) -> 'PromptFeedback':
        _safetyRatings = [SafetyRating.from_dict(y) for y in obj.get("safetyRatings")]
        return PromptFeedback(_safetyRatings)
    
@dataclass
class Candidate:
    content: Content
    finishReason: str
    index: int
    safetyRatings: List[SafetyRating]

    @staticmethod
    def from_dict(obj: Any) -> 'Candidate':
        _content = Content.from_dict(obj.get("content"))
        _finishReason = str(obj.get("finishReason"))
        _index = int(obj.get("index"))
        _safetyRatings = [SafetyRating.from_dict(y) for y in obj.get("safetyRatings")]
        return Candidate(_content, _finishReason, _index, _safetyRatings)

@dataclass
class GeminiResponse:
    candidates: List[Candidate]
    promptFeedback: PromptFeedback

    @staticmethod
    def from_dict(obj: Any) -> 'GeminiResponse':
        _candidates = [Candidate.from_dict(y) for y in obj.get("candidates")]
        _promptFeedback = PromptFeedback.from_dict(obj.get("promptFeedback"))
        return GeminiResponse(_candidates, _promptFeedback)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)