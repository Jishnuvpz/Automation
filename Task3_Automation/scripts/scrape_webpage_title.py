#!/usr/bin/env python3
"""
Task Automation Script 3: Scrape Webpage Title
This script scrapes the title of a webpage and saves it to a file.
Key concepts: requests, HTML parsing, web scraping, file handling
"""

import requests
import re
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

def scrape_webpage_title(url, output_file=None, timeout=10):
    """
    Scrape the title of a webpage and save it to a file.
    
    Args:
        url (str): URL of the webpage to scrape
        output_file (str, optional): Path to the output file. If None, auto-generates filename.
        timeout (int): Request timeout in seconds
    
    Returns:
        tuple: (title, output_file_path, status_code) - scraped title, output file path, HTTP status
    """
    try:
        # Validate URL format
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            print(f"Error: Invalid URL format: {url}")
            return None, None, None
        
        print(f"Scraping webpage: {url}")
        
        # Set up headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the HTTP request
        response = requests.get(url, headers=headers, timeout=timeout)
        status_code = response.status_code
        
        if response.status_code == 200:
            # Extract title using regex
            # This pattern looks for <title>...</title> tags (case-insensitive)
            title_pattern = r'<title[^>]*>(.*?)</title>'
            title_match = re.search(title_pattern, response.text, re.IGNORECASE | re.DOTALL)
            
            if title_match:
                # Get the title and clean it up
                title = title_match.group(1).strip()
                # Remove extra whitespace and newlines
                title = re.sub(r'\s+', ' ', title)
                # Decode HTML entities (basic ones)
                title = title.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
                
                print(f"Title found: {title}")
                
                # Generate output filename if not provided
                if output_file is None:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    safe_domain = re.sub(r'[^\w\-_\.]', '_', parsed_url.netloc)
                    output_file = Path(__file__).parent.parent / "output" / f"webpage_title_{safe_domain}_{timestamp}.txt"
                else:
                    output_file = Path(output_file)
                
                # Create output directory if it doesn't exist
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Save title to file
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(f"Webpage Title Extraction Report\n")
                    file.write("=" * 40 + "\n\n")
                    file.write(f"URL: {url}\n")
                    file.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write(f"HTTP Status: {status_code}\n")
                    file.write(f"Domain: {parsed_url.netloc}\n")
                    file.write("-" * 40 + "\n\n")
                    file.write(f"Title: {title}\n\n")
                    file.write(f"Title length: {len(title)} characters\n")
                    file.write(f"Title word count: {len(title.split())}\n")
                
                print(f"Title saved to: {output_file}")
                return title, str(output_file), status_code
            else:
                print("Error: No title tag found in the webpage")
                return None, None, status_code
        else:
            print(f"Error: HTTP {status_code} - Failed to fetch the webpage")
            return None, None, status_code
            
    except requests.exceptions.Timeout:
        print(f"Error: Request timed out after {timeout} seconds")
        return None, None, None
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed. Check your internet connection or URL.")
        return None, None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {str(e)}")
        return None, None, None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None, None, None

def scrape_multiple_urls(urls, output_dir=None):
    """
    Scrape titles from multiple URLs and save them to individual files.
    
    Args:
        urls (list): List of URLs to scrape
        output_dir (str, optional): Directory to save output files
    
    Returns:
        dict: Dictionary with results for each URL
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "output" / "bulk_scraping"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = {}
    successful_scrapes = 0
    
    print(f"Scraping {len(urls)} URLs...")
    print("=" * 50)
    
    for i, url in enumerate(urls, 1):
        print(f"\n{i}/{len(urls)}: Processing {url}")
        
        # Generate individual output file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        parsed_url = urlparse(url)
        safe_domain = re.sub(r'[^\w\-_\.]', '_', parsed_url.netloc)
        individual_output = output_dir / f"title_{i:02d}_{safe_domain}_{timestamp}.txt"
        
        title, output_file, status_code = scrape_webpage_title(url, individual_output)
        
        results[url] = {
            'title': title,
            'output_file': output_file,
            'status_code': status_code,
            'success': title is not None
        }
        
        if title:
            successful_scrapes += 1
    
    # Create a summary report
    summary_file = output_dir / f"scraping_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(summary_file, 'w', encoding='utf-8') as file:
        file.write(f"Bulk Web Scraping Summary\n")
        file.write("=" * 30 + "\n\n")
        file.write(f"Total URLs processed: {len(urls)}\n")
        file.write(f"Successful scrapes: {successful_scrapes}\n")
        file.write(f"Failed scrapes: {len(urls) - successful_scrapes}\n")
        file.write(f"Success rate: {(successful_scrapes/len(urls)*100):.1f}%\n\n")
        
        file.write("Results:\n")
        file.write("-" * 10 + "\n")
        for i, (url, result) in enumerate(results.items(), 1):
            status = "SUCCESS" if result['success'] else "FAILED"
            file.write(f"{i}. {status} - {url}\n")
            if result['title']:
                file.write(f"   Title: {result['title'][:80]}{'...' if len(result['title']) > 80 else ''}\n")
            if result['status_code']:
                file.write(f"   HTTP Status: {result['status_code']}\n")
            file.write("\n")
    
    print(f"\nSummary saved to: {summary_file}")
    return results

def main():
    """Main function to demonstrate the script usage."""
    print("=" * 50)
    print("Webpage Title Scraper Script")
    print("=" * 50)
    
    # Example URLs to scrape (you can modify these)
    test_urls = [
        "https://www.python.org",
        "https://github.com",
        "https://stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    print("Testing single URL scraping:")
    print("-" * 30)
    
    # Test single URL scraping
    test_url = test_urls[0]
    title, output_file, status_code = scrape_webpage_title(test_url)
    
    if title:
        print(f"Successfully scraped: {title}")
    else:
        print("Failed to scrape the webpage")
    
    print("\n" + "=" * 50)
    print("Testing multiple URL scraping:")
    print("-" * 30)
    
    # Test multiple URL scraping
    results = scrape_multiple_urls(test_urls)
    
    # Display summary
    successful = sum(1 for result in results.values() if result['success'])
    print(f"\nBulk scraping completed: {successful}/{len(test_urls)} URLs successful")

if __name__ == "__main__":
    main()
