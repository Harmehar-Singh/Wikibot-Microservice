import wikipedia
def ScrapeWikipedia(name = "Microsoft", length = 3):
    try:
        summary = wikipedia.summary(name, sentences = length)
        return summary
    except Exception as e:
        return f"Error: {str(e)}"
print(ScrapeWikipedia())