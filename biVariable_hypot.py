import gc
import random
import gmpy2
import numpy as np

width = 0
result = {'hypot_result_error': 0, 'hypot_result_float1': 0, 'hypot_result_float2': 0, 'hypot_result_number1': 0,
          'hypot_result_number2': 0}


def hypot_error_cal(first_pa, second_pa, first_pa_high, second_pa_high):
    result_h = np.hypot(first_pa, second_pa)
    str_float1 = f"{result_h:.160f}"
    result_h = gmpy2.mpfr(str_float1)

    result_h_high = gmpy2.hypot(first_pa_high, second_pa_high)
    if str(result_h) != 'inf' and str(result_h) != '-inf' and str(result_h_high) != 'inf' and str(
            result_h_high) != 'inf' and str(result_h_high) != 'nan' and str(result_h) != 'nan':
        error_h = abs(result_h - result_h_high) / (np.spacing(np.float32(float(result_h_high))))
    else:
        error_h = 0
    return error_h


# randomly choose threshold number of value between 'lower' and 'upper' to find the largest error
def test_bi(lower_bound=0, upper_bound=9223372036854775807, threshold=100000000):
    global result
    print("start to test mathematical function")
    print("start in loop")
    if lower_bound == upper_bound:
        return 0
    largest_error_h = 0

    for loop_positive in range(0, threshold, 1):
        random_int = random.randint(lower_bound, upper_bound)
        string_value = str(bin(random_int))

        first_pa = 0
        integer_first = 0
        first_pa_high = 0

        if string_value[0] == '0':
            if len(string_value) > 34:
                string_first = string_value[2:-32]
                integer_first = int(string_first, 2)

                first_pa = np.int32(integer_first).view(np.float32)

                str_float = f"{first_pa:.160f}"
                first_pa_high = gmpy2.mpfr(str_float)

                string_second = string_value[-31:]
                integer_second = int(string_second, 2)
                second_pa = np.int32(integer_second).view(np.float32)
                if string_value[-32] == '1':
                    second_pa = -second_pa

                str_float = f"{second_pa:.160f}"
                second_pa_high = gmpy2.mpfr(str_float)
            else:
                string_second = string_value[2:]
                integer_second = int(string_second, 2)
                second_pa = np.int32(integer_second).view(np.float32)

                str_float = f"{second_pa:.160f}"
                second_pa_high = gmpy2.mpfr(str_float)
        else:
            if len(string_value) > 35:
                string_first = string_value[3:-32]
                integer_first = int(string_first, 2)

                first_pa = np.int32(integer_first).view(np.float32)
                first_pa = -first_pa

                str_float = f"{first_pa:.160f}"
                first_pa_high = gmpy2.mpfr(str_float)

                string_second = string_value[-31:]
                integer_second = int(string_second, 2)
                second_pa = np.int32(integer_second).view(np.float32)
                if string_value[-32] == '1':
                    second_pa = -second_pa

                str_float = f"{second_pa:.160f}"
                second_pa_high = gmpy2.mpfr(str_float)
            else:
                string_second = string_value[3:]
                integer_second = int(string_second, 2)
                second_pa = np.int32(integer_second).view(np.float32)

                str_float = f"{second_pa:.160f}"
                second_pa_high = gmpy2.mpfr(str_float)

        str_float = f"{first_pa:.50f}"
        str_float1 = f"{second_pa:.50f}"
        if str_float == 'nan' or str_float == '-inf' or str_float == 'inf' or str_float == '+inf' \
                or str_float1 == 'nan' or str_float1 == '-inf' or str_float1 == 'inf' or str_float1 == '+inf':
            loop_positive -= 1
            continue

        error_h = hypot_error_cal(first_pa, second_pa, first_pa_high, second_pa_high)
        if largest_error_h < error_h:
            largest_error_h = error_h
        if result['hypot_result_error'] < error_h:
            result['hypot_result_error'] = error_h
            result['hypot_result_float1'] = first_pa
            result['hypot_result_float2'] = second_pa
            result['hypot_result_number1'] = integer_first
            result['hypot_result_number2'] = integer_second
        gc.collect()
    return largest_error_h


def controller(lower, upper):
    stra = "  interval :" + str(lower) + "  to  " + str(upper)
    write_file(stra)

    global width
    global result

    middle_value = (lower + upper) / 2

    if upper - lower <= width or middle_value == lower or middle_value == upper:
        return

    error_h_first = 0
    error_h_second = 0
    try:
        error_h_first = test_bi(lower_bound=lower, upper_bound=middle_value)
        error_h_second = test_bi(lower_bound=middle_value, upper_bound=upper)
    except Exception as e:
        print("lower vound:   " + str(lower))
        print("middle value :   " + str(middle_value))
        print("upper bound :   " + str(upper))
        print(e)

    width += 1
    gc.collect()
    if error_h_first > error_h_second:
        controller(lower, middle_value)
    else:
        controller(middle_value, upper)

def write_file(x):
    global result
    with open('bivariable_hypot/part1.txt', 'w') as f:
        f.write(f'The data compute : {x}\n\n')

        # write hypot data
        f.write(f'hypot_result_error: {result["hypot_result_error"]}\n')
        f.write(f'hypot_result_float1: {result["hypot_result_float1"]}\n')
        f.write(f'hypot_result_float2: {result["hypot_result_float2"]}\n')
        f.write(f'hypot_result_number1: {result["hypot_result_number1"]}\n')
        f.write(f'hypot_result_number2: {result["hypot_result_number2"]}\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gmpy2.get_context().precision = 128

    controller(lower=0, upper=9223372036854775807)
    gc.collect()

    controller(lower=-9223372036854775807, upper=0)
    gc.collect()

    print("end of the loop")
    print("start to write the result in file")
    write_file("all thing done")

