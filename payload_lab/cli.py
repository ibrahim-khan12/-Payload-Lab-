"""
Payload Lab - CLI Interface
Command-line interface for educational payload generation

⚠️ EDUCATIONAL USE ONLY
"""

import argparse
import sys
from typing import List

from .core import PayloadEncoder, PayloadExporter
from .modules import XSSModule, SQLiModule, CMDiModule


class PayloadLabCLI:
    """Command-line interface for Payload Lab"""
    
    def __init__(self):
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create argument parser with all options"""
        parser = argparse.ArgumentParser(
            prog='payload_lab',
            description="""
╔═══════════════════════════════════════════════════════════════════════════╗
║                          PAYLOAD LAB v1.0.0                               ║
║               Educational Payload Template Generator                      ║
╚═══════════════════════════════════════════════════════════════════════════╝

⚠️  ETHICS & SAFETY WARNING ⚠️
This tool generates EDUCATIONAL payload templates for authorized security
testing and training purposes ONLY.

DO NOT USE for:
  ✗ Unauthorized penetration testing
  ✗ Malicious attacks or exploitation
  ✗ Any activity without explicit written authorization

Aligned with OWASP Code of Ethics.
            """,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # List all XSS payloads
  payload_lab --module xss
  
  # Generate SQL injection payloads for MySQL
  payload_lab --module sqli --db mysql
  
  # Export command injection payloads to JSON
  payload_lab --module cmdi --os linux --export json --out cmdi_payloads.json
  
  # Show specific payload details
  payload_lab --show xss-001
  
  # List all available payloads
  payload_lab --list
  
  # Generate with encoding variations
  payload_lab --module xss --encode url
  
  # Create comprehensive report
  payload_lab --module all --export report --out security_payloads.txt

For more information: https://owasp.org/
            """
        )
        
        # Module selection
        parser.add_argument(
            '--module',
            choices=['xss', 'sqli', 'cmdi', 'all'],
            help='Vulnerability module to use'
        )
        
        # Database filter for SQLi
        parser.add_argument(
            '--db',
            choices=['mysql', 'postgres', 'mssql', 'generic'],
            help='Database type for SQL injection payloads'
        )
        
        # OS filter for CMDi
        parser.add_argument(
            '--os',
            choices=['linux', 'windows', 'cross-platform'],
            help='Operating system for command injection payloads'
        )
        
        # XSS filters
        parser.add_argument(
            '--context',
            choices=['html', 'attribute', 'javascript'],
            help='XSS context filter'
        )
        
        parser.add_argument(
            '--xss-type',
            choices=['reflected', 'stored', 'dom'],
            help='XSS type filter'
        )
        
        # Encoding
        parser.add_argument(
            '--encode',
            choices=['url', 'base64', 'hex', 'unicode', 'all'],
            help='Apply encoding to payloads'
        )
        
        # Export options
        parser.add_argument(
            '--export',
            choices=['json', 'txt', 'csv', 'burp', 'report'],
            help='Export format'
        )
        
        parser.add_argument(
            '--out',
            type=str,
            help='Output file path'
        )
        
        # List and show
        parser.add_argument(
            '--list',
            action='store_true',
            help='List all available payloads'
        )
        
        parser.add_argument(
            '--show',
            type=str,
            metavar='PAYLOAD_ID',
            help='Show detailed information for specific payload'
        )
        
        # Quiet mode
        parser.add_argument(
            '--quiet',
            action='store_true',
            help='Suppress banner and warnings'
        )
        
        # Version
        parser.add_argument(
            '--version',
            action='version',
            version='Payload Lab v1.0.0'
        )
        
        return parser
    
    def run(self, args=None):
        """Execute CLI based on arguments"""
        parsed_args = self.parser.parse_args(args)
        
        # Show banner unless quiet
        if not parsed_args.quiet:
            self._show_banner()
        
        # Handle list command
        if parsed_args.list:
            self._list_all_payloads()
            return
        
        # Handle show command
        if parsed_args.show:
            self._show_payload(parsed_args.show)
            return
        
        # Require module if not using --list or --show
        if not parsed_args.module:
            self.parser.print_help()
            return
        
        # Generate payloads
        payloads = self._generate_payloads(parsed_args)
        
        if not payloads:
            print("No payloads matched the specified criteria.")
            return
        
        # Apply encoding if requested
        if parsed_args.encode:
            payloads = self._apply_encoding(payloads, parsed_args.encode)
        
        # Export or display
        if parsed_args.export:
            self._export_payloads(payloads, parsed_args.export, parsed_args.out)
        else:
            self._display_payloads(payloads)
    
    def _show_banner(self):
        """Display startup banner with warnings"""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                          PAYLOAD LAB v1.0.0                               ║
║               Educational Payload Template Generator                      ║
╚═══════════════════════════════════════════════════════════════════════════╝

⚠️  ETHICS & SAFETY DISCLAIMER ⚠️

These payload templates are for EDUCATIONAL PURPOSES ONLY.

AUTHORIZED USE ONLY:
  ✓ Security training and education
  ✓ Authorized penetration testing with written permission
  ✓ Security research in controlled environments

PROHIBITED USE:
  ✗ Unauthorized security testing
  ✗ Malicious attacks or exploitation
  ✗ Any illegal activity

By using this tool, you agree to use it ethically and legally.
Aligned with OWASP Code of Ethics.

════════════════════════════════════════════════════════════════════════════
        """)
    
    def _generate_payloads(self, args) -> List:
        """Generate payloads based on arguments"""
        payloads = []
        
        if args.module == 'xss' or args.module == 'all':
            xss_payloads = XSSModule.get_all_payloads()
            
            # Apply filters
            if args.context:
                xss_payloads = [p for p in xss_payloads if p.context == args.context]
            if args.xss_type:
                xss_payloads = [p for p in xss_payloads if p.type == args.xss_type]
            
            payloads.extend(xss_payloads)
        
        if args.module == 'sqli' or args.module == 'all':
            if args.db:
                sqli_payloads = SQLiModule.get_by_database(args.db)
            else:
                sqli_payloads = SQLiModule.get_all_payloads()
            
            payloads.extend(sqli_payloads)
        
        if args.module == 'cmdi' or args.module == 'all':
            if args.os:
                cmdi_payloads = CMDiModule.get_by_os(args.os)
            else:
                cmdi_payloads = CMDiModule.get_all_payloads()
            
            payloads.extend(cmdi_payloads)
        
        return payloads
    
    def _apply_encoding(self, payloads, encoding_type):
        """Apply encoding to payloads (for educational purposes)"""
        print(f"\n[*] Applying {encoding_type} encoding (educational demonstration)...\n")
        
        encoder = PayloadEncoder()
        
        # Note: This creates new payload objects with encoded templates
        # Original payloads are preserved
        encoded_payloads = []
        
        for payload in payloads:
            if encoding_type == 'url':
                encoded_template = encoder.url_encode(payload.template)
            elif encoding_type == 'base64':
                encoded_template = encoder.base64_encode(payload.template)
            elif encoding_type == 'hex':
                encoded_template = encoder.hex_encode(payload.template)
            elif encoding_type == 'unicode':
                encoded_template = encoder.unicode_encode(payload.template)
            elif encoding_type == 'all':
                # Show all variations
                variations = encoder.get_encoding_variations(payload.template)
                print(f"[{payload.id}] Encoding Variations:")
                for enc_type, enc_value in variations.items():
                    print(f"  {enc_type}: {enc_value}")
                print()
                continue
            else:
                encoded_template = payload.template
            
            # Create copy with encoded template
            import copy
            encoded_payload = copy.deepcopy(payload)
            encoded_payload.template = encoded_template
            encoded_payload.explanation += f" [Encoded: {encoding_type}]"
            encoded_payloads.append(encoded_payload)
        
        if encoding_type != 'all':
            return encoded_payloads
        return payloads
    
    def _export_payloads(self, payloads, export_format, output_file):
        """Export payloads to specified format"""
        exporter = PayloadExporter()
        
        if export_format == 'json':
            content = exporter.to_json(payloads, filepath=output_file)
            if output_file:
                print(f"[+] Exported {len(payloads)} payloads to {output_file} (JSON)")
            else:
                print(content)
        
        elif export_format == 'txt':
            content = exporter.to_txt(payloads, filepath=output_file)
            if output_file:
                print(f"[+] Exported {len(payloads)} payloads to {output_file} (TXT)")
            else:
                print(content)
        
        elif export_format == 'csv':
            content = exporter.to_csv(payloads, filepath=output_file)
            if output_file:
                print(f"[+] Exported {len(payloads)} payloads to {output_file} (CSV)")
            else:
                print(content)
        
        elif export_format == 'burp':
            content = exporter.to_burp_intruder(payloads, filepath=output_file)
            if output_file:
                print(f"[+] Exported {len(payloads)} payloads to {output_file} (Burp Suite format)")
            else:
                print(content)
        
        elif export_format == 'report':
            content = exporter.create_report(payloads, filepath=output_file)
            if output_file:
                print(f"[+] Generated report with {len(payloads)} payloads: {output_file}")
            else:
                print(content)
    
    def _display_payloads(self, payloads):
        """Display payloads to console"""
        print(f"\n[*] Generated {len(payloads)} payload template(s)\n")
        print("=" * 80)
        
        for i, payload in enumerate(payloads, 1):
            print(f"\n[{i}] {payload.id}")
            print("-" * 80)
            print(f"Category: {payload.category.upper()}")
            
            # Type-specific fields
            if hasattr(payload, 'type') and payload.type:
                print(f"Type: {payload.type}")
            if hasattr(payload, 'context') and payload.context:
                print(f"Context: {payload.context}")
            if hasattr(payload, 'db') and payload.db:
                print(f"Database: {payload.db}")
            if hasattr(payload, 'os') and payload.os:
                print(f"OS: {payload.os}")
            
            print(f"\nTemplate:")
            print(f"  {payload.template}")
            print(f"\nExplanation:")
            print(f"  {payload.explanation}")
            print(f"\n🛡️  Defensive Notes:")
            print(f"  {payload.defensive_notes}")
        
        print("\n" + "=" * 80)
        print(f"Total: {len(payloads)} payload template(s)")
        print("=" * 80)
    
    def _list_all_payloads(self):
        """List all available payloads"""
        print("\n" + "=" * 80)
        print("AVAILABLE PAYLOAD TEMPLATES")
        print("=" * 80)
        
        # XSS
        print("\n▼ XSS PAYLOADS")
        print("-" * 80)
        xss_payloads = XSSModule.get_all_payloads()
        for p in xss_payloads:
            print(f"  {p.id:<15} [{p.type}/{p.context}]  {p.template[:50]}...")
        
        # SQLi
        print("\n▼ SQL INJECTION PAYLOADS")
        print("-" * 80)
        sqli_payloads = SQLiModule.get_all_payloads()
        for p in sqli_payloads:
            print(f"  {p.id:<15} [{p.db}/{p.injection_type}]  {p.template[:50]}...")
        
        # CMDi
        print("\n▼ COMMAND INJECTION PAYLOADS")
        print("-" * 80)
        cmdi_payloads = CMDiModule.get_all_payloads()
        for p in cmdi_payloads:
            print(f"  {p.id:<15} [{p.os}/{p.pattern_type}]  {p.template[:50]}...")
        
        print("\n" + "=" * 80)
        total = len(xss_payloads) + len(sqli_payloads) + len(cmdi_payloads)
        print(f"Total: {total} payload templates available")
        print("=" * 80)
        print("\nUse --show <payload_id> to view detailed information")
    
    def _show_payload(self, payload_id):
        """Show detailed information for specific payload"""
        # Search all modules
        all_payloads = []
        all_payloads.extend(XSSModule.get_all_payloads())
        all_payloads.extend(SQLiModule.get_all_payloads())
        all_payloads.extend(CMDiModule.get_all_payloads())
        
        # Find payload
        payload = None
        for p in all_payloads:
            if p.id == payload_id:
                payload = p
                break
        
        if not payload:
            print(f"[!] Payload '{payload_id}' not found")
            print(f"[*] Use --list to see all available payloads")
            return
        
        # Display detailed info
        print("\n" + "=" * 80)
        print(f"PAYLOAD DETAILS: {payload.id}")
        print("=" * 80)
        print(f"\nCategory: {payload.category.upper()}")
        
        if hasattr(payload, 'type') and payload.type:
            print(f"Type: {payload.type}")
        if hasattr(payload, 'context') and payload.context:
            print(f"Context: {payload.context}")
        if hasattr(payload, 'db') and payload.db:
            print(f"Database: {payload.db}")
        if hasattr(payload, 'injection_type') and payload.injection_type:
            print(f"Injection Type: {payload.injection_type}")
        if hasattr(payload, 'os') and payload.os:
            print(f"Operating System: {payload.os}")
        if hasattr(payload, 'pattern_type') and payload.pattern_type:
            print(f"Pattern Type: {payload.pattern_type}")
        
        print(f"\n📝 Template:")
        print(f"  {payload.template}")
        
        print(f"\n💡 Explanation:")
        print(f"  {payload.explanation}")
        
        print(f"\n🛡️  Defensive Notes:")
        print(f"  {payload.defensive_notes}")
        
        # Show encoding variations
        print(f"\n🔧 Encoding Variations (Educational):")
        print("-" * 80)
        encoder = PayloadEncoder()
        variations = encoder.get_encoding_variations(payload.template)
        for enc_type, enc_value in variations.items():
            if enc_type != "defensive_note":
                print(f"  {enc_type:20s}: {enc_value[:60]}...")
        
        print("\n" + "=" * 80)


def main():
    """Main entry point"""
    cli = PayloadLabCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
