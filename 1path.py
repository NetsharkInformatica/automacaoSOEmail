from pathlib import Path

p1= Path('dados','arquivo.txt')

print(p1)

if p1.exists():
    with open(p1, 'r',encoding='utf-8') as file:
        print(file.read())
        