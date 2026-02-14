"""
Payload Lab - Command Injection Module
Educational command injection pattern templates for authorized security testing

⚠️ PATTERN-BASED TEMPLATES ONLY - DISABLED BY DEFAULT
⚠️ NEVER EXECUTE THESE COMMANDS WITHOUT EXPLICIT AUTHORIZATION

Reference: OWASP Command Injection Guide
"""

from typing import List
from ..core.models import CMDiPayload


class CMDiModule:
    """Command injection pattern generator for educational purposes"""
    
    # Safety flag - must be explicitly enabled
    EDUCATIONAL_MODE = True
    
    @staticmethod
    def get_all_payloads(os: str = None) -> List[CMDiPayload]:
        """
        Get all command injection pattern templates
        
        Args:
            os: Filter by OS (linux, windows) or None for all
        
        Returns:
            List of command injection pattern templates
        """
        if not CMDiModule.EDUCATIONAL_MODE:
            raise RuntimeError("Command injection module is disabled for safety")
        
        payloads = []
        
        # Command separator patterns
        payloads.extend(CMDiModule._get_separator_patterns())
        
        # Command substitution patterns
        payloads.extend(CMDiModule._get_substitution_patterns())
        
        # Redirection patterns
        payloads.extend(CMDiModule._get_redirection_patterns())
        
        # Bypass patterns
        payloads.extend(CMDiModule._get_bypass_patterns())
        
        # Filter by OS if specified
        if os:
            payloads = [p for p in payloads if p.os == os.lower() or p.os == "cross-platform"]
        
        return payloads
    
    @staticmethod
    def _get_separator_patterns() -> List[CMDiPayload]:
        """Command separator pattern templates"""
        return [
            CMDiPayload(
                id="cmdi-001",
                category="cmdi",
                os="linux",
                pattern_type="separator",
                template="; whoami",
                explanation="Semicolon command separator - executes whoami after original command (Linux/Unix)",
                defensive_notes="Input validation: whitelist allowed characters. Never pass user input directly to system(), exec(), shell_exec(). Use argument arrays, not shell strings."
            ),
            CMDiPayload(
                id="cmdi-002",
                category="cmdi",
                os="linux",
                pattern_type="separator",
                template="| whoami",
                explanation="Pipe operator - passes output of first command to whoami (usually shows username)",
                defensive_notes="Avoid shell execution entirely. Use language-native APIs (subprocess with shell=False in Python, child_process.execFile in Node)."
            ),
            CMDiPayload(
                id="cmdi-003",
                category="cmdi",
                os="linux",
                pattern_type="separator",
                template="|| whoami",
                explanation="OR operator - executes whoami if first command fails",
                defensive_notes="Principle of least privilege: run application with minimal OS permissions. Disable shell access if possible."
            ),
            CMDiPayload(
                id="cmdi-004",
                category="cmdi",
                os="linux",
                pattern_type="separator",
                template="& whoami",
                explanation="Background execution - runs whoami in background (Linux/Unix)",
                defensive_notes="Use parameterized command execution. In PHP: escapeshellarg() + escapeshellcmd() as last resort, better to avoid shell."
            ),
            CMDiPayload(
                id="cmdi-005",
                category="cmdi",
                os="linux",
                pattern_type="separator",
                template="&& whoami",
                explanation="AND operator - executes whoami only if first command succeeds",
                defensive_notes="Strict input validation: whitelist known-good inputs. Monitor process execution for anomalies."
            ),
            CMDiPayload(
                id="cmdi-006",
                category="cmdi",
                os="windows",
                pattern_type="separator",
                template="& whoami",
                explanation="Windows command separator using ampersand",
                defensive_notes="On Windows: use subprocess without shell=True. Avoid cmd.exe entirely. Use Windows API directly when possible."
            ),
            CMDiPayload(
                id="cmdi-007",
                category="cmdi",
                os="windows",
                pattern_type="separator",
                template="| whoami",
                explanation="Windows pipe operator - works in cmd.exe and PowerShell",
                defensive_notes="In .NET: use Process.Start() with argument lists, never with shell command strings."
            ),
            CMDiPayload(
                id="cmdi-008",
                category="cmdi",
                os="cross-platform",
                pattern_type="separator",
                template="\n whoami",
                explanation="Newline separator - executes as separate command in some contexts",
                defensive_notes="Normalize and validate input. Remove/escape control characters including newlines and carriage returns."
            ),
        ]
    
    @staticmethod
    def _get_substitution_patterns() -> List[CMDiPayload]:
        """Command substitution pattern templates"""
        return [
            CMDiPayload(
                id="cmdi-101",
                category="cmdi",
                os="linux",
                pattern_type="substitution",
                template="`whoami`",
                explanation="Backtick command substitution - output of whoami replaces the expression (Linux/Unix)",
                defensive_notes="Never use shell metacharacters in commands. Whitelist approach: define allowed values, reject everything else."
            ),
            CMDiPayload(
                id="cmdi-102",
                category="cmdi",
                os="linux",
                pattern_type="substitution",
                template="$(whoami)",
                explanation="Dollar-parenthesis command substitution - modern syntax in bash/sh",
                defensive_notes="Use application-level functions instead of OS commands when possible. For file operations: use language file APIs, not cat/ls/dir."
            ),
            CMDiPayload(
                id="cmdi-103",
                category="cmdi",
                os="windows",
                pattern_type="substitution",
                template="%USERPROFILE%",
                explanation="Windows environment variable expansion - can leak sensitive paths",
                defensive_notes="Disable or sanitize environment variable expansion. In cmd.exe, use setlocal to limit variable scope."
            ),
            CMDiPayload(
                id="cmdi-104",
                category="cmdi",
                os="linux",
                pattern_type="substitution",
                template="${IFS}",
                explanation="Internal Field Separator variable - used to bypass space filtering in bash",
                defensive_notes="Blacklist filtering is insufficient. Use structured command execution (execve with argv array)."
            ),
        ]
    
    @staticmethod
    def _get_redirection_patterns() -> List[CMDiPayload]:
        """Input/Output redirection pattern templates"""
        return [
            CMDiPayload(
                id="cmdi-201",
                category="cmdi",
                os="linux",
                pattern_type="redirection",
                template="> /tmp/output.txt",
                explanation="Output redirection - writes command output to file (potential for file creation/overwrite)",
                defensive_notes="File system permissions: ensure web user cannot write to sensitive directories. Monitor for unexpected file creation."
            ),
            CMDiPayload(
                id="cmdi-202",
                category="cmdi",
                os="linux",
                pattern_type="redirection",
                template="< /etc/passwd",
                explanation="Input redirection - reads from file and uses as command input (potential information disclosure)",
                defensive_notes="Restrict read access to sensitive files. Use SELinux/AppArmor to enforce mandatory access control."
            ),
            CMDiPayload(
                id="cmdi-203",
                category="cmdi",
                os="linux",
                pattern_type="redirection",
                template="2>&1",
                explanation="Error redirection - combines stderr with stdout (can reveal error messages with sensitive info)",
                defensive_notes="Don't display raw command output/errors to users. Log securely, show generic error messages to users."
            ),
            CMDiPayload(
                id="cmdi-204",
                category="cmdi",
                os="windows",
                pattern_type="redirection",
                template="> C:\\output.txt",
                explanation="Windows output redirection to file",
                defensive_notes="On Windows: NTFS permissions to restrict file operations. Use User Account Control (UAC) properly."
            ),
        ]
    
    @staticmethod
    def _get_bypass_patterns() -> List[CMDiPayload]:
        """Filter bypass pattern demonstrations (strings only)"""
        return [
            CMDiPayload(
                id="cmdi-301",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template="wh''oami",
                explanation="Empty string injection - bypasses simple string matching for 'whoami'",
                defensive_notes="Don't rely on blacklisting commands. Whitelist allowed inputs or avoid shell execution entirely."
            ),
            CMDiPayload(
                id="cmdi-302",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template="who$@ami",
                explanation="Special variable insertion ($@ = empty in many contexts) to obfuscate command",
                defensive_notes="Complex bypass attempts indicate attack. Use allowlist validation + logging of rejected inputs."
            ),
            CMDiPayload(
                id="cmdi-303",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template="w\\ho\\am\\i",
                explanation="Backslash escaping - can bypass pattern matching in some shells",
                defensive_notes="Normalize input before validation. Remove escape sequences or reject inputs containing them."
            ),
            CMDiPayload(
                id="cmdi-304",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template="/usr/bin/who``ami",
                explanation="Full path + empty backticks - bypasses command name filters",
                defensive_notes="Whitelist acceptable values, don't blacklist commands. Better: don't use shell at all."
            ),
            CMDiPayload(
                id="cmdi-305",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template=";{cat,/etc/passwd}",
                explanation="Brace expansion in bash - {cat,/etc/passwd} expands to 'cat /etc/passwd'",
                defensive_notes="Use bash with --norc --noprofile options if shell is unavoidable. Better: use execve() directly."
            ),
            CMDiPayload(
                id="cmdi-306",
                category="cmdi",
                os="windows",
                pattern_type="bypass",
                template="who^ami",
                explanation="Windows caret escape character - 'who^ami' becomes 'whoami' in cmd.exe",
                defensive_notes="On Windows: avoid cmd.exe. Use ProcessStartInfo with UseShellExecute=false in .NET."
            ),
            CMDiPayload(
                id="cmdi-307",
                category="cmdi",
                os="linux",
                pattern_type="bypass",
                template=";ca\\t${IFS}/etc/passwd",
                explanation="Combined obfuscation: backslash escape + IFS variable for space",
                defensive_notes="Multiple obfuscation layers indicate sophisticated attack. Defense: no shell execution + strict validation."
            ),
            CMDiPayload(
                id="cmdi-308",
                category="cmdi",
                os="cross-platform",
                pattern_type="bypass",
                template="%0a whoami",
                explanation="URL-encoded newline separator - may execute as separate command after decoding",
                defensive_notes="Decode user input, then validate. Check for encoded metacharacters. Reject, don't try to sanitize."
            ),
        ]
    
    @staticmethod
    def get_by_os(os: str) -> List[CMDiPayload]:
        """
        Get payloads filtered by operating system
        
        Args:
            os: linux, windows, or cross-platform
        
        Returns:
            Filtered list of command injection payloads
        """
        if not CMDiModule.EDUCATIONAL_MODE:
            raise RuntimeError("Command injection module is disabled for safety")
        
        all_payloads = CMDiModule.get_all_payloads()
        return [p for p in all_payloads if p.os == os.lower() or p.os == "cross-platform"]
    
    @staticmethod
    def get_by_pattern_type(pattern_type: str) -> List[CMDiPayload]:
        """
        Get payloads filtered by pattern type
        
        Args:
            pattern_type: separator, substitution, redirection, bypass
        
        Returns:
            Filtered list of command injection payloads
        """
        if not CMDiModule.EDUCATIONAL_MODE:
            raise RuntimeError("Command injection module is disabled for safety")
        
        all_payloads = CMDiModule.get_all_payloads()
        return [p for p in all_payloads if p.pattern_type == pattern_type]
    
    @staticmethod
    def get_safe_explanation() -> str:
        """Return educational explanation about command injection"""
        return """
Command Injection Vulnerability - Educational Overview

WHAT IS IT?
Command injection occurs when an application passes unsafe user input to a system shell.
Attackers inject shell metacharacters to execute arbitrary commands on the server.

WHY IT'S DANGEROUS:
- Full server compromise possible
- Data theft, malware installation, lateral movement
- Often leads to complete system takeover

SECURE CODING PRACTICES:
1. NEVER use system(), exec(), shell_exec(), eval() with user input
2. Use language-native APIs instead of shell commands
3. If shell is unavoidable:
   - Use argument arrays (e.g., subprocess with shell=False)
   - Whitelist allowed inputs
   - Apply strict input validation
4. Run application with least privilege
5. Use application sandboxing (containers, VMs)

DETECTION:
- Monitor process execution patterns
- Log all command executions
- Alert on shell metacharacters in input
- Use runtime application self-protection (RASP)

REFERENCES:
- OWASP Command Injection: https://owasp.org/www-community/attacks/Command_Injection
- CWE-78: https://cwe.mitre.org/data/definitions/78.html
"""
