# PayloadLab - Quick Reference Guide

## 🚀 Quick Command Reference

### Installation
```bash
pip install -e .
# OR
python -m payload_lab --help
```

---

## 📋 Common Commands

### View Help
```bash
payload_lab --help
payload_lab --version
```

### List All Payloads
```bash
payload_lab --list
```

### View Specific Payload
```bash
payload_lab --show xss-001
payload_lab --show sqli-005
payload_lab --show cmdi-003
```

---

## 🎯 Module Commands

### XSS Module
```bash
# All XSS payloads
payload_lab --module xss

# By type
payload_lab --module xss --xss-type reflected
payload_lab --module xss --xss-type stored
payload_lab --module xss --xss-type dom

# By context
payload_lab --module xss --context html
payload_lab --module xss --context attribute
payload_lab --module xss --context javascript
```

### SQLi Module
```bash
# All SQLi payloads
payload_lab --module sqli

# By database
payload_lab --module sqli --db mysql
payload_lab --module sqli --db postgres
payload_lab --module sqli --db mssql
```

### CMDi Module
```bash
# All command injection payloads
payload_lab --module cmdi

# By OS
payload_lab --module cmdi --os linux
payload_lab --module cmdi --os windows
```

### All Modules
```bash
payload_lab --module all
```

---

## 📤 Export Commands

### JSON Export
```bash
payload_lab --module xss --export json --out output.json
```

### TXT Export
```bash
payload_lab --module sqli --export txt --out output.txt
```

### CSV Export
```bash
payload_lab --module cmdi --export csv --out output.csv
```

### Burp Suite Format
```bash
payload_lab --module xss --export burp --out burp_payloads.txt
```

### Comprehensive Report
```bash
payload_lab --module all --export report --out full_report.txt
```

---

## 🔐 Encoding Commands

```bash
# URL encoding
payload_lab --module xss --encode url

# Base64 encoding
payload_lab --module sqli --encode base64

# Hex encoding
payload_lab --module cmdi --encode hex

# Unicode encoding
payload_lab --module xss --encode unicode

# All encoding variations
payload_lab --module xss --encode all
```

---

## 🎨 Combination Examples

```bash
# MySQL SQLi exported to JSON
payload_lab --module sqli --db mysql --export json --out sqli_mysql.json

# Reflected XSS in HTML context to CSV
payload_lab --module xss --xss-type reflected --context html --export csv --out xss.csv

# Linux command injection with URL encoding
payload_lab --module cmdi --os linux --encode url --export txt --out cmdi_linux.txt

# Everything in comprehensive report
payload_lab --module all --export report --out complete_catalog.txt

# Quiet mode (no banner)
payload_lab --module xss --quiet --export json --out xss.json
```

---

## 📊 Payload Statistics

| Module | Count | Contexts | Databases/OS |
|--------|-------|----------|--------------|
| XSS    | 23    | HTML, Attribute, JavaScript | N/A |
| SQLi   | 30    | N/A      | MySQL, PostgreSQL, MSSQL |
| CMDi   | 24    | N/A      | Linux, Windows |
| **Total** | **77** | | |

---

## 🛡️ Safety Reminders

⚠️ **ALWAYS:**
- Get written authorization
- Use in controlled environments
- Document all activities
- Follow OWASP ethics
- Study defensive controls

❌ **NEVER:**
- Test without permission
- Use against production systems
- Exploit real vulnerabilities
- Share attack tools maliciously

---

## 📁 Sample Files Generated

Located in `samples/` directory:

```
samples/
├── USAGE_EXAMPLES.md                    # Detailed usage guide
├── xss_payloads.json                    # 23 XSS templates
├── sqli_payloads.txt                    # 30 SQLi templates
├── cmdi_payloads.json                   # 24 CMDi templates
├── sqli_mysql.csv                       # MySQL SQLi (CSV)
├── xss_burp_intruder.txt               # Burp Suite format
└── comprehensive_payload_catalog.txt    # Complete (77 payloads)
```

---

## 🔍 Payload ID Reference

### XSS Payload IDs
- `xss-001` to `xss-023`
- Types: reflected, stored, dom
- Contexts: html, attribute, javascript

### SQLi Payload IDs
- `sqli-001` to `sqli-030`
- Databases: generic, mysql, postgres, mssql
- Types: error-based, union-based, blind

### CMDi Payload IDs
- `cmdi-001` to `cmdi-024`
- OS: linux, windows, cross-platform
- Patterns: separators, inline, chaining

---

## 🧪 Testing Workflow

1. **Explore available payloads**
   ```bash
   payload_lab --list
   ```

2. **Study specific payload**
   ```bash
   payload_lab --show <payload-id>
   ```

3. **Generate payload set**
   ```bash
   payload_lab --module <module> --export json --out test.json
   ```

4. **Use in authorized testing**
   - Load into testing tool
   - Document scope
   - Test defensive controls
   - Record results

---

## 📚 Educational Use Cases

### Security Training
```bash
# Generate study materials
payload_lab --module all --export report --out training_materials.txt
```

### WAF Testing
```bash
# Create test payload sets
payload_lab --module xss --export burp --out waf_xss_tests.txt
payload_lab --module sqli --export burp --out waf_sqli_tests.txt
```

### Code Review Practice
```bash
# Export for documentation
payload_lab --module all --export json --out documentation.json
```

### Defensive Research
```bash
# Study bypass techniques
payload_lab --show xss-015  # Bypass example
payload_lab --show sqli-020 # Advanced SQLi
```

---

## 🐛 Troubleshooting

### Command not found
```bash
# Use Python module syntax
python -m payload_lab --help
```

### Import errors
```bash
# Reinstall
pip install -e .
```

### Permission denied
```bash
# Check output directory permissions
# Use absolute path
payload_lab --module xss --export json --out /full/path/output.json
```

---

## 🎓 Learning Path

1. **Start with basics**
   ```bash
   payload_lab --show xss-001
   payload_lab --show sqli-001
   payload_lab --show cmdi-001
   ```

2. **Explore variations**
   ```bash
   payload_lab --module xss --context html
   payload_lab --module sqli --db mysql
   ```

3. **Study encoding**
   ```bash
   payload_lab --show xss-001  # See all encodings
   ```

4. **Export for practice**
   ```bash
   payload_lab --module all --export report --out study_guide.txt
   ```

---

## 🔗 Additional Resources

- **OWASP Testing Guide**: https://owasp.org/www-project-web-security-testing-guide/
- **PortSwigger Academy**: https://portswigger.net/web-security
- **OWASP Cheat Sheets**: https://cheatsheetseries.owasp.org/
- **Project README**: See README.md for full documentation

---

## ⚡ Pro Tips

1. Use `--quiet` for clean exports
2. Combine filters for specific payloads
3. Study defensive_notes for each payload
4. Compare encoding variations
5. Use `--show` to understand context
6. Export to multiple formats for different tools
7. Always document your testing scope

---

**Version:** 1.0.0  
**Last Updated:** February 14, 2026  
**License:** Educational Use Only

Remember: **Education, Not Exploitation** 🛡️
