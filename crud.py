# crud.py
# Dummy CRUD functions (No MySQL, no DB connection)
from db_mysql import fetch_one, fetch_all, execute
# ADD PRODUCT
def add_product(product_id, name, category_id, supplier_id, cost_price, selling_price, stock_qty, expiry_date):
    query = """
        INSERT INTO Product(ProductID, ProductName, CategoryID, SupplierID,
                            CostPrice, SellingPrice, StockQty, ExpiryDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    params = (product_id, name, category_id, supplier_id,
              cost_price, selling_price, stock_qty, expiry_date)

    success = execute(query, params)

    if success:
        return {"status": "Product added", "ProductID": product_id}
    else:
        return {"status": "Error adding product"}  


# GET PRODUCT
def get_product(product_id):
    query = "SELECT * FROM Product WHERE ProductID = %s;"
    params = (product_id,)
    
    row = fetch_one(query, params)

    if row:
        return row
    else:
        return {"status": "Product not found", "ProductID": product_id}


# UPDATE PRODUCT
def update_product(product_id, new_stock=None, new_price=None):
    # Build dynamic SQL based on what is provided
    updates = []
    params = []

    if new_stock is not None:
        updates.append("StockQty = %s")
        params.append(new_stock)

    if new_price is not None:
        updates.append("SellingPrice = %s")
        params.append(new_price)

    # If nothing to update
    if not updates:
        return {"status": "No fields to update", "ProductID": product_id}

    # Add ProductID to params
    params.append(product_id)

    query = f"UPDATE Product SET {', '.join(updates)} WHERE ProductID = %s;"

    success = execute(query, tuple(params))

    if success:
        return {"status": "Product updated", "ProductID": product_id}
    else:
        return {"status": "Error updating product", "ProductID": product_id}

# RECORD SALE
def record_sale(product_id, qty_sold, price):
    query = """
        INSERT INTO Sales(ProductID, QuantitySold, SaleDate, SellingPriceAtSale)
        VALUES (%s, %s, CURDATE(), %s);
    """
    params = (product_id, qty_sold, price)

    success = execute(query, params)

    if success:
        return {"status": "Sale recorded", "ProductID": product_id, "QuantitySold": qty_sold}
    else:
        return {"status": "Error recording sale", "ProductID": product_id}


# NEAR EXPIRY
def get_near_expiry(days=7):
    query = """
        SELECT ProductID, ProductName, ExpiryDate, StockQty
        FROM Product
        WHERE DATEDIFF(ExpiryDate, CURDATE()) <= %s
        AND DATEDIFF(ExpiryDate, CURDATE()) >= 0
        ORDER BY ExpiryDate ASC;
    """
    params = (days,)
    rows = fetch_all(query, params)

    return rows if rows else []


# WASTE SUMMARY
def get_waste_summary():
    query = """
        SELECT 
            DATE_FORMAT(RecordedDate, '%Y-%m') AS Month,
            SUM(QuantityWaste) AS TotalWaste
        FROM Waste
        GROUP BY DATE_FORMAT(RecordedDate, '%Y-%m')
        ORDER BY Month ASC;
    """

    rows = fetch_all(query)

    return rows if rows else []


