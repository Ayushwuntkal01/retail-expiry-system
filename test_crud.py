from crud import add_product, get_product, update_product

print("\n=== TEST 1: ADD PRODUCT (101) ===")
res1 = add_product(
    product_id=101,
    name="Shampoo",
    category_id=1,
    supplier_id=1,
    cost_price=60,
    selling_price=80,
    stock_qty=50,
    expiry_date="2025-12-31"
)
print("Result of add_product:", res1)

print("\n=== TEST 2: GET PRODUCT (101) BEFORE UPDATE ===")
prod_before = get_product(101)
print("Before update:", prod_before)

print("\n=== TEST 3: UPDATE PRODUCT (101) ===")
res_update = update_product(
    product_id=101,
    new_stock=40,
    new_price=85
)
print("Result of update_product:", res_update)

print("\n=== TEST 4: GET PRODUCT (101) AFTER UPDATE ===")
prod_after = get_product(101)
print("After update:", prod_after)

from crud import record_sale

print("\n=== TEST 5: RECORD SALE ===")
sale_result = record_sale(101, 5, 85)
print("Sale result:", sale_result)

print("\n=== TEST 6: GET PRODUCT AFTER SALE ===")
prod_after_sale = get_product(101)
print("Product after sale:", prod_after_sale)

from crud import get_near_expiry

print("\n=== TEST 7: GET NEAR EXPIRY (next 60 days) ===")
near_expiry = get_near_expiry(60)
print("Near expiry products:", near_expiry)

from crud import get_waste_summary

print("\n=== TEST 8: WASTE SUMMARY ===")
waste = get_waste_summary()
print("Waste summary:", waste)