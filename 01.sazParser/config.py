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

# 一般字段
general_fields = {
    # 一般字段
    "description": u"描述",
    "name": u"名称",
    "id": u"id",
    "user_id": u"用户id",
    "project_id": u"项目id",
    "created_at": u"创建时间",
    "createdAt": u"创建时间",
    "updated_at": u"更新时间",
    "updatedAt": u"更新时间",
    "deletedAt": u"删除时间",
    "imageId": u"镜像id",
    "resource_id": u"资源id",
    "resource_type": u"资源类型",
    "plan_id": u"计划id",
    "device_id": u"设备id",
    "material": u"材料",
    "fingerprint": u"指纹",
    "is_public": u"是否公共",
    "enabled": u"是否可用",
    "type": u"类型",
    "category": u"类别",
    "flavor": u"特点",
    "profile": u"简介",
    # 关于集群
    "cluster_id": u"集群id",
    "cluster_ip": u"集群ip",
    "cluster_global_state": u"集群全局状态",
    "tags": u"标记信息",
    "template_id": u"模板id",
    "vm_ids": u"虚拟机id信息",
    "size": u"大小",
    "storage_pool": u"存储池",
    "source_id": u"资源id",
}
# 网络
network_fields = {
    # 关于网络
    "mtu": u"路径mtu",
    "shared": u"是否共享",
    "cidr": u"无类别域间路由cidr",
    "dns_name": u"DNS名称",
    "mac_address": u"MAC地址",
    "subnet_id": u"子网id",
    "network_id": u"网络id",
    "port": u"端口",
    "host_routes": u"主机路由",
    "ip_version": u"ip版本",
    "ip_address": u"ip地址",
    "enable_snat": u"是否开启snat",
    "enable_dhcp": u"是否开启dhcp",
    "allocation_pools": u"分配池",
    "ha": u"是否高可用",
    "start": u"开始",
    "end": u"结束",
    "routes": u"路由信息",
    "ipv6_address_mode": u"ipv6地址模式",
    "ipv6_ra_mode": u"ipv6的ra模式",
    "subnetpool_id": u"子网池id",
    "gateway_ip": u"网关ip",
    "dns_nameservers": u"dns服务器",
    "router:external": u"路由可扩展",
    "provider:physical_network": u"提供者:物理网络",
    "provider:network_type": u"提供者:网络类型",
    "provider:segmentation_id": u"提供着:段id",
    "port_security_enabled": u"端口安全性是否开启",
    # 关于浮动ip
    "fixed_ips": u"固定ip信息",
    "fixed_ip_address": u"固定的ip地址",
    "floating_ip_address": u"浮动ip的地址",
    "floating_network_id": u"浮动网络id",
    "port_id": u"端口id",
    "route_id": u"路由id",
    "protocol": u"端口",
    "security_group_id": u"安全组id",
    "remote_group_id": u"远程组id",
    "ethertype": u"以太网类型",
    "port_range_min": u"端口最小值",
    "port_range_max": u"端口最大值",
    "hostname": u"主机名",
    "allowed_address_pairs": u"允许的地址对",
    "fqdn": u"全称域名",
    "dns_assignment": u"DNS配置",
    "floating_ip_id": u"浮动ip的id",
    "external_ip": u"外部ip",
    "external_network_id": u"外部网络id",
}
# 存储
storage_fields = {
    "memory_mb": u"内存大小(MB)",
    "disk_gb": u"磁盘大小(GB)",
    "vcpus": u"虚拟cpu数量",
    "ramMB": u"RAM大小",
}
# 计算
calculate_fields = {
    # 关于计算

}
# 用户与权限
user_fields = {
    # 关于租户
    "domain_id": u"租户id",
    "domain_name": u"租户名",
    "default_project": u"默认项目",
    "device_owner": u"设备拥有者",
    "security_groups": u"安全组",
    "tenant_id": u"租户id",
    "status": u"状态",
}

key2info = {}
key2info.update(general_fields)
key2info.update(network_fields)
key2info.update(storage_fields)
key2info.update(calculate_fields)
key2info.update(user_fields)
