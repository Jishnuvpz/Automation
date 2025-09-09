#!/usr/bin/env python3
"""
Task Automation Demo Script
This script demonstrates all three automation tasks:
1. Move JPG files to a new folder
2. Extract email addresses from a text file
3. Scrape webpage titles

Key concepts demonstrated: os, shutil, re, requests, file handling
"""

import sys
import os
from pathlib import Path

# Add the scripts directory to the Python path so we can import our modules
scripts_dir = Path(__file__).parent
sys.path.append(str(scripts_dir))

try:
    from move_jpg_files import move_jpg_files
    from extract_emails import extract_emails_from_text, validate_emails
    from scrape_webpage_title import scrape_webpage_title, scrape_multiple_urls
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all script files are in the same directory.")
    sys.exit(1)

def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("TASK AUTOMATION DEMO SCRIPT")
    print("=" * 60)
    print("Choose an automation task to run:")
    print()
    print("1. Move JPG Files")
    print("   - Moves all .jpg/.jpeg files from test_data/images to output/moved_images")
    print()
    print("2. Extract Email Addresses") 
    print("   - Extracts emails from test_data/sample_text_with_emails.txt")
    print()
    print("3. Scrape Webpage Title")
    print("   - Scrapes title from a webpage and saves it to file")
    print()
    print("4. Run All Tasks")
    print("   - Demonstrates all three automation tasks")
    print()
    print("5. Install Required Packages")
    print("   - Install requests package if not available")
    print()
    print("0. Exit")
    print("=" * 60)

def task_move_jpg_files():
    """Demonstrate the JPG file moving task."""
    print("\n" + "-" * 50)
    print("TASK 1: MOVE JPG FILES")
    print("-" * 50)
    
    current_dir = Path(__file__).parent.parent
    source_folder = current_dir / "test_data" / "images"
    destination_folder = current_dir / "output" / "moved_images"
    
    print(f"Source: {source_folder}")
    print(f"Destination: {destination_folder}")
    
    if not source_folder.exists():
        print("ERROR: Source folder does not exist!")
        return False
    
    # List files before moving
    image_files = list(source_folder.glob("*.jpg")) + list(source_folder.glob("*.JPG")) + \
                  list(source_folder.glob("*.jpeg")) + list(source_folder.glob("*.JPEG"))
    
    if not image_files:
        print("No image files found to move.")
        return False
    
    print(f"\nFiles to move:")
    for file in image_files:
        print(f"  - {file.name}")
    
    # Execute the move operation
    moved_count, errors = move_jpg_files(source_folder, destination_folder)
    
    if moved_count > 0:
        print(f"SUCCESS: Moved {moved_count} files successfully!")
    else:
        print("No files were moved.")
    
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(f"  - {error}")
    
    return moved_count > 0

def task_extract_emails():
    """Demonstrate the email extraction task."""
    print("\n" + "-" * 50)
    print("TASK 2: EXTRACT EMAIL ADDRESSES")
    print("-" * 50)
    
    current_dir = Path(__file__).parent.parent
    input_file = current_dir / "test_data" / "sample_text_with_emails.txt"
    
    print(f"Input file: {input_file}")
    
    if not input_file.exists():
        print("ERROR: Input file does not exist!")
        return False
    
    # Extract emails
    emails, output_file = extract_emails_from_text(input_file)
    
    if emails:
        # Validate emails
        validation_results = validate_emails(emails)
        
        print(f"\nSUCCESS: Found {len(emails)} unique email addresses!")
        print(f"Valid emails: {validation_results['total_valid']}")
        print(f"Invalid emails: {validation_results['total_invalid']}")
        print(f"Output saved to: {output_file}")
        
        return True
    else:
        print("No email addresses found.")
        return False

def task_scrape_webpage():
    """Demonstrate the webpage scraping task."""
    print("\n" + "-" * 50)
    print("TASK 3: SCRAPE WEBPAGE TITLE")
    print("-" * 50)
    
    # Test with a reliable website
    test_url = "https://www.python.org"
    
    print(f"Scraping: {test_url}")
    print("(Note: This requires an internet connection)")
    
    try:
        title, output_file, status_code = scrape_webpage_title(test_url)
        
        if title:
            print(f"SUCCESS: Scraped title - '{title}'")
            print(f"Output saved to: {output_file}")
            return True
        else:
            print(f"Failed to scrape title. HTTP Status: {status_code}")
            return False
            
    except Exception as e:
        print(f"Error: {str(e)}")
        print("This may be due to no internet connection or the requests module not being installed.")
        return False

def run_all_tasks():
    """Run all three automation tasks in sequence."""
    print("\n" + "=" * 60)
    print("RUNNING ALL AUTOMATION TASKS")
    print("=" * 60)
    
    results = {}
    
    # Task 1: Move JPG files
    results['jpg_move'] = task_move_jpg_files()
    
    # Task 2: Extract emails
    results['email_extract'] = task_extract_emails()
    
    # Task 3: Scrape webpage
    results['webpage_scrape'] = task_scrape_webpage()
    
    # Display summary
    print("\n" + "=" * 60)
    print("AUTOMATION TASKS SUMMARY")
    print("=" * 60)
    
    total_tasks = len(results)
    successful_tasks = sum(results.values())
    
    print(f"Total tasks: {total_tasks}")
    print(f"Successful: {successful_tasks}")
    print(f"Failed: {total_tasks - successful_tasks}")
    print(f"Success rate: {(successful_tasks/total_tasks*100):.1f}%")
    
    print("\nDetailed results:")
    for task, success in results.items():
        status = "SUCCESS" if success else "FAILED"
        task_name = task.replace('_', ' ').title()
        print(f"  {task_name}: {status}")

def install_requirements():
    """Install required packages."""
    print("\n" + "-" * 50)
    print("INSTALLING REQUIRED PACKAGES")
    print("-" * 50)
    
    try:
        import subprocess
        result = subprocess.run([sys.executable, "-m", "pip", "install", "requests"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Successfully installed 'requests' package!")
        else:
            print("Failed to install 'requests' package.")
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error installing packages: {str(e)}")

def check_environment():
    """Check if the environment is set up correctly."""
    issues = []
    
    # Check if test data exists
    current_dir = Path(__file__).parent.parent
    test_data_dir = current_dir / "test_data"
    
    if not test_data_dir.exists():
        issues.append("test_data directory missing")
    
    sample_text = test_data_dir / "sample_text_with_emails.txt"
    if not sample_text.exists():
        issues.append("sample_text_with_emails.txt missing")
    
    images_dir = test_data_dir / "images"
    if not images_dir.exists():
        issues.append("test_data/images directory missing")
    
    # Check for requests module
    try:
        import requests
    except ImportError:
        issues.append("requests module not installed")
    
    if issues:
        print("\nEnvironment Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nSome tasks may not work properly.")
    else:
        print("\nEnvironment looks good!")
    
    return len(issues) == 0

def main():
    """Main function with interactive menu."""
    # Check environment first
    check_environment()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-5): ").strip()
            
            if choice == '0':
                print("Goodbye!")
                break
            elif choice == '1':
                task_move_jpg_files()
            elif choice == '2':
                task_extract_emails()
            elif choice == '3':
                task_scrape_webpage()
            elif choice == '4':
                run_all_tasks()
            elif choice == '5':
                install_requirements()
            else:
                print("Invalid choice! Please enter a number between 0-5.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
