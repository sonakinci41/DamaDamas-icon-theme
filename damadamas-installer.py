#!/usr/bin/python3
import os


def file_icons_change_color(url,c_color,new_color):
	"""We change the index, the color to change, the new color parameters,
	and change the color to the new color for all the icons in the corresponding index."""
	try:
		file_ = open(url,"r")
		read_ = file_.read()
		fonkk = search_color(read_,c_color)
		read_1 = change_icon_color(read_,new_color,fonkk)
		file_.close()
		file_ = open(url,"w")
		file_.write(read_1)
		file_.close()
	except IOError:
		pass


def folder_icons_change_color(url,c_color,new_color):
	"""We change the index, the color to change, the new color parameters,
	and change the color to the new color for all the icons in the corresponding index."""
	dirs = os.listdir(url)
	dirs.sort()
	for i in dirs:
		file_ = i.lower()
		if file_.endswith(".svg"):
			try:
				file_ = open(url+"/"+i,"r")
				read_ = file_.read()
				fonkk = search_color(read_,c_color)
				read_1 = change_icon_color(read_,new_color,fonkk)
				file_.close()
				file_ = open(url+"/"+i,"w")
				file_.write(read_1)
				file_.close()
			except:
				pass
		elif os.path.isdir(url+"/"+i):
			folder_icons_change_color(url+"/"+i,c_color,new_color)

def search_color(read_,color):
	"""We simply search in the file and write the coordinates in which the color is in the list and return"""
	list_ = []
	for i in range(len(read_)):
		if read_[i:i+len(color)]==color:
			list_.append(i)
	return list_

def change_icon_color(read_,new_color,list_coordinates):
	n_read_ = ""
	coordinat = 0
	if len(list_coordinates) != 0:
		for x in list_coordinates:
			n_read_ += read_[coordinat:x]
			n_read_ += new_color
			coordinat = x + len(new_color)
		n_read_ += read_[coordinat:len(read_)]
		return n_read_
	else:
		return read_

def question_is_delete():
	"""We are alerted to the fact that the icons are already installed
	in the system and we are waiting for your reply."""
	question = input("If you continue the DamaDamas icon theme board will be deleted and installed on your system.\nWould you like to do it?(Y) or (N)::")
	if question == "Y":
		is_delete =  True
	elif question == "N":
		quit()
	else:
		print("Cant understand Y or N please.\n")
		question_is_delete()

def question_color_change():
	"""Asking the user if he wants to change color"""
	global color_change
	question = input("Damadamas icons are prepared in SVG format.\nThis advantage gives you the possibility to determine the color of the icons.\n Do you want to change colors? (Y) or (N)::")
	if question == "Y":
		color_change = True
	elif question == "N":
		color_change = False
	else:
		question_color_change()


folder_colors = {"default":["faec6d","ffb800"],"black":["383e43","212121"],"blue":["3daed8","2c89a0"],"brown":["c87137","a05a2c"],
				"cyan":["5fd3bc","2ca089"],"green":["99ff55","55d400"],"grey":["9b9b9b","6e6e6e"],"orange":["ff7f2a","d45500"],
				"pink":["ff5599","ff2a7f"],"red":["ff2a2a","d40000"]}

def folder_colors_options():
	"""The user is presented with file color options and expects feedback.
	If the user chooses a color, we return it in a list.
	If we want to enter it manually, we direct it to the corresponding function."""
	global folder_color
	question = input("\nPlease specify a file color. \n Options:\n[ ] default \n[ ] black\n[ ] blue\n[ ] brown\n[ ] cyan\n[ ] green\n[ ] grey\n[ ] orange\n[ ] pink\n[ ] red\n[ ] custom\n::")
	if question == "default":
		folder_color = False
	elif question == "custom":
		folder_color = custom_folder_color()
	else:
		dic_check = folder_colors.get(question, "No")
		if dic_check == "No":
			print("Cant understand\n====================================")
			folder_colors_options()
		else:
			folder_color = dic_check

def color_control(color):
	"""We check to see if it matches the color rules from the user."""
	liste = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	if len(color) != 6:
		return False
	for i in color:
		if i in liste:
			pass
		else:
			return False
	return True

def custom_folder_color():
	"""We get the custom file color from the user."""
	print("Please enter a color in HTML color format.\n(do not put # in rich first) Example: ffffff")
	question_light = input("light color ::")
	question_dark = input("dark color ::")
	if color_control(question_light) and color_control(question_dark):
		return [question_light,question_dark]
	else:
		print("Incorrect color format\n")
		custom_folder_color()

def custom_actions_colors():
	"""We get the custom file actions from the user."""
	print("Please enter a color in HTML color format.\n(do not put # in rich first) Example: ffffff")
	question = input("color ::")
	if color_control(question):
		return question
	else:
		print("Incorrect color format\n")
		custom_actions_colors()

def actions_colors_options():
	global actions_colors
	question = input("\nPlease select colors for actions icons.\n Options:\n[ ] dark\n[ ] light\n[ ] custom\n::")
	if question == "dark":
		actions_colors = False
	elif question == "light":
		actions_colors = "f7f7f7"
	elif question == "custom":
		actions_colors = custom_actions_colors()
	else:
		print("Cant understand\n====================================")
		actions_colors_options()

def panel_colors_options():
	global panel_colors
	question = input("\nPlease select colors for panel icons.\n Options:\n[ ] dark\n[ ] light\n[ ] custom\n::")
	if question == "dark":
		panel_colors = "394050"
	elif question == "light":
		panel_colors = False
	else:
		panel_colors = custom_actions_colors()

def question_h_or_v():
	"""We ask the user to choose between
	vertical icons or horizontal icons."""
	global h_or_v
	question = input("\nThere are two versions of the DamaDamas icon theme, vertical and horizontal. Which one do you want to setup?\nOptions:\n[ ] horizontal\n[ ] vertical\n::")
	if question == "horizontal":
		h_or_v = "horizontal"
	elif question == "vertical":
		h_or_v = "vertical"
	else:
		print("Cant understand\n====================================")
		question_h_or_v()


print("Welcome to the DamaDamas icon theme installer.\n\n")
if os.getuid() != 0:
	print("Damadamas icon theme installer will run as not root.\nThe icon will be installed in {}/.icons file.\n\n".format(os.path.expanduser("~")))
	url = os.path.expanduser("~")+"/.icons"
else:
	print("Damadamas icon theme installer will run as root.\nThe icon will be installed in /usr/share/icons file.\n\n")
	url = "/usr/share/icons"

is_delete = False
if os.path.exists(url+"/DamaDamas-icon-theme"):
	question_is_delete()

question_h_or_v()

question_color_change()

print("Copying files. Please wait...")
if not os.path.exists(url+"/DamaDamas-icon-theme"):
	os.makedirs(url+"/DamaDamas-icon-theme")

"""We set up and copy the directories to be copied according to the user's choice."""

if h_or_v == "horizontal":
    copy_dirs = ['mimetypes', 'categories', 'places', 'emblems', 'apps', 'extras', 'index.theme', 'devices', 'actions', 'status']
else:
    copy_dirs = ['vertical/mimetypes', 'categories', 'vertical/places', 'emblems', 'apps', 'extras', 'index.theme', 'devices', 'actions', 'status']
for dirs in copy_dirs:
	print(os.getcwd()+"/"+dirs)
	os.system("rsync --delete -axHAWX --numeric-ids " + os.getcwd()+"/"+dirs + " " + url + "/DamaDamas-icon-theme" + " --exclude /proc")
print("Complate.\n=====================================")

if color_change:
	"""We learn from the user how to change colors."""
	folder_colors_options()
	actions_colors_options()
	panel_colors_options()
	if folder_color:
		"""Change folder colors"""
		print("Change folder colors...")
		folder_icons_change_color(url + "/DamaDamas-icon-theme/places/user-folders/",folder_colors.get("default")[0],folder_color[0])
		folder_icons_change_color(url + "/DamaDamas-icon-theme/places/user-folders/",folder_colors.get("default")[1],folder_color[1])
		file_icons_change_color(url+"/DamaDamas-icon-theme/mimetypes/file-types/inode-directory.svg",folder_colors.get("default")[0],folder_color[0])
		file_icons_change_color(url+"/DamaDamas-icon-theme/mimetypes/file-types/inode-directory.svg",folder_colors.get("default")[1],folder_color[1])
	if actions_colors:
		"""Change actions colors"""
		print("Change actions colors...")
		folder_icons_change_color(url + "/DamaDamas-icon-theme/actions/","394050",actions_colors)
	if panel_colors:
		"""Change panel colors"""
		print("Change actions colors...")
		folder_icons_change_color(url + "/DamaDamas-icon-theme/status/panel/","f7f7f7",panel_colors)
	print("İnstalled Success..\nYou can use damadamas theme from system settings.")
