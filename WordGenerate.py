#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import wx
import wx.lib.scrolledpanel
from docxtpl import DocxTemplate
import rmb_upper
import os
import time
import json
from datetime import datetime

app_title = '合同生成器器'

class MyFrame(wx.Frame):
    file_generate_error = False
    text_right_pad = 3
    input_right_pad = 20
    input_height = 22
    label_flag = wx.FIXED_MINSIZE | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
    input_flag = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL

    choice_data_arr = ['float_direction', 'repayment_method', 'sex1']
    input_data_arr = ['borrower_name1', 'borrower_home1', 'borrower_adress1',
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
                 'age1', 'household1', 'marg',
                 'month_income1', 'month_income2', 'sup_people',
                 'company1', 'company2', 'company_phone1', 'company_phone2',
                 'home_income', 'house_uint_price', 'paid_house_money',
                 'house_no', 'birthday'
                 ]

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title,
            size=(1280, 768))
        self.label_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        self.button_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        self.input_font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.LIGHT)

        self.Centre()
        self.createUI()

    def onClose(self, event):
        self.timer.Stop()
        self.Close()

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
        self.borrower_adress1.Bind(wx.EVT_TEXT, self.syn_borrower_address)
        self.pack_input_text(hbox_temp, "借款人1通讯地址", self.borrower_adress1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox2
        self.borrower_id1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1身份证号", self.borrower_id1)

        self.borrower_phone1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "电话", self.borrower_phone1)

        sex_arr = ['男', '女']
        self.sex1 = self.get_choice(sex_arr)
        self.pack_input_text(hbox_temp, "性别", self.sex1)

        self.age1 = self.get_input_text(50)
        self.pack_input_text(hbox_temp, "年龄", self.age1)

        self.household1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "户籍", self.household1)

        hbox22 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox22
        self.company1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1单位", self.company1)
        self.company_phone1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "单位电话", self.company_phone1)
        self.month_income1 = self.get_input_text(100)
        self.month_income1.Bind(wx.EVT_TEXT, self.cal_home_income)
        self.pack_input_text(hbox_temp, "月收入", self.month_income1)
        self.sup_people = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "供养人数", self.sup_people)

        hbox23 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox23
        self.company2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2单位", self.company2)
        self.company_phone2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "单位电话", self.company_phone2)
        self.month_income2 = self.get_input_text(100)
        self.month_income2.Bind(wx.EVT_TEXT, self.cal_home_income)
        self.pack_input_text(hbox_temp, "月收入", self.month_income2)
        self.home_income = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "家庭月收入", self.home_income)


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
        self.pack_input_text(hbox_temp, "借款人2身份证号", self.borrower_id2)

        self.borrower_phone2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2电话", self.borrower_phone2)

        self.marg = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款人1婚姻状况", self.marg)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox5
        self.loan_proportion = self.get_input_text(100)
        self.loan_proportion.Bind(wx.EVT_TEXT, self.cal_house_price)
        self.pack_input_text(hbox_temp, "几成购房贷款", self.loan_proportion)

        self.loan_number_small = self.get_input_text(150)
        self.loan_number_small.Bind(wx.EVT_TEXT, self.convert_loan_number)
        self.pack_input_text(hbox_temp, "贷款金额小写", self.loan_number_small)

        self.loan_number_big = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "贷款金额大写", self.loan_number_big)

        self.house_price = self.get_input_text(100)
        self.house_price.Bind(wx.EVT_TEXT, self.cal_house_uint_price)
        self.pack_input_text(hbox_temp, "房屋售价", self.house_price)

        hbox52 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox52
        self.house_location = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "购房地址", self.house_location)

        self.house_no = self.get_input_text(150)
        self.pack_input_text(hbox_temp, "房屋座别", self.house_no)

        self.house_area = self.get_input_text(100)
        self.house_area.Bind(wx.EVT_TEXT, self.cal_house_uint_price)
        self.pack_input_text(hbox_temp, "建筑面积", self.house_area)

        self.house_uint_price = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "房屋单价", self.house_uint_price)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox6

        self.paid_house_money = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "已付购房款", self.paid_house_money)

        self.loan_duration_month = self.get_input_text(100)
        self.loan_duration_month.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "借款期限/月", self.loan_duration_month)

        self.start_year = self.get_input_text(100)
        self.start_year.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "起始年", self.start_year)

        self.start_month = self.get_input_text(100)
        self.start_month.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "-月", self.start_month)

        self.start_day = self.get_input_text(100)
        self.start_day.Bind(wx.EVT_TEXT, self.cal_end_date)
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
        self.standard_rate.SetLabelText("4.9")
        self.pack_input_text(hbox_temp, "基准利率", self.standard_rate)

        float_direction_arr = ["上", "下"]
        self.float_direction = self.get_choice(float_direction_arr)
        self.float_direction.Bind(wx.EVT_TEXT, self.cal_actual_rate)
        self.pack_input_text(hbox_temp, "浮动（上/下）", self.float_direction)

        self.float_num = self.get_input_text(100)
        self.float_num.Bind(wx.EVT_TEXT, self.cal_actual_rate)
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

        self.birthday = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1出生日期", self.birthday)
        self.set_input_text(self.birthday, '年 月 日')

        panel_box.Add(hbox1)
        panel_box.Add(hbox2)
        panel_box.Add(hbox3)
        panel_box.Add(hbox4)
        panel_box.Add(hbox5)
        panel_box.Add(hbox52)
        panel_box.Add(hbox6)
        panel_box.Add(hbox7)
        panel_box.Add(hbox8)
        panel_box.Add(hbox9)
        panel_box.Add(hbox22)
        panel_box.Add(hbox23)

        self.panel.SetSizer(panel_box)

        rootBox.Add(self.panel, 1, wx.EXPAND | wx.ALL, 20)

        self.btn_generate_template = self.get_button("生成合同", self.pre_generate_template)
        self.btn_set_save_path = self.get_button("文件路径", self.set_save_path)
        self.label_set_save_path = wx.StaticText(self, -1, label="当前路径")
        self.label_set_save_path.SetFont(self.input_font)
        cur_path = os.path.abspath(".")
        self.label_set_save_path.SetLabelText(cur_path)

        bottom_box = wx.BoxSizer(wx.HORIZONTAL)
        bottom_box2 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_save_data = self.get_button("保存", self.save_user_data)
        self.btn_resume_last_data = self.get_button("恢复", self.resume_last_data)
        self.btn_resume_selected_data = self.get_button("选择恢复", self.resume_selected_user_data)
        self.btn_clear_data = self.get_button("一键清空", self.clear_input_data)
        self.btn_full_screen = self.get_button("全屏切换", self.show_full_screen)

        # self.btn_test = self.get_button("测试", self.test_button_event)
        # bottom_box.Add(self.btn_test, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)

        bottom_box.Add(self.btn_save_data, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 0)
        bottom_box.Add(self.btn_resume_last_data, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        bottom_box.Add(self.btn_resume_selected_data, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        bottom_box.Add(self.btn_clear_data, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        bottom_box.Add(self.btn_generate_template, 0, wx.ALIGN_CENTER | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 60)
        bottom_box.Add(self.btn_full_screen, 0, wx.ALIGN_CENTER | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 60)

        bottom_box.Add(self.btn_set_save_path, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        bottom_box.Add(self.label_set_save_path, 0, wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        rootBox.Add(bottom_box, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 40)
        # rootBox.Add(bottom_box2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.DOWN | wx.EXPAND, 40)

        self.SetSizer(rootBox)
        self.SetBackgroundColour(self.panel.GetBackgroundColour())


        # 创建定时器
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.refresh_timer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)
        self.resume_setting()

        # icon = wx.EmptyIcon()
        # icon.CopyFromBitmap(wx.Bitmap("my.ico", wx.BITMAP_TYPE_ANY))
        # self.SetIcon(icon)
        # self.SetBackgroundColour((0, 0, 0))
        pass

    def show_full_screen(self, e):
        isFull = self.IsFullScreen()
        if isFull:
            self.ShowFullScreen(False, wx.FULLSCREEN_NOMENUBAR)
        else:
            self.ShowFullScreen(True, wx.FULLSCREEN_NOMENUBAR)
        pass

    def test_button_event(self, e):

        pass

    def check_app_valid(self):
        now = datetime.now()
        now_ts = now.timestamp()
        target_date = datetime(2019, 4, 18, 0, 0, 0)
        target_date_ts = target_date.timestamp()
        print(target_date, '      ', target_date_ts)
        print(now, now.timestamp())

        if (now_ts < target_date_ts):
            print('app is valid')
            return

        print('alert, app is invalid')
        dlg = wx.MessageDialog(None, "软件异常，请联系开发者", caption="提示",
                               style=wx.OK | wx.ICON_INFORMATION, pos=wx.DefaultPosition)
        ret = dlg.ShowModal()
        print("app close")
        self.Close()

    def refresh_timer(self, e):
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.SetTitle(app_title + '                        ' + cur_time)
        # self.check_app_valid()

    def get_button(self, text, on_button_method):
        button = wx.Button(self, wx.ID_ANY, text)
        button.Bind(wx.EVT_BUTTON, on_button_method)
        button.SetFont(self.label_font)
        return button

    # 注意这里 label的父容器是panel
    def get_label(self, label):
        label = wx.StaticText(self.panel, -1, label=label)
        label.SetFont(self.label_font)
        # label.SetForegroundColour((255, 255, 255))
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

    def syn_borrower_address(self, e):
        self.borrower_adress2.SetLabelText(self.read_input_text(self.borrower_adress1))

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
            self.cal_house_price(e)

    def cal_house_price(self, e):
        try:
            loan_pr = float(self.read_input_text(self.loan_proportion))
            loan_num = float(self.read_input_text(self.loan_number_small))
        except BaseException:
            return

        house_price = loan_num / loan_pr * 10
        self.house_price.SetLabelText(str(round(house_price, 2)))
        pass

    def cal_actual_rate(self, e):
        print("cal_actual_rate")
        try:
            statand = float(self.read_input_text(self.standard_rate).replace("%", ""))
            dir = self.read_choice_text(self.float_direction)
            float_num = float(self.read_input_text(self.float_num).replace("%", ""))
        except BaseException:
            print("cal_actual_rate exception")
            return

        actual_rate = 0.0
        if dir == '上':
            actual_rate = statand * (1 + float_num/100)
        else:
            actual_rate = statand * (1 - float_num / 100)
        self.actual_rate.SetLabelText(str(round(actual_rate, 3)))

    def cal_end_date(self, e):
        if len(self.read_input_text(self.loan_duration_month)) > 0:
            self.repayment_times.SetLabelText(self.read_input_text(self.loan_duration_month))

        try:
            start_year = int(self.read_input_text(self.start_year))
            start_month = int(self.read_input_text(self.start_month))
            start_day = int(self.read_input_text(self.start_day))
            duartion_month = int(self.read_input_text(self.loan_duration_month))
        except BaseException:
            print("cal_end_date exception")
            return

        print("start calculate end date")
        total_m = duartion_month
        end_year = start_year + int(total_m / 12)
        end_month = start_month + total_m % 12
        if end_month > 12:
            end_month = end_month - 12
            end_year = end_year + 1
        end_day = start_day

        self.end_year.SetLabelText(str(end_year))
        self.end_month.SetLabelText(str(end_month))
        self.end_day.SetLabelText(str(end_day))
        # if start_year.isdigit() and start_month.isdigit() and start_day.isdigit() and duartion_month.isdigit():
        #     print("cal")

    def set_save_path(self, e):
        # Create open file dialog
        dlg = wx.DirDialog(self, "选择文件保存路径", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            print (dlg.GetPath())  # 文件夹路径
            self.label_set_save_path.SetLabelText(dlg.GetPath())

        dlg.Destroy()
        self.save_setting()

        pass

    def reset_file_save_path(self, file_name):
        path = self.label_set_save_path.GetLabelText()

        new_folder = os.path.join(path, self.borrower_name)
        print(new_folder)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        new_file = os.path.join(new_folder, file_name)
        print("move to ", new_file)
        try:
            if os.path.exists(new_file):
                os.remove(new_file)
            shutil.move(file_name, new_file)
        except BaseException:
            print("file save error ")
            self.file_generate_error = True
            wx.MessageBox("文件写如错误，请检查word文件是否关闭，关闭后重试", "提示", wx.OK | wx.ICON_INFORMATION)

    def check_input_valid(self):
        # if len(str(shen_fen_zheng)) != 3:
        #     wx.MessageBox("身份证输入有误，请检查", "提示", wx.OK | wx.ICON_INFORMATION)
        return True

    def get_templete_doc_files(self):
        curdir = os.getcwd()
        files = os.listdir(curdir)
        target = [item for item in files if str(item).find('模板') >= 0 and str(item).find('~$') == -1]
        print(target)
        return target

    def pre_generate_template(self, e):

        self.borrower_name = self.read_input_text(self.borrower_name1)
        dlg = wx.MessageDialog(None, "请关闭以 " + self.borrower_name + " 开头的生成的合同文档\n开始生成合同", caption="确认生成",
                               style=wx.OK | wx.CANCEL | wx.ICON_INFORMATION, pos=wx.DefaultPosition)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            self.generate_template(e)
        else:
            print("cancle")
        pass

    def generate_template(self, e):
        progress = wx.ProgressDialog("正在生成合同", "请稍等", maximum=100, parent=self,
                                     style=wx.PD_SMOOTH | wx.PD_AUTO_HIDE)
        # percent = 20
        # progress.Update(percent)

        input_arr = self.input_data_arr
        choice_arr = self.choice_data_arr

        borrower_name1 = self.read_input_text(self.borrower_name1)
        self.borrower_name = borrower_name1

        progress.Update(10)

        context = {
            # 'borrower_name1': borrower_name1
        }

        if not self.check_input_valid():
            return

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            read_command = 'self.read_input_text(self.' + input_arr[index] + ')'
            context.update({input_arr[index]: eval(read_command)})

        progress.Update(20)

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(choice_arr)):
            read_command = 'self.read_choice_text(self.' + choice_arr[index] + ')'
            context.update({choice_arr[index]: eval(read_command)})

        #给一些字段 添加别名
        context.update({'nm1': context['borrower_name1']})

        #自动计算相关数据
        # self.cal_some_data(context)

        print(context)

        # 文件数量
        # file_num = 1
        # file_name = "担保借款合同模板.docx"
        self.file_generate_error = False

        files = self.get_templete_doc_files()
        file_num = len(files)

        for one_file in files:
            self.generate_doc(str(one_file), borrower_name1, context, progress, file_num)

        # self.generate_doc(file_name, borrower_name1, context, progress, file_num)

        progress.Update(100)
        progress.Destroy()

        if not self.file_generate_error:
            wx.MessageBox("合同生成成功", "提示", wx.OK | wx.ICON_INFORMATION)

    def generate_doc(self, file_name, prefix_name, context, progress, file_num):
        progress_value = 80 / file_num
        origin_value = progress.GetValue()
        new_file_name = prefix_name + "_" + file_name
        new_file_name = new_file_name.replace('模板', '')
        msg = "正在生成：" + new_file_name
        try:
            doc = DocxTemplate(file_name)
            progress.Update(origin_value + progress_value * 0.2, msg)
            doc.render(context)
            progress.Update(origin_value + progress_value * 0.6, msg)
            doc.save(new_file_name)
        except BaseException:
            print("file save error in doc")
            self.file_generate_error = True
            wx.MessageBox("文件写如错误，请检查word文件是否关闭，关闭后重试", "提示", wx.OK | wx.ICON_INFORMATION)

        progress.Update(origin_value + progress_value * 0.8, msg)
        time.sleep(0.5)
        self.reset_file_save_path(new_file_name)
        progress.Update(origin_value + progress_value * 1, msg)

    def read_input_text(self, input):
        return input.GetLineText(0)
    def set_input_text(self, input, text):
        input.SetLabelText(str(text))

    def read_choice_text(self, ch):
        return ch.GetString(ch.GetSelection())

    def cal_home_income(self, context):
        # home_income = month_income1 + month_income2
        try:
            month_income1 = float(self.read_input_text(self.month_income1))
            month_income2 = float(self.read_input_text(self.month_income2))
        except BaseException:
            return

        home_income = month_income1 + month_income2
        home_income = int(home_income)
        # context.update({"home_income": str(home_income)})
        self.set_input_text(self.home_income, home_income)


    def cal_house_uint_price(self, context):
        # house_uint_price = house_price / house_area
        try:
            self.cal_paid_house_money(context)
        except BaseException:
            pass

        try:
            house_price = float(self.read_input_text(self.house_price))
            house_area = float(self.read_input_text(self.house_area))
        except BaseException:
            return

        house_uint_price = house_price / house_area
        house_uint_price = round(house_uint_price, 2)
        # context.update({"house_uint_price": str(house_uint_price)})
        self.set_input_text(self.house_uint_price, house_uint_price)

    def cal_paid_house_money(self, context):
        # paid_house_money = house_price * (1 - loan_proportion)
        try:
            house_price = float(self.read_input_text(self.house_price))
            loan_proportion = float(self.read_input_text(self.loan_proportion))
        except BaseException:
            return
        paid_house_money = house_price * (1 - loan_proportion / 10)
        paid_house_money = round(paid_house_money, 2)
        # context.update({"paid_house_money": str(paid_house_money)})
        self.set_input_text(self.paid_house_money, paid_house_money)

    def cal_some_data(self, context):
        # home_income = month_income1 + month_income2
        # house_uint_price = house_price / house_area
        # paid_house_money = house_price * (1 - loan_proportion)
        try:
            month_income1 = float(self.read_input_text(self.month_income1))
            month_income2 = float(self.read_input_text(self.month_income2))

            house_price = float(self.read_input_text(self.house_price))
            house_area = float(self.read_input_text(self.house_area))
            loan_proportion = float(self.read_input_text(self.loan_proportion))
        except BaseException:
            return

        home_income = month_income1 + month_income2
        home_income = int(home_income)

        house_uint_price = house_price / house_area
        house_uint_price = round(house_uint_price, 2)

        paid_house_money = house_price * (1 - loan_proportion / 10)
        paid_house_money = round(paid_house_money, 0)

        # context.update({"home_income": str(home_income)})
        # context.update({"house_uint_price": str(house_uint_price)})
        # context.update({"paid_house_money": str(paid_house_money)})

        self.home_income.SetLabelText(home_income)
        self.house_uint_price.SetLabelText(house_uint_price)
        self.paid_house_money.SetLabelText(paid_house_money)

        print("home_income:", home_income)
        print("house_uint_price:", house_uint_price)
        print("paid_house_money:", paid_house_money)

        pass

    def save_setting(self):
        setting = self.read_setting_file()
        save_path = self.label_set_save_path.GetLabel()
        setting.update({"save_path": save_path})

        with open('setting.ini', 'w', encoding='utf-8') as f:
            json.dump(setting, f)

    def resume_setting(self):
        setting = self.read_setting_file()
        save_path = setting['save_path']
        self.label_set_save_path.SetLabelText(save_path)
        print('set save path:', save_path)

    def read_setting_file(self):
        if not os.path.exists('setting.ini'):
            print('setting.ini is not exist')
            setting = {}
            setting.update({"save_path": os.getcwd()})
            setting.update({"user_date": ''})
            setting.update({"vlts": ''})
            with open('setting.ini', 'w', encoding='utf-8') as f:
                json.dump(setting, f)

        with open('setting.ini', encoding='utf-8') as f:
            setting = json.load(f)
            print('load file setting.ini')
            return setting

    def clear_input_data(self, e):
        input_arr = self.input_data_arr
        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            read_command = 'self.set_input_text(self.' + input_arr[index] + ', "")'
            # self.set_input_text(self.borrower_name1, '')
            eval(read_command)

        pass

    def save_user_data(self, e):
        input_arr = self.input_data_arr
        choice_arr = self.choice_data_arr
        context = {
            # 'borrower_name1': borrower_name1
        }

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            read_command = 'self.read_input_text(self.' + input_arr[index] + ')'
            context.update({input_arr[index]: eval(read_command)})

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(choice_arr)):
            read_command = 'self.read_choice_text(self.' + choice_arr[index] + ')'
            context.update({choice_arr[index]: eval(read_command)})

        setting = self.read_setting_file()
        save_path = self.label_set_save_path.GetLabel()
        setting.update({"save_path": save_path})
        setting.update({"user_date": context})

        with open('setting.ini', 'w', encoding='utf-8') as f:
            json.dump(setting, f)
        print("save all data")

        self.save_single_user_data_to_foler(context)
        pass

    def save_single_user_data_to_foler(self, data):
        data_save = {}
        data_save.update({"user_date": data})

        path = os.getcwd()
        data_folder = os.path.join(path, 'data')
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

        borrower_name = self.read_input_text(self.borrower_name1) + '.ini'
        file_name = os.path.join(data_folder, borrower_name)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data_save, f)

    def resume_selected_user_data(self, e):
        filesFilter = "Data (*.ini)|*.ini"

        path = os.getcwd()
        data_folder = os.path.join(path, 'data')
        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

        dir = os.path.join(os.getcwd(), 'data')
        fileDialog = wx.FileDialog(self, message="选择单个文件",defaultDir=dir, wildcard=filesFilter, style=wx.FD_OPEN)

        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return

        path = fileDialog.GetPath()
        print('select resume file is:', path)

        with open(path, encoding='utf-8') as f:
            setting = json.load(f)
            if setting == None:
                return

            context = setting['user_date']
            if context == None :
                return

            input_arr = self.input_data_arr
            choice_arr = self.choice_data_arr

            # eval(): 将字符串转成成表达式计算，并返回结果
            for index in range(len(input_arr)):
                value = eval("context['" + input_arr[index] + "']")
                set_command = 'self.' + input_arr[index] + '.SetLabelText("' + value + '")'
                eval(set_command)

            for index in range(len(choice_arr)):
                value = eval("context['" + choice_arr[index] + "']")
                set_command = 'self.' + choice_arr[index] + '.SetStringSelection("' + value + '")'
                eval(set_command)
        pass

    def resume_last_data(self, e):
        setting = self.read_setting_file()
        print('load file setting.ini')

        save_path = setting['save_path']
        self.label_set_save_path.SetLabelText(save_path)

        context = setting['user_date']
        if context == None :
            return

        input_arr = self.input_data_arr
        choice_arr = self.choice_data_arr

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            value = eval("context['" + input_arr[index] + "']")
            set_command = 'self.' + input_arr[index] + '.SetLabelText("' + value + '")'
            eval(set_command)

        for index in range(len(choice_arr)):
            value = eval("context['" + choice_arr[index] + "']")
            set_command = 'self.' + choice_arr[index] + '.SetStringSelection("' + value + '")'
            eval(set_command)
        pass

def main():
    app = wx.App()
    ex = MyFrame(None, title=app_title)
    ex.Show()
    ex.check_app_valid()
    app.MainLoop()


if __name__ == '__main__':
    main()
