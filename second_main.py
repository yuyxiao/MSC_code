import gc
import numpy as np
import gmpy2

result = {'arcsin_result_error': 0, 'arcsin_result_float': 0, 'arcsin_result_number': 0,
          'arccos_result_error': 0, 'arccos_result_float': 0, 'arccos_result_number': 0,
          'arctanh_result_error': 0, 'arctanh_result_float': 0, 'arctanh_result_number': 0}

def arcsin_error_cal(float_value, high_precision_f):
    arcsin_value_l = np.arcsin(float_value)
    str_float1 = f"{arcsin_value_l:.160f}"
    arcsin_value_l = gmpy2.mpfr(str_float1)

    arcsin_value_h = gmpy2.asin(high_precision_f)
    error = abs(arcsin_value_l - arcsin_value_h) / (np.spacing(np.float32(float(arcsin_value_h))))
    return error

def arccos_error_cal(float_value, high_precision_f):
    arccos_value_l = np.arccos(float_value)
    str_float1 = f"{arccos_value_l:.160f}"
    arccos_value_l = gmpy2.mpfr(str_float1)

    arccos_value_h = gmpy2.acos(high_precision_f)
    error = abs(arccos_value_l - arccos_value_h) / (np.spacing(np.float32(float(arccos_value_h))))
    return error


def arctanh_error_cal(float_value, high_precision_f):
    arctanh_value_l = np.arctanh(float_value)
    str_float1 = f"{arctanh_value_l:.160f}"
    arctanh_value_l = gmpy2.mpfr(str_float1)

    arctanh_value_h = gmpy2.atanh(high_precision_f)
    if str(arctanh_value_l) != 'inf' and str(arctanh_value_l) != '-inf' and str(
            arctanh_value_h) != 'inf' and str(arctanh_value_h) != 'inf' and str(
        arctanh_value_h) != 'nan' and str(arctanh_value_l) != 'nan':
        error = abs(arctanh_value_l - arctanh_value_h) / (np.spacing(np.float32(float(arctanh_value_h))))
    else:
        error = 0
    return error

def test_arc_sin_cos_tan(ne_lower=-1082130432, ne_upper=-2147483648, po_lower=0, po_upper=1065353216):
    print("start to test arcsin arccos arctanh mathematical function")
    gmpy2.get_context().precision = 128

    print("start in loop")
    global result

    # from -1 to 0
    for loop_value in range(ne_lower, ne_upper, -10):
        gc.collect()

        if loop_value % (-2147483) == 0:
            print(loop_value)
            print()
            write_file(loop_value, 0)

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.160f}"
        high_precision_f = gmpy2.mpfr(str_float)

        # arcsin function evaluate part
        error = arcsin_error_cal(float_value, high_precision_f)
        if result['arcsin_result_error'] < error:
            result['arcsin_result_error'] = error
            result['arcsin_result_float'] = float_value
            result['arcsin_result_number'] = loop_value

        # arccos function evaluate part
        error = arccos_error_cal(float_value, high_precision_f)
        if result['arccos_result_error'] < error:
            result['arccos_result_error'] = error
            result['arccos_result_float'] = float_value
            result['arccos_result_number'] = loop_value

        # arctanh function evaluate part
        error = arctanh_error_cal(float_value, high_precision_f)
        if result['arctanh_result_error'] < error:
            result['arctanh_result_error'] = error
            result['arctanh_result_float'] = float_value
            result['arctanh_result_number'] = loop_value

    # from 0 to +1
    for loop_value in range(po_lower, po_upper, 10):
        gc.collect()

        if loop_value % (1065353) == 0:
            print(loop_value)
            print()
            write_file("all things done", loop_value)

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.160f}"
        high_precision_f = gmpy2.mpfr(str_float)

        # arcsin function evaluate part
        error = arcsin_error_cal(float_value, high_precision_f)
        if result['arcsin_result_error'] < error:
            result['arcsin_result_error'] = error
            result['arcsin_result_float'] = float_value
            result['arcsin_result_number'] = loop_value

        # arccos function evaluate part
        error = arccos_error_cal(float_value, high_precision_f)
        if result['arccos_result_error'] < error:
            result['arccos_result_error'] = error
            result['arccos_result_float'] = float_value
            result['arccos_result_number'] = loop_value

        # arctanh function evaluate part
        error = arctanh_error_cal(float_value, high_precision_f)
        if result['arctanh_result_error'] < error:
            result['arctanh_result_error'] = error
            result['arctanh_result_float'] = float_value
            result['arctanh_result_number'] = loop_value

def write_file(negative, positive):
    global result
    with open('second_main/example5.txt', 'w') as f:
        f.write(f'The data compute negative : {negative}\n\n')
        f.write(f'The data compute positive : {positive}\n\n')

        # write arcsin data
        f.write(f'arcsin_result_error: {result["arcsin_result_error"]}\n')
        f.write(f'arcsin_result_float: {result["arcsin_result_float"]}\n')
        f.write(f'arcsin_result_number: {result["arcsin_result_number"]}\n\n')

        # write arccos data
        f.write(f'arccos_result_error: {result["arccos_result_error"]}\n')
        f.write(f'arccos_result_float: {result["arccos_result_float"]}\n')
        f.write(f'arccos_result_number: {result["arccos_result_number"]}\n\n')

        # write arctanh data
        f.write(f'arctanh_result_error: {result["arctanh_result_error"]}\n')
        f.write(f'arctanh_result_float: {result["arctanh_result_float"]}\n')
        f.write(f'arctanh_result_number: {result["arctanh_result_number"]}\n\n')

if __name__ == '__main__':
# -1146755922
# -1791000822
    test_arc_sin_cos_tan(ne_lower=-2147483648, ne_upper=-2147483648, po_lower=990778290, po_upper=1065353216)

    print("end of the loop")
    print("start to write the result in file")
    write_file("all things done", "all things done")
