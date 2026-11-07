from src.tools.tools import web_search, scrape_url


scraped_content = scrape_url.invoke({"url": "https://www.nbcnews.com/business/markets/tech-stocks-plunge-ai-midterms-rcna607650"})
print(scraped_content)