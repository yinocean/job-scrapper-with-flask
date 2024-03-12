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


class Berlin_Scrapper():
    def scrape_page(keyword):
        print(f"Berlinstartup Scrapping {keyword}")
        response = requests.get(
            url = f"https://berlinstartupjobs.com/skill-areas/{keyword}",
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )
        soup = BeautifulSoup(response.content, "html.parser")
        # 회사이름, 직무제목, 설명 및 직무 링크

        jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
        #print(jobs)
        if soup.find == None or soup.find == "":
            return []
        for job in jobs:
            company_name = job.find("a", class_="bjs-jlid__b").text
            position = job.find("h4", class_="bjs-jlid__h").text
            job_description = job.find(
                "div", class_="bjs-jlid__description").text
            link = job.find("h4", class_="bjs-jlid__h").find('a')['href']
            job_data = {
                "company_name": company_name,
                "position": position,
                "job_description": job_description,
                "link": link
            }
            all_jobs.append(job_data)
        #print(all_jobs)
        return all_jobs
    
    def get_pages(url):
        response = requests.get(url,
                                headers={
                                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                                }
                                )
        soup = BeautifulSoup(response.content, "html.parser")
        return len(soup.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers"))


# if __name__ == "__main__":
#     # total_pages = Berlin_Scrapper.get_pages(
#     #     "https://berlinstartupjobs.com/engineering/page/1")

#     # for x in range(total_pages):
#     #     url = f"https://berlinstartupjobs.com/engineering/page/{x+1}"
#     #     print(url)
#     #     Berlin_Scrapper.scrape_page(url)

#     for skill in skills:
#         Berlin_Scrapper.scrape_page(skill)
