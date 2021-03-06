import os
import glob
import pytest
import unittest
import consts as consts

from utils.utils import Utils
from log.logger import Logging
from flashtext import KeywordProcessor
from utils.system_utils import SystemUtils

log = Logging()
utils = Utils()
sys = SystemUtils()
keyword_processor = KeywordProcessor()

unittest.TestLoader.sortTestMethodsUsing = None


def _keyword_in_file(tbb_path, file_regex, keyword):
    if len(sys.find_files(tbb_path, file_regex)) != 0:
        file = str(sys.find_files(tbb_path, file_regex)[0])
    else:
        return None

    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword(keyword)
    return keyword_processor.extract_keywords(str(sys.strings(file)))


@pytest.mark.skip()
def test_keywords(connected_tbb):
    # strings = ""
    keyword_processor.add_keyword(consts.DUCKDUCKGO_SEARCH_KEYWORD)
    # path = consts.TBB_PATH
    path = connected_tbb.tbb_path
    log.info("Checking path: " + str(path))
    for filename in glob.iglob(path + '**/**', recursive=True):
        if os.path.isfile(filename):
            strings = str(sys.strings(filename))
            keywords_found = keyword_processor.extract_keywords(strings)
            if keywords_found:
                log.info("Keyword: " + str(keywords_found) +
                         " in file: " + str(filename))
        # sys.write_to_file(strings, "/tmp"+filename+"_strings")
    # keywords_found = keyword_processor.extract_keywords(strings)
    # log.info(keywords_found)


def test_site_security_service_state_url_22867(connected_tbb):
    keyword = utils.extract_url_object(consts.URL_ISSUE_22867).fld
    keywords_found = _keyword_in_file(
        connected_tbb.tbb_profile_path, consts.SITE_SECURITY_SERVICE_STATE, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_site_security_service_state_url_24866_1(connected_tbb):
    keyword = utils.extract_url_object(consts.URL_ISSUE_24866_1).parsed_url.netloc
    keywords_found = _keyword_in_file(
        connected_tbb.tbb_profile_path, consts.SITE_SECURITY_SERVICE_STATE, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_site_security_service_state_url_24866_2(connected_tbb):
    keyword = utils.extract_url_object(consts.URL_ISSUE_24866_2).fld
    keywords_found = _keyword_in_file(
        connected_tbb.tbb_profile_path, consts.SITE_SECURITY_SERVICE_STATE, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_site_security_service_state_url_duckduckgo(connected_tbb):
    keyword = utils.extract_url_object(consts.DUCKDUCKGO_URL).fld
    keywords_found = _keyword_in_file(
        connected_tbb.tbb_profile_path, consts.SITE_SECURITY_SERVICE_STATE, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True


def test_site_security_service_state_url_duckduckgo_onion(connected_tbb):
    keyword = utils.extract_url_object(consts.DUCKDUCKGO_ONION).fld
    keywords_found = _keyword_in_file(
        connected_tbb.tbb_profile_path, consts.SITE_SECURITY_SERVICE_STATE, keyword)

    log.info("Keywords: " + str(keywords_found))

    assert (keywords_found is None or len(keywords_found) == 0) is True
