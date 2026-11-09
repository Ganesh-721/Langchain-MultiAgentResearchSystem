import json

from src.agents.agents import writer_chain, critic_chain
from src.tools.tools import web_search, scrape_url


def run_research_pipeline(topic: str) -> dict:
    # Search and decode Tavily's JSON response
    raw_search = web_search.invoke({"query": topic})
    search_data = json.loads(raw_search)

    # Scrape each result
    scraped_contents = []

    for result in search_data.get("results", []):
        url = result.get("url")
        if not url:
            continue

        content = scrape_url.invoke({"url": url})
        scraped_contents.append(f"Source: {url}\n{content}")

    if not scraped_contents:
        raise RuntimeError(f"No pages could be scraped for topic: {topic}")

    # Write the report, then critique it
    research_report = writer_chain.invoke({
        "topic": topic,
        "research": "\n\n".join(scraped_contents),
    })

    critique = critic_chain.invoke({
        "report": research_report,
    })

    return {
        "research_report": research_report,
        "critique": critique,
    }