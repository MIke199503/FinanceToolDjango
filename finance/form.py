#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FinanceToolDjango
@File    ：form.py
@Author  ：朱桃禾 MikePy
@Date    ：2023/3/30 10:05
"""
from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={"required data-msg": "用户名",
                                               "placeholder": "Username",
                                               "id": "userName"
                                               }),
            'password': forms.PasswordInput(attrs={"required data-msg": "密码",
                                                   "placeholder": "Password",
                                                   "id": "pwd"
                                                   },
                                            )
        }
