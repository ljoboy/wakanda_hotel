#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


def db_connect():
    return pymysql.connect("localhost", 'root', "", 'new_wakanda')
