import analysis_file_system as afs

directory = r'D:\Education\Python\Dipping\Seminars\Seminar_8\test'
afs.get_dir_size(directory)
afs.traverse_directory(directory)
afs.save_results_to_csv(directory)
afs.save_results_to_json(directory)
afs.save_results_to_pickle(directory)
