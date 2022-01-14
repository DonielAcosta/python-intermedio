def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firsname": "Doniel", "lastname": "Acosta"}

    super_list = [
        {"firsname":"Doniel", "lastname": "Acosta"},
        {"firsname":"Miguel", "lastname": "Villamizar"},
        {"firsname":"Lina", "lastname": "Sanchez"},
        {"firsname":"Ruben", "lastname": "Garcia"},
        {"firsname":"Julian", "lastname": "Avendaño"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 3],
        "floating_nums": [1.1, 4.5, 6.5]
    }


    for key, value in super_dict.items():
        print(key, "-", value )


if __name__ == '__main__':
    run()