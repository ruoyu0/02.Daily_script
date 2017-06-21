#!coding=utf8

import os
import time

HOST_LIST = ["172.16.221.100", "172.16.221.101", "172.16.221.102", "172.16.221.103"]
saz_dir_name = "data"
zip_file_name = "data.zip"
url_record_name = "parserd_url.txt"
execl_dir_name = "result_%s.xls" % (time.strftime("%Y%m%d_%H%M%S", time.localtime()))
index_html = os.path.join(saz_dir_name, "_index.htm").replace('\\', '/')

html_filter_list = ["", "body", "custom", "comments", "process", "caching", "protocol", "req_data", "res_data"]
req_filter_list = ["data", "host", "accept", "connection", "accept_language", "accept_encoding", "cache_control", "x_auth_token"]
res_filter_list = ["data", "server", "connection", "status_code", "content_type", "content_encoding"]

key2info = {
    "description": u"描述",
    "name": u"名称",
    "id": u"id",
    "user_id": u"用户id",
    "project_id": u"项目id",
    "created_at": u"创建时间",
    "updated_at": u"更新时间",
    "vcpus": u"虚拟cpu数量",
    "ramMB": u"RAM大小",
    "imageId": u"镜像id",
    "resource_id": u"资源id",
    "resource_type": u"资源类型",
    "plan_id": u"计划id",
    "device_id": u"设备id",
    "device_owner": u"设备拥有者",
    "dns_name": u"DNS名称",
    "mac_adress": u"MAC地址",
    "security_groups": u"安全组",
    "tenant_id": u"租户id",
    "status": u"状态",
    "subnet_id": u"子网id",
    "network_id": u"网络id",
    "port": u"端口",
    "material": u"材料",
    "fingerprint": u"指纹",
    "is_public": u"是否公共",
    "memory_mb": u"内存大小(MB)",
    "disk_gb": u"磁盘大小(GB)",
    "": u"",
}
