from spider.spider import Spider
from xss.xsstrace import XssTrace
from csrf.csrftrace import Csrf
from HTMLtoPDF.html_to_pdf import HTMLtoPDF
from phish.phish import PhishDetector
class interface(object):
    def __init__(self, config_ini):
        super(interface, self).__init__()
        self.config_ini = config_ini

    def spider_interface(self, url):
        spi = Spider(url)
        url_list = spi.start(1)
        return url_list

    def xss_interface(self, url):
        xss = XssTrace(url, self.config_ini)
        xss_log, xss_warning = xss.execute_shell_command()
        return xss_log, xss_warning

    def phish_interface(self, url):
        phish_detector = PhishDetector(self.config_ini)
        phish_log, phish_warning = phish_detector.from_screen_To_ocr_result(url)
        return phish_log, phish_warning

    def csrf_interface(self, url):
        csrf = Csrf(url, self.config_ini)
        csrf_log, csrf_warning = csrf.execute_shell_command()
        return csrf_log, csrf_warning

    def download_interface(self, data):
        downloader = HTMLtoPDF(self.config_ini)
        for item_data in data:
            downloader.start(item_data)


