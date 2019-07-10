from selenium.common.exceptions import *
import xlrd

class Locatorgeneric:

    def __init__(self,driver):
        self.driver=driver

    def locator(self,loc_type,loc_val):

        try:

            if loc_type == 'id':
                ele = self.driver.find_element_by_id(loc_val)

            elif loc_type == 'xpath':
                ele = self.driver.find_element_by_xpath(loc_val)

            return ele

        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)
        except ElementClickInterceptedException as e:
            print(e)
        except UnexpectedTagNameException as e:
            print(e)
        except SessionNotCreatedException as e:
            print(e)
        except StaleElementReferenceException as e:
            print(e)
        except WebDriverException as e:
            print(e)
        except NoSuchWindowException as e:
            print(e)
        except Exception as e:
            print(e)

    def get_val(self, Sheet_Name, Input_val):

        wb = xlrd.open_workbook("C:/Users/Guest User/PycharmProjects/POM_Practice1/data/data.xlsx")
        ws = wb.sheet_by_name(Sheet_Name)
        row_count = ws.nrows
        col_count = ws.ncols
        for i in range(row_count):
            for j in range(col_count):
                if (ws.cell_value(i, j) == Input_val):
                    val = ws.cell_value(i + 1, j)
            break
        return val

    def delete_cookies(self):
        self.driver.delete_all_cookies()



