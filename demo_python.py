#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib, urllib2,base64
import ssl

#https
host='https://vcode.weibits.com'
path = '/vcode'
#post
method = 'POST'


#your appcode= 自己的appcode
appcode = 'APPCODE 自己的appcode'

querys = ''
bodys = {}
url = host + path

f=open('./2079569834.jpg','rb')
imgdata=f.read()
base64=base64.b64encode(imgdata)
#base64='/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAYADwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD35twU7QC2OATgE1xPiTx3Jp+r6fpmg6dLrOqT273T2kciRxJACQXeY/KhDKQOSOoPJU12kTO8SNImxyoLJnO09xnvXmXiHQ/EGj+MrzxN4c0641NtVjjiu9Pa4W3KOihUkEo/g2ggpuB3EMcjAW4LXUmUZPZnUeFvGDeIHudOv9Nm0XXrYM0un3R3Ex7ioljbAEsZIxuXjPHQqTHB43hbx+/hKa1KzrFkXAfKu+wPtC44Gwk5J6jHPWuCi8SaxpnxRv8AXfFOl2+nzw+Fi0VlDP5pA+0qqq7qCNzSZ5GQFZc8g1QufEuiWXg6yvrDV0l8U297/akxNrIpmlk/1sZYYCrggNtIDCPpzVwhfoc9erySVnbr6o9O8OeMrTxnYS3eizraiCXypYr2EM+SBtOFk4ByQCepB9Kj8UeMItChGkLJFdeI7pEFpaqjxLKZH2Kd2SFwc9XBO3qMg1yHw6sbbwtrem2KPvtfEmjRXJMxDsbpBvaMBfup5chPzDnjB7VzWpJrPirxvYazZi2kOoXsr6PJJJIoMVpkgYz8queSDg7gT8gOTbir2W39f8EmVSShdfE/6/yPVPAt9d3GmNbXuqR3Wo2dzPbXybB99HIBXheCCpJwc57HNbf/AAkWjrxLqVvbv3iuX8mRfqj4YevI6c1wfwytdWnutd/tKCx+zDUbjzijOZVugUzg5xtAJwfvA55559IMDgARyYUDHzlmP57qwbVy4TqygmieuR1vw34gutQSXQvG91pR8oJJBNaxXalVJ2lQ2Cp+ZgWJJb5cn5aKKm9jptcytN+G0Jna7udc1G+kvLmK51c3kO37a8Q+RApACRAk/JhhjAyNoI7LX7CXVfDmqadAyLNdWksCM5IUMyFQTjPGTRRTUnoJwim/M4SX4Y6g/gfTNKTVbWPU9PjuFinWBipWdCJIjluhLEb9uQAMKDnO7qHh2ePxb4Ml061xpmkR3UUh8wfulaFUjHzHc3THf3ooq/aye/n+JCpRW3l+Bp2j6L4fvr+13QWLXM325zLccTPJkM3zHg5Q8DgDHrgbRcA4Ib8FJoop1YqMYyXUzozbco9n/mf/2Q=='


bodys['convert_to_jpg'] = '0'
bodys['img_base64'] =base64
bodys['typeId'] = '34'

post_data = urllib.urlencode(bodys)
request = urllib2.Request(url, post_data)
request.add_header('Authorization', appcode)
request.add_header('connection', 'keep-alive');

request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request,context=ctx)
#response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
