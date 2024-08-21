from bs4 import BeautifulSoup
import requests


def extract_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    ).text

    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        publish_date = job.find("span", class_="sim-posted").span.text
        if "few" in publish_date:
            # use the replace method to remove the extra spaces and get the correctly formatted text
            # we replace the space with an empty string
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if odd_skill not in skills:
                #store text in it's own file
                with open(f'store/store_{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                    f.write("\n")
                
                #use the strip method to remove the extra spaces
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print(f"Information stored in file store_{index}.txt")
                print("")  # print an empty line to separate the jobs
                


if __name__ == "__main__":
    while True:
        print("Enter a skill that are new to you/you are not familiar or good with")
        odd_skill = input(">")
        print(f"Filtered out: {odd_skill}")
        extract_jobs()
        print("Do you want to search again? (yes/no)")
        answer = input(">")
        if answer.lower() == "no":
            break