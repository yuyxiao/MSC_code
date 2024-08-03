import gc
import gmpy2
import numpy as np

result = {'arccosh_result_error': 0, 'arccosh_result_float': 0, 'arccosh_result_number': 0,
          'log1p_result_error': 0, 'log1p_result_float': 0, 'log1p_result_number': 0}

def log1p_error_cal(float_value, high_precision_f):
    log1p_value_l = np.log1p(float_value)
    str_float1 = f"{log1p_value_l:.160f}"
    log1p_value_l = gmpy2.mpfr(str_float1)

    log1p_value_h = gmpy2.log1p(high_precision_f)
    if str(log1p_value_l) != 'inf' and str(log1p_value_l) != '-inf' and str(
            log1p_value_h) != 'inf' and str(log1p_value_h) != 'inf' and str(
        log1p_value_h) != 'nan' and str(log1p_value_l) != 'nan':
        error = abs(log1p_value_l - log1p_value_h) / (np.spacing(np.float32(float(log1p_value_h))))
    else:
        error = 0
    return error

def arccosh_error_cal(float_value, high_precision_f):
    arccosh_value_l = np.arccosh(float_value)
    str_float1 = f"{arccosh_value_l:.160f}"
    arccosh_value_l = gmpy2.mpfr(str_float1)

    arccosh_value_h = gmpy2.acosh(high_precision_f)
    if str(arccosh_value_l) != 'inf' and str(arccosh_value_l) != '-inf' and str(
            arccosh_value_h) != 'inf' and str(arccosh_value_h) != 'inf' and str(
            arccosh_value_h) != 'nan' and str(arccosh_value_l) != 'nan':
        error = abs(arccosh_value_l - arccosh_value_h) / (np.spacing(np.float32(float(arccosh_value_h))))
    else:
        error = 0
    return error

def test_all_possible(lower_nagetive=-1082130432, upper_nagetive=2147483647):
    print("start to test mathematical function")
    global result
    print("start in loop")
    gmpy2.get_context().precision = 128

    # loop for all nagetive float point
    for loop_value in range(lower_nagetive, upper_nagetive, 10):
        gc.collect()

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.50f}"

        if loop_value % (2147483) == 0:
            print(loop_value)
            write_file(loop_value)
            print()

        if str_float == 'nan' or str_float == '-inf' or str_float == 'inf' or str_float == '+inf':
            continue

        str_float = f"{float_value:.160f}"
        high_precision_f = gmpy2.mpfr(str_float)
        # float_value     high_precision_f

        # log1p function evaluate part
        error = log1p_error_cal(float_value, high_precision_f)
        if result['log1p_result_error'] < error:
            result['log1p_result_error'] = error
            result['log1p_result_float'] = float_value
            result['log1p_result_number'] = loop_value

        if loop_value > 1065353216:
            # arccosh function evaluate part
            error = arccosh_error_cal(float_value, high_precision_f)
            if result['arccosh_result_error'] < error:
                result['arccosh_result_error'] = error
                result['arccosh_result_float'] = float_value
                result['arccosh_result_number'] = loop_value
def write_file(x):
    global result

    with open('fifth_main/example6.txt', 'w') as f:
        f.write(f'The data compute : {x}\n\n')
        # write arccosh data
        f.write(f'arccosh_result_error: {result["arccosh_result_error"]}\n')
        f.write(f'arccosh_result_float: {result["arccosh_result_float"]}\n')
        f.write(f'arccosh_result_number: {result["arccosh_result_number"]}\n\n')

        # write log1p data
        f.write(f'log1p_result_error: {result["log1p_result_error"]}\n')
        f.write(f'log1p_result_float: {result["log1p_result_float"]}\n')
        f.write(f'log1p_result_number: {result["log1p_result_number"]}\n\n')

if __name__ == '__main__':
    np.seterr(over='ignore')
    test_all_possible(lower_nagetive=1795295788, upper_nagetive=2147483647)
    gc.collect()
    print("end of the loop")
    print("start to write the result in file")
    write_file("all thing done")
