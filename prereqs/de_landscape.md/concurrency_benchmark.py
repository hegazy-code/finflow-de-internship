

import requests
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

urls=[
"https://api.stlouisfed.org/fred/release/tables?release_id=53&api_key=abcdefghijklmnopqrstuvwxyz123456&element_id=12886",
"https://api.stlouisfed.org/fred/releases/dates?api_key=abcdefghijklmnopqrstuvwxyz123456",
"https://api.stlouisfed.org/fred/release/series?release_id=51&api_key=abcdefghijklmnopqrstuvwxyz123456",
"https://api.stlouisfed.org/fred/release/sources?release_id=51&api_key=abcdefghijklmnopqrstuvwxyz123456",
 "https://api.stlouisfed.org/fred/release/tags?release_id=86&api_key=abcdefghijklmnopqrstuvwxyz123456"
 


]
def fetch_sequential(urls):
    result1 = []
    for url in urls:
        response = requests.get(url)
        result1.append(len(response.content)) 
    
    return result1


def fetch_parallel(urls):
    result2 = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        result2.append(executor.map(requests.get, urls))
    return result2

def compute_heavy(n):
    prime_sum=0
    flag=True
    if n<2:
         flag=False
    for i in range(2,int(n**0.5)):
        if n%i==0:
            flag=False
    if flag==True:
        prime_sum+=n
    return prime_sum    
   

def run_squential(list:int)->int:
    list1=[]
    for i in list:
      list1.append(compute_heavy(i))
    return list1   





    
def run_parallel(list:int)->int:
 with ProcessPoolExecutor(max_workers=4) as executor: 
  executor.map(compute_heavy, list)
  

if __name__ == "__main__":

    listNum =  [500_000, 600_000, 700_000, 800_000]


    start = perf_counter()
    fetch_sequential(urls)
    end = perf_counter()
    print(end - start)

    start = perf_counter()
    fetch_parallel(urls)
    end = perf_counter()
    print(end - start)

    start = perf_counter()
    run_squential(listNum)
    end = perf_counter()
    print(end - start)

    start = perf_counter()
    run_parallel(listNum)
    end = perf_counter()
    print(end - start)

      
               
    
#In Part A, we used ThreadPoolExecutor because we had multiple URLs to download. If we downloaded them one by one, the program would spend a lot of time waiting for each
#server  to respond. Instead, ThreadPoolExecutor creates multiple worker threads and distributes the download tasks among them using threads allows multiple requests to be sent and received , which can  reduce the total time taken to download all the URLs.



#in part B,we used processpoolExcutor because the task involve hard calculations ProcessPoolExecutor creates multiple worker processes that can run calculations in parallel 
#on different CPU cores, which can significantly improve performance for calculations intensive tasks.