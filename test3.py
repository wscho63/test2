import sqlite3
import xlrd
import xlsxwriter
import math
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

con = sqlite3.connect("testDB")
cur = con.cursor()

print("=== 월 ====== 단체 ===== 그룹 =====레저====")
cur.execute("select month, sum(d_individual), sum(d_group), sum(d_leisure) as dum_of_d_group \
from jejutourist\
group by month;")
#order by month;") 

rows = cur.fetchall()
print(rows)
nda = np.asarray(rows)
x1 = nda[:,0]
y1 = nda[:,1]
y2 = nda[:,2]
y3 = nda[:,3]
plt.figure
plt.title('Graph for the number of Individual, Group, Leisure')
plt.xlabel('Month')
plt.ylabel('No. Visitors')
plt.plot(x1, y1, '-ro', label="Individual")
#plt.legend('individual', 'Location', 'northwest')
plt.plot(x1, y2, '-.mo', label="Group")
plt.plot(x1, y3, ':go', label="Leisure")
plt.legend(loc='upper left')
plt.show()

