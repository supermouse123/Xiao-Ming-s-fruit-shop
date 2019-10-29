from django.shortcuts import render, HttpResponse
from home.models import *
# Create your views here.

def index(request, typeid=104749, childid=0, sort_method=0):
    classifylist = ClassifyList.objects.all()
    selectkind = ClassifyList.objects.filter(typeid=typeid)
    kindlist = selectkind[0].childtypenames.split("#")
    if int(childid) == 0:
        selectgoods = AllGoods.objects.filter(categoryid=typeid)
    else:
        selectgoods = AllGoods.objects.filter(categoryid=typeid, childcid=childid)
    if int(sort_method) == 1:
        selectgoods = selectgoods.order_by("productnum")
    if int(sort_method) == 2:
        selectgoods = selectgoods.order_by("-price")
    if int(sort_method) == 3:
        selectgoods = selectgoods.order_by("price")

    print("-----", selectgoods)
    sort_list = [{"sortname": "综合排序", "sortid": 0}, {"sortname": "销量排序", "sortid": 1},
                 {"sortname": "价格最高", "sortid": 2}, {"sortname": "价格最低", "sortid": 3}]
    childlist = []
    curr_select = []
    for kind in kindlist:
        typelist = kind.split(":")
        childlist.append({"childname": typelist[0], "childid":typelist[-1]})
        if typelist[-1] == str(childid):
            for sort in sort_list:
                if int(sort["sortid"]) == int(sort_method):
                    sortname = sort["sortname"]
                    print(sortname)
            curr_select.append({"currname": typelist[0], "typeid": typeid, "childid": childid, "sortname": sortname})
    print(curr_select)
    goods_dict = request.session.get("goods_dict")
    print(goods_dict)
    return render(request, "classify.html", {"classifylist": classifylist, "childlist": childlist,
                                             "curr_select": curr_select, "sort_list": sort_list,
                                             "selectgoods": selectgoods, "goods_dict": goods_dict})