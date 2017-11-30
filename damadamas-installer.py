#!/usr/bin/python3
import os


def tekliDegisiklik(url,degisecekRenk,yeniRenk):
	try:
		dosya = open(url,"r")
		okunan = dosya.read()
		fonkk = degistirKoordinat(okunan,degisecekRenk)
		okunan_1 = degistir(okunan,yeniRenk,fonkk)
		dosya.close()
		dosya = open(url,"w")
		dosya.write(okunan_1)
		dosya.close()
	except IOError:
		pass


def sarkiKlasorAktar(url,degisecekRenk,yeniRenk):
	dosyaninici = os.listdir(url)
	dosyaninici.sort()
	for i in dosyaninici:
		dosya = i.lower()
		if dosya.endswith(".svg"):
			try:
				dosya = open(url+"/"+i,"r")
				okunan = dosya.read()
				fonkk = degistirKoordinat(okunan,degisecekRenk)
				okunan_1 = degistir(okunan,yeniRenk,fonkk)
				dosya.close()
				dosya = open(url+"/"+i,"w")
				dosya.write(okunan_1)
				dosya.close()
			except:
				pass
		elif os.path.isdir(url+"/"+i):
			sarkiKlasorAktar(url+"/"+i,degisecekRenk,yeniRenk)

def degistirKoordinat(metin,renk):
	liste = []
	for i in range(len(metin)):
		if metin[i:i+len(renk)]==renk:
			liste.append(i)
	return liste

def degistir(metin,yrenk,listeKoordinat):
	yeniMetin = ""
	koordinat = 0
	if len(listeKoordinat) != 0:
		for x in listeKoordinat:
			yeniMetin += metin[koordinat:x]
			yeniMetin += yrenk
			koordinat = x + len(yrenk)
		yeniMetin += metin[koordinat:len(metin)]
		return yeniMetin
	else:
		return metin

def silinsinmi():
	gelen = input("If you continue the DamaDamas icon theme board will be deleted and installed on your system.\nWould you like to do it?(Y) or (N)")
	if gelen == "Y":
		sil =  True
	elif gelen == "N":
		close()
	else:
		print("Cant understand Y or N please.\n")
		silinsinmi()

def renk_degissinmi():
	global renk_degissin
	gelen = input("Damadamas icons are prepared in SVG format.\nThis advantage gives you the possibility to determine the color of the icons.\n Do you want to change colors? (Y) or (N)::")
	if gelen == "Y":
		renk_degissin = True
	elif gelen == "N":
		renk_degissin = False
	else:
		renk_degissinmi()


folder_colors = {"default":["faec6d","ffb800"],"black":["383e43","212121"],"blue":["3daed8","2c89a0"],"brown":["c87137","a05a2c"],
				"cyan":["5fd3bc","2ca089"],"green":["99ff55","55d400"],"grey":["9b9b9b","6e6e6e"],"orange":["ff7f2a","d45500"],
				"pink":["ff5599","ff2a7f"],"red":["ff2a2a","d40000"]}
def dosya_rengi_secenekleri():
	global dosya_rengi
	gelen = input("\nPlease specify a file color. \n Options:\n[ ] default \n[ ] black\n[ ] blue\n[ ] brown\n[ ] cyan\n[ ] green\n[ ] grey\n[ ] orange\n[ ] pink\n[ ] red\n[ ] custom\n::")
	if gelen == "default":
		dosya_rengi = False
	elif gelen == "custom":
		dosya_rengi = custom_dosya_rengi()
	else:
		varmi = folder_colors.get(gelen, "bunelan")
		if varmi == "bunelan":
			print("Cant understand\n====================================")
			dosya_rengi_secenekleri()
		else:
			dosya_rengi = varmi

def renk_kontrol(renk):
	liste = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	if len(renk) != 6:
		return False
	for i in renk:
		if i in liste:
			pass
		else:
			return False
	return True

def custom_dosya_rengi():
	print("Please enter a color in HTML color format.\n(do not put # in rich first) Example: ffffff")
	gelen_acik = input("light color ::")
	gelen_koyu = input("dark color ::")
	if renk_kontrol(gelen_acik) and renk_kontrol(gelen_koyu):
		return [gelen_acik,gelen_koyu]
	else:
		print("Incorrect color format\n")
		custom_dosya_rengi()

def custom_aksiyon_rengi():
	print("Please enter a color in HTML color format.\n(do not put # in rich first) Example: ffffff")
	gelen = input("color ::")
	if renk_kontrol(gelen):
		return gelen
	else:
		print("Incorrect color format\n")
		custom_aksiyon_rengi()

def aksiyon_rengi_secenekleri():
	global aksiyon_rengi
	gelen = input("\nPlease select colors for actions icons.\n Options:\n[ ] dark\n[ ] light\n[ ] custom\n::")
	if gelen == "dark":
		aksiyon_rengi = False
	elif gelen == "light":
		aksiyon_rengi = "f7f7f7"
	elif gelen == "custom":
		aksiyon_rengi = custom_aksiyon_rengi()
	else:
		print("Cant understand\n====================================")
		aksiyon_rengi_secenekleri()

def panel_rengi_secenekleri():
	global panel_rengi
	gelen = input("\nPlease select colors for panel icons.\n Options:\n[ ] dark\n[ ] light\n[ ] custom\n::")
	if gelen == "dark":
		panel_rengi = "394050"
	elif gelen == "light":
		panel_rengi = False
	else:
		panel_rengi = custom_aksiyon_rengi()

print("Welcome to the DamaDamas icon theme installer.\n\n")
if os.getuid() != 0:
	print("Damadamas icon theme installer will run as not root.\nThe icon will be installed in {}/.icons file.\n\n".format(os.path.expanduser("~")))
	url = os.path.expanduser("~")+"/.icons"
else:
	print("Damadamas icon theme installer will run as root.\nThe icon will be installed in /usr/share/icons file.\n\n")
	url = "/usr/share/icons"

sil = False
if os.path.exists(url+"/DamaDamas-icon-theme"):
	silinsinmi()

renk_degissinmi()

print("Copying files. Please wait...")
if not os.path.exists(url+"/DamaDamas-icon-theme"):
	os.makedirs(url+"/DamaDamas-icon-theme")
for dirs in os.listdir(os.getcwd()):
	if dirs != "damadamas-installer.py":
		print(os.getcwd()+"/"+dirs)
		os.system("rsync --delete -axHAWX --numeric-ids " + os.getcwd()+"/"+dirs + " " + url + "/DamaDamas-icon-theme" + " --exclude /proc")
print("Complate.\n=====================================")

if renk_degissin:
	dosya_rengi_secenekleri()
	aksiyon_rengi_secenekleri()
	panel_rengi_secenekleri()
	if dosya_rengi:
		print("Change folder colors...")
		sarkiKlasorAktar(url + "/DamaDamas-icon-theme/places/user-folders/",folder_colors.get("default")[0],dosya_rengi[0])
		sarkiKlasorAktar(url + "/DamaDamas-icon-theme/places/user-folders/",folder_colors.get("default")[1],dosya_rengi[1])
		for i in [url+"/DamaDamas-icon-theme/apps/scalable/folder-template.svg",url+"/DamaDamas-icon-theme/apps/scalable/folder_templates.svg",url+"/DamaDamas-icon-theme/apps/scalable/folder-templates.svg",url+"/DamaDamas-icon-theme/apps/scalable/folder-wine.svg",url+"/DamaDamas-icon-theme/apps/scalable/network-workgroup.svg",url+"/DamaDamas-icon-theme/apps/scalable/shares.svg",url+"/DamaDamas-icon-theme/mimetypes/file-types/inode-directory.svg"]:
			tekliDegisiklik(i,folder_colors.get("default")[0],dosya_rengi[0])
			tekliDegisiklik(i,folder_colors.get("default")[1],dosya_rengi[1])
	if aksiyon_rengi:
		print("Change actions colors...")
		sarkiKlasorAktar(url + "/DamaDamas-icon-theme/actions/","394050",aksiyon_rengi)
	if panel_rengi:
		print("Change actions colors...")
		sarkiKlasorAktar(url + "/DamaDamas-icon-theme/status/panel/","f7f7f7",panel_rengi)
	print("İnstalled Success..\nYou can use damadamas theme from system settings.")
