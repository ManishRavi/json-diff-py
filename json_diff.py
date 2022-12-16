from collections import defaultdict
from deepdiff import DeepDiff

import json


class JSONDiff:
    def __init__(self) -> None:
        """Initializes the instance variables."""
        self.object_1 = {}
        self.object_2 = {}
        self.DISPLAY_MAP = {
            "incorrect_types_count": "incorrect type(s)",
            "unequal_values_count": "unequal value(s)",
            "missing_properties_count": "missing propertie(s)",
            "total_diff_count": "difference(s) found",
        }

    def compare(self, file_1_path: str, file_2_path: str) -> None:
        """Compares the two files and prints the feature specific difference counts."""
        self.load_json_files(file_1_path, file_2_path)
        deep_diff_result_map = DeepDiff(self.object_2, self.object_1)
        final_result_map = defaultdict(int)

        # * Count the values.
        for key in deep_diff_result_map:
            final_result_map["total_diff_count"] += len(deep_diff_result_map[key])
            # print(key, len(deep_diff_result_map[key]))
            if key == "type_changes":
                final_result_map["incorrect_types_count"] += len(
                    deep_diff_result_map[key]
                )
            elif key == "values_changed":
                final_result_map["unequal_values_count"] += len(
                    deep_diff_result_map[key]
                )
            else:
                final_result_map["missing_properties_count"] += len(
                    deep_diff_result_map[key]
                )

        # * Prints the results.
        for key, value in final_result_map.items():
            print(f"{value} {self.DISPLAY_MAP[key]}")

    def load_json_files(self, file_1_path: str, file_2_path: str) -> None:
        """Reads the files and loads the JSON object into the instance variables."""
        file_1 = open(file_1_path, "r")
        file_2 = open(file_2_path, "r")
        self.object_1 = json.loads(file_1.read())
        self.object_2 = json.loads(file_2.read())
