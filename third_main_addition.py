import gc
import gmpy2
import numpy as np

result = {'sinh_result_error': 0, 'sinh_result_float': 0, 'sinh_result_number': 0,
          'cosh_result_error': 0, 'cosh_result_float': 0, 'cosh_result_number': 0,
          'tanh_result_error': 0, 'tanh_result_float': 0, 'tanh_result_number': 0,
          'arcsinh_result_error': 0, 'arcsinh_result_float': 0, 'arcsinh_result_number': 0,
          'arctan_result_error': 0, 'arctan_result_float': 0, 'arctan_result_number': 0,
          'exp_result_error': 0, 'exp_result_float': 0, 'exp_result_number': 0,
          'expm1_result_error': 0, 'expm1_result_float': 0, 'expm1_result_number': 0,
          'exp2_result_error': 0, 'exp2_result_float': 0, 'exp2_result_number': 0,
          'cbrt_result_error': 0, 'cbrt_result_float': 0, 'cbrt_result_number': 0}


def sinh_error_cal(float_value, high_precision_f):
    sinh_value_l = np.sinh(float_value)
    str_float1 = f"{sinh_value_l:.160f}"
    sinh_value_l = gmpy2.mpfr(str_float1)

    sinh_value_h = gmpy2.sinh(high_precision_f)
    if str(sinh_value_l) != 'inf' and str(sinh_value_l) != '-inf' and str(sinh_value_h) != 'inf' and str(
            sinh_value_h) != 'inf' and str(sinh_value_h) != 'nan' and str(sinh_value_l) != 'nan':
        error = abs(sinh_value_l - sinh_value_h) / (np.spacing(np.float32(float(sinh_value_h))))
    else:
        error = 0
    return error

def cosh_error_cal(float_value, high_precision_f):
    cosh_value_l = np.cosh(float_value)
    str_float1 = f"{cosh_value_l:.160f}"
    cosh_value_l = gmpy2.mpfr(str_float1)

    cosh_value_h = gmpy2.cosh(high_precision_f)
    if str(cosh_value_l) != 'inf' and str(cosh_value_l) != '-inf' and str(cosh_value_h) != 'inf' and str(
            cosh_value_h) != 'inf' and str(cosh_value_h) != 'nan' and str(cosh_value_l) != 'nan':
        error = abs(cosh_value_l - cosh_value_h) / (np.spacing(np.float32(float(cosh_value_h))))
    else:
        error = 0
    return error

def tanh_error_cal(float_value, high_precision_f):
    tanh_value_l = np.tanh(float_value)
    str_float1 = f"{tanh_value_l:.160f}"
    tanh_value_l = gmpy2.mpfr(str_float1)

    tanh_value_h = gmpy2.tanh(high_precision_f)
    if str(tanh_value_l) != 'inf' and str(tanh_value_l) != '-inf' and str(tanh_value_h) != 'inf' and str(
            tanh_value_h) != 'inf' and str(tanh_value_h) != 'nan' and str(tanh_value_l) != 'nan':
        error = abs(tanh_value_l - tanh_value_h) / (np.spacing(np.float32(float(tanh_value_h))))
    else:
        error = 0
    return error

def arctan_error_cal(float_value, high_precision_f):
    arctan_value_l = np.arctan(float_value)
    str_float1 = f"{arctan_value_l:.160f}"
    arctan_value_l = gmpy2.mpfr(str_float1)

    arctan_value_h = gmpy2.atan(high_precision_f)
    error = abs(arctan_value_l - arctan_value_h) / (np.spacing(np.float32(float(arctan_value_h))))
    return error

def arcsinh_error_cal(float_value, high_precision_f):
    arcsinh_value_l = np.arcsinh(float_value)
    str_float1 = f"{arcsinh_value_l:.160f}"
    arcsinh_value_l = gmpy2.mpfr(str_float1)

    arcsinh_value_h = gmpy2.asinh(high_precision_f)
    if str(arcsinh_value_l) != 'inf' and str(arcsinh_value_l) != '-inf' and str(arcsinh_value_h) != 'inf' and str(
            arcsinh_value_h) != 'inf' and str(arcsinh_value_h) != 'nan' and str(arcsinh_value_l) != 'nan':
        error = abs(arcsinh_value_l - arcsinh_value_h) / (np.spacing(np.float32(float(arcsinh_value_h))))
    else:
        error = 0
    return error

def exp_error_cal(float_value, high_precision_f):
    exp_value_l = np.exp(float_value)
    str_float1 = f"{exp_value_l:.160f}"
    exp_value_l = gmpy2.mpfr(str_float1)

    exp_value_h = gmpy2.exp(high_precision_f)
    if str(exp_value_l) != 'inf' and str(exp_value_l) != '-inf' and str(exp_value_h) != 'inf' and str(
            exp_value_h) != 'inf' and str(exp_value_h) != 'nan' and str(exp_value_l) != 'nan':
        error = abs(exp_value_l - exp_value_h) / (np.spacing(np.float32(float(exp_value_h))))
    else:
        error = 0
    return error

def cbrt_error_cal(float_value, high_precision_f):
    cbrt_value_l = np.cbrt(float_value)
    str_float1 = f"{cbrt_value_l:.160f}"
    cbrt_value_l = gmpy2.mpfr(str_float1)

    cbrt_value_h = gmpy2.cbrt(high_precision_f)
    if str(cbrt_value_l) != 'inf' and str(cbrt_value_l) != '-inf' and str(cbrt_value_h) != 'inf' and str(
            cbrt_value_h) != 'inf' and str(cbrt_value_h) != 'nan' and str(cbrt_value_l) != 'nan':
        error = abs(cbrt_value_l - cbrt_value_h) / (np.spacing(np.float32(float(cbrt_value_h))))
    else:
        error = 0
    return error

def expm1_error_cal(float_value, high_precision_f):
    expm1_value_l = np.expm1(float_value)
    str_float1 = f"{expm1_value_l:.160f}"
    expm1_value_l = gmpy2.mpfr(str_float1)

    expm1_value_h = gmpy2.expm1(high_precision_f)
    if str(expm1_value_l) != 'inf' and str(expm1_value_l) != '-inf' and str(expm1_value_h) != 'inf' and str(
            expm1_value_h) != 'inf' and str(expm1_value_h) != 'nan' and str(expm1_value_l) != 'nan':
        error = abs(expm1_value_l - expm1_value_h) / (np.spacing(np.float32(float(expm1_value_h))))
    else:
        error = 0
    return error

def exp2_error_cal(float_value, high_precision_f):
    exp2_value_l = np.exp2(float_value)
    str_float1 = f"{exp2_value_l:.160f}"
    exp2_value_l = gmpy2.mpfr(str_float1)

    exp2_value_h = gmpy2.exp2(high_precision_f)
    if str(exp2_value_l) != 'inf' and str(exp2_value_l) != '-inf' and str(exp2_value_h) != 'inf' and str(
            exp2_value_h) != 'inf' and str(exp2_value_h) != 'nan' and str(exp2_value_l) != 'nan':
        error = abs(exp2_value_l - exp2_value_h) / (np.spacing(np.float32(float(exp2_value_h))))
    else:
        error = 0
    return error


def test_all_possible(lower=0, upper=2147483647):
    print("start to test mathematical function")
    gmpy2.get_context().precision = 128

    print("start in loop")
    global result

    # loop all positive float point
    for loop_value in range(lower, upper, 10):
        gc.collect()

        float_value = np.int32(loop_value).view(np.float32)
        str_float = f"{float_value:.50f}"
        if loop_value % (2147483) == 0:
            print(loop_value)
            print()
            write_file(loop_value)

        if str_float == 'nan' or str_float == '-inf' or str_float == 'inf' or str_float == '+inf':
            continue

        str_float = f"{float_value:.160f}"
        high_precision_f = gmpy2.mpfr(str_float)
        # float_value     high_precision_f

        # sinh function evaluate part
        error = sinh_error_cal(float_value, high_precision_f)
        if result['sinh_result_error'] < error:
            result['sinh_result_error'] = error
            result['sinh_result_float'] = float_value
            result['sinh_result_number'] = loop_value

        # cosh function evaluate part
        error = cosh_error_cal(float_value, high_precision_f)
        if result['cosh_result_error'] < error:
            result['cosh_result_error'] = error
            result['cosh_result_float'] = float_value
            result['cosh_result_number'] = loop_value

        # tanh function evaluate part
        error = tanh_error_cal(float_value, high_precision_f)
        if result['tanh_result_error'] < error:
            result['tanh_result_error'] = error
            result['tanh_result_float'] = float_value
            result['tanh_result_number'] = loop_value

        # arctan function evaluate part
        error = arctan_error_cal(float_value, high_precision_f)
        if result['arctan_result_error'] < error:
            result['arctan_result_error'] = error
            result['arctan_result_float'] = float_value
            result['arctan_result_number'] = loop_value

        gc.collect()

        # arcsinh function evaluate part
        error = arcsinh_error_cal(float_value, high_precision_f)
        if result['arcsinh_result_error'] < error:
            result['arcsinh_result_error'] = error
            result['arcsinh_result_float'] = float_value
            result['arcsinh_result_number'] = loop_value

        # exp function evaluate part
        error = exp_error_cal(float_value, high_precision_f)
        if result['exp_result_error'] < error:
            result['exp_result_error'] = error
            result['exp_result_float'] = float_value
            result['exp_result_number'] = loop_value

        # cbrt function evaluate part
        error = cbrt_error_cal(float_value, high_precision_f)
        if result['cbrt_result_error'] < error:
            result['cbrt_result_error'] = error
            result['cbrt_result_float'] = float_value
            result['cbrt_result_number'] = loop_value

        # expm1 function evaluate part
        error = expm1_error_cal(float_value, high_precision_f)
        if result['expm1_result_error'] < error:
            result['expm1_result_error'] = error
            result['expm1_result_float'] = float_value
            result['expm1_result_number'] = loop_value

        # exp2 function evaluate part
        error = exp2_error_cal(float_value, high_precision_f)
        if result['exp2_result_error'] < error:
            result['exp2_result_error'] = error
            result['exp2_result_float'] = float_value
            result['exp2_result_number'] = loop_value

        gc.collect()

def write_file(x):
    global result

    with open('third_main_addition/example3.txt', 'w') as f:
        f.write(f'The data compute : {x}\n\n')

        # write sinh data
        f.write(f'sinh_result_error: {result["sinh_result_error"]}\n')
        f.write(f'sinh_result_float: {result["sinh_result_float"]}\n')
        f.write(f'sinh_result_number: {result["sinh_result_number"]}\n\n')
     
        # write cosh data
        f.write(f'cosh_result_error: {result["cosh_result_error"]}\n')
        f.write(f'cosh_result_float: {result["cosh_result_float"]}\n')
        f.write(f'cosh_result_number: {result["cosh_result_number"]}\n\n')

        # write tanh data
        f.write(f'tanh_result_error: {result["tanh_result_error"]}\n')
        f.write(f'tanh_result_float: {result["tanh_result_float"]}\n')
        f.write(f'tanh_result_number: {result["tanh_result_number"]}\n\n')

        # write arctan data
        f.write(f'arctan_result_error: {result["arctan_result_error"]}\n')
        f.write(f'arctan_result_float: {result["arctan_result_float"]}\n')
        f.write(f'arctan_result_number: {result["arctan_result_number"]}\n\n')

        # write arcsinh data
        f.write(f'arcsinh_result_error: {result["arcsinh_result_error"]}\n')
        f.write(f'arcsinh_result_float: {result["arcsinh_result_float"]}\n')
        f.write(f'arcsinh_result_number: {result["arcsinh_result_number"]}\n\n')

        # write exp data
        f.write(f'exp_result_error: {result["exp_result_error"]}\n')
        f.write(f'exp_result_float: {result["exp_result_float"]}\n')
        f.write(f'exp_result_number: {result["exp_result_number"]}\n\n')

        # write expm1 data
        f.write(f'expm1_result_error: {result["expm1_result_error"]}\n')
        f.write(f'expm1_result_float: {result["expm1_result_float"]}\n')
        f.write(f'expm1_result_number: {result["expm1_result_number"]}\n\n')

        # write exp2 data
        f.write(f'exp2_result_error: {result["exp2_result_error"]}\n')
        f.write(f'exp2_result_float: {result["exp2_result_float"]}\n')
        f.write(f'exp2_result_number: {result["exp2_result_number"]}\n\n')

        # write cbrt data
        f.write(f'cbrt_result_error: {result["cbrt_result_error"]}\n')
        f.write(f'cbrt_result_float: {result["cbrt_result_float"]}\n')
        f.write(f'cbrt_result_number: {result["cbrt_result_number"]}\n\n')

if __name__ == '__main__':
    test_all_possible(lower=171798640, upper=2147483647)
    gc.collect()
    print("end of the loop")
    print("start to write the result in file")
    write_file("all thing done")