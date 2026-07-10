def spell(*args):
    res = {}
    for arg in args:
        key = arg[0].lower()
        res[key] = max(res.get(key, 0), len(arg))
    return res

if __name__ == "__main__":
    print(spell('россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН'))
    print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
    print(spell('fruit', 'football', 'February', 'forest', 'Family'))
