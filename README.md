# Android App Debloater

Deboat your phone with just a few clicks.

**DISCLAIMER: Use at your own risk.**

## Getting Started

1. Enable `Developer options` on your phone.
2. Turn on `USB debugging` from the Developer options.
3. Make sure you have ADB installed on your PC. If not, [visit this link](https://www.xda-developers.com/install-adb-windows-macos-linux/ "visit this link").
3. Connect your phone to your PC using a data cable.
   > If asked for "Allow USB debugging?", tap on "Allow."
4. Run `pip install easygui` to install EasyGUI module for python.
5. Double click on Debloater.py to run it.

## How to Use
1. Double click on `Debloater.py`.
2. Read the disclaimer.
3. Select any package you want to uninstall.
4. Select `Continue` to uninstall.

## Get the package name of an app
####Method 1
1. Download any package name viewer app on the phone and look for the package name of the app you want to uninstall. Recommended app: [Package Name Viewer 2.0](https://play.google.com/store/apps/details?id=com.csdroid.pkg "Package Name Viewer 2.0")

####Method 2
1. Open [Play Store](https://play.google.com/store "Play Store") in the browser and search for your app.
2. For example, [URL of WhatsApp](https://play.google.com/store/apps/details?id=com.whatsapp "URL of WhatsApp") will look like this: `https://play.google.com/store/apps/details?id=com.whatsapp`
3. The app's package name will be the part after `?id=`. For this case, it will be `com.whatsapp`.

