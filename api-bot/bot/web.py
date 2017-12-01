from selenium import webdriver
import json


def gen_driver():
    print("[+] Generating Driver")
    driver = webdriver.PhantomJS()
    driver.set_window_size(1920, 1080)
    print("[+] Success driver generated")
    return driver


def base_req(driver, url, repeats=None):
    if repeats is None:
        repeats = 10

    counter = 0
    while counter < repeats:
        try:
            driver.get(url)
            elem = driver.find_element_by_tag_name("pre")
            raw_data = elem.get_attribute("innerHTML")
            data = json.loads(raw_data)
            if "detial" in data and "throttled" in data["detail"]:
                print("[-] Request was throttled gathering data waiting 5 minutes to retry.")
                sleep(5 * 60)
            else:
                break
        except:
            print("[-] Error gathering data waiting 15 minutes to retry. Repeats: " + counter)
            counter += 1
            sleep(15 * 60)

    return data
