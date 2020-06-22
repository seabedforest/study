"""
主模块入口
"""
from usl01 import CommodityView

if __name__ == '__main__':
    try:
        view = CommodityView()
        view.main()
    except:
        print("出错了")
