import math
import numpy as np
import gmpy2
import gc

# float 64- 64 / float 32 ulp
result = {'sin_result_error': 0, 'sin_result_float': 0, 'sin_result_number': 0,
          'cos_result_error': 0, 'cos_result_float': 0, 'cos_result_number': 0,
          'tan_result_error': 0, 'tan_result_float': 0, 'tan_result_number': 0}

def sin_error_cal(float_value, high_precision_f):
    sin_value_l = np.sin(float_value)
    str_float1 = f"{sin_value_l:.160f}"
    sin_value_l = gmpy2.mpfr(str_float1)

    sin_value_h = gmpy2.sin(high_precision_f)
    error = abs(sin_value_l - sin_value_h) / (np.spacing(np.float32(float(sin_value_h))))
    return error

def cos_error_cal(float_value, high_precision_f):
    cos_value_l = np.cos(float_value)
    str_float1 = f"{cos_value_l:.160f}"
    cos_value_l = gmpy2.mpfr(str_float1)

    cos_value_h = gmpy2.cos(high_precision_f)
    error = abs(cos_value_l - cos_value_h) / (np.spacing(np.float32(float(cos_value_h))))
    return error

def tan_error_cal(float_value, high_precision_f):
    tan_value_l = np.tan(float_value)
    str_float1 = f"{tan_value_l:.160f}"
    tan_value_l = gmpy2.mpfr(str_float1)

    tan_value_h = gmpy2.tan(high_precision_f)
    error = abs(tan_value_l - tan_value_h) / (np.spacing(np.float32(float(tan_value_h))))
    return error

def test_sin_cos_tan(start=0, bound=2147483647):
    print("start to test sin cos tan mathematical function")
    print("start in loop")
    gmpy2.get_context().precision = 128
    global result

    for loop_value in range(start, bound, 10):
        gc.collect()

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.160f}"
        high_precision_f = gmpy2.mpfr(str_float)

        if high_precision_f > 2 * math.pi:
            break
        if loop_value % (2147483) == 0:
            print(loop_value)
            print()
            write_file(loop_value)

        # sin function evaluate part
        error = sin_error_cal(float_value, high_precision_f)
        if result['sin_result_error'] < error:
            result['sin_result_error'] = error
            result['sin_result_float'] = float_value
            result['sin_result_number'] = loop_value

        # cos function evaluate part
        error = cos_error_cal(float_value, high_precision_f)
        if result['cos_result_error'] < error:
            result['cos_result_error'] = error
            result['cos_result_float'] = float_value
            result['cos_result_number'] = loop_value

        # tan function evaluate part
        if high_precision_f <= math.pi:
            error = tan_error_cal(float_value, high_precision_f)
            if result['tan_result_error'] < error:
                result['tan_result_error'] = error
                result['tan_result_float'] = float_value
                result['tan_result_number'] = loop_value


def write_file(x):
    global result
    with open('first_main/example3.txt', 'w') as f:
        # Write the computed data
        f.write(f'The data compute: {x}\n\n')
        
        # Write sin data
        f.write(f'sin_result_error: {result["sin_result_error"]}\n')
        f.write(f'sin_result_float: {result["sin_result_float"]}\n')
        f.write(f'sin_result_number: {result["sin_result_number"]}\n\n')

        # Write cos data
        f.write(f'cos_result_error: {result["cos_result_error"]}\n')
        f.write(f'cos_result_float: {result["cos_result_float"]}\n')
        f.write(f'cos_result_number: {result["cos_result_number"]}\n\n')

        # Write tan data
        f.write(f'tan_result_error: {result["tan_result_error"]}\n')
        f.write(f'tan_result_float: {result["tan_result_float"]}\n')
        f.write(f'tan_result_number: {result["tan_result_number"]}\n')


if __name__ == '__main__':
    test_sin_cos_tan(730144220, 2147483647)
    print("end of the loop")
    print("start to write the result in file")
    write_file("all things done")
