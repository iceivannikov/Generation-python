def road(d_1, d_2, d_3):
    r_1 = d_1 + d_2 + d_3
    r_2 = 2 * d_1 + 2 * d_2
    r_3 = d_1 * 2 + d_3 * 2
    r_4 = d_2 * 2 + d_3 * 2
    return min(r_1, r_2, r_3, r_4)

if __name__ == "__main__":
    print(road(10, 20, 30))
    print(road(10, 10, 45))
    print(road(100, 33, 34))