from src.agents.agents import writer_chain, critic_chain
from src.tools.tools import get_search_results, scrape_url


def run_research_pipeline(topic: str) -> dict:
    search_data = get_search_results(topic)

    scraped_contents = []

    for result in search_data.get("results", []):
        url = result.get("url")
        if not url:
            continue

        content = scrape_url.invoke({"url": url})
        scraped_contents.append(f"Source: {url}\n{content}")

    if not scraped_contents:
        raise RuntimeError(f"No pages could be scraped for topic: {topic}")

    research_report = writer_chain.invoke({
        "topic": topic,
        "research": "\n\n".join(scraped_contents),
    })

    critique = critic_chain.invoke({"report": research_report})

    return {
        "research_report": research_report,
        "critique": critique,
    }