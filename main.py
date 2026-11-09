from src.pipelines.pipelines import run_research_pipeline

if __name__ == "__main__":
    topic = "Artificial Intelligence in Healthcare"
    results = run_research_pipeline(topic)
    print("Research Report:")
    print(results["research_report"])
    print("\nCritique:")
    print(results["critique"])

