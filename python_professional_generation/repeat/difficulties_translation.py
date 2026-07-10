def difficulties_translation():
    n = int(input()) - 1
    st = set(input().split(", "))
    for _ in range(n):
        st &= set(input().split(", "))
    if st:
        return ", ".join(sorted(st))
    else:
        return "Сериал снять не удастся"


if __name__ == "__main__":
    print(difficulties_translation())