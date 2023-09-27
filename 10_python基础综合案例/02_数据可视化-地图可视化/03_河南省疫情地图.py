"""
演示河南省疫情地图开发
"""

# 导包
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 数据读取
f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 数据处理
data_dict = json.loads(data)
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
city_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市" #城市名称
    city_confirm = city_data["total"]["confirm"]  # 确诊人数
    city_list.append((city_name, city_confirm))
city_list.append(("济源市", 5))
# 制图
map = Map()
map.add("河南省疫情分布", city_list, "河南")
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"}
        ]
    )
)
map.render("河南疫情地图.html")