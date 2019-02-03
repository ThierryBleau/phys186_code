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

def ly_star_distances(arc_secs):
	for i in arc_secs:
		ly = 3.26/i
		print(ly)

app_mag = [6.114,3.59,9.842]
parallax = [0.0724,0.0112,0.012]

def luminosity(mag,par):
	for i in mag:
		pari = par[mag.index(i)]
		abs_mag = i + 5 + 5*math.log10(pari)
		lum = math.pow(10,(4.8-abs_mag)/2.5)
		print(lum)
		return(lum)

temps = [3371,14447,705,17626,2894]
def peak_wavelength(temp):
	for i in temp:
		pw = 2897769.5/i
		print(pw)

wavelengths = [404,4110,383,860,446]
def temperature(wl):
	for i in wl:
		temp = 2897769.5/i
		print(temp)
		return(temp)

def lifetime(mass):
	lt = pow(10,10)*pow(mass,-2.5)
	print(lt)

def radius(lum,temp):
	r = pow(lum,1/2)/pow(temp/5800,2)
	print(r)

def lum_from_mass(mass):
	lum = pow(mass,3.5)
	print(lum)

def mass_from_lum(lum):
	mass = pow(lum,1/3.5)
	print(mass)

brightness_drops = [0.005,0.05,0.5,0.03,0.03,0.03]
radii = [1,1,1,0.5,1,10]

def planet_radii(drops,rads):
	for i in range(6):
		earth_radius = (drops[i]/100)**(1/2)*rads[i]*109
		print(earth_radius)
		jupiter_radius = earth_radius*0.0892
		print(jupiter_radius)
	return

planet_radii(brightness_drops,radii)
