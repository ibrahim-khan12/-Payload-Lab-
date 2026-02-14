"""
Payload Lab - Core Data Models
Educational payload template framework aligned with OWASP standards

⚠️ EDUCATIONAL USE ONLY - NO LIVE EXPLOITATION
"""

from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from datetime import datetime


@dataclass
class Payload:
    """Base payload template model"""
    id: str
    category: str
    template: str
    explanation: str
    defensive_notes: str
    created_at: str = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert payload to dictionary"""
        return asdict(self)


@dataclass
class XSSPayload(Payload):
    """XSS-specific payload template"""
    type: str = None  # reflected, stored, dom
    context: str = None  # html, attribute, javascript
    bypass_technique: str = None
    
    def __post_init__(self):
        super().__post_init__()
        if self.category != "xss":
            self.category = "xss"


@dataclass
class SQLiPayload(Payload):
    """SQL Injection payload template"""
    db: str = None  # mysql, postgres, mssql
    injection_type: str = None  # error-based, union-based, blind
    
    def __post_init__(self):
        super().__post_init__()
        if self.category != "sqli":
            self.category = "sqli"


@dataclass
class CMDiPayload(Payload):
    """Command Injection payload template"""
    os: str = None  # linux, windows
    pattern_type: str = None  # separator, substitution, redirection
    
    def __post_init__(self):
        super().__post_init__()
        if self.category != "cmdi":
            self.category = "cmdi"


@dataclass
class PayloadCollection:
    """Collection of payload templates"""
    name: str
    description: str
    payloads: list
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {
                "created_at": datetime.now().isoformat(),
                "version": "1.0.0",
                "framework": "payload_lab",
                "warning": "EDUCATIONAL TEMPLATES ONLY - DO NOT USE FOR UNAUTHORIZED TESTING"
            }
    
    def add_payload(self, payload: Payload):
        """Add a payload to the collection"""
        self.payloads.append(payload)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert collection to dictionary"""
        return {
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "payloads": [p.to_dict() for p in self.payloads]
        }
