import math

def comp1():
    for i in range(11,33):
        y = 1.5*i + 3
        print(i)
        print(y)

def comp2():
    for i in range(11,33):
        y = 10**(-8*i+7)
        print(i)
        print(y)

arc_secs = []
def ly_star_distances():
	for i in arc_secs:
		ly = 3.26/i
		print(ly)

app_mag = [6.114,3.59,9.842]
parallax = [0.0724,0.0112,0.012]

def luminosity(mag,par):
	for i in mag:
		print(i)
		pari = par[mag.index(i)]
		abs_mag = i + 5 + 5*math.log10(pari)
		lum = math.pow(10,(4.8-abs_mag)/2.5)
		print(lum)

luminosity(app_mag,parallax)