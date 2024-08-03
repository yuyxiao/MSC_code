import gc
import random
import numpy as np
import gmpy2

width = 0
result = {'arctan2_result_error': 0, 'arctan2_result_float1': 0, 'arctan2_result_float2': 0,
          'arctan2_result_number1': 0, 'arctan2_result_number2': 0}

def arctan2_error_cal(first_pa, second_pa, first_pa_high, second_pa_high):
    result_a = np.arctan2(first_pa, second_pa)
    str_float1 = f"{result_a:.160f}"
    result_a = gmpy2.mpfr(str_float1)

    result_a_high = gmpy2.atan2(first_pa_high, second_pa_high)
    if str(result_a) != 'inf' and str(result_a) != '-inf' and str(result_a_high) != 'inf' and str(
            result_a_high) != 'inf' and str(result_a_high) != 'nan' and str(result_a) != 'nan':
        error_a = abs(result_a_high - result_a) / (np.spacing(np.float32(float(result_a_high))))
    else:
        error_a = 0
    return error_a


# randomly choose threshold number of value between 'lower' and 'upper' to find the largest error
def test_bi(lower_bound=0, upper_bound=9223372036854775807, threshold=100000000):
    print("start to test mathematical function")
    print("start in loop")
    global result

    if lower_bound == upper_bound:
        return 0
    largest_error_a = 0

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
        
        error_a = arctan2_error_cal(first_pa, second_pa, first_pa_high, second_pa_high)
        if largest_error_a < error_a:
            largest_error_a = error_a
        if result['arctan2_result_error'] < error_a:
            result['arctan2_result_error'] = error_a
            result['arctan2_result_float1'] = first_pa
            result['arctan2_result_float2'] = second_pa
            result['arctan2_result_number1'] = integer_first
            result['arctan2_result_number2'] = integer_second

        gc.collect()

    return largest_error_a


def controller(lower, upper):
    stra = " interval :"+ str(lower) + "  to  " + str(upper)
    write_file(stra)

    global width
    global result

    middle_value = (lower + upper) / 2

    if upper - lower <= width or middle_value == upper:
        return

    error_a_first = 0
    error_a_second = 0
    try:
        error_a_first = test_bi(lower_bound=lower, upper_bound=middle_value)
        error_a_second = test_bi(lower_bound=middle_value, upper_bound=upper)
    except Exception as e:
        print("lower bound:   " + str(lower))
        print("middle value :   " + str(middle_value))
        print("upper bound :   " + str(upper))
        print(e)

    width += 1
    gc.collect()
    if error_a_first > error_a_second:
        controller(lower, middle_value)
    else:
        controller(middle_value, upper)

def write_file(x):
    global result
    with open('bivariable_arctan2/part1.txt', 'w') as f:
        f.write(f'The data compute : {x}\n\n')

        # write arctan2 data
        f.write(f'arctan2_result_error: {result["arctan2_result_error"]}\n')
        f.write(f'arctan2_result_float1: {result["arctan2_result_float1"]}\n')
        f.write(f'arctan2_result_float2: {result["arctan2_result_float2"]}\n')
        f.write(f'arctan2_result_number1: {result["arctan2_result_number1"]}\n')
        f.write(f'arctan2_result_number2: {result["arctan2_result_number2"]}\n')


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
