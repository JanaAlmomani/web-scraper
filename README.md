# web-scraper
## Lab 17: web-scraper
## Author : Jana Almomani

## Feature Tasks and Requirements : 

`get_citations_needed_count(url)`: This function counts the number of citations needed on a web page by:

- Sending a GET request to the specified URL.
- Parsing the HTML content of the page.
- Finding all the citations needed indicators.
- Returning the count of citations as an integer.

`get_citations_needed_report(url)`: This function generates a report of the passages that require citations on a web page by:

- Sending a GET request to the specified URL.
- Parsing the HTML content of the page.
- Finding all the citations needed indicators.
- Iterating over each citation and extracting the corresponding passage.
- Formatting the passages into a report string.
- Returning the complete report as a string.

[The Code Link](./scraper.py)