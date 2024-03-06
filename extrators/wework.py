import requests
from bs4 import BeautifulSoup

all_jobs = []
skills = [
    "python",
    "javascript",
    "java",
    "rust",
    "golang"
]

class Wework_Scrapper():
    def scrape_page(keyword):
        print(f"Wework Scrapping {keyword}")
        response = requests.get(url=f"https://weworkremotely.com/categories/remote-full-stack-programming-jobs", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

        for job in jobs:
            title = job.find("span", class_="title").text
            company, position, region = job.find_all("span", class_ = "company")
            link = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
            job_data  = {
                "company_name":company.text,
                "position" : title,
                "job_description" : region.text,
                "link" : f"https://weworkremotely.com{link}"
            }
            all_jobs.append(job_data)
        # print(all_jobs)
        return all_jobs

    def get_pages(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find("div", class_="pagination").find_all("span", class_="page")

# if __name__ == "__main__":
    # total_pages = Wework_Scrapper.get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

    # for x in range(total_pages):
    #     url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    #     print(url)
    #     Wework_Scrapper.scrape_page(url)
    
    # for skill in skills:
    #     print(Wework_Scrapper.scrape_page(skill))