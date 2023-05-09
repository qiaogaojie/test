import csv
with open('submit_test_new.csv','w',encoding='utf8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[1], [2]])