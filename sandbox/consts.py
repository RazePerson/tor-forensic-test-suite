TBB_PATH="/home/ubuntu/tbb/browsed_a_lot/tor-browser_en-US"
GECKODRIVER="/home/ubuntu/geckodriver/geckodriver"
STRACE_FILE_TOR="/home/ubuntu/thesis/strace_output_tor"
STRACE_FILE_FIREFOX_REAL="/home/ubuntu/thesis/strace_output_firefox_real"
SOCKCS_PORT=9150
TEST_SITE="https://check.torproject.org"
TBB_RUNNABLE="start-tor-browser.desktop"
# tor_runnable="/home/ubuntu/tor-browser_en-US/Browser/start-tor-browser"
# current_dir = os.path.dirname(os.path.realpath(__file__))
LOCALHOST="127.0.0.1"
EXCLUDED_URLS=['mozilla.org/xre/app-info;1', 'mozilla.org/timer;1', 'mozilla.org/scripterror;1', 'mozilla.org/content/style-sheet-service;1', 'mozilla.org/addons/content-policy;1', 'http://www.w3.org/1999/xhtml', 'https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands#Key_combinations', 'mozilla.org/network/protocol/about;1?what=', 'mozilla.org/network/serialization-helper;1', 'mozilla.org/uriloader/external-protocol-service;1', 'mozilla.org/chrome/chrome-registry;1', 'mozilla.org/io/string-input-stream;1', 'mozilla.org/network/mime-input-stream;1', 'mozmonkey.com/debuglogger/manager;1', 'torproject.org/torbutton-logger;1', 'mozilla.org/process/environment;1', 'torproject.org/torbutton-logger;1', 'mozilla.org/streamconv;1?from=', 'mozilla.org/devtools/jsonview-sniffer;1', 'mozilla.org/uuid-generator;1', 'mozilla.org/referrer-info;1', 'mozilla.org/docshell/structured-clone-container;1', 'mozilla.org/content/style-sheet-service;1', 'mozilla.org/timer;1', 'http://www.w3.org/1999/xhtml', 'mozilla.org/toolkit/finalizationwitness;1', 'mozilla.org/scripterror;1', 'mozilla.org/satchel/form-fill-controller;1', 'mozilla.org/autocomplete/controller;1']
TOR_ARCHIVE_URLS="https://archive.torproject.org/tor-package-archive/torbrowser/"
TBB_DOWNLOAD_PATH="/home/ubuntu/tor_browser_archive/"
BIN_FILE_URL_PATH="/home/ubuntu/thesis/bin_file_urls/"
URL_REGEX=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

CAPABILITIES={
                "marionette": True,
                "capabilities": {
                    "alwaysMatch": {
                        "moz:firefoxOptions": {
                            "log": {"level": "info"},
                            "args": ["-profile", "/home/ubuntu/tbb/bal_profile"]
                        }
                    }
                }
            }

SQLITE_TABLE_QUERY="SELECT name FROM sqlite_master WHERE type='table';"
SQLITE_SELECT_ALL_QUERY="SELECT * FROM "
TEST_SQLITE_FILE="/home/ubuntu/tbb/browsed_a_lot/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default/storage.sqlite"
CSV_DUMP_DIR="/home/ubuntu/thesis/csv_dumps/"