
def test_sauce6():
    NAME = driver.find_element(By.ID, "item_2_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
    driver.back()
def test_sauce7():
    NAME = driver.find_element(By.ID, "item_3_title_link").text
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
    driver.back()
def test_sauce8():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(NAME2)
    driver.find_element(By.ID, "password").send_keys(PSWD)
    driver.find_element(By.ID, "login-button").click()
    URL = "https://www.saucedemo.com/inventory.html"
    assert URL == driver.current_url
    if URL != driver.current_url:
        return pytest.fail("There is problem with login on" + " " + NAME2)
def test_sauce9():
    driver.get("https://www.saucedemo.com/inventory.html")
    NAME = driver.find_element(By.ID, "item_4_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.back()
def test_sauce10():
    NAME = driver.find_element(By.ID, "item_0_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    driver.back()
def test_sauce11():
    NAME = driver.find_element(By.ID, "item_1_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    driver.back()
def test_sauce12():
    NAME = driver.find_element(By.ID, "item_5_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
    driver.back()
def test_sauce13():
    NAME = driver.find_element(By.ID, "item_2_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
    driver.back()
def test_sauce14():
    NAME = driver.find_element(By.ID, "item_3_title_link").text
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
    driver.back()
def test_sauce15():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(NAME3)
    driver.find_element(By.ID, "password").send_keys(PSWD)
    driver.find_element(By.ID, "login-button").click()
    URL = "https://www.saucedemo.com/inventory.html"
    assert URL == driver.current_url
    if URL != driver.current_url:
        return pytest.fail("There is problem with login on" + " " + NAME3)
def test_sauce16():
    driver.get("https://www.saucedemo.com/inventory.html")
    NAME = driver.find_element(By.ID, "item_4_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.back()
def test_sauce17():
    NAME = driver.find_element(By.ID, "item_0_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    driver.back()
def test_sauce18():
    NAME = driver.find_element(By.ID, "item_1_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    driver.back()
def test_sauce19():
    NAME = driver.find_element(By.ID, "item_5_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
    driver.back()
def test_sauce20():
    NAME = driver.find_element(By.ID, "item_2_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
    driver.back()
def test_sauce21():
    NAME = driver.find_element(By.ID, "item_3_title_link").text
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
    driver.back()
def test_sauce22():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(NAME4)
    driver.find_element(By.ID, "password").send_keys(PSWD)
    driver.find_element(By.ID, "login-button").click()
    URL = "https://www.saucedemo.com/inventory.html"
    assert URL == driver.current_url
    if URL != driver.current_url:
        return pytest.fail("There is problem with login on" + " " + NAME4)
def test_sauce23():
    driver.get("https://www.saucedemo.com/inventory.html")
    NAME = driver.find_element(By.ID, "item_4_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.back()
def test_sauce24():
    NAME = driver.find_element(By.ID, "item_0_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    driver.back()
def test_sauce25():
    NAME = driver.find_element(By.ID, "item_1_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    driver.back()
def test_sauce26():
    NAME = driver.find_element(By.ID, "item_5_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
    driver.back()
def test_sauce27():
    NAME = driver.find_element(By.ID, "item_2_title_link").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
    driver.back()
def test_sauce28():
    NAME = driver.find_element(By.ID, "item_3_title_link").text
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    CART = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    if NAME != CART:
        pytest.fail("There is problem with:" + " " + NAME)
    driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
    driver.back()


