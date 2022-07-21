# 2140666102 李永杰
shop = {'牛奶': 65, '面包': 15, '可乐': 39, '饼干': 45, '糖果': 24, '水果': 35.8}
shop['可乐'] = 60
sum = 0
for i in shop.values():
    sum += i
print("您购买6件物品，共计：%.2f" % sum)
# # 2140666102 李永杰
# seq_cardNo = tuple(["610" + "%03d" % a for a in range(1, 101)])
#
# dict_card = dict.fromkeys(seq_cardNo, "000000")
#
# print("100个银行卡及密码如下所示：", dict_card)
# # 2140666102 李永杰
# dict_pricetable = {"牛奶": 5.5, "方便面": 4, "糖果": 12, "咖啡": 6,
#
#                    "饼干": 6, "火腿肠": 5, "奶茶": 5}
#
# dict_sale1 = {"日期": "11月24日", "牛奶": 15, "方便面": 25, "糖果": 10}
#
# dict_sale2 = {"日期": "11月25日", "牛奶": 25, "咖啡": 5, "饼干": 15, "火腿肠": 10}
#
# dict_sale3 = {"日期": "11月26日", "奶茶": 10, "牛奶": 20, "方便面": 15}
#
# # 因为每日销售数据类似，为了方便处理，将每日销售字典作为元素创建销售列表
#
# list_sale = [dict_sale1, dict_sale2, dict_sale3]
#
# for dict_sale in list_sale:
#     count = 0
#     sum_money = 0
#     for key in dict_sale.keys():
#         if key == "日期":  # 打印商品数量及单价
#             print(dict_sale[key])
#         else:
#             print("\t " + key + ":", end="\t")
#             print("数量:%d" % dict_sale[key], end="\t")
#             print("单价:%.1f" % dict_pricetable[key], end="\t")
#             count += dict_sale[key]
#             sum_money += dict_sale[key] * dict_pricetable[key]
#             print()
#             print("\t%s卖出货物%d件,小计：%.1f元" % (dict_sale["日期"], count, sum_money))















