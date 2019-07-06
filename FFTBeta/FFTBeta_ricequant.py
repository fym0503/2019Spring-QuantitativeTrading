#这段代码可以在ricequant回测平台上运行
# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。
import numpy as np
import talib as ta
# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # 在context中保存全局变量
    context.s1 = "000002.XSHE"
    # 实时打印日志
    context.alpha=0.0
    context.beta=0.8
    context.OBSERVATION=100
    logger.info("RunInfo: {}".format(context.run_info))

# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    pass


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    # TODO: 开始编写你的算法吧！
    prices = history_bars(context.s1, context.OBSERVATION, '1d', 'close')
    transform_fft=np.fft.fft(prices)
    recover=np.fft.ifft(transform_fft)
    truncate=[]
    min_freq=len(transform_fft)*context.alpha
    max_freq=len(transform_fft)*context.beta
    for i in range(len(transform_fft)):
        if i<=max_freq and i>=min_freq:
            truncate.append(transform_fft[i])
        else:
            truncate.append(0)
    recover_truncate=np.fft.ifft(np.array(truncate))
    if prices[-1]<1*np.abs(recover_truncate[-1]):
        order_target_percent(context.s1, 0.8)
    elif prices[-1]>1.2*np.abs(recover_truncate[-1]):
        order_target_pe(context.s1, 0)

# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass