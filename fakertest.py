from faker import Factory
from faker import Faker
fake = Factory.create()
f=Faker()
import pyexcel
#column header list
colomn=['Name','Email','Address','Company']
data=[]
#appending header to data list
data.append(colomn)
count=raw_input("How many test data you wants: ")
for i in range(0,int(count)):
    name=fake.name()
    email=fake.email()
    address=fake.address()
    company=fake.company()
    c=[name,email,address,company]
    data.append(c)
print data
try:
    pyexcel.save_as(array = data, dest_file_name = 'fake_data.csv')
except:
    print "File write error! Try again"     