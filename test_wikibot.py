from wikibot import ScrapeWikipedia


def test_scrape_wikipedia():
    result = ScrapeWikipedia("Python (programming language)", 2)
    assert "Python" in result
