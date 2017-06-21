#!coding=utf8

import json
import xlwt
import zipfile
import operator
from bs4 import BeautifulSoup
from xmlParser import XmlDictConfig
from config import *
import xml.etree.cElementTree as ElementTree


def str_to_lower(k):
    return k.lower().replace('-', '_')


def xml_str_to_dict(xml_str):
    root = ElementTree.XML(xml_str)
    xml_dict = XmlDictConfig(root)
    return xml_dict


def file_parser(file_path, mark=0):
    """
    :param file_path: 路径
    :param mark: 0代表request， 1代表response
    :return:
    """
    result = {}
    with open(file_path) as fd:
        lines = fd.read().split('\n')
        for line_num, line in enumerate(lines):
            if not line:
                pass
            elif line_num == 0:
                if mark == 0:
                    result["method"] = lines[0].split()[0]
                    result["url"] = lines[0].split()[1]
                else:
                    result["status_code"] = lines[0].split()[1]
            elif line_num == len(lines) - 1:
                dict_str = line.strip()
                if "content_type" in result and result["content_type"] == "application/xml":  # xml
                    dict_str = json.dumps(xml_str_to_dict(line.strip()))
                result["data"] = json.loads(dict_str)
            else:
                result[str_to_lower(line.split(":", 1)[0])] = line.split(":", 1)[1].strip()
    return result


class sazParser():
    def __init__(self, html_path):
        self.id2url = {}
        self.html_key_list = []
        self.req_data_list = []
        # 分析html页面
        self.soup = BeautifulSoup(open(html_path), 'html.parser', from_encoding='utf-8')

    def html_parser(self):
        # 解析html里面的key
        thead_res = self.soup.find(name='thead')
        self.html_key_list = [str_to_lower(th_res.text.strip()) for th_res in thead_res.find_all(name="th")]
        # 解析html里的body，以及相关的request，response文件
        tbody_res = self.soup.find(name='tbody')
        for tr_res in tbody_res.find_all(name="tr"):
            one_data = dict(zip(self.html_key_list, [td_res.text.strip() for td_res in tr_res.find_all(name="td")]))
            if one_data.get("host", "") in HOSTS:
                req_file_path = os.path.join(saz_dir_name, tr_res.find(name='a', text="C").attrs["href"]).replace('\\', '/')
                res_file_path = os.path.join(saz_dir_name, tr_res.find(name='a', text="S").attrs["href"]).replace('\\', '/')
                one_data["req_data"] = file_parser(req_file_path, mark=0)
                one_data["res_data"] = file_parser(res_file_path, mark=1)
                self.req_data_list.append(one_data)

    def generate_xls(self):
        def common_data_write(table, id_list, data, filter_list):
            for key, value in data.iteritems():
                if key not in filter_list:
                    table.write(id_list[0], 0, key)
                    table.write(id_list[0], 1, value)
                    id_list[0] += 1
            id_list[0] += 1

        def data_parser(table, id_list, head, data):
            while data and isinstance(data, list):
                head = "%s[0]" % head if head else ""
                data = data[0]
            if data and isinstance(data, dict):
                for key, value in sorted(data.iteritems(), key=operator.itemgetter(0)):
                    new_head = key if not head else "%s[\"%s\"]" % (head, key)
                    table.write(id_list[0], 0, new_head)
                    table.write(id_list[0], 2, str(type(value)).split("'")[1].replace("unicode", "str").replace("NoneType", ""))
                    table.write(id_list[0], 3, key2info.get(key.replace("-", "_"), ""))
                    table.write(id_list[0], 5, value if isinstance(value, (str, unicode)) else json.dumps(value))
                    id_list[0] += 1
                    if isinstance(value, (dict, list)):
                        data_parser(table, id_list, new_head, value)

        def parameter_data_write(table, id_list, data):
            table.write(id_list[0], 0, "DATA:")
            table.write(id_list[0], 1, json.dumps(data))
            id_list[0] += 1
            id_record = id_list[0]
            data_parser(table, id_list, "", data)
            id_record = id_list[0] - id_record
            table.write(id_list[0], 0, "KEY_NUM:")
            table.write(id_list[0], 1, str(id_record))
            id_list[0] += 2

        xls_obj = xlwt.Workbook()
        for one_data in self.req_data_list:
            _id, url = one_data["#"], one_data["url"]
            table = xls_obj.add_sheet(_id + "--")
            self.id2url[_id] = url
            id_list = [1]

            # 基本数据写入
            common_data_write(table, id_list, one_data, html_filter_list)
            common_data_write(table, id_list, one_data.get("req_data", {}), req_filter_list)
            common_data_write(table, id_list, one_data.get("res_data", {}), res_filter_list)

            # 参数写入
            parameter_data_write(table, id_list, one_data.get("req_data", {}).get("data", {}))
            parameter_data_write(table, id_list, one_data.get("res_data", {}).get("data", {}))

        xls_obj.save(execl_dir_name)

    def print_id2url(self):
        print "\n".join("%2s: %s" % (k, v) for k, v in self.id2url.iteritems())


def main():
    # 1.解压缩zip文件
    f = zipfile.ZipFile(zip_file_name, "r")
    for file in f.namelist():
        f.extract(file, saz_dir_name)

    # 2.文件解析
    saz_parser_obj = sazParser(index_html)
    saz_parser_obj.html_parser()
    saz_parser_obj.generate_xls()

    # 3.success
    print "#### URL LIST:"
    saz_parser_obj.print_id2url()


if __name__ == '__main__':
    main()
