#import project file
import main
import second_main
import third_main
import third_main_addition
import fourth_main
import fifth_main
import biVariable
import biVariable_hypot

#import library used to complete unit test
import numpy as np
import gmpy2

# parameter data which is an integer used to represent the floating number

def test_for_sin(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = main.sin_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")

def test_for_cos(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = main.cos_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_tan(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = main.tan_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arcsin(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = second_main.arcsin_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arccos(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = second_main.arccos_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arctanh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = second_main.arctanh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")

def test_for_sinh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.sinh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")

def test_for_cosh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.cosh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")

def test_for_tanh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.tanh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arctan(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.arctan_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arcsinh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.arcsinh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")

def test_for_exp(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.exp_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_cbrt(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.cbrt_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")



def test_for_expm1(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.expm1_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_exp2(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = third_main.exp2_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")



def test_for_sqrt(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fourth_main.sqrt_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_log(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fourth_main.log_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_log2(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fourth_main.log2_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_log10(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fourth_main.log10_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_log1p(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fifth_main.log1p_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_arccosh(data, result):
    float_value = np.int32(data).view(np.float32)
    str_float = f"{float_value:.160f}"
    high_precision_f = gmpy2.mpfr(str_float)

    error = fifth_main.arccosh_error_cal(float_value, high_precision_f)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


#######################
def test_for_arctan2(par1, par2 , result):
    first_pa = np.int32(par1).view(np.float32)
    str_float = f"{first_pa:.160f}"
    first_pa_high = gmpy2.mpfr(str_float)

    second_pa = np.int32(par2).view(np.float32)
    str_float = f"{second_pa:.160f}"
    second_pa_high = gmpy2.mpfr(str_float)

    error = biVariable.arctan2_error_cal(first_pa, second_pa, first_pa_high, second_pa_high)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")


def test_for_hypot(par1, par2 , result):
    first_pa = np.int32(par1).view(np.float32)
    str_float = f"{first_pa:.160f}"
    first_pa_high = gmpy2.mpfr(str_float)

    second_pa = np.int32(par2).view(np.float32)
    str_float = f"{second_pa:.160f}"
    second_pa_high = gmpy2.mpfr(str_float)

    error = biVariable_hypot.hypot_error_cal(first_pa, second_pa, first_pa_high, second_pa_high)
    if abs(error - result) >= 0.001:
        print("test for sin function pass")
    else:
        print("test for sin function fail  !!!!!!!!!!")



if __name__ == '__main__':
    gmpy2.get_context().precision = 128


    test_for_arccos(0.647,-1000000111111101101100100110100)
    # test_for_arccosh()
    # test_for_arcsin()
    # test_for_arcsinh()
    # test_for_arctan()
    # test_for_arctanh()
    # test_for_cbrt()
    # test_for_cos()
    # test_for_cosh()
    # test_for_expm1()
    # test_for_exp2()
    # test_for_exp()
    # test_for_tanh()
    # test_for_tan()
    # test_for_sinh()
    # test_for_sin()
    # test_for_log2()
    # test_for_log1p()
    # test_for_log10()
    # test_for_log()
    # test_for_sqrt()



    # test_for_hypot()
    # test_for_arctan2()