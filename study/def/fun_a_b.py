def fun_b():
    print("_2_")


def fun_a():
    print("_1_")
    fun_b()
    print("_3_")


fun_a()
