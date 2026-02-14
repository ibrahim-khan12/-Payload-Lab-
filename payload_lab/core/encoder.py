"""
Payload Lab - Encoding Demonstrations
Shows how attackers use encoding to evade basic filters

⚠️ EDUCATIONAL DEMONSTRATIONS ONLY
"""

import base64
import urllib.parse
from typing import List, Dict


class PayloadEncoder:
    """Educational encoding demonstrations for payload obfuscation"""
    
    @staticmethod
    def url_encode(payload: str, double: bool = False) -> str:
        """
        URL encoding demonstration
        
        Args:
            payload: The payload template to encode
            double: Apply double encoding (common WAF bypass attempt)
        
        Returns:
            URL-encoded payload
        """
        encoded = urllib.parse.quote(payload)
        if double:
            encoded = urllib.parse.quote(encoded)
        return encoded
    
    @staticmethod
    def base64_encode(payload: str) -> str:
        """
        Base64 encoding demonstration
        
        Common in:
        - Data exfiltration attempts
        - Command obfuscation
        - Payload smuggling
        
        Args:
            payload: The payload template to encode
        
        Returns:
            Base64-encoded payload
        """
        encoded_bytes = base64.b64encode(payload.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    
    @staticmethod
    def hex_encode(payload: str) -> str:
        """
        Hexadecimal encoding demonstration
        
        Common in:
        - SQL injection (0x... syntax)
        - JavaScript string obfuscation
        - Binary data representation
        
        Args:
            payload: The payload template to encode
        
        Returns:
            Hex-encoded payload
        """
        return ''.join([f'\\x{ord(c):02x}' for c in payload])
    
    @staticmethod
    def html_entity_encode(payload: str) -> str:
        """
        HTML entity encoding demonstration
        
        Used in XSS bypass attempts:
        - Numeric entities (&#...)
        - Named entities (&lt;, &gt;)
        
        Args:
            payload: The payload template to encode
        
        Returns:
            HTML entity-encoded payload
        """
        entities = {
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;',
            '&': '&amp;'
        }
        result = payload
        for char, entity in entities.items():
            result = result.replace(char, entity)
        return result
    
    @staticmethod
    def mixed_case(payload: str) -> str:
        """
        Case variation demonstration
        
        Attempts to bypass case-sensitive filters
        Example: <ScRiPt> vs <script>
        
        Args:
            payload: The payload template to vary
        
        Returns:
            Mixed-case payload
        """
        result = []
        for i, char in enumerate(payload):
            if i % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
        return ''.join(result)
    
    @staticmethod
    def comment_insertion(payload: str, comment_type: str = "sql") -> str:
        """
        Comment insertion demonstration
        
        Shows how attackers insert comments to bypass:
        - Pattern matching
        - Signature detection
        - Keyword filters
        
        Args:
            payload: The payload template
            comment_type: Type of comment (sql, html, javascript)
        
        Returns:
            Payload with inserted comments
        """
        if comment_type == "sql":
            # SQL comment insertion: SEL/**/ECT
            keywords = ["SELECT", "UNION", "WHERE", "FROM", "AND", "OR"]
            result = payload
            for keyword in keywords:
                if keyword in result:
                    mid = len(keyword) // 2
                    result = result.replace(
                        keyword,
                        f"{keyword[:mid]}/*comment*/{keyword[mid:]}"
                    )
            return result
        
        elif comment_type == "html":
            # HTML comment insertion
            return payload.replace('<', '<!--><')
        
        elif comment_type == "javascript":
            # JavaScript comment insertion
            return payload.replace(';', ';/*comment*/')
        
        return payload
    
    @staticmethod
    def unicode_encode(payload: str) -> str:
        """
        Unicode encoding demonstration
        
        Shows Unicode escape sequences:
        - \u0061 for 'a'
        - Used in JavaScript context
        
        Args:
            payload: The payload template to encode
        
        Returns:
            Unicode-encoded payload
        """
        return ''.join([f'\\u{ord(c):04x}' for c in payload])
    
    @staticmethod
    def get_encoding_variations(payload: str) -> Dict[str, str]:
        """
        Generate all encoding variations for educational purposes
        
        Args:
            payload: The base payload template
        
        Returns:
            Dictionary of encoding type -> encoded payload
        """
        encoder = PayloadEncoder()
        
        return {
            "original": payload,
            "url_encoded": encoder.url_encode(payload),
            "double_url_encoded": encoder.url_encode(payload, double=True),
            "base64": encoder.base64_encode(payload),
            "hex": encoder.hex_encode(payload),
            "html_entities": encoder.html_entity_encode(payload),
            "mixed_case": encoder.mixed_case(payload),
            "unicode": encoder.unicode_encode(payload),
            "sql_comments": encoder.comment_insertion(payload, "sql"),
            "defensive_note": "Modern WAFs use multiple detection layers. Encoding alone rarely bypasses proper security controls."
        }
