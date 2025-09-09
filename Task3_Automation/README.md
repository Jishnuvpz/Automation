# Task 3: Task Automation with Python Scripts

## Overview
This is **Task 3** of the Internship project series. This project demonstrates three real-life task automation examples using Python. Each script automates a common repetitive task that occurs in everyday computing scenarios.

## Key Concepts Demonstrated
- **os** - Operating system interface
- **shutil** - High-level file operations
- **re** - Regular expressions for pattern matching
- **requests** - HTTP requests for web scraping
- **file handling** - Reading, writing, and processing files
- **pathlib** - Modern path handling
- **datetime** - Date and time operations

## Project Structure
```
Task3_Automation/
├── README.md
├── scripts/
│   ├── automation_demo.py      # Main demo script with interactive menu
│   ├── move_jpg_files.py       # Task 1: Move JPG files
│   ├── extract_emails.py       # Task 2: Extract email addresses
│   └── scrape_webpage_title.py # Task 3: Scrape webpage titles
├── test_data/
│   ├── images/                 # Sample JPG files for testing
│   │   ├── photo1.jpg
│   │   ├── vacation.JPG
│   │   ├── document_scan.jpeg
│   │   ├── profile_pic.JPEG
│   │   └── readme.txt         # Non-image file (ignored by script)
│   └── sample_text_with_emails.txt # Sample text with email addresses
└── output/                     # Generated output files
    ├── moved_images/          # Moved JPG files
    ├── extracted_emails_*.txt # Extracted email lists
    ├── email_validation_report.txt
    └── webpage_title_*.txt    # Scraped webpage titles
```

## Three Automation Tasks

### Task 1: Move JPG Files to New Folder
**File:** `scripts/move_jpg_files.py`

**Purpose:** Automatically move all `.jpg`, `.JPG`, `.jpeg`, and `.JPEG` files from a source folder to a destination folder.

**Key Features:**
- Case-insensitive file extension matching
- Automatic destination folder creation
- Duplicate file handling (skips existing files)
- Comprehensive error reporting
- Support for multiple image formats

**Usage:**
```bash
python scripts/move_jpg_files.py
```

**Real-world Applications:**
- Organizing photos from camera dumps
- Sorting downloaded images
- Cleaning up desktop screenshots
- Batch organizing media files

### Task 2: Extract Email Addresses from Text File
**File:** `scripts/extract_emails.py`

**Purpose:** Find and extract all email addresses from a text file using regular expressions, then save them to a clean list.

**Key Features:**
- Regex pattern matching for email detection
- Duplicate removal while preserving order
- Email validation with strict patterns
- Detailed extraction reports
- Support for various email formats

**Usage:**
```bash
python scripts/extract_emails.py
```

**Real-world Applications:**
- Processing customer feedback forms
- Extracting contacts from documents
- Cleaning mailing lists
- Data mining from text files

### Task 3: Scrape Webpage Title and Save
**File:** `scripts/scrape_webpage_title.py`

**Purpose:** Extract the title from a webpage and save it to a file with metadata.

**Key Features:**
- HTTP requests with proper headers
- HTML title extraction using regex
- Bulk scraping capability
- Error handling for network issues
- Comprehensive reporting

**Usage:**
```bash
python scripts/scrape_webpage_title.py
```

**Real-world Applications:**
- Website monitoring
- Content research and cataloging
- SEO analysis
- Bookmark management

## Getting Started

### Prerequisites
- Python 3.7 or higher
- `requests` module (for web scraping)

### Installation
1. Clone or download the project
2. Navigate to the project directory
3. Install required packages:
   ```bash
   pip install requests
   ```

### Quick Start
Run the interactive demo script:
```bash
python scripts/automation_demo.py
```

This will present a menu where you can:
1. Test individual automation tasks
2. Run all tasks together
3. Install required packages
4. Check environment setup

## Individual Script Usage

### Move JPG Files
```python
from move_jpg_files import move_jpg_files

# Move files from source to destination
source = "path/to/source/folder"
destination = "path/to/destination/folder"
moved_count, errors = move_jpg_files(source, destination)

print(f"Moved {moved_count} files")
```

### Extract Emails
```python
from extract_emails import extract_emails_from_text, validate_emails

# Extract emails from a text file
input_file = "sample_document.txt"
emails, output_file = extract_emails_from_text(input_file)

# Validate the extracted emails
validation_results = validate_emails(emails)
print(f"Found {len(emails)} emails, {validation_results['total_valid']} valid")
```

### Scrape Webpage Title
```python
from scrape_webpage_title import scrape_webpage_title

# Scrape a single webpage
url = "https://example.com"
title, output_file, status_code = scrape_webpage_title(url)

if title:
    print(f"Title: {title}")
    print(f"Saved to: {output_file}")
```

## Sample Data

### Test Images
The project includes sample image files in `test_data/images/`:
- `photo1.jpg` - Sample photo
- `vacation.JPG` - Vacation picture (uppercase extension)
- `document_scan.jpeg` - Scanned document
- `profile_pic.JPEG` - Profile picture (uppercase JPEG)
- `readme.txt` - Non-image file (should be ignored)

### Sample Text with Emails
`test_data/sample_text_with_emails.txt` contains approximately 28 email addresses mixed within various text content, including:
- Business emails (contact@company.com)
- Personal emails (john.doe@gmail.com)
- Special format emails (alice+billing@finance.co.uk)
- International domains (.org, .eu, .co.uk)

## Output Files

### Email Extraction Output
```
Email addresses extracted from: input_file.txt
Extraction date: 2024-01-15 14:30:25
Total unique emails found: 28
--------------------------------------------------

1. contact@company.com
2. sales@businesscorp.org
3. tech-support@helpdesk.net
...
```

### Webpage Title Output
```
Webpage Title Extraction Report
========================================

URL: https://www.python.org
Scraped on: 2024-01-15 14:30:45
HTTP Status: 200
Domain: www.python.org
----------------------------------------

Title: Welcome to Python.org

Title length: 21 characters
Title word count: 3
```

## Error Handling

All scripts include comprehensive error handling for:
- File not found errors
- Network connection issues
- Permission errors
- Invalid file formats
- Malformed URLs
- Encoding issues

## Customization

### Modifying File Patterns
To change which file types are moved in Task 1, edit the glob patterns in `move_jpg_files.py`:
```python
# Current patterns
jpg_files = list(source_path.glob("*.jpg")) + list(source_path.glob("*.JPG")) + \
           list(source_path.glob("*.jpeg")) + list(source_path.glob("*.JPEG"))

# Add more patterns
jpg_files += list(source_path.glob("*.png")) + list(source_path.glob("*.gif"))
```

### Modifying Email Regex
To change email detection patterns in Task 2, edit the regex in `extract_emails.py`:
```python
# Current pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# More restrictive pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}\b'
```

### Changing Target Websites
To change the websites scraped in Task 3, edit the URL list in `scrape_webpage_title.py`:
```python
test_urls = [
    "https://www.python.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://news.ycombinator.com"  # Add your own URLs
]
```

## Troubleshooting

### Common Issues

1. **Unicode/Encoding Errors on Windows:**
   - The demo script has been designed to work on Windows CMD/PowerShell
   - All Unicode characters have been removed for compatibility

2. **Requests Module Not Found:**
   - Install with: `pip install requests`
   - Or use the demo script's built-in installer (option 5)

3. **Permission Errors:**
   - Run with administrator privileges if moving files to protected directories
   - Ensure destination folders are writable

4. **Network Issues:**
   - Web scraping requires internet connection
   - Some websites may block automated requests
   - Try different URLs if specific sites fail

## Extensions and Improvements

### Potential Enhancements:
1. **GUI Interface:** Add a tkinter or PyQt interface
2. **Configuration Files:** Use JSON/YAML for settings
3. **Logging:** Add detailed logging with the logging module
4. **Parallel Processing:** Use threading for bulk operations
5. **Database Integration:** Store results in SQLite/PostgreSQL
6. **Cloud Integration:** Upload results to cloud storage
7. **Scheduling:** Add cron/Task Scheduler integration

### Advanced Features:
1. **Machine Learning:** Use ML to classify emails or images
2. **API Integration:** Send results to web APIs
3. **Real-time Monitoring:** Watch folders for new files
4. **Data Visualization:** Create charts from extraction results

## License

This project is for educational purposes and demonstrates practical automation techniques using Python's standard library and common third-party packages.

## Contributing

Feel free to fork this project and add your own automation tasks! Consider adding:
- PDF text extraction
- Excel file processing
- System monitoring scripts
- Database backup automation
- Social media automation

---

**Happy Automating! 🚀**
