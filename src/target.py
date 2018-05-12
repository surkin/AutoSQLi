# From AutoSQLi

import uuid

class Target:
    url = ""
    waf_detection_done = False
    is_protected_by_waf = False
    waf_name = ""
    working_tampers = []
    sqlmap_exploitation_done = False
    is_vulnerable = False
    sqlmap_logs = []

    def __init__(self, url):
        """ create a new Target from a url"""
        self.url = url
        self.uuid = uuid.uuid4()  # random UUID ( used to update in a list )


def urls_to_targets(urls):
    """ convert an url array to a Target array """
    target_list = []
    for url in urls:
        target_list.append(Target(url))

    return target_list
