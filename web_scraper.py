# ============================================================
# Advanced Web Scraper using Beautiful Soup
# Features: Data Extraction | Multiple Formats | Error Handling
# ============================================================

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
from datetime import datetime
import os

class WebScraper:
    """
    A comprehensive web scraper with error handling and multiple export formats.
    """
    
    def __init__(self, base_url, headers=None):
        """
        Initialize the scraper with a base URL and optional headers.
        
        Args:
            base_url (str): The website URL to scrape
            headers (dict): Optional HTTP headers for requests
        """
        self.base_url = base_url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.data = []
    
    def fetch_page(self, url):
        """
        Fetch a webpage with error handling.
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup object or None if error occurs
        """
        try:
            print(f"Fetching: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            
            soup = BeautifulSoup(response.content, 'html.parser')
            print("✅ Page fetched successfully")
            return soup
            
        except requests.exceptions.Timeout:
            print("❌ Error: Request timed out")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ Error: Connection failed. Check your internet.")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP Error: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None
    
    def scrape_quotes(self):
        """
        Example: Scrape quotes from quotes.toscrape.com
        """
        print("\n" + "="*60)
        print("SCRAPING QUOTES FROM QUOTES.TOSCRAPE.COM")
        print("="*60 + "\n")
        
        page = 1
        max_pages = 3  # Limit to 3 pages for demo
        
        while page <= max_pages:
            url = f"{self.base_url}/page/{page}/"
            soup = self.fetch_page(url)
            
            if soup is None:
                break
            
            # Find all quote containers
            quotes = soup.find_all('div', class_='quote')
            
            if not quotes:
                print("No more quotes found.")
                break
            
            for quote in quotes:
                try:
                    # Extract quote text
                    text = quote.find('span', class_='text').get_text()
                    
                    # Extract author
                    author = quote.find('small', class_='author').get_text()
                    
                    # Extract tags
                    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                    
                    # Store data
                    self.data.append({
                        'quote': text,
                        'author': author,
                        'tags': ', '.join(tags),
                        'page': page,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                    
                except AttributeError as e:
                    print(f"⚠️ Warning: Could not extract all data from a quote: {e}")
                    continue
            
            print(f"✅ Scraped {len(quotes)} quotes from page {page}")
            page += 1
            time.sleep(1)  # Be polite to the server
        
        print(f"\n📊 Total quotes scraped: {len(self.data)}")
    
    def scrape_books(self):
        """
        Example: Scrape books from books.toscrape.com
        """
        print("\n" + "="*60)
        print("SCRAPING BOOKS FROM BOOKS.TOSCRAPE.COM")
        print("="*60 + "\n")
        
        soup = self.fetch_page(self.base_url)
        
        if soup is None:
            return
        
        # Find all book containers
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            try:
                # Extract title
                title = book.find('h3').find('a')['title']
                
                # Extract price
                price = book.find('p', class_='price_color').get_text()
                
                # Extract rating
                rating_class = book.find('p', class_='star-rating')['class']
                rating = rating_class[1]  # Second class is the rating
                
                # Extract availability
                availability = book.find('p', class_='instock availability').get_text(strip=True)
                
                # Store data
                self.data.append({
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'availability': availability,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
                
            except (AttributeError, KeyError) as e:
                print(f"⚠️ Warning: Could not extract all data from a book: {e}")
                continue
        
        print(f"✅ Scraped {len(self.data)} books")
    
    def save_to_csv(self, filename='scraped_data.csv'):
        """
        Save scraped data to CSV file.
        """
        if not self.data:
            print("❌ No data to save!")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            
            print(f"✅ Data saved to {filename}")
        
        except IOError as e:
            print(f"❌ Error saving CSV: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def save_to_json(self, filename='scraped_data.json'):
        """
        Save scraped data to JSON file.
        """
        if not self.data:
            print("❌ No data to save!")
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            
            print(f"✅ Data saved to {filename}")
        
        except IOError as e:
            print(f"❌ Error saving JSON: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def save_to_txt(self, filename='scraped_data.txt'):
        """
        Save scraped data to text file.
        """
        if not self.data:
            print("❌ No data to save!")
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for idx, item in enumerate(self.data, 1):
                    file.write(f"--- Record {idx} ---\n")
                    for key, value in item.items():
                        file.write(f"{key}: {value}\n")
                    file.write("\n")
            
            print(f"✅ Data saved to {filename}")
        
        except IOError as e:
            print(f"❌ Error saving TXT: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def display_data(self, limit=5):
        """
        Display scraped data in console.
        """
        if not self.data:
            print("❌ No data to display!")
            return
        
        print("\n" + "="*60)
        print(f"DISPLAYING FIRST {min(limit, len(self.data))} RECORDS")
        print("="*60 + "\n")
        
        for idx, item in enumerate(self.data[:limit], 1):
            print(f"--- Record {idx} ---")
            for key, value in item.items():
                print(f"{key}: {value}")
            print()


# ============================================================
# EXAMPLE USAGE
# ============================================================

def main():
    """
    Main function demonstrating different scraping scenarios.
    """
    
    print("\n🌐 WEB SCRAPER DEMONSTRATION")
    print("=" * 60)
    
    # Menu
    print("\nChoose what to scrape:")
    print("1. Quotes (from quotes.toscrape.com)")
    print("2. Books (from books.toscrape.com)")
    print("3. Custom URL")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        # Scrape Quotes
        scraper = WebScraper('http://quotes.toscrape.com')
        scraper.scrape_quotes()
        
        # Display sample data
        scraper.display_data(limit=3)
        
        # Save in multiple formats
        print("\n" + "="*60)
        print("SAVING DATA")
        print("="*60 + "\n")
        scraper.save_to_csv('quotes.csv')
        scraper.save_to_json('quotes.json')
        scraper.save_to_txt('quotes.txt')
    
    elif choice == '2':
        # Scrape Books
        scraper = WebScraper('http://books.toscrape.com')
        scraper.scrape_books()
        
        # Display sample data
        scraper.display_data(limit=3)
        
        # Save in multiple formats
        print("\n" + "="*60)
        print("SAVING DATA")
        print("="*60 + "\n")
        scraper.save_to_csv('books.csv')
        scraper.save_to_json('books.json')
        scraper.save_to_txt('books.txt')
    
    elif choice == '3':
        # Custom URL scraping
        url = input("Enter the URL to scrape: ")
        scraper = WebScraper(url)
        
        print("\n⚠️ Note: You'll need to customize the scraping logic")
        print("for your specific website structure.")
        
        soup = scraper.fetch_page(url)
        if soup:
            print("\n✅ Page structure:")
            print(soup.prettify()[:500] + "...\n")
    
    else:
        print("❌ Invalid choice!")
    
    print("\n" + "="*60)
    print("SCRAPING COMPLETED")
    print("="*60)


# ============================================================
# ADVANCED EXAMPLE: Custom Scraper with Pagination
# ============================================================

class AdvancedScraper(WebScraper):
    """
    Extended scraper with advanced features.
    """
    
    def scrape_with_pagination(self, max_pages=5):
        """
        Scrape multiple pages with pagination support.
        """
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}?page={page}"
            soup = self.fetch_page(url)
            
            if soup is None:
                break
            
            # Add your custom scraping logic here
            print(f"Processing page {page}...")
            time.sleep(1)  # Respectful delay
    
    def scrape_with_retries(self, url, max_retries=3):
        """
        Fetch page with retry mechanism.
        """
        for attempt in range(max_retries):
            soup = self.fetch_page(url)
            if soup is not None:
                return soup
            
            print(f"Retrying... ({attempt + 1}/{max_retries})")
            time.sleep(2 ** attempt)  # Exponential backoff
        
        return None


if __name__ == "__main__":
    main()
