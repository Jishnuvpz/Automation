#!/usr/bin/env python3
"""
Task Automation Script 1: Move JPG Files
This script moves all .jpg files from a source folder to a destination folder.
Key concepts: os, shutil, file handling
"""

import os
import shutil
from pathlib import Path

def move_jpg_files(source_folder, destination_folder):
    """
    Move all .jpg files from source folder to destination folder.
    
    Args:
        source_folder (str): Path to the source folder containing .jpg files
        destination_folder (str): Path to the destination folder
    
    Returns:
        tuple: (moved_count, error_list) - number of files moved and list of errors
    """
    # Convert to Path objects for better handling
    source_path = Path(source_folder)
    dest_path = Path(destination_folder)
    
    # Check if source folder exists
    if not source_path.exists():
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return 0, [f"Source folder '{source_folder}' does not exist."]
    
    # Create destination folder if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)
    print(f"Destination folder created/verified: {destination_folder}")
    
    moved_count = 0
    errors = []
    
    try:
        # Find all .jpg files (case-insensitive)
        jpg_files = list(source_path.glob("*.jpg")) + list(source_path.glob("*.JPG")) + \
                   list(source_path.glob("*.jpeg")) + list(source_path.glob("*.JPEG"))
        
        if not jpg_files:
            print("No .jpg files found in the source folder.")
            return 0, []
        
        print(f"Found {len(jpg_files)} image files to move...")
        
        for jpg_file in jpg_files:
            try:
                # Create destination file path
                dest_file = dest_path / jpg_file.name
                
                # Check if file already exists in destination
                if dest_file.exists():
                    print(f"Warning: {jpg_file.name} already exists in destination. Skipping...")
                    continue
                
                # Move the file
                shutil.move(str(jpg_file), str(dest_file))
                print(f"Moved: {jpg_file.name}")
                moved_count += 1
                
            except Exception as e:
                error_msg = f"Error moving {jpg_file.name}: {str(e)}"
                errors.append(error_msg)
                print(f"Error: {error_msg}")
        
        print(f"\nOperation completed! Moved {moved_count} files.")
        if errors:
            print(f"Encountered {len(errors)} errors.")
            
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        errors.append(error_msg)
        print(f"Error: {error_msg}")
    
    return moved_count, errors

def main():
    """Main function to demonstrate the script usage."""
    print("=" * 50)
    print("JPG Files Mover Script")
    print("=" * 50)
    
    # You can modify these paths or make them command-line arguments
    current_dir = Path(__file__).parent.parent
    source_folder = current_dir / "test_data" / "images"
    destination_folder = current_dir / "output" / "moved_images"
    
    print(f"Source folder: {source_folder}")
    print(f"Destination folder: {destination_folder}")
    print("-" * 50)
    
    # Execute the file moving operation
    moved_count, errors = move_jpg_files(source_folder, destination_folder)
    
    # Print summary
    print("-" * 50)
    print(f"Summary: {moved_count} files moved successfully")
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(f"  - {error}")

if __name__ == "__main__":
    main()
