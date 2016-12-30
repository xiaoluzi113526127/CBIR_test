#coding=utf-8
def solr_find(tag):
    import pysolr
    # print type(tag[0]), tag[0]
    #直接链接到固定的solr server及固定的索引
    solr = pysolr.Solr('http://127.0.0.1:8983/solr/'+'ImageNet')
    #直接设置查询参数进行检索
    results = solr.search('tag:\[\'{}\'\]'.format(tag[0]), **{'rows': 5000})    #这里直接设置最大索引的数量为5000
    # #获取检索到的文档数量
    # print results.hits
    #获取检索到的文档
    # print results.docs
    # for data in results.docs:
    #     print data[u'id'], data[u'value'][1]
    # #获取检索到的需要高亮显示的文档
    # print results.highlighting
    return results.docs
# solr_find(['10100'])