import requests
import csv
from typing import List, Tuple
import Bio
import threading
import time
from Bio.Blast import NCBIWWW


results = []
threads = []


def blastn_helper(sequence: str):
    print("starting thread"+sequence, flush=True)
    blast_result = NCBIWWW.qblast('blastp', 'nr', sequence, hitlist_size=1)
    protiens = (sequence, blast_result)
    results.append(protiens)
    print("proteins: "+str(protiens), flush=True)
    print("results: "+str(results), flush=True)
    print("helper method done", flush= True)


def get_ids(data: csv) -> List[Tuple]:

    with open(data) as prion_data:
        reader = csv.reader(prion_data, delimiter=",")
        ids_list = []
        count = 0
        for lines in reader:
            print(count, flush=True)
            if(count >=2):
                break
            # blast_result = NCBIWWW.qblast("tblastn", "nr", lines[1],
            #                               hitlist_size=1)
            # proteins = (lines[1], blast_result)
            # ids_list.append(proteins)
            time.sleep(0.5)
            download_thread = threading.Thread(target=blastn_helper, args=[lines[1]])
            threads.append(download_thread)
            download_thread.start()
            count += 1
        return ids_list


print(get_ids("data.csv"))

print("ahhhhhhhhhhhhhhhhhhhhhh")
