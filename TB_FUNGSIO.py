import tkinter as tk
from tkinter import ttk

# Pure function untuk menghitung total pembayaran
def calculate_total(items):
    return sum(int(item[1]) * int(item[2]) for item in items)

# Closure untuk menyimpan riwayat transaksi
def transaction_history():
    history = []

    def add_to_history(items, total):
        nonlocal history
        history.append({'items': items, 'total': total})
        print("Riwayat Transaksi:")
        for idx, transaction in enumerate(history, start=1):
            print(f"Transaksi ke-{idx}: {transaction['items']} - Total: {transaction['total']}")

    return add_to_history

# Decorator untuk menampilkan pesan sebelum dan setelah menjalankan fungsi
def message_decorator(func):
    def wrapper(*args, **kwargs):
        print("Mengeksekusi fungsi...")
        result = func(*args, **kwargs)
        print("Fungsi selesai dieksekusi.")
        return result
    return wrapper

# High-order function yang menggunakan lambda
def apply_discount(discount):
    return lambda price: price * (1 - discount)

# List comprehension untuk menghasilkan data item
def generate_items():
    items = [
        ('Gula', 10000, 2),
        ('Telur', 20000, 1),
        ('Minyak', 25000, 2)
    ]
    return items

# Generator untuk menghasilkan nilai secara lazim
def generate_numbers(n):
    for i in range(n):
        yield i

# GUI menggunakan Tkinter
def create_gui():
    def calculate():
        total = calculate_total(cart)
        total_label.config(text=f"Total Pembayaran: Rp {total:,}")

    def add_to_cart():
        item = tuple(map(lambda x: x.get(), (item_name, item_price, item_quantity)))
        cart.append(item)
        item_name.delete(0, tk.END)
        item_price.delete(0, tk.END)
        item_quantity.delete(0, tk.END)

    def show_history():
        history_function = transaction_history()
        history_function(cart, calculate_total(cart))

    cart = generate_items()

    root = tk.Tk()
    root.title("Program Kasir")
    root.configure(background="gainsboro")

    # Mengatur ukuran kolom
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    item_name_label = tk.Label(root, text="Nama Barang:", foreground="black", font=("Helvetica", 12, "bold"), background="gainsboro")
    item_name_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
    item_name = tk.Entry(root, font=("Helvetica", 12))
    item_name.grid(row=0, column=1, pady=10, padx=10)

    item_price_label = tk.Label(root, text="Harga Barang (Rp):", foreground="black", font=("Helvetica", 12, "bold"), background="gainsboro")
    item_price_label.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
    item_price = tk.Entry(root, font=("Helvetica", 12))
    item_price.grid(row=1, column=1, pady=10, padx=10)

    item_quantity_label = tk.Label(root, text="Jumlah Barang:", foreground="black", font=("Helvetica", 12, "bold"), background="gainsboro")
    item_quantity_label.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)
    item_quantity = tk.Entry(root, font=("Helvetica", 12))
    item_quantity.grid(row=2, column=1, pady=10, padx=10)

    style = ttk.Style()
    style.configure("TButton", foreground="black", background="white", font=("Helvetica", 12))

    add_to_cart_button = ttk.Button(root, text="Tambah ke Keranjang", command=add_to_cart, style="TButton")
    add_to_cart_button.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)

    calculate_button = ttk.Button(root, text="Hitung Total", command=calculate, style="TButton")
    calculate_button.grid(row=4, column=0, columnspan=2, pady=5)

    total_label = tk.Label(root, text="Total Pembayaran: Rp 0", font=("Helvetica", 12), background="gainsboro")
    total_label.grid(row=5, column=0, columnspan=2, pady=5)

    history_button = ttk.Button(root, text="Tampilkan Riwayat Transaksi", command=show_history, style="TButton")
    history_button.grid(row=3, column=1, pady=5, padx=10, sticky=tk.E)

    root.mainloop()

# Menjalankan GUI
if __name__ == "__main__":
    create_gui()