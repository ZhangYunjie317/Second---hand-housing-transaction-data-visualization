import json

from pyecharts import options as opts
from pyecharts.charts import Pie
import pymongo

# 获取结果表
def get_db_df():
    client = pymongo.MongoClient('hdp', 27017)
    db = client['test']
    collection = db['demo02']
    res = collection.find({},{'_id':0})
    return res

# 热门户型
def drawChart():
    data = []
    for item in get_db_df():
        js = json.loads(str(item).replace("\'",'\"'))
        row = (str(js['unit_type']), int(js['cnt']))
        data.append(row)

    c = (
        Pie()
            .add("", data)
            .set_colors(["blcak", "orange", 'green', 'blue', 'grey'])
            .set_global_opts(title_opts=opts.TitleOpts(title="热门户型"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("output_pic/result.html")
    )
#生成柱状图html文件代码
# list1 = []
# list2 = []
# for i in range(5):
#     list1[i] = data[i][0]
#     list2[i] = data[i][1]
#
# b = (
#     Bar()
#         .add_xaxis(list1)
#         .add_yaxis("热门户型",list2)
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="热门户型"),
#         yaxis_opts=opts.AxisOpts(name="数量"),
#         xaxis_opts=opts.AxisOpts(name="户型"),)
# )
if __name__ == '__main__':
    drawChart()