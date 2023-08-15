from json import dump, load


class JSUtils(object):
    @staticmethod
    def scroll_to_the_bottom(driver):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


class DataUtils(object):
    @staticmethod
    def get_data(file):
        with open(file) as f:
            return load(f)

    @staticmethod
    def save_info_to_json(items_info_file_path, first_item_info, second_item_info):
        with open(items_info_file_path, "w") as f:
            dump([first_item_info, second_item_info], f, indent=4)
