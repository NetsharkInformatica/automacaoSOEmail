from pathlib import Path

root_dir= Path('dados')

file_path=root_dir.iterdir()

#print(list(file_path))
for path in file_path:
    new_filename=f'new-{path.stem}{path.suffix}'
    print(new_filename)
    new_filepath=path.with_name(new_filename)
    path.rename(new_filename)
    
    