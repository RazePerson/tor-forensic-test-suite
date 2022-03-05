TBB_PATH = "/home/ubuntu/tbb/browsed_a_lot/tor-browser_en-US"
FIREFOX_PATH = "/home/ubuntu/.mozilla/firefox"

DEFAULT_GECKODRIVER_EXECUTABLE = "/home/ubuntu/geckodriver/geckodriver"
STRACE_FILE_TOR = "/home/ubuntu/thesis/strace_output_tor"
STRACE_FILE_FIREFOX_REAL = "/home/ubuntu/thesis/strace_output_firefox_real"
SOCKCS_PORT = 9250

TEST_SITE = "https://check.torproject.org"
JETSTREAM = "https://browserbench.org/JetStream/"
GOOGLE = "https://google.com"
DUCKDUCKGO_ONION = "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"

URL_ISSUE_22867 = "https://us-u.openx.net/w/1.0/pd?plm=10&ph=e26121be-304d-460c-92c5-0b3d1d4c9b7a"
URL_ISSUE_24866_1 = "https://accounts.google.com/ServiceLogin?continue=https://www.blogger.com/comment-iframe.g?blogID%3D2266550428847361277%26postID%3D6186454555221678264%26blogspotRpcToken%3D3273703%26bpli%3D1&followup=https://www.blogger.com/comment-iframe.g?blogID%3D2266550428847361277%26postID%3D6186454555221678264%26blogspotRpcToken%3D3273703%26bpli%3D1&passive=true&go=true#%7B%22color%22%3A%22rgb(110%2C%20110%2C%20110)%22%2C%22backgroundColor%22%3A%22rgb(204%2C%20204%2C%20204)%22%2C%22unvisitedLinkColor%22%3A%22rgb(0%2C%200%2C%200)%22%2C%22fontFamily%22%3A%22Verdana%2CGeneva%2Csans-serif%22%7D"
URL_ISSUE_24866_2 = "https://id.rlcdn.com/463496.gif?credir=https%3A%2F%2Fsimage4.pubmatic.com%2FAdServer%2FSPug%3Fo%3D3%26u%3D1292AC75-4860-4D0E-8AC2-F720B90009E0%26vcode%3Dbz0yJnR5cGU9MSZjb2RlPTMzMzkmdGw9MTI5NjAw%26piggybackCookie%3D&redirect=1"

TBB_RUNNABLE = "start-tor-browser.desktop"
# tor_runnable="/home/ubuntu/tor-browser_en-US/Browser/start-tor-browser"
# current_dir = os.path.dirname(os.path.realpath(__file__))
LOCALHOST = "127.0.0.1"
EXCLUDED_URLS = ['mozilla.org/xre/app-info;1', 'mozilla.org/timer;1', 'mozilla.org/scripterror;1', 'mozilla.org/content/style-sheet-service;1', 'mozilla.org/addons/content-policy;1', 'http://www.w3.org/1999/xhtml', 'https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands#Key_combinations', 'mozilla.org/network/protocol/about;1?what=', 'mozilla.org/network/serialization-helper;1', 'mozilla.org/uriloader/external-protocol-service;1', 'mozilla.org/chrome/chrome-registry;1', 'mozilla.org/io/string-input-stream;1', 'mozilla.org/network/mime-input-stream;1',
                 'mozmonkey.com/debuglogger/manager;1', 'torproject.org/torbutton-logger;1', 'mozilla.org/process/environment;1', 'torproject.org/torbutton-logger;1', 'mozilla.org/streamconv;1?from=', 'mozilla.org/devtools/jsonview-sniffer;1', 'mozilla.org/uuid-generator;1', 'mozilla.org/referrer-info;1', 'mozilla.org/docshell/structured-clone-container;1', 'mozilla.org/content/style-sheet-service;1', 'mozilla.org/timer;1', 'http://www.w3.org/1999/xhtml', 'mozilla.org/toolkit/finalizationwitness;1', 'mozilla.org/scripterror;1', 'mozilla.org/satchel/form-fill-controller;1', 'mozilla.org/autocomplete/controller;1']
TOR_ARCHIVE_URLS = "https://archive.torproject.org/tor-package-archive/torbrowser/"
TBB_DOWNLOAD_PATH = "/tmp/tor_browser_archive/"
BIN_FILE_URL_PATH = "/home/ubuntu/thesis/bin_file_urls/"
URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

SQLITE_TABLE_QUERY = "SELECT name FROM sqlite_master WHERE type='table';"
SQLITE_SELECT_ALL_QUERY = "SELECT * FROM "
TEST_SQLITE_FILE = "/home/ubuntu/tbb/browsed_a_lot/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default/storage.sqlite"
CSV_DUMP_DIR = "/home/ubuntu/thesis/csv_dumps/"

DEFAULT_TBB_PROFILE_PATH = "/home/ubuntu/default_tbb_profile_path/"
PLACEHOLDER_PROFILE_PATH_SUFFIX = "Browser/TorBrowser/Data/Browser/profile.default"
DEV_NULL = "/dev/null"
TEMP_TEST_DIR = "/tmp/testing_tbb"

JETSTREAM_START_TEST_XPATH = "/html/body/main/div[2]/a"
GOOGLE_SEARCH_BOX_XPATH = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
COOKIE_AGREE_XPATH = "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]/div"
DUCKDUCKGO_SEARCH_BOX_XPATH = "//*[@id=\"search_form_input_homepage\"]"

GC_GECKO = "gecko"
GC_FIREFOX = "firefox"
GECKO_COMPATIBILITY = {"gecko": ["0.30.0", "0.29.1", "0.29.0", "0.28.0", "0.27.0", "0.26.0", "0.25.0", "0.24.0", "0.23.0", "0.22.0", "0.21.0", "0.20.1", "0.20.0",
                                 "0.19.1", "0.19.0", "0.18.0", "0.17.0"], "firefox": [78, 60, 60, 60, 60, 60, 57, 57, 57, 57, 57, 55, 55, 55, 55, 53, 52]}

GECKODRIVER_RELEASE_PAGE = "https://github.com/mozilla/geckodriver/releases/download/v{version}/geckodriver-v{version}-linux64.tar.gz"
GECKODRIVER_DOWNLOAD_PATH = "/tmp/geckodriver_archive/"
GECKODRIVER_TAR_FILE = "geckodriver-v{version}-linux64.tar.gz"

FIREFOX_VERSION="Milestone="
FIREFOX_VERSION_FILE_REGEX="^platform.ini$"