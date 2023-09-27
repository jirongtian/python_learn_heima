"""
字符串格式化课后练习题
"""
# 定义需要的变量
name = "智传播客"
stock_price = 19.99
stock_code = "003032"
# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
groth_days = 7

finally_stock_price = stock_price_daily_growth_factor, groth_days, stock_price * stock_price_daily_growth_factor ** groth_days
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到了：%.2f" %(finally_stock_price))