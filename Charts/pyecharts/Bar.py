from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from pyecharts import options as opts
from pyecharts.globals import ThemeType

from snapshot_selenium import snapshot

# 在使用 Pandas&Numpy 时，确保将数值类型转换为 python 原生的 int/float。比如整数类型请确保为 int，而不是 numpy.int32

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    #  .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)

#  bar.render('./charts/bar.html')
make_snapshot(snapshot, bar.render(), "./charts/bar.pdf")
