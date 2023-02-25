from time import sleep
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd


# init drive
driver = webdriver.Chrome(executable_path='C:/Users/***PATH***/chromedriver.exe')
driver.maximize_window()

df=pd.read_excel('C:/Users/chris/Desktop/***LIST OF PART NAMES TO FIX***.xlsx')
skulist= df.values.tolist()

def signin():
    
    url= "https://***URL***.sera.tech/departments/337/pricebook?tab=pb_tasks"
    # open the url
    driver.get(url)
    timeout= 10
    try:
        element_present = EC.presence_of_element_located((By.ID, 'admin_email'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    username= driver.find_element(By.ID,'admin_email')
    username.send_keys('***USER***')

    try:
        element_present = EC.presence_of_element_located((By.ID, 'admin_password'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    password= driver.find_element(By.ID, 'admin_password')
    password.send_keys('***PASSWORD***')
    submit= driver.find_element(By.NAME, 'commit')
    submit.click()
    sleep(1)
    
    return driver

# def partspagesetup():

#     //*[@id="vendor_id"]
#     try:
#         element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="products-table_filter"]/label/input'))
#         WebDriverWait(driver, 10).until(element_present)
#     except TimeoutException:
#         print("Timed out waiting for page to load")
#     //*[@id="products-table_length"]/label/select




def partssearch(SKU):
    url2='https://***URL***.sera.tech/departments/337/pricebook?tab=pb_parts'
    driver.get(url2)

    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="products-table_filter"]/label/input'))
    #     WebDriverWait(driver, 10).until(element_present)
    # except TimeoutException:
    #     print("Timed out waiting for page to load")
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="products-table_filter"]/label/input'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    search = driver.find_element(By.XPATH, '//*[@id="products-table_filter"]/label/input')
    search.click()
    search.clear()
    
    search.send_keys(str(SKU))
    sleep (1)
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="products-table"]/tbody/tr[2]/td[1]/div/span'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    sleep(2)
    linkele= driver.find_elements(By.XPATH, '//span[@class="link"]')
    for i in linkele:
        index2= str(i.get_attribute('innerText'))
        if index2.find(str(SKU))!= -1:
            i.click()
            return
    linkele[0].click()
    
    # for i in range(len(links)):
    #     print(links[i].get_attribute('name'))

    # parts=links
    # print(parts)
    # for i in parts:
    #     if parts[i] == SKU:
    #         parts[i].click()
    #         return
    #     else:
    #         parts[0].click()
    
    return


def copypastesku():
    sleep(2)
    #grab sku and then paste/append it to name and vendor name
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Part SKU"]'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    grabsku= driver.find_element(By.XPATH, '//input[@placeholder="Part SKU"][@class="form-control"]')
    skutext=grabsku.get_attribute('_value')
    ##
    ##
    partnameskuadd=driver.find_element(By.XPATH,'//input[@placeholder="Part Name"]')
    partnamecheck= partnameskuadd.get_attribute('_value')
    index = partnamecheck.find(skutext)
    if index == -1:
        partnameskuadd.click()
        partnameskuadd.send_keys(Keys.END)
        partnameskuadd.send_keys(Keys.SPACE, str(skutext))
    else:
        print(f'"{skutext}" not in "{partnamecheck}" part')

    partnamewithsku= partnameskuadd.get_attribute('_value')
    print(partnamewithsku)

    vendnameskuadd=driver.find_element(By.XPATH,'//input[@placeholder="Vendor Name"]')

    vendnameskuadd.click()
    vendnameskuadd.clear()
    vendnameskuadd.send_keys(str(partnamewithsku))
    
    savebutton= driver.find_element(By.XPATH,'//button[@class="btn btn-sm btn-primary btn-ml"]')
    savebutton.click()
   
    return

def skulistloop():
    for i in skulist:
        partssearch(i[0])
        copypastesku()
    return

def main():
    signin()
    skulistloop()
    driver.quit()

if __name__ == '__main__':
    main()





##parts search bar
#<input type="search" class="form-control form-control-sm" placeholder="" aria-controls="products-table">

###TASKS
#class=" dt-body-right task-link text-center"
#<td class=" dt-body-right task-link text-center"><a href="/departments/337/pricebook?part_id=470429">1</a></td>
##products-table > tbody > tr.odd > td.dt-body-right.task-link.text-center
#/html/body/div[1]/div[2]/div[2]/main/div[2]/div/div[2]/div/div/div/main[1]/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]

##number of matches
#<div class="dataTables_info" id="products-table_info" role="status" aria-live="polite">Showing 1 to 1 of 1 entries (filtered from 875 total entries)</div>



###parts page link
#//*[@id="products-table"]/tbody/tr[2]/td[1]/div/span ###class="link"
###parts name
#//*[@id="products-table"]/tbody/tr[2]/td[2]

##SKU ERROR
#/html/body/div[1]
#<div class="toastify on mt-5 alert toastify-right toastify-top" aria-live="polite" style="background: rgb(220, 53, 69); transform: translate(0px, 0px); top: 15px;">Vendor sku SKU must be unique per vendor<button type="button" aria-label="Close" class="toast-close">✖</button></div>

##Part Name Box
#<input data-v-45d49f92="" placeholder="Part Name" data-cy="name" type="" class="form-control">

#Vend Name
#<input data-v-45d49f92="" placeholder="Vendor Name" data-cy="vendor-name" type="" class="form-control">

#4 boxes by class, then name
#<div data-v-45d49f92="" class="d-flex flex-column full-width"><input data-v-45d49f92="" placeholder="Part SKU" data-cy="sku" type="" class="form-control"> <!----></div>

##TASK NUMs
#/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/span




