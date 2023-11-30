# 定义变量
name = "传播知客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
now_stock_price = stock_price * stock_price_daily_growth_factor**growth_days

# 打印出结果
print(f"公司:{name} 股票代码:{stock_code} 当前股价:{stock_price}")
print(
    "每日增长系数:%.1f,经过%d天的增长后,股票达到了%.2f"
    % (
        stock_price_daily_growth_factor,
        growth_days,
        now_stock_price,
    )
)
