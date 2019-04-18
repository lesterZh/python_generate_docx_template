import os
import time
import json
from datetime import datetime
from datetime import timedelta
import base64

class GSetting:
    def get_setting_file_name(self):
        set_path = os.path.join(os.path.expanduser('~'), 'word')
        if not os.path.exists(set_path):
            os.mkdir(set_path)

        set_file = os.path.join(set_path, 'setting.ini')
        return 'setting.ini'

    def get_day_after(self, d):
        now = datetime.now()
        delta = timedelta(days=d)
        n_days = now + delta
        print("return:", n_days.strftime('%Y-%m-%d %H:%M:%S'))
        return n_days.strftime('%Y-%m-%d %H:%M:%S')

    def encode_str_base64(self, encode_str):
        encode_date = base64.b64encode(encode_str.encode('utf-8'))
        ret = str(encode_date, 'utf-8')
        print('you get date encode:' + ret)
        return ret

    def generate_setting_file(self, input_day):
        if not os.path.exists(self.get_setting_file_name()):
            print('setting.ini is not exist, create it')
            setting = {}
            setting.update({"save_path": os.path.join(os.path.expanduser("~"), 'Desktop')})
            setting.update({"user_date": ''})
            setting.update({"vlts": ''})
            with open(self.get_setting_file_name(), 'w', encoding='utf-8') as f:
                json.dump(setting, f)

        with open(self.get_setting_file_name(),  encoding='utf-8') as f:
            print('load file setting.ini')
            self.setting = json.load(f)
            valid_date = self.encode_str_base64(self.get_day_after(input_day))
            self.setting.update({"vlts": valid_date})

        with open(self.get_setting_file_name(), 'w', encoding='utf-8') as f:
            json.dump(self.setting, f)
            print('rewrite setting.ini')

if __name__ == '__main__':

    name = input("enter name:")
    pw = input("enter pw:")
    if not (name == 'zht' and pw == '17760028696'):
        print('input wrong')
        exit(0)

    day = input("enter day:")
    generate_set = GSetting()
    generate_set.generate_setting_file(float(day))