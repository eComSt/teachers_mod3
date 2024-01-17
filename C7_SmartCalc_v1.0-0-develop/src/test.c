#include <check.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "simple_calc.h"

START_TEST(calc_t) {
  rpn ans = calc("+1+(-1)+cos(sin(0))+x*x+x-x-1/1 mod 1", 1.);
  printf("%f\n", ans.num);
  ck_assert(ans.num == 1.);
}
END_TEST

START_TEST(cred_c) {
  double ans = cred(1000000., 120, 10., 'a');
  ck_assert(ans == 13215.08);
}
END_TEST
START_TEST(cred_d) {
  calc_deb(1000000, 10, 10., 8., 'd', 'y');
  ck_assert(1. == 1.);
}
END_TEST

Suite *example_suite_create(void) {
  Suite *suite = suite_create("s21_calc");
  TCase *tcase_core = tcase_create("Core");
  tcase_add_test(tcase_core, calc_t);
  tcase_add_test(tcase_core, cred_c);
  tcase_add_test(tcase_core, cred_d);
  suite_add_tcase(suite, tcase_core);

  return suite;
}

int main(void) {
  Suite *suite = example_suite_create();
  SRunner *suite_runner = srunner_create(suite);

  srunner_run_all(suite_runner, CK_NORMAL);

  int failed_count = srunner_ntests_failed(suite_runner);
  srunner_free(suite_runner);

  if (failed_count != 0) {
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}