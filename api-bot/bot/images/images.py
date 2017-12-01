import pyimgur
import urllib
import urllib3
import os
from time import sleep

urllib3.disable_warnings()


def save_image(url, name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/queue"
    did_download = False
    while not did_download:
        try:
            urllib.urlretrieve(url, file_path + "/" + name + ".png")
            did_download = True
        except:
            print("[-] Error downloading file. Waiting 5 minutes before retry")
            sleep(5 * 60)

    return file_path + "/" + name + ".png"


def remove_file(name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/queue"
    os.remove(file_path + "/" + name + ".png")


def upload_image(client_id, path, name):
    im = pyimgur.Imgur(client_id)

    did_upload = False
    while not did_upload:
        try:
            uploaded_image = im.upload_image(path, title=name)
            did_upload = True
        except:
            print("[-] Error uploading file. Waiting 1 hour before retry")
            sleep(60 * 60)
    return uploaded_image.link


def handle_file(client_id, url, name):
    path = save_image(url, name)
    url = upload_image(client_id, path, name)
    remove_file(name)
    return url
