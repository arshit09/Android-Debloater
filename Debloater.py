import os
import sys
import easygui

msg = "Debloat your phone with just a few clicks.\n\nPlease visit my Github repo(https://github.com/arshit09/Android-Debloater) for the instructions.\n\nDISCLAIMER:\nUSE AT YOUR OWN RISK, PLEASE.\n\nAnything that happens to your phone is not my responsibility.\nBy pressing 'Continue', you are agreeing that anything that happens with your phone is ONLY AND ONLY RESULT OF YOUR ACTION."
title = "Debloater by Arshit Vaghasiya"
if easygui.ccbox(msg, title):
    pass
else:
    sys.exit(0)

text = "Select package name to uninstall:"
choices = ["Geek", "Super Geeek", "Super Geek 2", "Super Geek God"]
package_list = os.popen('adb shell cmd package list packages').read()

new_list = [s.replace("package:", "") for s in package_list.split('\n')]
new_list.sort()
new_list.pop(0)
for i in range (0, len(new_list)):
    new_list[i] = str(i+1) + ". " + new_list[i]

output = easygui.multchoicebox(text, title, choices=new_list)
confirm_list = output

for i in range (0, len(output)):
    output[i] = output[i][int(output[i].find(' '))+1:]
msg = "Do you want to really uninstall following packages?\n"
msg = msg + "\nTotal number of apps to be uninstalled:\n" + str(len(confirm_list)) + "\n\nPackage name(s):\n"
for i in  range (0, len(confirm_list)):
    msg = msg + confirm_list[i] + "\n"

title = "! CAUTION ! - Debloater by Arshit Vaghasiya"
msg = msg + "\n--------------------------\n\n--------------------------\n| I KNOW WHAT I AM DOING | \n--------------------------\n\n--------------------------"

if easygui.ccbox(msg, title):
    pass
else:
    sys.exit(0)

for i in range (0, len(output)):
    package = "adb shell pm uninstall -k --user 0 " + output[i]
    os.system(package)

msg = "Following package(s) uninstalled sucessfully!\n\n"
for i in  range (0, len(confirm_list)):
    msg = msg + confirm_list[i] + "\n"
button = "Exit and Thank you :)"
easygui.msgbox(msg, title, button )