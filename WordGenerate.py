#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import wx
import wx.lib.scrolledpanel
from docxtpl import DocxTemplate
import rmb_upper
from decimal import Decimal

class MyFrame(wx.Frame):

    text_right_pad = 3
    input_right_pad = 20
    input_height = 22
    label_flag = wx.FIXED_MINSIZE | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
    input_flag = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL


    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title,
            size=(1280, 768))
        self.label_font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        self.input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT)

        self.Centre()
        self.createUI()
        

    def createUI(self):

        rootBox = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self, wx.ID_ANY)
        # self.panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(1024, 400), pos=(0, 0), style=wx.SIMPLE_BORDER)
        # self.panel.SetupScrolling()
        # self.panel.SetBackgroundColour('#FFFFFF')

        panel_box = wx.GridSizer(14, 1, 5, 0)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox1
        self.borrower_name1 = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款人1姓名", self.borrower_name1)

        self.borrower_home1 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人1住所地", self.borrower_home1)

        self.borrower_adress1 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人1通讯地址", self.borrower_adress1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox2
        self.borrower_id1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1身份证编号", self.borrower_id1)

        self.borrower_phone1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1电话", self.borrower_phone1)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox3
        self.borrower_name2 = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款人2姓名", self.borrower_name2)

        self.borrower_home2 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人2住所地", self.borrower_home2)

        self.borrower_adress2 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人2通讯地址", self.borrower_adress2)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox4
        self.borrower_id2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2身份证编号", self.borrower_id2)

        self.borrower_phone2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2电话", self.borrower_phone2)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox5
        self.loan_proportion = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "几成购房贷款", self.loan_proportion)

        self.loan_number_small = self.get_input_text(150)
        self.loan_number_small.Bind(wx.EVT_TEXT, self.convert_loan_number)
        self.pack_input_text(hbox_temp, "贷款金额小写", self.loan_number_small)

        self.loan_number_big = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "贷款金额大写", self.loan_number_big)

        self.house_price = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "房屋售价", self.house_price)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox6
        self.house_location = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "购房地址", self.house_location)

        self.house_area = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "建筑面积", self.house_area)

        self.loan_duration_month = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款期限：月", self.loan_duration_month)

        self.start_year = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "起始年", self.start_year)

        self.start_month = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-月", self.start_month)

        self.start_day = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-日", self.start_day)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox7
        self.end_year = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "截止年", self.end_year)

        self.end_month = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-月", self.end_month)

        self.end_day = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-日", self.end_day)

        self.standard_rate = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "基准利率", self.standard_rate)

        float_direction_arr = ["上", "下"]
        self.float_direction = self.get_choice(float_direction_arr)
        self.pack_input_text(hbox_temp, "浮动（上/下）", self.float_direction)

        self.float_num = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "浮动百分百", self.float_num)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox8
        self.actual_rate = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "执行年利率", self.actual_rate)

        self.account_name = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "户名", self.account_name)

        self.account_num = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "账号", self.account_num)

        self.repayment_times = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "还款期数", self.repayment_times)

        choice_arr = ["A", "B"]
        self.repayment_method = self.get_choice(choice_arr)
        self.pack_input_text(hbox_temp, "还款方式:（A/B）", self.repayment_method)

        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox9
        self.repayment_num_small = self.get_input_text(150)
        self.repayment_num_small.Bind(wx.EVT_TEXT, self.convert_repayment_num)
        self.pack_input_text(hbox_temp, "还款金额小写", self.repayment_num_small)

        self.repayment_num_big = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "还款金额大写", self.repayment_num_big)

        self.pawn_num = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "抵押物编号", self.pawn_num)

        hbox10 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox10
        self.contract_num = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "合同份数：大写", self.contract_num)

        self.loan_contract_id = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款合同编号", self.loan_contract_id)

        self.contract_id = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "合同编号", self.contract_id)

        panel_box.Add(hbox1)
        panel_box.Add(hbox2)
        panel_box.Add(hbox3)
        panel_box.Add(hbox4)
        panel_box.Add(hbox5)
        panel_box.Add(hbox6)
        panel_box.Add(hbox7)
        panel_box.Add(hbox8)
        panel_box.Add(hbox9)
        panel_box.Add(hbox10)
        self.panel.SetSizer(panel_box)
        rootBox.Add(self.panel, 1, wx.EXPAND | wx.ALL, 20)

        self.btn_generate_template = self.get_button("生成合同", self.generate_template)
        # self.btn_set_save_path = self.get_button("设置文件保存路径", self.generate_template)

        bottom_box = wx.BoxSizer(wx.HORIZONTAL)
        bottom_box2 = wx.BoxSizer(wx.HORIZONTAL)
        # bottom_box.Add(self.input_save_path, 1)
        # self.pack_label(bottom_box, self.input_save_path)

        bottom_box.Add(self.btn_generate_template, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        # bottom_box2.Add(self.input_save_path, 0, wx.ALIGN_LEFT | wx.ALL, 10)

        rootBox.Add(bottom_box, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        self.SetSizer(rootBox)
        self.SetBackgroundColour(self.panel.GetBackgroundColour())

        # xing_bie_arr = ['男', '女']
        # self.xing_bie = self.get_choice(xing_bie_arr)
        # self.pack_input_text(hbox1, "性别", self.xing_bie)

        pass

    def get_button(self, text, on_button_method):
        button = wx.Button(self, wx.ID_ANY, text)
        button.Bind(wx.EVT_BUTTON, on_button_method)
        button.SetFont(self.label_font)
        return button

    def get_label(self, label):
        label = wx.StaticText(self.panel, -1, label=label)
        label.SetFont(self.label_font)
        # label.SetForegroundColour((255, 0, 0))
        return label

    def get_input_text(self, width):
        input_edit_text = wx.TextCtrl(self.panel, size=(width, self.input_height), style=wx.TE_CENTRE)
        input_edit_text.SetFont(self.input_font)
        return input_edit_text

    def pack_label(self, hbox, label):
        hbox.Add(label, 0, self.label_flag, self.text_right_pad)

    def pack_input_text(self, hbox, input_text):
        hbox.Add(input_text, 0, self.input_flag, self.input_right_pad)

    def pack_input_text(self, hbox, label_name, input_text):
        hbox.Add(self.get_label(label_name), 0, self.label_flag, self.text_right_pad)
        hbox.Add(input_text, 0, self.input_flag, self.input_right_pad)

    def get_choice(self, arr):
        ch = wx.Choice(self.panel, size=(50, 22),  choices=arr)
        ch.Center()
        ch.SetStringSelection(arr[0])
        ch.SetFont(self.input_font)
        return ch

    def convert_repayment_num(self, e):
        money = e.GetString()
        if len(money) == 0:
            self.repayment_num_big.SetLabelText("")
        else:
            self.repayment_num_big.SetLabelText(rmb_upper.cncurrency(e.GetString()))

    def convert_loan_number(self, e):
        money = e.GetString()
        if len(money) == 0:
            self.loan_number_big.SetLabelText("")
        else:
            self.loan_number_big.SetLabelText(rmb_upper.cncurrency(e.GetString()))

    def set_save_path(self):

        pass

    def reset_file_save_path(self, file_name):
        path = "D:/"
        shutil.move(file_name, path + file_name)

    def check_input_valid(self):
        # if len(str(shen_fen_zheng)) != 3:
        #     wx.MessageBox("身份证输入有误，请检查", "提示", wx.OK | wx.ICON_INFORMATION)
        return True

    def generate_template(self, e):
        input_arr = ['borrower_name1', 'borrower_home1', 'borrower_adress1',
                     'borrower_id1', 'borrower_phone1', 'borrower_name2',
                     'borrower_home2', 'borrower_adress2', 'borrower_id2',
                     'borrower_phone2', 'loan_proportion', 'loan_number_big',
                     'loan_number_small', 'house_location', 'house_area',
                     'house_price', 'loan_duration_month', 'start_year',
                     'start_month', 'start_day', 'end_year',
                     'end_month', 'end_day', 'standard_rate',
                      'float_num', 'actual_rate',
                     'account_name', 'account_num', 'repayment_times',
                      'repayment_num_big', 'repayment_num_small',
                     'pawn_num', 'contract_num', 'loan_contract_id',
                     'contract_id'
                     ]
        choice_arr = ['float_direction', 'repayment_method']

        borrower_name1 = self.read_input_text(self.borrower_name1)


        doc = DocxTemplate("模板.docx")

        context = {
            # 'borrower_name1': borrower_name1
        }

        if not self.check_input_valid():
            return

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            read_command = 'self.read_input_text(self.' + input_arr[index] + ')'
            context.update({input_arr[index]: eval(read_command)})

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(choice_arr)):
            read_command = 'self.read_choice_text(self.' + choice_arr[index] + ')'
            context.update({choice_arr[index]: eval(read_command)})

        print(context)

        file_name = borrower_name1 + "_资料.docx"
        doc.render(context)
        doc.save(file_name)
        wx.MessageBox("文件生成成功", "提示", wx.OK | wx.ICON_INFORMATION)

    def read_input_text(self, input):
        return input.GetLineText(0)

    def read_choice_text(self, ch):
        return ch.GetString(ch.GetSelection())

def main():
    app = wx.App()
    ex = MyFrame(None, title='合同自动生成器')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
