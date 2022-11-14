#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        emp_id = argv[1]
        page = "https://jsonplaceholder.typicode.com/"
        respo = requests.get("{}users/{}".format(page, emp_id))
        name = respo.json().get("name")
        if name:
            allreq = requests.get(
                    "{}todos?userid={}".format(page, emp_id)).json()
            alltsk = len(allreq)
            complatedtask = []
            for t in allreq:
                if t.get("completed") is True:
                    complatedtask.append(t)
            count = len(complatedtask)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in complatedtask:
                print("\t {}".format(title.get("title")))
