import tkinter as tk
from tkinter import simpledialog


class Node:
    def __init__(self, data):
        # mendefinisikan single linked list
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        # membuat variabel first
        self.first = None

    # insert first
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.first
        self.first = new_node

    # insert setelah indeks
    def insert_index(self, data, index):
        if index < 0:
            tk.messagebox.showerror("Error","Indeks tidak boleh negatif")
            return

        new_node = Node(data)
        if index == 0:
            self.insert_first(data)
        else:
            current_node = self._get_node_at_index(index - 1)
            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                tk.messagebox.showerror("Error","Indeks tidak ditemukan")

    # insert last
    def insert_end(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
        else:
            current_node = self.first
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # update pada indeks
    def update_index(self, index, value):
        if index < 0:
            tk.messagebox.showerror("Error","Indeks tidak boleh negatif")
            return

        current_node = self._get_node_at_index(index - 1)
        if current_node:
            current_node.data = value
        else:
            tk.messagebox.showerror("Error","Indeks tidak ditemukan")

    # delete first
    def delete_first(self):
        if self.first:
            self.first = self.first.next
        else:
            tk.messagebox.showerror("Error","List kosong")

    # delete pada indeks
    def delete_index(self, index):
        if index < 0:
            tk.messagebox.showerror("Error","Indeks tidak boleh negatif")
            return

        if self.first is None:
            tk.messagebox.showerror("Error","List kosong")
            return

        if index == 0:
            self.delete_first()
        else:
            current_node = self._get_node_at_index(index - 1)
            if current_node and current_node.next:
                current_node.next = current_node.next.next
            else:
                tk.messagebox.showerror("Error","Indeks tidak ditemukan")

    #delete last
    def delete_last(self):
        if self.first is None:
            tk.messagebox.showerror("Error","List kosong")
            return

        if self.first.next is None:
            self.first = None
            return

        current_node = self.first
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # dapatkan indeks
    def _get_node_at_index(self, index):
        if index < 0:
            return None

        current_node = self.first
        position = 0

        while current_node and position < index:
            current_node = current_node.next
            position += 1

        return current_node
    
    # conjugate list kedua ke list pertama
    def conjugate_list(self, other_list):
        if self.first is None:
            tk.messagebox.showerror("Error","List 1 kosong")
        else:
            last_node_list1 = self.first
            while last_node_list1.next:
                last_node_list1 = last_node_list1.next

            if other_list.first is not None:
                last_node_list1.next = other_list.first
                other_list.first = None

# visualisasi
class LinkedListVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualisasi Linked List")


        self.linked_list1 = Linked_List()
        self.linked_list2 = Linked_List()

        self.canvas = tk.Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack()
        
        frame1 = tk.Frame(master)
        frame1.pack(side=tk.TOP)

        frame2 = tk.Frame(master)
        frame2.pack(side=tk.TOP)

        self.insert_first_button1 = tk.Button(frame1, text="Insert Indeks Pertama (List 1)", command=self.insert_first1)
        self.insert_first_button1.pack(side=tk.LEFT)

        self.insert_end_button1 = tk.Button(frame1, text="Insert Indeks Terakhir (List 1)", command=self.insert_end1)
        self.insert_end_button1.pack(side=tk.LEFT)

        self.insert_index_button1 = tk.Button(frame1, text="Insert Setelah Indeks (List 1)", command=self.insert_index1)
        self.insert_index_button1.pack(side=tk.LEFT)

        self.update_index_button1 = tk.Button(frame1, text="Update Di Indeks (List 1)", command=self.update_index1)
        self.update_index_button1.pack(side=tk.LEFT)

        self.delete_first_button1 = tk.Button(frame1, text="Hapus Indeks Pertama (List 1)", command=self.delete_first1)
        self.delete_first_button1.pack(side=tk.LEFT)

        self.delete_index_button1 = tk.Button(frame1, text="Hapus Pada Indeks (List 1)", command=self.delete_index1)
        self.delete_index_button1.pack(side=tk.LEFT)

        self.delete_last_button1 = tk.Button(frame1, text="Hapus Indeks Terakhir (List 1)", command=self.delete_last1)
        self.delete_last_button1.pack(side=tk.LEFT)

        self.insert_first_button2 = tk.Button(frame2, text="Insert Indeks Pertama (List 2)", command=self.insert_first2)
        self.insert_first_button2.pack(side=tk.LEFT)

        self.insert_end_button2 = tk.Button(frame2, text="Insert Indeks Terakhir (List 2)", command=self.insert_end2)
        self.insert_end_button2.pack(side=tk.LEFT)

        self.insert_index_button2 = tk.Button(frame2, text="Insert Setelah Indeks (List 2)", command=self.insert_index2)
        self.insert_index_button2.pack(side=tk.LEFT)

        self.update_index_button2 = tk.Button(frame2, text="Update Di Indeks (List 2)", command=self.update_index2)
        self.update_index_button2.pack(side=tk.LEFT)

        self.delete_first_button2 = tk.Button(frame2, text="Hapus Elemen Pertama (List 2)", command=self.delete_first2)
        self.delete_first_button2.pack(side=tk.LEFT)

        self.delete_index_button2 = tk.Button(frame2, text="Hapus Pada Indeks (List 2)", command=self.delete_index2)
        self.delete_index_button2.pack(side=tk.LEFT)

        self.delete_last_button2 = tk.Button(frame2, text="Hapus Indeks Terakhir (List 2)", command=self.delete_last2)
        self.delete_last_button2.pack(side=tk.LEFT)

        self.concatenate_button = tk.Button(frame2, text="Gabung List", command=self.conjugate_lists)
        self.concatenate_button.pack(side=tk.LEFT)

        self.draw_linked_lists()

    def draw_first(self, linked_list, y_offset):
        # Draw block for next data (square)
        self.canvas.create_rectangle(50, 50 + y_offset,
                                     80, 80 + y_offset, fill="lightgreen")
        self.canvas.create_text(50 + (80 - 50) / 2, 50 + (80 - 50) / 2 + y_offset,
                                text="NIL" if linked_list.first is None else "First", font=("Arial", 10))

        # Draw arrow
        if linked_list.first:
            self.canvas.create_line(50 + (80 - 50) / 2, 50 + (80 - 50) + y_offset,
                                    50 + (80 - 50) / 2, 120 + (80 - 50) + y_offset, arrow=tk.LAST)

    def draw_linked_list(self, linked_list, y_offset):
        current_node = linked_list.first
        x = 50 
        y = 150 + y_offset
        width = 60
        height = 30
        arrow_length = 60
        square_size = 30

        while current_node:
            # Draw block for data
            self.canvas.create_rectangle(x, y, x + width, y + height, fill="lightblue")
            self.canvas.create_text(x + width / 2, y + height / 2, text=str(current_node.data), font=("Arial", 10))

            # Draw block for next data (square)
            self.canvas.create_rectangle(x + width, y + (height - square_size) / 2,
                                         x + width + square_size, y + (height + square_size) / 2, fill="lightgreen")
            if not current_node.next:
                self.canvas.create_text(x + width + square_size / 2, y + height / 2,
                                        text="NIL", font=("Arial", 10))
            else:
                self.canvas.create_line(x + width / 1.2 + square_size, y + height / 2,
                                        x + width + square_size + arrow_length / 2, y + height / 2, arrow=tk.LAST)

            x += width + square_size + arrow_length / 2
            current_node = current_node.next

    def draw_linked_lists(self):
        self.canvas.delete("all")

        self.draw_first(self.linked_list1, 0)
        self.draw_linked_list(self.linked_list1, 0)

        y_offset = 200
        self.draw_first(self.linked_list2, y_offset)
        self.draw_linked_list(self.linked_list2, y_offset)

    def insert_first1(self):
        data = simpledialog.askinteger("Insert Indeks Pertama (List 1)", "Masukkan data:")
        if data is not None:
            self.linked_list1.insert_first(data)
            self.draw_linked_lists()

    def insert_end1(self):
        data = simpledialog.askinteger("Insert Indeks Terakhir (List 1)", "Masukkan data:")
        if data is not None:
            self.linked_list1.insert_end(data)
            self.draw_linked_lists()

    def insert_index1(self):
        index = simpledialog.askinteger("Insert at Index (List 1)", "Masukkan indeks:")
        data = simpledialog.askinteger("Insert at Index (List 1)", "Masukkan data:")
        if index is not None and data is not None:
            self.linked_list1.insert_index(data, index)
            self.draw_linked_lists()

    def update_index1(self):
        index = simpledialog.askinteger("Update Di Indeks (List 1)", "Masukkan indeks:")
        data = simpledialog.askinteger("Update Di Indeks (List 1)", "Masukkan data:")
        if index is not None and data is not None:
            self.linked_list1.update_index(index, data)
            self.draw_linked_lists()

    def delete_first1(self):
        self.linked_list1.delete_first()
        self.draw_linked_lists()

    def delete_index1(self):
        index = simpledialog.askinteger("Hapus Pada Indeks (List 1)", "Masukkan indeks:")
        if index is not None:
            self.linked_list1.delete_index(index)
            self.draw_linked_lists()

    def delete_last1(self):
        self.linked_list1.delete_last()
        self.draw_linked_lists()

    def insert_first2(self):
        data = simpledialog.askinteger("Insert Indeks Pertama (List 2)", "Masukkan data:")
        if data is not None:
            self.linked_list2.insert_first(data)
            self.draw_linked_lists()

    def insert_end2(self):
        data = simpledialog.askinteger("Insert Indeks Terakhir (List 2)", "Masukkan data:")
        if data is not None:
            self.linked_list2.insert_end(data)
            self.draw_linked_lists()

    def insert_index2(self):
        index = simpledialog.askinteger("Insert at Index (List 2)", "Masukkan indeks:")
        data = simpledialog.askinteger("Insert at Index (List 2)", "Masukkan data:")
        if index is not None and data is not None:
            self.linked_list2.insert_index(data, index)
            self.draw_linked_lists()

    def update_index2(self):
        index = simpledialog.askinteger("Update Di Indeks (List 2)", "Masukkan indeks:")
        data = simpledialog.askinteger("Update Di Indeks (List 2)", "Masukkan data:")
        if index is not None and data is not None:
            self.linked_list2.update_index(index, data)
            self.draw_linked_lists()

    def delete_first2(self):
        self.linked_list2.delete_first()
        self.draw_linked_lists()

    def delete_index2(self):
        index = simpledialog.askinteger("Hapus Pada Indeks (List 2)", "Masukkan indeks:")
        if index is not None:
            self.linked_list2.delete_index(index)
            self.draw_linked_lists()

    def delete_last2(self):
        self.linked_list2.delete_last()
        self.draw_linked_lists()

    def conjugate_lists(self):
        self.linked_list1.conjugate_list(self.linked_list2)
        self.draw_linked_lists()

root = tk.Tk()
app = LinkedListVisualizer(root)
root.mainloop()
