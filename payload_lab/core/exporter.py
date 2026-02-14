"""
Payload Lab - Export Functions
Handles exporting payload templates to various formats

⚠️ EDUCATIONAL USE ONLY
"""

import json
from typing import List, Dict, Any
from pathlib import Path
from datetime import datetime

from .models import Payload, PayloadCollection


class PayloadExporter:
    """Export payload templates to various formats"""
    
    @staticmethod
    def to_json(payloads: List[Payload], filepath: str = None, pretty: bool = True) -> str:
        """
        Export payloads to JSON format
        
        Args:
            payloads: List of payload objects
            filepath: Optional file path to write to
            pretty: Use pretty formatting
        
        Returns:
            JSON string
        """
        # Create collection
        collection = PayloadCollection(
            name="Payload Lab Export",
            description="Educational payload templates for security testing training",
            payloads=payloads
        )
        
        # Add strong warning
        data = collection.to_dict()
        data["WARNING"] = "EDUCATIONAL TEMPLATES ONLY - DO NOT USE FOR UNAUTHORIZED TESTING"
        data["DISCLAIMER"] = "These payloads are for learning purposes in authorized environments only"
        
        # Convert to JSON
        if pretty:
            json_str = json.dumps(data, indent=2, ensure_ascii=False)
        else:
            json_str = json.dumps(data, ensure_ascii=False)
        
        # Write to file if specified
        if filepath:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(json_str)
        
        return json_str
    
    @staticmethod
    def to_txt(payloads: List[Payload], filepath: str = None, 
               include_metadata: bool = True) -> str:
        """
        Export payloads to text catalog format
        
        Args:
            payloads: List of payload objects
            filepath: Optional file path to write to
            include_metadata: Include explanations and defensive notes
        
        Returns:
            Text string
        """
        lines = []
        
        # Header
        lines.append("=" * 80)
        lines.append("PAYLOAD LAB - EDUCATIONAL TEMPLATE CATALOG")
        lines.append("=" * 80)
        lines.append("")
        lines.append("⚠️  WARNING: EDUCATIONAL USE ONLY")
        lines.append("⚠️  DO NOT USE FOR UNAUTHORIZED SECURITY TESTING")
        lines.append("")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Total Payloads: {len(payloads)}")
        lines.append("")
        lines.append("=" * 80)
        lines.append("")
        
        # Payloads
        for i, payload in enumerate(payloads, 1):
            lines.append(f"\n[{i}] {payload.id}")
            lines.append("-" * 80)
            lines.append(f"Category: {payload.category.upper()}")
            
            # Add type-specific fields
            if hasattr(payload, 'type') and payload.type:
                lines.append(f"Type: {payload.type}")
            if hasattr(payload, 'context') and payload.context:
                lines.append(f"Context: {payload.context}")
            if hasattr(payload, 'db') and payload.db:
                lines.append(f"Database: {payload.db}")
            if hasattr(payload, 'os') and payload.os:
                lines.append(f"OS: {payload.os}")
            
            lines.append(f"\nTemplate:")
            lines.append(f"  {payload.template}")
            
            if include_metadata:
                lines.append(f"\nExplanation:")
                lines.append(f"  {payload.explanation}")
                lines.append(f"\nDefensive Notes:")
                lines.append(f"  {payload.defensive_notes}")
            
            lines.append("")
        
        # Footer
        lines.append("=" * 80)
        lines.append("End of Payload Catalog")
        lines.append("=" * 80)
        
        txt_content = "\n".join(lines)
        
        # Write to file if specified
        if filepath:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(txt_content)
        
        return txt_content
    
    @staticmethod
    def to_burp_intruder(payloads: List[Payload], filepath: str = None) -> str:
        """
        Export payloads in Burp Suite Intruder format
        (Simple list format compatible with Burp)
        
        Args:
            payloads: List of payload objects
            filepath: Optional file path to write to
        
        Returns:
            Newline-separated payload list
        """
        lines = [
            "# Payload Lab - Burp Suite Intruder Payload List",
            "# EDUCATIONAL USE ONLY - AUTHORIZED TESTING ENVIRONMENTS ONLY",
            "# Generated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            ""
        ]
        
        # Extract just the templates
        for payload in payloads:
            lines.append(payload.template)
        
        content = "\n".join(lines)
        
        # Write to file if specified
        if filepath:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return content
    
    @staticmethod
    def to_csv(payloads: List[Payload], filepath: str = None) -> str:
        """
        Export payloads to CSV format
        
        Args:
            payloads: List of payload objects
            filepath: Optional file path to write to
        
        Returns:
            CSV string
        """
        import csv
        from io import StringIO
        
        output = StringIO()
        
        if not payloads:
            return ""
        
        # Get all possible fields from first payload
        fieldnames = list(payloads[0].to_dict().keys())
        
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        
        for payload in payloads:
            writer.writerow(payload.to_dict())
        
        csv_content = output.getvalue()
        output.close()
        
        # Write to file if specified
        if filepath:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(csv_content)
        
        return csv_content
    
    @staticmethod
    def create_report(payloads: List[Payload], filepath: str = None) -> str:
        """
        Create a detailed educational report
        
        Args:
            payloads: List of payload objects
            filepath: Optional file path to write to
        
        Returns:
            Report string
        """
        lines = []
        
        # Header
        lines.append("╔" + "═" * 78 + "╗")
        lines.append("║" + " " * 20 + "PAYLOAD LAB EDUCATIONAL REPORT" + " " * 28 + "║")
        lines.append("╚" + "═" * 78 + "╝")
        lines.append("")
        lines.append("⚠️  ETHICS & SAFETY DISCLAIMER")
        lines.append("-" * 80)
        lines.append("This report contains educational security payload templates designed for:")
        lines.append("  • Authorized security testing in controlled environments")
        lines.append("  • Educational purposes in cybersecurity training")
        lines.append("  • Understanding defensive security controls")
        lines.append("")
        lines.append("These templates MUST NOT be used for:")
        lines.append("  ✗ Unauthorized penetration testing")
        lines.append("  ✗ Malicious attacks or exploitation")
        lines.append("  ✗ Any activity without explicit written authorization")
        lines.append("")
        lines.append(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Statistics
        lines.append("\n📊 PAYLOAD STATISTICS")
        lines.append("-" * 80)
        
        categories = {}
        for p in payloads:
            categories[p.category] = categories.get(p.category, 0) + 1
        
        lines.append(f"Total Payloads: {len(payloads)}")
        lines.append("\nBreakdown by Category:")
        for cat, count in categories.items():
            lines.append(f"  • {cat.upper()}: {count} templates")
        
        # Detailed payloads
        lines.append("\n\n📚 DETAILED PAYLOAD TEMPLATES")
        lines.append("=" * 80)
        
        current_category = None
        for payload in sorted(payloads, key=lambda x: x.category):
            if payload.category != current_category:
                current_category = payload.category
                lines.append(f"\n\n▼ {current_category.upper()} PAYLOADS")
                lines.append("─" * 80)
            
            lines.append(f"\n{payload.id}")
            lines.append("  Template: {0}".format(payload.template))
            lines.append(f"  Purpose: {payload.explanation}")
            lines.append(f"  🛡️  Defense: {payload.defensive_notes}")
            lines.append("")
        
        # Footer
        lines.append("\n" + "=" * 80)
        lines.append("End of Report - Use Responsibly and Ethically")
        lines.append("=" * 80)
        
        report = "\n".join(lines)
        
        # Write to file if specified
        if filepath:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report)
        
        return report
