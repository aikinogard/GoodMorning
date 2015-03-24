import urllib2
import re
import time

def which_weekday():
	"""
		return which weekday it is.
		Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
	"""
	return time.strftime('%A',time.localtime(time.time()))

def which_day():
	"""
		return dd/mm
	"""
	m = time.strftime('%m',time.localtime(time.time()))
	if m[0] == '0':
		m = m[1:]
	d = time.strftime('%d',time.localtime(time.time()))
	if d[0] == '0':
		d = d[1:]
	return m+'/'+d

def check_holiday(day):
	"""
		TODO: check whether today is a holiday
	"""
	req = urllib2.Request('http://www.campusrec.uci.edu/arc/hours.asp')
	source = urllib2.urlopen(req).read()
	m = re.search(r'UPCOMING HOLIDAY HOURS.*?(\<table.*?</table>)',source,re.DOTALL)
	print m.group(1).strip()


def ARC_hours_normal(weekday=None):
	"""
		Give the ARC hour
	"""
	if weekday==None:
		weekday = which_weekday()
	req = urllib2.Request('http://www.campusrec.uci.edu/arc/hours.asp')
	source = urllib2.urlopen(req).read()

	if weekday in ['Friday','Saturday','Sunday']:
		day_string = weekday
	else:
		day_string = r'Monday\s-\sThursday'

	m = re.search(r'Fitness\sLab,\sWellness\sLab.*?'+day_string+'.*?(\d+\s?[ap]m\s-\s\d+\s?[ap]m)',source,re.DOTALL)
	print 'ARC hours on %s: %s'%(weekday,m.group(1).strip())

if __name__=='__main__':
	ARC_hours_normal('Monday')
	ARC_hours_normal('Friday')
	ARC_hours_normal('Saturday')
	ARC_hours_normal('Sunday')
	print which_day()
	print check_holiday('d')



