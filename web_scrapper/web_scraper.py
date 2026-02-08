from .core.driver import create_driver
from .workflows import search_and_get_result
from config import BASE_URL

def scraper(vat_id, country):
    driver = create_driver()
    driver.get(BASE_URL)
    
    try:
        output = search_and_get_result(
                driver,
                vat_id=vat_id,
                country=country
            )
        return output
    except Exception as e:
        output = {"name":"scrapping error","address":"scrapping error","result":"scrapping error" + str(e)}
        return output
    finally:
        driver.quit()

if __name__ == "__scraper__":
    scraper()
