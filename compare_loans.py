
loan_products = [
    {"company": "신한은행", "product": "신한주택대출(아파트)", "base_rate": 3.42, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "우리은행", "product": "우리 WON 갈아타기 직장인대출", "base_rate": 3.97, "additional_rate": 2.60, "preferred_rate": 1.40},
    {"company": "BNK", "product": "BNK모바일주택담보대출", "base_rate": 3.14, "additional_rate": 3.99, "preferred_rate": 0.60},
    {"company": "신한은행", "product": "신한 MY CAR 신차 대출", "base_rate": 3.41, "additional_rate": 2.60, "preferred_rate": 0.60},
    {"company": "국민은행", "product": "KB 스타 아파트 담보대출 혼합금리(주택자금)", "base_rate": 3.15, "additional_rate": 2.24, "preferred_rate": 1.40},
    {"company": "주식회사 카카오뱅크", "product": "일반신용대출", "base_rate": 3.32, "additional_rate": 1.53, "preferred_rate": 0.60},
    {"company": "신한은행", "product": "신한은행 쏠편한 직장인대출S I", "base_rate": 4.87, "additional_rate": 1.30, "preferred_rate": 1.40}
]


'''
대출액 100만원
1. 매달 상환 원금을 구함 모든 상품 동일 
1. 각 상품별 상환 원금을 24개월 단위로 구함
2. 이자는 상품별 상이 상환 원금 * 이자
3. 
'''

def calculate_equal_principal_payments(principal, month, loan_interest):
    per_product_principal_amount = []
    repayment_month = []
    monthly_principal = principal / month
    for products in loan_interest:
        principal = 1000000
        for num in range(month) :
            repayment_month.append(monthly_principal + (principal * products/1200))
            # print(p + (d * loan_interest[5]/1200))
            # print(d)
            # print((d * loan_interest[5]/12))
            principal-=monthly_principal

        per_product_principal_amount.append(sum(repayment_month))
        #products_repayment.append(repayment_month.copy())
        repayment_month.clear()

    return per_product_principal_amount

def calc_final_interest_rate(loan_products_list) :
    base_interest = [x['base_rate'] for x in loan_products_list]
    preferred_interest = [y['preferred_rate'] for y in loan_products_list]
    additional_interest = [x['additional_rate'] for x in loan_products_list]
    return [x+y-z for x,y,z in zip(base_interest,additional_interest,preferred_interest)]


repayment_period = 24
principal_amount = 1000000

products_names = [x['product'] for x in loan_products]

final_interest_rate = calc_final_interest_rate(loan_products)
# print(final_interest_rate)

result_list = calculate_equal_principal_payments(principal_amount, repayment_period, final_interest_rate)

#product_rank_list = [(x,y,z) for x,y,z in zip(products_repayment,products_names,loan_interest)]
product_rank_list = [(x,y) for x,y in zip(result_list, products_names)]
product_rank_list.sort(key=lambda x: x[0])
# print(product_rank_list)

for amount, product_name in product_rank_list:
    print("{}, {:,.0f}원".format(product_name, amount))

# print('제일유리한 상품 : ', product_rank_list[0])
print("제일유리한 상품 :{}, {:,.0f}원".format(product_rank_list[0][1], product_rank_list[0][0]))