import os


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range):
    file_list = os.listdir("test_folder")

    counter = 1
    for filename in file_list:
        if filename.endswith("." + source_ext):
            original_name = filename[name_range[0] - 1: name_range[1]]
            new_name = f"{desired_name}{original_name}_{counter:0{num_digits}}.{target_ext}"
            os.rename(os.path.join("test_folder", filename),
                      os.path.join("test_folder", new_name))
            counter += 1


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=3, source_ext="jpeg",
                 target_ext="doc", name_range=[1, 4])
