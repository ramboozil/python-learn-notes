#!/usr/bin/env python3
#-*-coding:utf-8-*-
name=input('请输入您的姓名：')
s1=int(input('请输入您去年的成绩：'))
s2=int(input('请输入您今年的成绩：'))
c=(s2-s1)/s1*100
if c > 0 :
    print('您成绩相比于去年提高了%.1f%%' % c)
else:
    print('您成绩相比于去年下降了%.1f%%' %-c)