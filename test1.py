#!/usr/bin/env /usr/bin/python
import datetime
now = datetime.datetime.now()
print "-" * 25
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

print "-" * 25
print "1 week ago was it: ", now - datetime.timedelta(weeks=1)
print "100 days ago was: ", now - datetime.timedelta(days=100)
print "1 week from now is it: ",  now + datetime.timedelta(weeks=1)
print "In 1000 days from now is it: ", now + datetime.timedelta(days=1000)

print "-" * 30
birthday = datetime.datetime(1972,8,04)

print "Birthday in ... ", now - birthday
print "-" * 30

print "test: {}".format(10)
print "test: {}".format(20)
print "for commit -1 : {}".format(20)
print "for commit -2 : {}".format(20)
