from ingest_all_sequential import ingest_paysim
from ingest_all_sequential import ingest_fred
from ingest_all_sequential import run_sequential
from concurrent.futures import ThreadPoolExecutor,as_completed,ProcessPoolExecutor
import time



def run_parallel(max_workers: int = 2):
    with ThreadPoolExecutor (max_workers=max_workers) as excute:
        f1=excute.submit(ingest_paysim)
        f2=excute.submit(ingest_fred)
        futures=[f1,f2]
        for i in as_completed(futures):
          try:
               i.result()
          except Exception as e:
               print(e)

                  
def  benchmark_ingestion():
          start=time.perf_counter()
          run_sequential()
          end=time.perf_counter()
          r1=(end-start)
        
          start=time.perf_counter()
          run_parallel()
          end=time.perf_counter()
          r2=(end-start)
          return(r1,r2)
          
 
    

          
#if __name__ == "__main__":
      #sequential, parallel = benchmark_ingestion()

      #print("Sequential:", sequential)
      #print("Parallel:", parallel)

sequential_times = []
parallel_times = []

for _ in range(10):
    start = time.perf_counter()
    run_sequential()
    sequential_times.append(time.perf_counter() - start)

    start = time.perf_counter()
    run_parallel()
    parallel_times.append(time.perf_counter() - start)

#print("Average Sequential:", sum(sequential_times) / len(sequential_times))
#print("Average Parallel:", sum(parallel_times) / len(parallel_times))      


def parallel(max_workers: int = 2):

    with ProcessPoolExecutor(max_workers=max_workers) as executor:

        f1 = executor.submit(ingest_paysim)
        f2 = executor.submit(ingest_fred)
        

        futures = [f1, f2]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(e)
parallel()
