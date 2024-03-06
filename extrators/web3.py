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


class Web3_Scrapper():
    def scrape_page(keyword):
        print(f"Web3 Scrapping {keyword}")
        response = requests.get(url=f"https://web3.career/{keyword}-jobs", headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("tbody", class_ = "tbody").find_all("tr")
        for job in jobs:
            if not job.find("h3") == None:
                company_name = job.find("h3").text
            if not job.find("h2") == None:
                position = job.find("h2").text
            if not job.find("p", class_="ps-0 mb-0 text-salary") == None:
                job_description = job.find("p", class_="ps-0 mb-0 text-salary").text
            if not job.find("div", class_="mb-auto align-middle job-title-mobile") == None:
                link = job.find("div", class_="mb-auto align-middle job-title-mobile").find('a')['href']
            job_data = {
                "company_name": company_name,
                "position": position,
                "job_description": job_description,
                "link": f"https://web3.career{link}"
            }
            all_jobs.append(job_data)
        #print(all_jobs)
        return all_jobs 
    
# if __name__ == "__main__":
#     for skill in skills:
#         url =  f"https://web3.career/{skill}-jobs"
#         Web3_Scrapper.scrape_page(url)
#         #print(Web3_Scrapper.scrape_page(url))