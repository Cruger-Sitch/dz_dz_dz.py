
from __future__ import annotations

from  abc import  abstractmethod

class Musicl_group:
    def __init__(self, filename: str):
        self.__musicls: dict[str, str] = Musicl_group.__from_file(filename)

    @staticmethod
    def __from_file(filename: str) -> dict[str, str]:
        musicls: dict[str, str] = {}

        with open(filename, 'r', encoding='utf-8') as f:
            lines: list[str] = f.readlines()
            for line in lines:
                group_name, album_name = [item.strip() for  item in line.split(' ')]
                musicls[group_name] = album_name

        return  musicls

    def to_file(self, filename) -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines([f'{group_name} {album_name}\n' for group_name, album_name in self.__musicls.items()])

    def add(self, group: [str,str]):
        group_name, album_name = group
        self.__musicls[group_name] = album_name

    def remove(self, group_name: str):
        del self.__musicls[group_name]

    def find(self, group_name: str) -> str:
        return self.__musicls[group_name]

    def __str__(self) -> str:
        return  str(self.__musicls)



cm = Musicl_group('musicls.txt')
cm.add(('ДДТ', 'Просвистела'))
print(cm)
cm.to_file('c2.txt')


