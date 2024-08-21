# Python Job Listings Webscraper

This project is a Python-based webscraper tool that extracts job listings related to Python from [TimesJobs](https://www.timesjobs.com/). The tool leverages the `requests` library to fetch HTML content from the job search page and `BeautifulSoup` with the `lxml` parser to parse and extract relevant job data from the website.

## Features

- **Job Extraction**: Fetches Python-related job listings from TimesJobs.
- **Skill Filtering**: Allows users to input a skill they are not familiar with and filters out jobs that require that skill.
- **Job Details Storage**: Extracted job details, including company names, required skills, and job links, are stored in individual text files for easy access and review.

## How It Works

1. The script sends an HTTP request to the TimesJobs website to retrieve job listings related to Python.
2. The HTML content is parsed using `BeautifulSoup`, and job postings are extracted based on specific HTML tags and classes.
3. The user is prompted to enter a skill they are not familiar with. The tool then filters out any jobs that list this skill as a requirement.
4. For each filtered job, details such as the company name, required skills, and a link to more information are printed to the console and saved in a text file within the `store` directory.

## Usage

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/angelshinh1/Web_Scraper_Python.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd Web_Scraper_Python
    ```
3. **Install Required Libraries**:
    ```bash
    pip install requests
    pip install beautifulsoup4
    pip install lxml
    ```
4. **Run the Script**:
    ```bash
    python main.py
    ```
5. **Follow the Prompts**: Enter a skill you want to filter out, and the script will extract and save relevant job listings.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` (`bs4` package)
- `lxml` parser

You can install the required libraries using:
```bash
pip install requests beautifulsoup4 lxml

