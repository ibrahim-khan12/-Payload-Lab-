# Payload Lab - Usage Examples

This document provides practical examples of using PayloadLab for educational security testing.

⚠️ **EDUCATIONAL USE ONLY - AUTHORIZED ENVIRONMENTS ONLY**

---

## Quick Start Examples

### 1. List All Available Payloads

```bash
payload_lab --list
```

This displays all available payload templates with their IDs and descriptions.

---

### 2. View Detailed Payload Information

```bash
payload_lab --show xss-001
```

Shows complete details for a specific payload including:
- Template code
- Explanation of how it works
- Defensive notes
- Encoding variations

---

## Module-Specific Examples

### XSS Module

#### Generate All XSS Payloads
```bash
payload_lab --module xss
```

#### Filter by XSS Type
```bash
# Reflected XSS only
payload_lab --module xss --xss-type reflected

# DOM-based XSS only
payload_lab --module xss --xss-type dom

# Stored XSS only
payload_lab --module xss --xss-type stored
```

#### Filter by Context
```bash
# HTML context payloads
payload_lab --module xss --context html

# JavaScript context payloads
payload_lab --module xss --context javascript

# Attribute context payloads
payload_lab --module xss --context attribute
```

#### Export XSS Payloads
```bash
# Export to JSON
payload_lab --module xss --export json --out xss_templates.json

# Export to TXT
payload_lab --module xss --export txt --out xss_templates.txt

# Export for Burp Suite Intruder
payload_lab --module xss --export burp --out xss_burp.txt
```

---

### SQL Injection Module

#### Generate All SQLi Payloads
```bash
payload_lab --module sqli
```

#### Database-Specific Payloads
```bash
# MySQL payloads
payload_lab --module sqli --db mysql

# PostgreSQL payloads
payload_lab --module sqli --db postgres

# MSSQL payloads
payload_lab --module sqli --db mssql
```

#### Export SQLi Payloads
```bash
# Export MySQL SQLi to CSV
payload_lab --module sqli --db mysql --export csv --out sqli_mysql.csv

# Export to comprehensive report
payload_lab --module sqli --export report --out sqli_report.txt
```

---

### Command Injection Module

#### Generate All CMDi Payloads
```bash
payload_lab --module cmdi
```

#### OS-Specific Payloads
```bash
# Linux command injection
payload_lab --module cmdi --os linux

# Windows command injection
payload_lab --module cmdi --os windows

# Cross-platform payloads
payload_lab --module cmdi --os cross-platform
```

#### Export CMDi Payloads
```bash
# Export to JSON
payload_lab --module cmdi --os linux --export json --out cmdi_linux.json
```

---

## Encoding Examples

### Apply URL Encoding
```bash
payload_lab --module xss --encode url
```

### Apply Base64 Encoding
```bash
payload_lab --module sqli --encode base64
```

### Apply Hex Encoding
```bash
payload_lab --module cmdi --encode hex
```

### Show All Encoding Variations
```bash
payload_lab --module xss --encode all
```

---

## Comprehensive Examples

### Generate Complete Payload Catalog
```bash
# All modules, comprehensive report
payload_lab --module all --export report --out complete_catalog.txt
```

### Export All Payloads to JSON
```bash
payload_lab --module all --export json --out all_payloads.json
```

### Create Burp Suite Payload Sets
```bash
# XSS payloads for Burp Intruder
payload_lab --module xss --export burp --out burp_xss.txt

# SQLi payloads for Burp Intruder
payload_lab --module sqli --db mysql --export burp --out burp_sqli.txt
```

---

## Advanced Combinations

### MySQL SQLi with URL Encoding
```bash
payload_lab --module sqli --db mysql --encode url --export json --out sqli_mysql_encoded.json
```

### Linux CMDi with Comprehensive Report
```bash
payload_lab --module cmdi --os linux --export report --out cmdi_linux_report.txt
```

### Reflected XSS in HTML Context
```bash
payload_lab --module xss --xss-type reflected --context html --export csv --out xss_reflected_html.csv
```

### Quiet Mode (Suppress Banner)
```bash
payload_lab --module xss --quiet --export json --out xss.json
```

---

## Educational Workflow Examples

### Security Training Scenario

1. **Study XSS Payloads**
   ```bash
   payload_lab --module xss --export txt --out xss_study.txt
   ```

2. **Analyze Defensive Notes**
   ```bash
   payload_lab --show xss-001
   payload_lab --show xss-002
   ```

3. **Compare Encoding Techniques**
   ```bash
   payload_lab --module xss --encode all
   ```

### Defensive Control Testing

1. **Generate Test Payload Set**
   ```bash
   payload_lab --module all --export json --out test_payloads.json
   ```

2. **Create WAF Test Cases**
   ```bash
   # XSS filter testing
   payload_lab --module xss --export burp --out waf_xss_tests.txt
   
   # SQLi filter testing
   payload_lab --module sqli --export burp --out waf_sqli_tests.txt
   ```

3. **Export for Documentation**
   ```bash
   payload_lab --module all --export report --out security_payload_documentation.txt
   ```

---

## Integration Examples

### Burp Suite Integration

1. **Export payload list**
   ```bash
   payload_lab --module xss --export burp --out payloads.txt
   ```

2. **In Burp Suite:**
   - Go to Intruder → Payloads tab
   - Payload Sets → Load from file
   - Select the exported `payloads.txt`
   - Use for authorized testing only

### OWASP ZAP Integration

1. **Export to JSON**
   ```bash
   payload_lab --module all --export json --out zap_payloads.json
   ```

2. **Use for custom fuzzer configuration**
   - Load JSON in custom scripts
   - Parse payloads for ZAP fuzzer
   - Educational analysis only

---

## Sample Output Files

All sample outputs are available in the `samples/` directory:

- `xss_payloads.json` - XSS templates in JSON format
- `sqli_payloads.txt` - SQLi templates in text format
- `cmdi_payloads.json` - Command injection templates
- `comprehensive_payload_catalog.txt` - All payloads with full details
- `xss_burp_intruder.txt` - Burp Suite format
- `sqli_mysql.csv` - MySQL SQLi in CSV format

---

## Best Practices

1. **Always obtain written authorization** before using these templates in testing
2. **Use only in isolated environments** for education and authorized testing
3. **Document all testing activities** with timestamps and scope
4. **Never use against production systems** without explicit permission
5. **Follow OWASP ethical guidelines** at all times
6. **Understand defensive controls** - study the defensive_notes for each payload

---

## Troubleshooting

### Command Not Found
If `payload_lab` command is not found:
```bash
# Run as Python module
python -m payload_lab --help

# Or install in development mode
pip install -e .
```

### Permission Errors
Ensure you have write permissions for the output directory:
```bash
# Specify absolute path
payload_lab --module xss --export json --out /path/to/output.json
```

### Display Issues
If output is truncated or formatted incorrectly:
```bash
# Use quiet mode for clean output
payload_lab --module xss --quiet --export txt --out output.txt
```

---

## Additional Resources

- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- PortSwigger XSS Cheat Sheet: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
- OWASP SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
- OWASP Command Injection: https://owasp.org/www-community/attacks/Command_Injection
- OWASP Code of Ethics: https://owasp.org/www-policy/operational/code-of-ethics

---

**Remember: Education, Not Exploitation** 🛡️

This tool exists to help security professionals understand attack patterns and build better defenses.
Use it responsibly and ethically.
