from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.chrome.options import Options;
#from selenium.webdriver.common.keys import Keys;

DEFAULT_DIR = "C:/Users/allan/AppData/Local/Google/Chrome/User Data"
PROFILE = ["Profile 1", "Profile 2", "Profile 3", "Profile 4"];           #PROFILES
PROFILE_ENTITY = ["ENTITYZA5DLHLE8215", "ENTITY1CYX8CNAV1RAA", "ENTITY2X8CIDJBWBZDA", "ENTITY178U66HOFEQW5"]

SELECTORS = ["span.sc-storm-ui-30041982__sc-may1nv-1:nth-child(4) > button:nth-child(1)",           #BOTAO PERFIL
                   ".sc-storm-ui-30041982__sc-amnlzo-2",                                            #BOTAO SELECIONAR LINGUA
                   "button.sc-storm-ui-30041982__sc-1a042f9-1:nth-child(1)",                        #ESCOLHER LINGUA
                   ".sc-pcLhl",                                                                     #BOTAO APLICAR MODIFICAÇÃO
                   "#includeZeroImpressionEntities",                                                #CHECK BOX
                   "#includeSponsoredBrandsData",                                                   #CHECK BOX 
                   "#includeSponsoredBrandsV4Data",                                                 #CHECK BOX        
                   "#includeSponsoredDisplayData",                                                  #CHECK BOX
                   "#includeSbSearchTermReportData",                                                #CHECK BOX
                   "button.sc-storm-ui-20042007__sc-d3w8xm-0:nth-child(2)",                         #BOTAO PARA ESCOLHER A DATA
                   "button.sc-storm-ui-20042007__sc-1rm1drt-0:nth-child(5)",                        #BOTAO PARA SALVARA DATA SEELCIONADA
                   "button.dQwwDk:nth-child(2)",                                                    #BOTAO SOLICITAR SPREADSHEET
                   ".dQwwDk"]

def main():
    #execRequest()
    options = Options()
    options.add_argument('--user-data-dir=C:/Users/allan/AppData/Local/Google/Chrome/User Data')
    options.add_argument('--profile-directory=Profile 3')
    browser = webdriver.Chrome(options=options)
    ##options.add_argument("--headless")
    browser.get("https://www.google.com") 
    #pathAuto(SELECTORS)
    browser.quit()



# def execRequest():
#     for i in len(SELECTORS):
#         runAuto(PROFILE[i], PROFILE_ENTITY[i])
    


# def runAuto(profile, profile_entity):
#     options = Options()
#     options.add_argument("")

#     browser = webdriver.Chrome(chrome_options=options)

#     browser.get("https://www.google.com") 
#     #pathAuto(SELECTORS)
#     #browser.quit()

#     def pathAuto(selectors):
#         for i in len(SELECTORS):
#             clickComponent(selectors[i])

#     def clickComponent(selectorCSS):
#         #browser.findElement(By.css(selectorCSS)).then(el => el.click());
#         return
    


main()
