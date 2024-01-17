#include "simple_calc.h"
double sum(double a, double b) { return a + b; }
double sub(double a, double b) { return a - b; }
double mul(double a, double b) { return a * b; }
double di(double a, double b) { return a / b; }
double u_sub(double a) { return -a; }
double u_add(double a) { return a; }
int rpn_len(rpn *mass) {
  for (int ans = 0;; ans++)
    if (!mass[ans].type) return ans;
}
const char prefix_oper[19][5] = {
    "sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "ln", "log", "u+",
    "u-",  "(",   "+",   "-",    "*",    "/",    "mod",  "^",  ")"};

double (*f_2[11])(double) = {sin,  cos, tan,   asin,  acos, atan,
                             sqrt, log, log10, u_add, u_sub};
double (*f_1[6])(double, double) = {sum, sub, mul, di, fmod, pow};
rpn calc(char *str, double x) {
  rpn polish[1024] = {{0, 0}}, mass[1024] = {{0, 0}};
  int c = 0, d = 1023;
  for (int i = 0; *str; i++) {
    str += take_next(str, mass + i, x);
    if (mass[i].type == 0) break;
  }
  for (int ans = 0; ans < rpn_len(mass); ans++) {
    if ((mass[ans].type == 1) &&
        ((mass[ans].num == 12) || (mass[ans].num == 13)))
      if ((ans == 0) || ((mass[ans - 1].type == 1) && (mass[ans - 1].num < 16)))
        mass[ans].num -= 3;
  }
  for (int i = 0; i < rpn_len(mass); i++)
    if (mass[i].type > 1)
      polish[c++] = mass[i];
    else {
      if ((mass[i].num == 18) && (++d))
        while ((d < 1023) && polish[d].num != 11) polish[c++] = polish[d++];
      else if (mass[i].num > 11)
        while ((d < 1023) && (polish[d + 1].num != 11) &&
               ((polish[d + 1].num / 2 >= mass[i].num / 2) ||
                (polish[d + 1].num < 11)))
          polish[c++] = polish[++d];
      if (mass[i].num != 18) polish[d--] = mass[i];
    }
  for (; d < 1023;) polish[c++] = polish[++d];
  for (int i = c; i < 1024; i++) polish[i] = (rpn){0, 0};
  for (int i = 0, c = 1023; i < rpn_len(polish); i++)
    if (polish[i].type > 1)
      polish[c--] = polish[i];
    else if (polish[i].num != 11)
      polish[c + 1].num = (polish[i].num < 11)
                              ? f_2[(int)(polish[i].num)](polish[c + 1].num)
                              : f_1[(int)(polish[i].num) - 12](
                                    polish[c + 1].num, polish[++c].num);

  return polish[1023];
}
int take_next(char *str, rpn *elem, double x) {
  int ans = 0;
  for (int i = 0; i < 19; i++)
    if (strstr(str, prefix_oper[i]) == str && (ans = strlen(prefix_oper[i])))
      *elem = (rpn){1, i};
  if ((!ans) && sscanf(str, "%lf", &(elem->num)))
    for (elem->type = 2; strchr("0123456789.", str[ans]);) ans++;
  if (((*str == 'x') || (*str == 'X')) && (ans = 1)) *elem = (rpn){2, x};
  return ans;
}
double cred(double s, int mnth, double t, char tp) {
  double pay = 0, osn = 0, proc = 0;
  FILE *ff = fopen("graph.txt", "w");
  //  int m = localtime(&timer)->tm_mon, y = localtime(&timer)->tm_year;
  if (tp == 'a')
    pay = rnd(ann(s, mnth, t));
  else
    osn = rnd(s / mnth);
  for (int i = 1; i < mnth; i++) {
    proc = rnd(s * t / 1200);
    if (tp == 'a')
      osn = pay - proc;
    else
      pay = osn + proc;
    fprintf(ff, "%d\t%15.2f\t%15.2f\t%15.2f\t%15.2f\n", i, pay, proc, osn,
            s - osn);
    s -= osn;
  }
  proc = rnd(s * t / 1200);
  osn = s;
  fprintf(ff, "%d\t%15.2f\t%15.2f\t%15.2f\t%15.2f\n", mnth, s + proc, proc, s,
          0.);
  fclose(ff);
  return pay;
}
void calc_deb(double s, int mnth, double p, double n, char per, char cap) {
  const time_t timer = time(NULL);
  char line[1024] = {0};
  int m = localtime(&timer)->tm_mon, y = localtime(&timer)->tm_year;
  const int dday = calc_days(y, m, 1, mnth);
  double mass[dday], s2 = s, pl = 0;
  for (int i = 0; i < dday; i++) mass[i] = 0.;
  FILE *ff = fopen("deb.txt", "r");
  while (!feof(ff)) {
    fgets(line, 255, ff);
    int num = 0;
    double sum = 0;
    sscanf(line, "%d %lf\n", &num, &sum);
    if (num < dday) mass[num] += sum;
    pl += sum;
  }
  fclose(ff);
  double ans = 0, ppd = p / days_y(y);
  double cap_date[mnth];
  for (int i = 0; i < mnth; i++) cap_date[i] = calc_days(y, m, 1, i + 1);
  for (int i = 0; i < dday; i++) {
    s += mass[i];
    if (cap == 'y') {
      if (per == 'd')
        s += s / 100 * ppd;
      else {
        ans += s / 100 * ppd;
        for (int j = 0; j < mnth; j++)
          if (cap_date[j] == i) {
            s += ans;
            ans = 0;
          }
      }
    } else
      ans += s / 100 * ppd;
  }
  s += ans;
  FILE *f = fopen("deb2.txt", "w");
  double nal = p - n;
  nal = (nal > 0) ? 0.13 * (s - s2 - pl) * (1. - n / p) : 0.;
  fprintf(f, "начислено %%%.2f удержано налога %.2f, сумма в конце %.2f",
          s - s2 - pl, nal, s - nal);
  fclose(f);
}
int calc_days(int y, int m, int d, int mnth) {
  int y2 = y + mnth / 12, m2 = m + mnth % 12,
      d2 = days_m(m2, d2) >= d ? d : days_m(m2, d2);
  return ymd_to_mord(y2, m2, d2) - ymd_to_mord(y, m, d);
}
int ymd_to_mord(int year, int month, int day) {
  return day + (153 * (month + 12 * ((int)(14 - month) / 12) - 3) + 2) / 5 +
         365 * (year - (14 - month) / 12) + (year - (14 - month) / 12) / 4 -
         (year - (14 - month) / 12) / 100 + (year - (14 - month) / 12) / 400;
}
