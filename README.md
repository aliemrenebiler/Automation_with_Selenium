# Get Products with Selenium

This is an excel file generator for bathroom products.

-   It gets the product codes from excel file,
-   finds the product in multiple pages,
-   and puts the product URLs to excel file.

## How To Use?

1. (Optional) Install virtuel environment.
    ```
    pip install venv
    ```
2. (Optional) Create a virtuel environment.
    ```
    python -m venv venv
    ```
3. (Optional) Activate the virtuel environment.
    - For Windows:
        ```
        .venv/bin/Activate.bat
        ```
    - For Linux/MacOS:
        ```
        source .venv/bin/activate
        ```
4. Install required packages from requirements.txt.
    ```
    pip install -r requirements.txt
    ```
5. Edit configurations:

    - EXCEL_FILE_PATH: The path of the excel (.xls or .xlsx) file, which will be edited and saved. The code will override on the existing data.
    - SHEET_NAME: The sheet name that you want to edit.
    - WEBSITES_ROW_NUMBER: The row number which will include websites.
    - WEBSITES_START_COL_NUMBER: The column number which will start to add the websites. (Row A is 1, row B is 2...)
    - PRODUCT_CODES_COL_NUMBER: The column number which includes product codes. (Row A is 1, row B is 2...)
    - PRODUCTS_START_ROW_NUMBER: The row number which the product codes starts.
    - WEBSITES: List of websites and configurations. For a website, it must be dictionary and must include "url", "query" and "product_element" keys. "startup_close_element" key can be used optionally, if there is a pop-up at start. A website looks like this:
        ```
        {
            "url": "https://www.website.com",
            "query": lambda code: f"/search/?query={code}",
            "startup_close_element": (By.ID, "cookie_accept_all_button"),
            "product_element": (By.CLASS_NAME, "a_product_item"),
        }
        ```
    - TIMEOUT: The default timeout for finding a product in a website.

6. Run the Python (.py) file.
    ```
    python get_product_urls.py
    ```
