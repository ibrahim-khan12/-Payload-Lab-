"""
Payload Lab - Vulnerability Modules
Educational payload generators
"""

from .xss import XSSModule
from .sqli import SQLiModule
from .cmdi import CMDiModule

__all__ = ['XSSModule', 'SQLiModule', 'CMDiModule']
