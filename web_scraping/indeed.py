import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_indedde_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    # ! 더보기 칸 class 이름 pagination인 div 중 a태그들 뽑아서 list만들기
    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')

    # ! a태그의 string값(1,2,3,4,5, ...) 저장
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def get_job(a_box):

    # ! title
    job_title = a_box.find("h2", {"class": "jobTitle"})
    title = job_title.find("span").string
    if title == "new":
        title = job_title.find_all("span")[1].string

    # ! company
    company = a_box.find('span', {'class': 'companyName'}).string

    # ! location
    location = a_box.find('div', {'class': 'companyLocation'}).get_text()

    job_id = a_box['data-jk']
    return {'title': title, 'company': company, 'location': location, 'link': f'https://www.indeed.com/viewjob?jk={job_id}'}


def get_indeed_jobs():

    last_page = 10
    jobs = []
    for page in range(last_page):
        print(f"Scraping indeed page:{page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "fs-unmask"})

        for result in results:
            job = get_job(result)
            jobs.append(job)
    return jobs
