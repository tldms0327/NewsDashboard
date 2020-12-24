from NewsCrawler.time_crawler import Crawler
from multiprocessing import Process
from time import sleep


categories = {'정치': 100, '경제': 101, '사회': 102, '생활문화': 103, '세계': 104, 'IT과학': 105, '오피니언': 110}
keys = list(categories.keys())
procs = []
for category_name in keys:
    crawler = Crawler(category_name)
    proc = Process(target=crawler.continuous_crawling)
    procs.append(proc)
    proc.start()
    sleep(3)

for proc in procs:
    proc.join()