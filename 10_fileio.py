FILE_NAME = "products.csv"

# doc du lieu tu file va tra ve ds doc duoc
def read_products():
    # tao 1 bien kieu list chua tat ca sp doc duoc tu file
    productList = []

    try:

        with open(FILE_NAME, "r") as file:
            # bo qua dong dau
            file.readline()
            # doc tiep tu dong so 2
            for line in file:
                line = line.strip() # bo ky tu \n o cuoi moi~ dong

                # cat chuoi thanh mang
                data = line.split(",")
                # tao sp theo dang dictionary
                product = {
                    "id": data[0],
                    "name": data[1],
                    "price": data[2]
                }

            # them sp vao list
            productList.append(product)
    except FileNotFoundError:
        print("File ko tim thay")
    except Exception as e:
        print("Error: ", e)
    # print(productList)
    return productList



read_products()


# ham hien thi sp
def display_product(products):
    # kiem tra neu file rong(chua co du lieu)
    if len(products) == 0:
        print("No product")
        return

    # neu co du lieu thi in ra
    print("\n -------------------Product List---------------")
    for p in products:
        print(f"ProductID: {p['id']} --- ProductName: {p['name']} --- Price: {p['price']}")

# ham them sp
def add_product(products):
    try:
        # cho nhap product id
        product_id = input("Enter Product ID")
        # kiem tra xem id nay co ton tai hay chua?
        for p in products:
            if p['id'].lower() == product_id.lower():
                print("ID was duplicated")
                return

        # nhap ten
        product_name = input("Enter Product Name:")
        # nhap gia
        product_price = float(input("Enter price:"))
        
        # tao sp theo dang dictionary
        product = {"id": product_id, "name": product_name, "price": product_price}
        # them sp vao danh sach
        products.append(product)
        print("Product added succesfully")
    except ValueError:
            print("Price must be number!!!")

# ham tim kiem sp
def search_product(products):
    # nhap ID de tim kiem
    product_id = input(" Enter Product ID:")

    #tao 1 bien kieu list de chua sp tim thay duoc
    found = []
    for p in products:
        if product_id.lower() in p['id'].lower():
            found.append(p)

    # kiem tra xem co tim kiem duoc hay ko
    if len(found) > 0:
        display_product(found)
    else:
        print("No product found")

# ham luu vao file
def save_product(products):
    try:
        with open(FILE_NAME, "w") as file:
            # ghi lai dong dau tien
            file.write("ProductID,ProductName,Price\n")

            #ghi cac dong tiep theo dua vao ds
            for p in products:
                line = p['id'] + "," + p['name'] + "," + str(p['price']) + "\n"
                file.write(line)
            print("Write succesfully")
    except Exception as e:
        print("Error: ", e)
    
# Main Menu
def main():
    # doc du lieu khi chuong trinh chay, goi ham read products()
    products = read_products()


    while True:
        print("******************MENU*****************")
        print("1. Display all product")
        print("2. Add product")
        print("3. Search product by ID")
        print("4. Save products to file")
        print("5. Exit Program")
        print("******************MENU*****************")

        choice = input("Enter your choice")
        if choice == "1":
            display_product(products)
            
        elif choice =="2":
            
            add_product(products)
            
        elif choice =="3":
            search_product(products)
            
        elif choice =="4":
            save_product(products)
            pass
        elif choice == "5":
            print("Exit Program")
            break
        else:
            print("Wrong choice. Enter 1-5")
# goi ham main
main()




