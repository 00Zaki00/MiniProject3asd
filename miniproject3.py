from prettytable import PrettyTable

class Node:
    def __init__(self, kode, merk, tipe, harga, stok):
        self.kode = kode
        self.merk = merk
        self.tipe = tipe
        self.harga = harga
        self.stok = stok
        self.next = None

class TokoLaptop:
    def __init__(self):
        self.head = None

    def tambah_laptop(self, kode, merk, tipe, harga, stok):
        new_laptop = Node(kode, merk, tipe, harga, stok)
        new_laptop.next = self.head
        self.head = new_laptop
        print(f"Laptop {merk} {tipe} berhasil ditambahkan.")

    def lihat_laptop(self, kode=None):
        current = self.head
        found = False

        while current:
            if kode is None or current.kode == kode:
                self.display_laptop(current)
                found = True

            current = current.next

        if not found:
            print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def ubah_laptop(self, kode, field, nilai_baru):
        current = self.head
        found = False

        while current:
            if current.kode == kode:
                if hasattr(current, field):
                    setattr(current, field, nilai_baru)
                    print(f"Data {field} untuk laptop dengan kode {kode} berhasil diubah.")
                    found = True
                    break
                else:
                    print(f"Field {field} tidak valid.")
                    break

            current = current.next

        if not found:
            print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def hapus_laptop(self, kode):
        current = self.head
        previous = None
        found = False

        while current:
            if current.kode == kode:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                print(f"Laptop dengan kode {kode} berhasil dihapus.")
                found = True
                break

            previous = current
            current = current.next

        if not found:
            print(f"Laptop dengan kode {kode} tidak ditemukan.")

    def lihat_semua_laptop(self, ascending=True, sort_by="kode"):
        laptops = self.get_laptops_as_list()
        sorted_laptops = self.sort_laptops(laptops, ascending, sort_by)

        if not sorted_laptops:
            print("Tidak ada laptop yang tersedia.")
            return

        for laptop in sorted_laptops:
            self.display_laptop(laptop)

    def sort_laptops(self, laptops, ascending, sort_by):
        reverse_order = not ascending
        if sort_by in ["kode", "merk", "tipe", "harga", "stok"]:
            return sorted(laptops, key=lambda x: getattr(x, sort_by), reverse=reverse_order)
        else:
            print("Sorting tidak dapat dilakukan. Field tidak valid.")
            return laptops

    def get_laptops_as_list(self):
        laptops = []
        current = self.head
        while current:
            laptops.append(current)
            current = current.next
        return laptops

    def display_laptop(self, laptop):
        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        for key, value in laptop.__dict__.items():
            table.add_row([key.capitalize(), value])
        print(f"Detail Laptop {laptop.kode}:\n{table}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Laptop")
            print("2. Lihat Laptop")
            print("3. Ubah Laptop")
            print("4. Hapus Laptop")
            print("5. Lihat Semua Laptop")
            print("6. Sortir Laptop (Ascending)")
            print("7. Sortir Laptop (Descending)")
            print("0. Keluar")

            choice = input("Pilih menu (0-7): ")

            if choice == '1':
                kode = input("Masukkan kode laptop: ")
                merk = input("Masukkan merk laptop: ")
                tipe = input("Masukkan tipe laptop: ")
                harga = int(input("Masukkan harga laptop: "))
                stok = int(input("Masukkan stok laptop: "))
                self.tambah_laptop(kode, merk, tipe, harga, stok)

            elif choice == '2':
                kode = input("Masukkan kode laptop (atau biarkan kosong untuk melihat semua): ")
                self.lihat_laptop(kode)

            elif choice == '3':
                kode = input("Masukkan kode laptop: ")
                field = input("Masukkan field yang ingin diubah (merk/tipe/harga/stok): ")
                nilai_baru = input("Masukkan nilai baru: ")
                self.ubah_laptop(kode, field, nilai_baru)

            elif choice == '4':
                kode = input("Masukkan kode laptop yang ingin dihapus: ")
                self.hapus_laptop(kode)

            elif choice == '5':
                self.lihat_semua_laptop()

            elif choice == '6':
                self.lihat_semua_laptop(ascending=True)
            
            elif choice == '7':
                self.lihat_semua_laptop(ascending=False)

            elif choice == '0':
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# Contoh penggunaan
toko_laptop = TokoLaptop()

toko_laptop.tambah_laptop('1', 'Asus', 'ROG Strix', 15000000, 10)
toko_laptop.tambah_laptop('2', 'Dell', 'Inspiron', 8000000, 15)
toko_laptop.tambah_laptop('3', 'Acer', 'Nitro 5', 18000000, 3)

toko_laptop.menu()
