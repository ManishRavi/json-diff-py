from json_diff import JSONDiff


json_diff_obj = JSONDiff()
json_diff_obj.compare("./resources/file_1.json", "./resources/file_2.json")
