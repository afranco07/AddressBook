"""Class that holds the window for the export button"""

from tkinter import *

class ExportWindow(object):

    def __init__(self, customer_dict):
        """Constructor"""
        self.customer_dict = customer_dict
        self.root = Tk()
        self.root.wm_title('Export Customer')
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)

        self.name_label = Label(self.top_frame, text=customer_dict['full_name'])
        self.address_1_label = Label(self.top_frame, text=customer_dict['address_1'])
        if customer_dict['address_2'] != '':
            self.address_2_label = Label(self.top_frame, text=customer_dict['address_2'])
        self.address_3_label = Label(self.top_frame, text=customer_dict['address_3'])


        self.name_label.pack()
        self.address_1_label.pack()
        if customer_dict['address_2'] != '':
            self.address_2_label.pack()
        self.address_3_label.pack()

        self.top_frame.pack(side=TOP)

        self.root.mainloop()
