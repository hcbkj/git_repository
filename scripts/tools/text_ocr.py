# -*- coding: utf-8 -*-
# @Time    : 2022/8/18 14:28

import re
"""
[['晋商银行'], ['Jinshang Bank'], ['汇款日期'], ['2020-11-2517:46'], ['汇款编号'], ['2020112500638025'], ['收款户名'], ['白学彦'], ['收款'], ['收款卡号'], ['6228480150107593215'], ['大'], ['收款银行'], ['中国农业银行股份有限公司'], ['付款户名'], ['晋商消费金融股份有限公司'], ['付款人'], ['付款卡号'], ['35110180500000019'], ['付款银行'], ['晋商银行股份有限公司'], ['汇款金额'], ['付款金额'], ['38200元（人民币）'], ['手续费金额'], ['0元（人民币）'], ['附言'], ['放款'], ['手机'], ['温馨提示'], ['商銀'], ['1、转账交易以资金实际到账为准'], ['2、本回单不作为收款方发货依据，请勿']]
"""

lst = [['晋商银行'], ['Jinshang Bank'], ['汇款日期'], ['2020-11-2517:46'], ['汇款编号'], ['2020112500638025'], ['收款户名'], ['白学彦'], ['收款'], ['收款卡号'], ['6228480150107593215'], ['大'], ['收款银行'], ['中国农业银行股份有限公司'], ['付款户名'], ['晋商消费金融股份有限公司'], ['付款人'], ['付款卡号'], ['35110180500000019'], ['付款银行'], ['晋商银行股份有限公司'], ['汇款金额'], ['付款金额'], ['38200元（人民币）'], ['手续费金额'], ['0元（人民币）'], ['附言'], ['放款'], ['手机'], ['温馨提示'], ['商銀'], ['1、转账交易以资金实际到账为准'], ['2、本回单不作为收款方发货依据，请勿']]

text = str(lst)

text = text.replace("[", '')
text = text.replace("]", '')
print(text)

# ht_name = re.search('收款户名(.*?)收款', text, re.S).group(1).replace("'", '').replace(',', '').strip()
ht_num = re.search('付款金额(.*?)元', text, re.S).group(1).replace("'", '').replace(',', '').strip()
print(type(ht_num))
print(ht_num)
