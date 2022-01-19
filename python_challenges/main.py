import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://www.alba.co.kr/'


def get_last_pages(link):
    result = requests.get(link)
    result = requests.get('http://jindoya.alba.co.kr/job/brand/')
    soup = BeautifulSoup(result.text, 'html.parser')

    paging = soup.find('div', {'class': 'goodsJob'}).find_all(
        'script', {'type': 'text/javascript'})[-1]
    last_page = str(paging).split(
        'Number(intPage) == Number("')[1].split('")')[0]
    return int(last_page)


def get_jobs(link, page):
    jobs_list = []
    result = requests.get(f'{link}?page={page}')
    soup = BeautifulSoup(result.text, 'html.parser')
    goodsList = soup.find('div', {'class': 'goodsList'}).find(
        'tbody').find_all('tr', {'class': ''})

    # ! 채용공고 없는 회사
    if goodsList[0].get_text() == '채용공고가 없습니다.':
        return jobs_list

    for jobs in goodsList:
        place = jobs.find('td', {'class': 'local'}).get_text(strip=True)
        if('\xa0' in place):
            place1, palce2 = place.split('\xa0')
            place = place1 + ' ' + palce2
        title = jobs.find('td', {'class': 'title'}).find(
            'span', {'class': 'company'}).get_text(strip=True)
        time = jobs.find('td', {'class': 'data'}).get_text()
        pay_time = jobs.find('td', {'class': 'pay'}).find(
            'span', {'class': 'payIcon'}).get_text(strip=True)
        pay_number = jobs.find('td', {'class': 'pay'}).find(
            'span', {'class': 'number'}).get_text(strip=True)
        date = jobs.find('td', {'class': 'regDate'}).get_text()
        jobs_list.append({'place': place, 'title': title,
                          'time': time, 'pay': pay_time + pay_number, 'date': date})
    return jobs_list
# print(jobs_list)


def save_csv(jobs, brand):
    if '/' in brand:
        brand = brand.replace('/', ',')
    file = open(f'{brand}.csv', mode="w")
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])

    for job_list in jobs:
        for job in job_list:
            writer.writerow(list(job.values()))


def super_brand():
    companies_list = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    companies = soup.find_all('li', {'class': 'impact'})

    for company in companies:
        jobs = []
        brand = company.find('span', {'class': 'company'}).get_text(strip=True)
        print(type(brand), brand)
        link = company.find('a')['href']

        last_page = get_last_pages(link)
        for page in range(last_page):
            jobs.append(get_jobs(link, page+1))

        save_csv(jobs, brand)

    return companies_list


super_brand()
