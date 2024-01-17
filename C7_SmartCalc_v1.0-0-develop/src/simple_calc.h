#pragma once
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#define ann(s, m, t) \
  (t * s * pow(t / 1200 + 1, m) / (pow(t / 1200 + 1, m) - 1) / 1200)
#define days_m(x, y)                                         \
  (28 + (x + 1 + (x > 6)) % 2 + 2 % (x + 1) + 2 * (x == 0) + \
   (y % 4 == 0) * (x == 1))
#define days_y(y) (365 + (y % 4 == 0))
#define p_d(s, p, y) p *s / (100 * days_y(y))
#define p_m(s, p, m, y) days_m(m, y) * p_d(s, p, y)
#define rnd(x) ((double)((int)(x * 100) + (x - (int)x > 0.)) / 100)
#define print(x) printf("%f\n", (double)x)
typedef struct {
  int type;
  double num;
} rpn;

double cred(double s, int mnth, double t, char tp);
rpn calc(char *str, double x);
int take_next(char *str, rpn *elem, double x);
int calc_days(int y, int m, int d, int mnth);
void calc_deb(double s, int mnth, double p, double n, char per, char cap);
int ymd_to_mord(int year, int month, int day);