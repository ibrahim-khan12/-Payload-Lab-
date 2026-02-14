"""
Payload Lab - Educational Payload Template Framework
Version: 1.0.0

⚠️ EDUCATIONAL USE ONLY - AUTHORIZED TESTING ENVIRONMENTS ONLY ⚠️

Aligned with OWASP Code of Ethics
"""

__version__ = '1.0.0'
__author__ = 'Payload Lab Project'
__license__ = 'Educational Use Only'

from .core import (
    Payload,
    XSSPayload,
    SQLiPayload,
    CMDiPayload,
    PayloadCollection,
    PayloadEncoder,
    PayloadExporter
)

from .modules import XSSModule, SQLiModule, CMDiModule

__all__ = [
    'Payload',
    'XSSPayload',
    'SQLiPayload',
    'CMDiPayload',
    'PayloadCollection',
    'PayloadEncoder',
    'PayloadExporter',
    'XSSModule',
    'SQLiModule',
    'CMDiModule',
]


def get_version():
    """Return version string"""
    return __version__


def show_disclaimer():
    """Display ethics and safety disclaimer"""
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                          PAYLOAD LAB v1.0.0                               ║
║               Educational Payload Template Framework                      ║
╚═══════════════════════════════════════════════════════════════════════════╝

⚠️  ETHICS & SAFETY DISCLAIMER ⚠️

This framework generates EDUCATIONAL payload templates for:
  ✓ Security training and education
  ✓ Authorized penetration testing with written permission
  ✓ Understanding defensive security controls

PROHIBITED USE:
  ✗ Unauthorized security testing
  ✗ Malicious attacks or exploitation
  ✗ Any illegal or unethical activity

By using this framework, you agree to:
  • Use it only in authorized environments
  • Comply with all applicable laws and regulations
  • Follow OWASP Code of Ethics
  • Never harm or compromise systems without permission

NO WARRANTY: This software is provided "as is" without warranty of any kind.

════════════════════════════════════════════════════════════════════════════
    """)
