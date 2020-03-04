'''
  S E N D 
+ M O R E
---------
M O N E Y
---------
'''


def test(s,e,n,d,m,o,r,y):
	return (s * 1000 + e * 100 + n * 10 + d + m * 1000 + o * 100 + r * 10 + e == m * 10000 + o * 1000 + n * 100 + e * 10 + y) 

s = 1
while s <=9:
	m = 1
	while m <= 9:
		if s + m < 9 or m == s:
			m += 1
			continue
		e = 0
		while e <= 9:
			if e == m or e == s:
				e += 1
				continue
			n = 0
			while n <= 9:
				if n == e or n == m or n == s:
					n += 1
					continue
				d = 0
				while d <= 9:
					if d == n or d ==  e or d == m or d == s:
						d += 1
						continue
					o = 0
					while o <= 9:
						if o == d or o == n or o == e or e == m or e == s:
							o += 1
							continue
						r = 0
						while r <= 9:
							if r == o or r == d or r == n or r == e or r == m or r == s:
								r += 1
								continue 
							y = 0
							while y <= 9:
								if y == r or y == o or y == d or y == n or y == e or y == m or y == s:
									y += 1
									continue
								if test(s,e,n,d,m,o,r,y):
									send = s * 1000 + e * 100 + n * 10 + d
									more = m * 1000 + o * 100 + r * 10 + e
									print('  %d' % (send))
									print(' +%d' % (more))
									print(' -----')
									print(' %d' % (send+more))
									print(' -----\n\n')
								y += 1
							r += 1
						o += 1
					d += 1
				n += 1
			e += 1
		m += 1
	s += 1
 
						
									
				 
