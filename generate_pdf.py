from fpdf import FPDF

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Inventory Management System - C++ Code Explanation", ln=True, align="C")
pdf.ln(10)

# Section headers with VS Code-style formatting (dark background for code sections)
def add_heading(pdf, text, level=1):
    font_size = {1: 12, 2: 11, 3: 10}[level]
    pdf.set_font("Arial", "B", font_size)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 10, text, ln=True, fill=True)
    pdf.ln(5)

# Adding Code Block Style
def add_code_block(pdf, code):
    pdf.set_font("Courier", "", 10)
    pdf.set_fill_color(245, 245, 245)
    for line in code.splitlines():
        pdf.cell(0, 7, line, ln=True, fill=True)

# Content
add_heading(pdf, "1. Structure to Hold Product Information", 1)
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 10, "The Product structure is used to define what a product should look like in terms of its id, name, quantity, and price. Each product in the inventory will have these four data points.")

# Code snippet for Product Structure
product_code = """
struct Product {
    int id;
    string name;
    int quantity;
    double price;
};
"""
add_code_block(pdf, product_code)

# Inventory Class Section
add_heading(pdf, "2. Inventory Class", 1)
pdf.multi_cell(0, 10, "The Inventory class manages all products and has functions for adding, updating, deleting, restocking, and selling products, as well as displaying all products in the inventory.")

# Key parts of the Inventory Class
add_heading(pdf, "Key Parts of the Inventory Class", 2)
pdf.multi_cell(0, 10, "Private Variables:")
inventory_private_vars = """
vector<Product> products;   // Holds all products in the inventory
int lowStockThreshold;      // Minimum quantity for low stock alert
"""
add_code_block(pdf, inventory_private_vars)

# Functions in the Inventory Class
add_heading(pdf, "Functions in the Inventory Class", 2)

# Adding function details
functions_details = [
    ("addProduct", "Adds a new product to the inventory and checks if the product ID is unique."),
    ("updateProduct", "Updates the quantity and price of an existing product and checks for low stock."),
    ("deleteProduct", "Deletes a product from inventory based on its ID."),
    ("restockProduct", "Increases the quantity of a product by a specified amount."),
    ("sellProduct", "Reduces quantity upon sale. Shows an error if there is insufficient quantity."),
    ("checkLowStock", "Checks if a product's quantity is below the threshold and shows a low stock warning."),
    ("displayProducts", "Displays all products in the inventory with their details.")
]

for func_name, func_desc in functions_details:
    add_heading(pdf, f"{func_name}:", 3)
    pdf.multi_cell(0, 8, func_desc)

# Main Function and Menu System
add_heading(pdf, "3. Main Function and Menu System", 1)
pdf.multi_cell(0, 10, "The main function provides a user menu to perform various inventory management actions, like adding or deleting products. The program runs until the user chooses to exit.")

# Code snippet for Main Function
main_function_code = """
int main() {
    Inventory inventory(5); // Low stock threshold set to 5
    int choice;

    while (true) {
        cout << "--- Inventory Management System ---" << endl;
        cout << "1. Add Product" << endl;
        cout << "2. Update Product" << endl;
        cout << "3. Delete Product" << endl;
        cout << "4. Restock Product" << endl;
        cout << "5. Sell Product" << endl;
        cout << "6. Display All Products" << endl;
        cout << "7. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 7) break;

        int id, quantity;
        double price;
        string name;

        switch (choice) {
            case 1:
                cout << "Enter product ID: ";
                cin >> id;
                cout << "Enter product name: ";
                cin.ignore();
                getline(cin, name);
                cout << "Enter quantity: ";
                cin >> quantity;
                cout << "Enter price: ";
                cin >> price;
                inventory.addProduct(id, name, quantity, price);
                break;
            // Other cases follow...
        }
    }
    return 0;
}
"""
add_code_block(pdf, main_function_code)

# Saving the PDF
pdf_output_path = "Inventory_Management_C++_Explanation.pdf"
pdf.output(pdf_output_path)
