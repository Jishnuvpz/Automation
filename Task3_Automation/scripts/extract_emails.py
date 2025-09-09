#!/usr/bin/env python3
"""
Task Automation Script 2: Extract Email Addresses
This script extracts all email addresses from a .txt file and saves them to another file.
Key concepts: re (regex), file handling, text processing
"""

import re
import os
from pathlib import Path
from datetime import datetime

def extract_emails_from_text(input_file, output_file=None):
    """
    Extract email addresses from a text file and save them to another file.
    
    Args:
        input_file (str): Path to the input text file
        output_file (str, optional): Path to the output file. If None, auto-generates filename.
    
    Returns:
        tuple: (email_list, output_file_path) - list of found emails and output file path
    """
    input_path = Path(input_file)
    
    # Check if input file exists
    if not input_path.exists():
        print(f"Error: Input file '{input_file}' does not exist.")
        return [], None
    
    # Generate output filename if not provided
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = input_path.parent / f"extracted_emails_{timestamp}.txt"
    else:
        output_file = Path(output_file)
    
    # Regex pattern for email addresses
    # This pattern matches most common email formats
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    emails = []
    
    try:
        # Read the input file
        print(f"Reading file: {input_file}")
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Find all email addresses
        found_emails = re.findall(email_pattern, content)
        
        # Remove duplicates while preserving order
        seen = set()
        for email in found_emails:
            if email.lower() not in seen:
                emails.append(email)
                seen.add(email.lower())
        
        print(f"Found {len(found_emails)} email addresses ({len(emails)} unique)")
        
        if emails:
            # Create output directory if it doesn't exist
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write emails to output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(f"Email addresses extracted from: {input_file}\n")
                file.write(f"Extraction date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total unique emails found: {len(emails)}\n")
                file.write("-" * 50 + "\n\n")
                
                for i, email in enumerate(emails, 1):
                    file.write(f"{i}. {email}\n")
            
            print(f"Emails saved to: {output_file}")
            
            # Also display found emails
            print("\nExtracted emails:")
            for i, email in enumerate(emails, 1):
                print(f"  {i}. {email}")
        else:
            print("No email addresses found in the file.")
            
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return [], None
    
    return emails, str(output_file)

def validate_emails(email_list):
    """
    Perform additional validation on extracted emails.
    
    Args:
        email_list (list): List of email addresses to validate
    
    Returns:
        dict: Dictionary with validation results
    """
    # More strict email validation pattern
    strict_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    valid_emails = []
    invalid_emails = []
    
    for email in email_list:
        if re.match(strict_pattern, email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    
    return {
        'valid': valid_emails,
        'invalid': invalid_emails,
        'total_valid': len(valid_emails),
        'total_invalid': len(invalid_emails)
    }

def main():
    """Main function to demonstrate the script usage."""
    print("=" * 50)
    print("Email Address Extractor Script")
    print("=" * 50)
    
    # Set up file paths
    current_dir = Path(__file__).parent.parent
    input_file = current_dir / "test_data" / "sample_text_with_emails.txt"
    output_dir = current_dir / "output"
    
    print(f"Input file: {input_file}")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Extract emails
    emails, output_file = extract_emails_from_text(input_file)
    
    if emails:
        # Validate emails
        validation_results = validate_emails(emails)
        
        print("-" * 50)
        print("Validation Results:")
        print(f"Valid emails: {validation_results['total_valid']}")
        print(f"Invalid emails: {validation_results['total_invalid']}")
        
        if validation_results['invalid']:
            print("\nEmails that may need review:")
            for email in validation_results['invalid']:
                print(f"  - {email}")
        
        # Save validation results
        if output_file:
            validation_file = Path(output_file).with_name("email_validation_report.txt")
            with open(validation_file, 'w', encoding='utf-8') as file:
                file.write("Email Validation Report\n")
                file.write("=" * 30 + "\n\n")
                file.write(f"Total emails found: {len(emails)}\n")
                file.write(f"Valid emails: {validation_results['total_valid']}\n")
                file.write(f"Invalid emails: {validation_results['total_invalid']}\n\n")
                
                if validation_results['valid']:
                    file.write("Valid Emails:\n")
                    file.write("-" * 15 + "\n")
                    for email in validation_results['valid']:
                        file.write(f"{email}\n")
                
                if validation_results['invalid']:
                    file.write("\nEmails Needing Review:\n")
                    file.write("-" * 25 + "\n")
                    for email in validation_results['invalid']:
                        file.write(f"{email}\n")
            
            print(f"Validation report saved to: {validation_file}")

if __name__ == "__main__":
    main()
