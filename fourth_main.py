import gc
import gmpy2
import numpy as np
result = {'sqrt_result_error': 0, 'sqrt_result_float': 0, 'sqrt_result_number': 0,
              'log_result_error': 0, 'log_result_float': 0, 'log_result_number': 0,
              'log10_result_error': 0, 'log10_result_float': 0, 'log10_result_number': 0,
              'log2_result_error': 0, 'log2_result_float': 0, 'log2_result_number': 0}


def sqrt_error_cal(float_value, high_precision_f):
    sqrt_value_l = np.sqrt(float_value)
    str_float1 = f"{sqrt_value_l:.160}"
    sqrt_value_l = gmpy2.mpfr(str_float1)

    sqrt_value_h = gmpy2.sqrt(high_precision_f)
    if str(sqrt_value_l) != 'inf' and str(sqrt_value_l) != '-inf' and str(sqrt_value_h) != 'inf' and str(
            sqrt_value_h) != 'inf' and str(sqrt_value_h) != 'nan' and str(sqrt_value_l) != 'nan':
        error = abs(sqrt_value_l - sqrt_value_h) / (np.spacing(np.float32(float(sqrt_value_h))))
    else:
        error = 0
    return error

def log_error_cal(float_value, high_precision_f):
    log_value_l = np.log(float_value)
    str_float1 = f"{log_value_l:.160f}"
    log_value_l = gmpy2.mpfr(str_float1)

    log_value_h = gmpy2.log(high_precision_f)
    if str(log_value_l) != 'inf' and str(log_value_l) != '-inf' and str(
            log_value_h) != 'inf' and str(log_value_h) != 'inf' and str(
        log_value_h) != 'nan' and str(log_value_l) != 'nan':
        error = abs(log_value_l - log_value_h) / (np.spacing(np.float32(float(log_value_h))))
    else:
        error = 0
    return error


def log2_error_cal(float_value, high_precision_f):
    log2_value_l = np.log2(float_value)
    str_float1 = f"{log2_value_l:.160f}"
    log2_value_l = gmpy2.mpfr(str_float1)

    log2_value_h = gmpy2.log2(high_precision_f)
    if str(log2_value_l) != 'inf' and str(log2_value_l) != '-inf' and str(
            log2_value_h) != 'inf' and str(log2_value_h) != 'inf' and str(
        log2_value_h) != 'nan' and str(log2_value_l) != 'nan':
        error = abs(log2_value_l - log2_value_h) / (np.spacing(np.float32(float(log2_value_h))))
    else:
        error = 0
    return error

def log10_error_cal(float_value, high_precision_f):
    log10_value_l = np.log10(float_value)
    str_float1 = f"{log10_value_l:.160f}"
    log10_value_l = gmpy2.mpfr(str_float1)

    log10_value_h = gmpy2.log10(high_precision_f)
    if str(log10_value_l) != 'inf' and str(log10_value_l) != '-inf' and str(
            log10_value_h) != 'inf' and str(log10_value_h) != 'inf' and str(
        log10_value_h) != 'nan' and str(log10_value_l) != 'nan':
        error = abs(log10_value_l - log10_value_h) / (np.spacing(np.float32(float(log10_value_h))))
    else:
        error = 0
    return error


def test_sqrt(x=0):
    global result
    print("start to test mathematical function")
    gmpy2.get_context().precision = 128
    print("start in loop")

    # loop all positive float point
    for loop_value in range(x, 2147483647, 10):
        gc.collect()

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.50f}"
        if loop_value % (2147483) == 0:
            print(loop_value)
            write_file(loop_value)
            print()

        if str_float == 'nan' or str_float == '-inf' or str_float == 'inf' or str_float == '+inf':
            continue
        str_float = f"{float_value:.160}"
        high_precision_f = gmpy2.mpfr(str_float)
        # float_value     high_precision_f

        # sqrt function evaluate part
        error = sqrt_error_cal(float_value, high_precision_f)
        if result['sqrt_result_error'] < error:
            result['sqrt_result_error'] = error
            result['sqrt_result_float'] = float_value
            result['sqrt_result_number'] = loop_value

        # log function evaluate part
        error = log_error_cal(float_value, high_precision_f)
        if result['log_result_error'] < error:
            result['log_result_error'] = error
            result['log_result_float'] = float_value
            result['log_result_number'] = loop_value

        # log2 function evaluate part
        error = log2_error_cal(float_value, high_precision_f)
        if result['log2_result_error'] < error:
            result['log2_result_error'] = error
            result['log2_result_float'] = float_value
            result['log2_result_number'] = loop_value

        gc.collect()

        # log10 function evaluate part
        error = log10_error_cal(float_value, high_precision_f)
        if result['log10_result_error'] < error:
            result['log10_result_error'] = error
            result['log10_result_float'] = float_value
            result['log10_result_number'] = loop_value

def write_file(x):
    global result
    with open('fourth_main/example7.txt', 'w') as f:
        f.write(f'The data compute : {x}\n\n')

        # write sqrt data
        f.write(f'sqrt_result_error: {result["sqrt_result_error"]}\n')
        f.write(f'sqrt_result_float: {result["sqrt_result_float"]}\n')
        f.write(f'sqrt_result_number: {result["sqrt_result_number"]}\n\n')

        # write log data
        f.write(f'log_result_error: {result["log_result_error"]}\n')
        f.write(f'log_result_float: {result["log_result_float"]}\n')
        f.write(f'log_result_number: {result["log_result_number"]}\n\n')

        # write log10 data
        f.write(f'log10_result_error: {result["log10_result_error"]}\n')
        f.write(f'log10_result_float: {result["log10_result_float"]}\n')
        f.write(f'log10_result_number: {result["log10_result_number"]}\n\n')

        # write log2 data
        f.write(f'log2_result_error: {result["log2_result_error"]}\n')
        f.write(f'log2_result_float: {result["log2_result_float"]}\n')
        f.write(f'log2_result_number: {result["log2_result_number"]}\n\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_sqrt(x=1954209530)
    print("end of the loop")
    print("start to write the result in file")
    write_file("all thing done")
