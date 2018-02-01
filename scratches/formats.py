year = 2017
principal = 0.212745646541541
print("{0:3d} {1:0.10f} {2:s}".format(year, principal, 'Vada'))
print("{} {:0.2f} {}".format(year, principal, 'Vada'))

url = 'http://mypage/page_number_{}/help'
url2 = 'http://mypage/page_number_%d/help'

print(url.format(123))
print(url.format(1232))
print(url2 % 123)
