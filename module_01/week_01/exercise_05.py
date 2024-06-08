def calculate_mdre(y, y_hat, n, p):
    root_diff = (y ** (1/n)) - (y_hat ** (1/n))
    md_nre = root_diff ** p
    print(f'MDnRE: {md_nre}')
    return md_nre


calculate_mdre(100, 99.5, 2, 1)
calculate_mdre(50, 49.5, 2, 1)
calculate_mdre(20, 19.5, 2, 1)
calculate_mdre(0.6, 0.1, 2, 1)
