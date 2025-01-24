
def cal_interest(deposit, rate, tax, period):
    result = []
    for month in range(1,period+1):
        result.append(deposit * (1+rate*(1-tax)*month))
    return result



def compare_deposits(deposit, rate, tax, period, unit):

    result_list = []

    for dep in deposit:
        for r, t in zip(rate, tax):
            result_list.append(cal_interest(dep,r,t,period))

    return result_list



deposit_my_list = [4500000, 9800000]
bank_rate_year = [0.024, 0.036, 0.042]
bank_tax_interest_rate = [0, 0.154, 0.154]

ret_list = compare_deposits(deposit_my_list,bank_rate_year,bank_tax_interest_rate,32,3)

#print('원금:',str(deposit_my_list[0])+',상품 A 이율:',)
# print("원금 : {0:,} \
#     상품 A 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[0],\
#              bank_rate_year[0] * 100, \
#                 bank_tax_interest_rate[0]* 100))
# print([f"{x:.2f}" for x in ret_list[0][2::3]])
# print("원금 : {0:,} \
#     상품 B 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[0],\
#              bank_rate_year[1]* 100, \
#                 bank_tax_interest_rate[1]* 100))
# print([f"{x:.2f}" for x in ret_list[1][2::3]])
# print("원금 : {0:,} \
#     상품 C 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[0],\
#              bank_rate_year[2]* 100, \
#                 bank_tax_interest_rate[2]* 100))
# print([f"{x:.2f}" for x in ret_list[2][2::3]])
# print("원금 : {0:,} \
#     상품 A 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[1],\
#              bank_rate_year[0]* 100, \
#                 bank_tax_interest_rate[0]* 100))
# print([f"{x:.2f}" for x in ret_list[3][2::3]])
# print("원금 : {0:,} \
#     상품 B 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[1],\
#              bank_rate_year[1]* 100, \
#                 bank_tax_interest_rate[1]* 100))
# print([f"{x:.2f}" for x in ret_list[4][2::3]])
# print("원금 : {0:,} \
#     상품 C 이율 : {1:.2f}%, \
#         세금 : {2:.2f}%".format(deposit_my_list[1],\
#              bank_rate_year[2]* 100, \
#                 bank_tax_interest_rate[2]* 100))
# print([f"{x:.2f}" for x in ret_list[5][2::3]])

'''
원금 : 4,500,000     상품 A 이율 : 2.40%,         세금 : 0.00%
['4824000.00', '5148000.00', '5472000.00', '5796000.00', '6120000.00', '6444000.00', '6768000.00', '7092000.00', '7416000.00', '7740000.00']
원금 : 4,500,000     상품 B 이율 : 3.60%,         세금 : 15.40%     
['4911156.00', '5322312.00', '5733468.00', '6144624.00', '6555780.00', '6966936.00', '7378092.00', '7789248.00', '8200404.00', '8611560.00']
원금 : 4,500,000     상품 C 이율 : 4.20%,         세금 : 15.40%     
['4979682.00', '5459364.00', '5939046.00', '6418728.00', '6898410.00', '7378092.00', '7857774.00', '8337456.00', '8817138.00', '9296820.00']
원금 : 9,800,000     상품 A 이율 : 2.40%,         세금 : 0.00%      
['10505600.00', '11211200.00', '11916800.00', '12622400.00', '13328000.00', '14033600.00', '14739200.00', '15444800.00', '16150400.00', 
'16856000.00']
원금 : 9,800,000     상품 B 이율 : 3.60%,         세금 : 15.40%     
['10695406.40', '11590812.80', '12486219.20', '13381625.60', '14277032.00', '15172438.40', '16067844.80', '16963251.20', '17858657.60', 
'18754064.00']
원금 : 9,800,000     상품 C 이율 : 4.20%,         세금 : 15.40%     
['10844640.80', '11889281.60', '12933922.40', '13978563.20', '15023204.00', '16067844.80', '17112485.60', '18157126.40', '19201767.20', 
'20246408.00']
'''

products = ['A', 'B', 'C']

for i, deposit in enumerate(deposit_my_list):
    for j, (rate, tax) in enumerate(zip(bank_rate_year, bank_tax_interest_rate)):
        print("원금 : {0:,} 상품 {1} 이율 : {2:.2f}%, 세금 : {3:.2f}%".format(deposit, products[j], rate * 100, tax * 100))
        print([f"{x:.2f}" for x in ret_list[i*3 + j][2::3]])