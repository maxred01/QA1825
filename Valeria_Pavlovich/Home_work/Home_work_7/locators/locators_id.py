class LocatorsWebTables:
    add_button = '//*[@id="addNewRecordButton"]'
    registration_form = '//form[@id="userForm"]'
    close_button = '//*[@aria-modal="true"]//*[@aria-hidden="true"]'
    first_name = '//*[@id="firstName"]'
    last_name = '//*[@id="lastName"]'
    email = '//*[@id="userEmail"]'
    age = '//*[@id="age"]'
    salary = '//*[@id="salary"]'
    dept = '//*[@id="department"]'
    submit_button = '//*[@id="submit"]'
    table_rows = "//div[@class='rt-tbody']//div[contains(text(), '{}')]"
    table_rows_all = "//div[@class='rt-tr-group']"
