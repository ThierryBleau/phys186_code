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

brightness_drops = [0.06,0.05,0.5,0.03,0.03,0.03]
radii = [2.36,1,1,0.5,1,10]

def planet_radii(drops,rads):
	for i in range(6):
		earth_radius = (drops[i]/100)**(1/2)*rads[i]*109
		print(earth_radius)
		jupiter_radius = earth_radius*0.0892
		print(jupiter_radius)
	return

planet_radii([0.06,0,0,0,0,0,0],[2.36,0,0,0,0,0,0])

def vol_from_radius(rads):
	for i in rads:
		volume = (4/3)*(math.pi)*(i**3)
		print(volume)
	return

def density(masses,volumes):
	for i in range(len(masses)):
		density = masses[i]/volumes[i]
		print(density)
	return

def density_from_radii(radii,masses):
	for i in range(len(radii)):
		density = masses[i]/((4/3)*math.pi*radii[i]**3)
		print(density)
	return

def star_velocity(max_line_shift,rest_wavelength):
	velocity = (max_line_shift/rest_wavelength)*3e8
	print(velocity)
	return(velocity)

def mass_from_velocity_earth(velocity,orbit,star_mass):
	mass = ((velocity**2)*(orbit)*(star_mass))**(1/2)*(11.177)
	print(mass)
	return

def mass_from_velocity_jupiter(velocity,orbit,star_mass):
	mass = ((velocity**2)*(orbit)*(star_mass))**(1/2)*(0.0352)
	print(mass)
	return



shifts = 0.000007

mass_from_velocity_earth(star_velocity(shifts,656.3),0.3822639055257155,3.02)
mass_from_velocity_jupiter(star_velocity(shifts,656.3),0.3822639055257155,3.02)