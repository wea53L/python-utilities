# with the demise of ftp.mozilla.org, i needed a direct way to download
# specific locales of specific versions of firefox. 
# change local_path before first use.
# 2015 Warren Kopp - if you think you can use this, feel free

import requests
import os

default_url = "https://archive.mozilla.org/pub/firefox/releases/"
platforms = ("mac", "win32") # parenthesis = immutable
requested_version = raw_input("Please enter the version(##.#.#esr):")
#eventually need input validation here.

local_path = "C:/Users/wkopp/Desktop/temp/python/"

def check_path(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for unique in platforms:
    if (unique == "mac"):
        locale = ["en-US", "es-ES", "fr", "ja-JP-mac", "pt-BR"]
        for i in locale:
            # build URI of download file
            specific_version = default_url + requested_version + "/" + unique + "/" + i + "/" "Firefox " + requested_version + ".dmg"
            # check local file location
            specific_path = local_path + requested_version + "/" + unique + "/" + i + "/"
            check_path(specific_path)
            # download specific_version to local location
            specific_path = specific_path + "Firefox " + requested_version + ".dmg"
            print "local_path: " + specific_path
            f = requests.get(specific_version)
            with open(specific_path, 'wb') as code:
                    code.write(f.content)

    elif (unique == "win32"):
        locale = ["en-US", "es-ES", "fr", "ja", "pt-BR"] # single for testing, can add others if/when nesrecessary
        for i in locale:
            specific_version = default_url + unique + "/" + i + "/" "Firefox Setup " + requested_version + ".exe"
            # check local file location
            specific_path = local_path + requested_version + "/" + unique + "/" + i + "/"
            check_path(specific_path)
            # download specific_version to local location
            specific_path = specific_path + "Firefox Setup " + requested_version + ".exe"
            print "local_path: " + specific_path
            f = requests.get(specific_version)
            with open(specific_path, 'wb') as code:
                    code.write(f.content)

    else : continue





