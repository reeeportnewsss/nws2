import os
import logging

# ==== CONFIGURATION ====
INPUT_NEWS_FILE = "all_stock_news.txt"  # Input file with stock news
OUTPUT_NEWS_FILE = "processed_stock_news.txt"  # Output file with instruction added

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('news_processing.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Instruction to add at the top of the file
INSTRUCTION = """
You will receive a stream of news items related to publicly traded companies. 
1. **Scan comprehensively**—do not miss any headline.
2. **Identify and prioritize** only those items with clear positive OR negative impact potential on share price; discard irrelevant fluff.
3. **Focus specifically** on these event types (but stay alert for other impactful news):
   - Mergers & Acquisitions (acquisition talks, takeover bids, joint-ventures)
   - Major Deals & Partnerships (contracts, supply agreements, strategic alliances)
   - Legal & Regulatory Actions (court rulings, lawsuits, fines, government investigations)
   - Capital Moves (fundraising rounds, debt issuances, equity offerings, share buybacks, dividends)
   - Project Launches & Infrastructure (new plant builds, R&D programs, technology roll-outs, site openings)
   - Management & Governance (CEO/CFO changes, board reshuffles, executive departures)
   - Product Milestones (FDA approvals, patent grants, major product launches)
   - Analyst Ratings & Brokerage Actions (upgrades, downgrades, new coverage, price-target revisions)
   - Earnings & Guidance (quarterly results, forward-looking guidance changes)
   - Insider & Shareholder Moves (insider buys/sells, block trades, activist stakes)
   - Sector & Macro Indicators (key economic data, industry outlook reports)
4. **For each impactful item**, indicate:
   - **Type** (e.g., “M&A,” “Rating Upgrade,” “Lawsuit,” “Funding”)
   - **Sentiment** (positive or negative)
   - **Rationale** (why it will likely drive the stock)
   - **Severity** (e.g., “high,” “moderate,” “low” impact)
5. **Ignore** any news that doesn’t clearly fit a market-moving category.

Return a ranked list: highest-impact positive stories first, highest-impact negative stories last.
"""

def process_news_file():
    """
    Read all_stock_news.txt, add instruction at the top, and save to processed_stock_news.txt.
    """
    try:
        # Read the input file
        if not os.path.exists(INPUT_NEWS_FILE):
            logger.warning(f"Input file {INPUT_NEWS_FILE} not found.")
            return False

        with open(INPUT_NEWS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
        
        if not content:
            logger.warning(f"Input file {INPUT_NEWS_FILE} is empty.")
            return False

        logger.info(f"Successfully read content from {INPUT_NEWS_FILE}")

        # Combine instruction and content
        output_content = f"{INSTRUCTION}\n\n{content}"

        # Save to output file
        with open(OUTPUT_NEWS_FILE, 'w', encoding='utf-8') as file:
            file.write(output_content)
        
        logger.info(f"Processed content saved to {OUTPUT_NEWS_FILE}")
        return True

    except Exception as e:
        logger.error(f"Error processing news file: {e}")
        return False

def main():
    """
    Main function to process the news file.
    """
    if process_news_file():
        logger.info("News file processing completed successfully.")
    else:
        logger.error("News file processing failed.")

if __name__ == "__main__":
    main()
