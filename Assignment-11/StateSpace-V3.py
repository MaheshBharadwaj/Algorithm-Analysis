'''
 S H A N T A 
+  M E E N A
------------
 G A N D H I
------------
'''
def test(s,h,a,n,t,m,e,g,d,i):
	return (s * 100000 + h * 10000 + a * 1000 +  n * 100 + t * 10 + a +\
            m * 10000 + e * (1000 + 100) + n * 10 + a\
            == g * 100000 + a * 10000 + n * 1000 + d * 100 + h * 10 + i)

i = 0
while i < 9:
    s = 1
    while s <=9:
        if s == i:
            s += 1
            continue
        m = 1
        while m <= 9:
            if m == s or m == i:
                m += 1
                continue
            h = 0
            while h <= 9:
                if h + m < 9 or h == i or h == m or h == s:
                    h += 1
                    continue
                n = 0
                while n <= 9:
                    if n == i or n == h or n == m or n == s:
                        n += 1
                        continue
                    t = 0
                    while t <= 9:
                        if t == i or t == m or t == h or t == n or t == s:
                            t += 1
                            continue
                        e = 0
                        while e <= 9:
                            if e == i or e == s or e == m or e == h or e == n or e == t:
                                e += 1
                                continue
                            a = 0
                            while a <= 9:
                                if a == i or a == s or a == m or a == h or a == n or a == t or a == e:
                                    a += 1
                                    continue 
                                g = 1
                                while g <= 9:
                                    if g == i or g == s or g == m or g == h or g == n or g == t or g == e or g == a:
                                        g += 1
                                        continue
                                    d = 0
                                    while d <= 9:
                                        if d == i or d == s or d == m or d == h or d == n or d == t or d == e or d == a or d == g:
                                            d += 1
                                            continue
                                        if test(s,h,a,n,t,m,e,g,d,i):
                                            shanta = s * 100000 + h * 10000 + a * 1000 + n * 100 + t * 10 +  a
                                            meena = m * 10000 + e * (1000 + 100) + n * 10 + a
                                            print('  %d' % (shanta))
                                            print(' + %d' % (meena))
                                            print('  ------')
                                            print('  %d' % (shanta + meena))
                                            print('  ------\n\n')
                                        d += 1
                                    g += 1
                                a += 1
                            e += 1
                        t += 1
                    n += 1
                h += 1
            m += 1
        s += 1
    i += 2
						
									
				 
