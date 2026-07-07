import hashlib
import os
import pickle
import sqlite3

import requests
from flask import Flask, request

app = Flask(__name__)

SUPER_SECRET_TOKEN_0 = "AKIAIOSFODNN7EXAMPLE_token_0"
SUPER_SECRET_TOKEN_1 = "AKIAIOSFODNN7EXAMPLE_token_1"
SUPER_SECRET_TOKEN_2 = "AKIAIOSFODNN7EXAMPLE_token_2"
SUPER_SECRET_TOKEN_3 = "AKIAIOSFODNN7EXAMPLE_token_3"
SUPER_SECRET_TOKEN_4 = "AKIAIOSFODNN7EXAMPLE_token_4"
SUPER_SECRET_TOKEN_5 = "AKIAIOSFODNN7EXAMPLE_token_5"
SUPER_SECRET_TOKEN_6 = "AKIAIOSFODNN7EXAMPLE_token_6"
SUPER_SECRET_TOKEN_7 = "AKIAIOSFODNN7EXAMPLE_token_7"
SUPER_SECRET_TOKEN_8 = "AKIAIOSFODNN7EXAMPLE_token_8"
SUPER_SECRET_TOKEN_9 = "AKIAIOSFODNN7EXAMPLE_token_9"


@app.route("/vuln_endpoint_0")
def vuln_endpoint_0():
    user_input = request.args.get("input_0")
    # SQL Injection 0
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_1")
def vuln_endpoint_1():
    user_input = request.args.get("input_1")
    # Command Injection 1
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_2")
def vuln_endpoint_2():
    user_input = request.args.get("input_2")
    # Insecure Deserialization 2
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_3")
def vuln_endpoint_3():
    user_input = request.args.get("input_3")
    # SSRF & TLS Disabled 3
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_4")
def vuln_endpoint_4():
    user_input = request.args.get("input_4")
    # Weak Crypto 4
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_5")
def vuln_endpoint_5():
    user_input = request.args.get("input_5")
    # SQL Injection 5
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_6")
def vuln_endpoint_6():
    user_input = request.args.get("input_6")
    # Command Injection 6
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_7")
def vuln_endpoint_7():
    user_input = request.args.get("input_7")
    # Insecure Deserialization 7
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_8")
def vuln_endpoint_8():
    user_input = request.args.get("input_8")
    # SSRF & TLS Disabled 8
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_9")
def vuln_endpoint_9():
    user_input = request.args.get("input_9")
    # Weak Crypto 9
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_10")
def vuln_endpoint_10():
    user_input = request.args.get("input_10")
    # SQL Injection 10
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_11")
def vuln_endpoint_11():
    user_input = request.args.get("input_11")
    # Command Injection 11
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_12")
def vuln_endpoint_12():
    user_input = request.args.get("input_12")
    # Insecure Deserialization 12
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_13")
def vuln_endpoint_13():
    user_input = request.args.get("input_13")
    # SSRF & TLS Disabled 13
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_14")
def vuln_endpoint_14():
    user_input = request.args.get("input_14")
    # Weak Crypto 14
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_15")
def vuln_endpoint_15():
    user_input = request.args.get("input_15")
    # SQL Injection 15
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_16")
def vuln_endpoint_16():
    user_input = request.args.get("input_16")
    # Command Injection 16
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_17")
def vuln_endpoint_17():
    user_input = request.args.get("input_17")
    # Insecure Deserialization 17
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_18")
def vuln_endpoint_18():
    user_input = request.args.get("input_18")
    # SSRF & TLS Disabled 18
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_19")
def vuln_endpoint_19():
    user_input = request.args.get("input_19")
    # Weak Crypto 19
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_20")
def vuln_endpoint_20():
    user_input = request.args.get("input_20")
    # SQL Injection 20
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_21")
def vuln_endpoint_21():
    user_input = request.args.get("input_21")
    # Command Injection 21
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_22")
def vuln_endpoint_22():
    user_input = request.args.get("input_22")
    # Insecure Deserialization 22
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_23")
def vuln_endpoint_23():
    user_input = request.args.get("input_23")
    # SSRF & TLS Disabled 23
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_24")
def vuln_endpoint_24():
    user_input = request.args.get("input_24")
    # Weak Crypto 24
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_25")
def vuln_endpoint_25():
    user_input = request.args.get("input_25")
    # SQL Injection 25
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_26")
def vuln_endpoint_26():
    user_input = request.args.get("input_26")
    # Command Injection 26
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_27")
def vuln_endpoint_27():
    user_input = request.args.get("input_27")
    # Insecure Deserialization 27
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_28")
def vuln_endpoint_28():
    user_input = request.args.get("input_28")
    # SSRF & TLS Disabled 28
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_29")
def vuln_endpoint_29():
    user_input = request.args.get("input_29")
    # Weak Crypto 29
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_30")
def vuln_endpoint_30():
    user_input = request.args.get("input_30")
    # SQL Injection 30
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_31")
def vuln_endpoint_31():
    user_input = request.args.get("input_31")
    # Command Injection 31
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_32")
def vuln_endpoint_32():
    user_input = request.args.get("input_32")
    # Insecure Deserialization 32
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_33")
def vuln_endpoint_33():
    user_input = request.args.get("input_33")
    # SSRF & TLS Disabled 33
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_34")
def vuln_endpoint_34():
    user_input = request.args.get("input_34")
    # Weak Crypto 34
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_35")
def vuln_endpoint_35():
    user_input = request.args.get("input_35")
    # SQL Injection 35
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_36")
def vuln_endpoint_36():
    user_input = request.args.get("input_36")
    # Command Injection 36
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_37")
def vuln_endpoint_37():
    user_input = request.args.get("input_37")
    # Insecure Deserialization 37
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_38")
def vuln_endpoint_38():
    user_input = request.args.get("input_38")
    # SSRF & TLS Disabled 38
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_39")
def vuln_endpoint_39():
    user_input = request.args.get("input_39")
    # Weak Crypto 39
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_40")
def vuln_endpoint_40():
    user_input = request.args.get("input_40")
    # SQL Injection 40
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_41")
def vuln_endpoint_41():
    user_input = request.args.get("input_41")
    # Command Injection 41
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_42")
def vuln_endpoint_42():
    user_input = request.args.get("input_42")
    # Insecure Deserialization 42
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_43")
def vuln_endpoint_43():
    user_input = request.args.get("input_43")
    # SSRF & TLS Disabled 43
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_44")
def vuln_endpoint_44():
    user_input = request.args.get("input_44")
    # Weak Crypto 44
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_45")
def vuln_endpoint_45():
    user_input = request.args.get("input_45")
    # SQL Injection 45
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_46")
def vuln_endpoint_46():
    user_input = request.args.get("input_46")
    # Command Injection 46
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_47")
def vuln_endpoint_47():
    user_input = request.args.get("input_47")
    # Insecure Deserialization 47
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_48")
def vuln_endpoint_48():
    user_input = request.args.get("input_48")
    # SSRF & TLS Disabled 48
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_49")
def vuln_endpoint_49():
    user_input = request.args.get("input_49")
    # Weak Crypto 49
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_50")
def vuln_endpoint_50():
    user_input = request.args.get("input_50")
    # SQL Injection 50
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_51")
def vuln_endpoint_51():
    user_input = request.args.get("input_51")
    # Command Injection 51
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_52")
def vuln_endpoint_52():
    user_input = request.args.get("input_52")
    # Insecure Deserialization 52
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_53")
def vuln_endpoint_53():
    user_input = request.args.get("input_53")
    # SSRF & TLS Disabled 53
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_54")
def vuln_endpoint_54():
    user_input = request.args.get("input_54")
    # Weak Crypto 54
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_55")
def vuln_endpoint_55():
    user_input = request.args.get("input_55")
    # SQL Injection 55
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_56")
def vuln_endpoint_56():
    user_input = request.args.get("input_56")
    # Command Injection 56
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_57")
def vuln_endpoint_57():
    user_input = request.args.get("input_57")
    # Insecure Deserialization 57
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_58")
def vuln_endpoint_58():
    user_input = request.args.get("input_58")
    # SSRF & TLS Disabled 58
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_59")
def vuln_endpoint_59():
    user_input = request.args.get("input_59")
    # Weak Crypto 59
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_60")
def vuln_endpoint_60():
    user_input = request.args.get("input_60")
    # SQL Injection 60
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_61")
def vuln_endpoint_61():
    user_input = request.args.get("input_61")
    # Command Injection 61
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_62")
def vuln_endpoint_62():
    user_input = request.args.get("input_62")
    # Insecure Deserialization 62
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_63")
def vuln_endpoint_63():
    user_input = request.args.get("input_63")
    # SSRF & TLS Disabled 63
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_64")
def vuln_endpoint_64():
    user_input = request.args.get("input_64")
    # Weak Crypto 64
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_65")
def vuln_endpoint_65():
    user_input = request.args.get("input_65")
    # SQL Injection 65
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_66")
def vuln_endpoint_66():
    user_input = request.args.get("input_66")
    # Command Injection 66
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_67")
def vuln_endpoint_67():
    user_input = request.args.get("input_67")
    # Insecure Deserialization 67
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_68")
def vuln_endpoint_68():
    user_input = request.args.get("input_68")
    # SSRF & TLS Disabled 68
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_69")
def vuln_endpoint_69():
    user_input = request.args.get("input_69")
    # Weak Crypto 69
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_70")
def vuln_endpoint_70():
    user_input = request.args.get("input_70")
    # SQL Injection 70
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_71")
def vuln_endpoint_71():
    user_input = request.args.get("input_71")
    # Command Injection 71
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_72")
def vuln_endpoint_72():
    user_input = request.args.get("input_72")
    # Insecure Deserialization 72
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_73")
def vuln_endpoint_73():
    user_input = request.args.get("input_73")
    # SSRF & TLS Disabled 73
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_74")
def vuln_endpoint_74():
    user_input = request.args.get("input_74")
    # Weak Crypto 74
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_75")
def vuln_endpoint_75():
    user_input = request.args.get("input_75")
    # SQL Injection 75
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_76")
def vuln_endpoint_76():
    user_input = request.args.get("input_76")
    # Command Injection 76
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_77")
def vuln_endpoint_77():
    user_input = request.args.get("input_77")
    # Insecure Deserialization 77
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_78")
def vuln_endpoint_78():
    user_input = request.args.get("input_78")
    # SSRF & TLS Disabled 78
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_79")
def vuln_endpoint_79():
    user_input = request.args.get("input_79")
    # Weak Crypto 79
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_80")
def vuln_endpoint_80():
    user_input = request.args.get("input_80")
    # SQL Injection 80
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_81")
def vuln_endpoint_81():
    user_input = request.args.get("input_81")
    # Command Injection 81
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_82")
def vuln_endpoint_82():
    user_input = request.args.get("input_82")
    # Insecure Deserialization 82
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_83")
def vuln_endpoint_83():
    user_input = request.args.get("input_83")
    # SSRF & TLS Disabled 83
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_84")
def vuln_endpoint_84():
    user_input = request.args.get("input_84")
    # Weak Crypto 84
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_85")
def vuln_endpoint_85():
    user_input = request.args.get("input_85")
    # SQL Injection 85
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_86")
def vuln_endpoint_86():
    user_input = request.args.get("input_86")
    # Command Injection 86
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_87")
def vuln_endpoint_87():
    user_input = request.args.get("input_87")
    # Insecure Deserialization 87
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_88")
def vuln_endpoint_88():
    user_input = request.args.get("input_88")
    # SSRF & TLS Disabled 88
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_89")
def vuln_endpoint_89():
    user_input = request.args.get("input_89")
    # Weak Crypto 89
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_90")
def vuln_endpoint_90():
    user_input = request.args.get("input_90")
    # SQL Injection 90
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_91")
def vuln_endpoint_91():
    user_input = request.args.get("input_91")
    # Command Injection 91
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_92")
def vuln_endpoint_92():
    user_input = request.args.get("input_92")
    # Insecure Deserialization 92
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_93")
def vuln_endpoint_93():
    user_input = request.args.get("input_93")
    # SSRF & TLS Disabled 93
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_94")
def vuln_endpoint_94():
    user_input = request.args.get("input_94")
    # Weak Crypto 94
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_95")
def vuln_endpoint_95():
    user_input = request.args.get("input_95")
    # SQL Injection 95
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_96")
def vuln_endpoint_96():
    user_input = request.args.get("input_96")
    # Command Injection 96
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_97")
def vuln_endpoint_97():
    user_input = request.args.get("input_97")
    # Insecure Deserialization 97
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_98")
def vuln_endpoint_98():
    user_input = request.args.get("input_98")
    # SSRF & TLS Disabled 98
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_99")
def vuln_endpoint_99():
    user_input = request.args.get("input_99")
    # Weak Crypto 99
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_100")
def vuln_endpoint_100():
    user_input = request.args.get("input_100")
    # SQL Injection 100
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_101")
def vuln_endpoint_101():
    user_input = request.args.get("input_101")
    # Command Injection 101
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_102")
def vuln_endpoint_102():
    user_input = request.args.get("input_102")
    # Insecure Deserialization 102
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_103")
def vuln_endpoint_103():
    user_input = request.args.get("input_103")
    # SSRF & TLS Disabled 103
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_104")
def vuln_endpoint_104():
    user_input = request.args.get("input_104")
    # Weak Crypto 104
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_105")
def vuln_endpoint_105():
    user_input = request.args.get("input_105")
    # SQL Injection 105
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_106")
def vuln_endpoint_106():
    user_input = request.args.get("input_106")
    # Command Injection 106
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_107")
def vuln_endpoint_107():
    user_input = request.args.get("input_107")
    # Insecure Deserialization 107
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_108")
def vuln_endpoint_108():
    user_input = request.args.get("input_108")
    # SSRF & TLS Disabled 108
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_109")
def vuln_endpoint_109():
    user_input = request.args.get("input_109")
    # Weak Crypto 109
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_110")
def vuln_endpoint_110():
    user_input = request.args.get("input_110")
    # SQL Injection 110
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_111")
def vuln_endpoint_111():
    user_input = request.args.get("input_111")
    # Command Injection 111
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_112")
def vuln_endpoint_112():
    user_input = request.args.get("input_112")
    # Insecure Deserialization 112
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_113")
def vuln_endpoint_113():
    user_input = request.args.get("input_113")
    # SSRF & TLS Disabled 113
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_114")
def vuln_endpoint_114():
    user_input = request.args.get("input_114")
    # Weak Crypto 114
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_115")
def vuln_endpoint_115():
    user_input = request.args.get("input_115")
    # SQL Injection 115
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_116")
def vuln_endpoint_116():
    user_input = request.args.get("input_116")
    # Command Injection 116
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_117")
def vuln_endpoint_117():
    user_input = request.args.get("input_117")
    # Insecure Deserialization 117
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_118")
def vuln_endpoint_118():
    user_input = request.args.get("input_118")
    # SSRF & TLS Disabled 118
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_119")
def vuln_endpoint_119():
    user_input = request.args.get("input_119")
    # Weak Crypto 119
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_120")
def vuln_endpoint_120():
    user_input = request.args.get("input_120")
    # SQL Injection 120
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_121")
def vuln_endpoint_121():
    user_input = request.args.get("input_121")
    # Command Injection 121
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_122")
def vuln_endpoint_122():
    user_input = request.args.get("input_122")
    # Insecure Deserialization 122
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_123")
def vuln_endpoint_123():
    user_input = request.args.get("input_123")
    # SSRF & TLS Disabled 123
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_124")
def vuln_endpoint_124():
    user_input = request.args.get("input_124")
    # Weak Crypto 124
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_125")
def vuln_endpoint_125():
    user_input = request.args.get("input_125")
    # SQL Injection 125
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_126")
def vuln_endpoint_126():
    user_input = request.args.get("input_126")
    # Command Injection 126
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_127")
def vuln_endpoint_127():
    user_input = request.args.get("input_127")
    # Insecure Deserialization 127
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_128")
def vuln_endpoint_128():
    user_input = request.args.get("input_128")
    # SSRF & TLS Disabled 128
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_129")
def vuln_endpoint_129():
    user_input = request.args.get("input_129")
    # Weak Crypto 129
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_130")
def vuln_endpoint_130():
    user_input = request.args.get("input_130")
    # SQL Injection 130
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_131")
def vuln_endpoint_131():
    user_input = request.args.get("input_131")
    # Command Injection 131
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_132")
def vuln_endpoint_132():
    user_input = request.args.get("input_132")
    # Insecure Deserialization 132
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_133")
def vuln_endpoint_133():
    user_input = request.args.get("input_133")
    # SSRF & TLS Disabled 133
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_134")
def vuln_endpoint_134():
    user_input = request.args.get("input_134")
    # Weak Crypto 134
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_135")
def vuln_endpoint_135():
    user_input = request.args.get("input_135")
    # SQL Injection 135
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_136")
def vuln_endpoint_136():
    user_input = request.args.get("input_136")
    # Command Injection 136
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_137")
def vuln_endpoint_137():
    user_input = request.args.get("input_137")
    # Insecure Deserialization 137
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_138")
def vuln_endpoint_138():
    user_input = request.args.get("input_138")
    # SSRF & TLS Disabled 138
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_139")
def vuln_endpoint_139():
    user_input = request.args.get("input_139")
    # Weak Crypto 139
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_140")
def vuln_endpoint_140():
    user_input = request.args.get("input_140")
    # SQL Injection 140
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_141")
def vuln_endpoint_141():
    user_input = request.args.get("input_141")
    # Command Injection 141
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_142")
def vuln_endpoint_142():
    user_input = request.args.get("input_142")
    # Insecure Deserialization 142
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_143")
def vuln_endpoint_143():
    user_input = request.args.get("input_143")
    # SSRF & TLS Disabled 143
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_144")
def vuln_endpoint_144():
    user_input = request.args.get("input_144")
    # Weak Crypto 144
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_145")
def vuln_endpoint_145():
    user_input = request.args.get("input_145")
    # SQL Injection 145
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_146")
def vuln_endpoint_146():
    user_input = request.args.get("input_146")
    # Command Injection 146
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_147")
def vuln_endpoint_147():
    user_input = request.args.get("input_147")
    # Insecure Deserialization 147
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_148")
def vuln_endpoint_148():
    user_input = request.args.get("input_148")
    # SSRF & TLS Disabled 148
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_149")
def vuln_endpoint_149():
    user_input = request.args.get("input_149")
    # Weak Crypto 149
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_150")
def vuln_endpoint_150():
    user_input = request.args.get("input_150")
    # SQL Injection 150
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_151")
def vuln_endpoint_151():
    user_input = request.args.get("input_151")
    # Command Injection 151
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_152")
def vuln_endpoint_152():
    user_input = request.args.get("input_152")
    # Insecure Deserialization 152
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_153")
def vuln_endpoint_153():
    user_input = request.args.get("input_153")
    # SSRF & TLS Disabled 153
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_154")
def vuln_endpoint_154():
    user_input = request.args.get("input_154")
    # Weak Crypto 154
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_155")
def vuln_endpoint_155():
    user_input = request.args.get("input_155")
    # SQL Injection 155
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_156")
def vuln_endpoint_156():
    user_input = request.args.get("input_156")
    # Command Injection 156
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_157")
def vuln_endpoint_157():
    user_input = request.args.get("input_157")
    # Insecure Deserialization 157
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_158")
def vuln_endpoint_158():
    user_input = request.args.get("input_158")
    # SSRF & TLS Disabled 158
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_159")
def vuln_endpoint_159():
    user_input = request.args.get("input_159")
    # Weak Crypto 159
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_160")
def vuln_endpoint_160():
    user_input = request.args.get("input_160")
    # SQL Injection 160
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_161")
def vuln_endpoint_161():
    user_input = request.args.get("input_161")
    # Command Injection 161
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_162")
def vuln_endpoint_162():
    user_input = request.args.get("input_162")
    # Insecure Deserialization 162
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_163")
def vuln_endpoint_163():
    user_input = request.args.get("input_163")
    # SSRF & TLS Disabled 163
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_164")
def vuln_endpoint_164():
    user_input = request.args.get("input_164")
    # Weak Crypto 164
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_165")
def vuln_endpoint_165():
    user_input = request.args.get("input_165")
    # SQL Injection 165
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_166")
def vuln_endpoint_166():
    user_input = request.args.get("input_166")
    # Command Injection 166
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_167")
def vuln_endpoint_167():
    user_input = request.args.get("input_167")
    # Insecure Deserialization 167
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_168")
def vuln_endpoint_168():
    user_input = request.args.get("input_168")
    # SSRF & TLS Disabled 168
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_169")
def vuln_endpoint_169():
    user_input = request.args.get("input_169")
    # Weak Crypto 169
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_170")
def vuln_endpoint_170():
    user_input = request.args.get("input_170")
    # SQL Injection 170
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_171")
def vuln_endpoint_171():
    user_input = request.args.get("input_171")
    # Command Injection 171
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_172")
def vuln_endpoint_172():
    user_input = request.args.get("input_172")
    # Insecure Deserialization 172
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_173")
def vuln_endpoint_173():
    user_input = request.args.get("input_173")
    # SSRF & TLS Disabled 173
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_174")
def vuln_endpoint_174():
    user_input = request.args.get("input_174")
    # Weak Crypto 174
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_175")
def vuln_endpoint_175():
    user_input = request.args.get("input_175")
    # SQL Injection 175
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_176")
def vuln_endpoint_176():
    user_input = request.args.get("input_176")
    # Command Injection 176
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_177")
def vuln_endpoint_177():
    user_input = request.args.get("input_177")
    # Insecure Deserialization 177
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_178")
def vuln_endpoint_178():
    user_input = request.args.get("input_178")
    # SSRF & TLS Disabled 178
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_179")
def vuln_endpoint_179():
    user_input = request.args.get("input_179")
    # Weak Crypto 179
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_180")
def vuln_endpoint_180():
    user_input = request.args.get("input_180")
    # SQL Injection 180
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_181")
def vuln_endpoint_181():
    user_input = request.args.get("input_181")
    # Command Injection 181
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_182")
def vuln_endpoint_182():
    user_input = request.args.get("input_182")
    # Insecure Deserialization 182
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_183")
def vuln_endpoint_183():
    user_input = request.args.get("input_183")
    # SSRF & TLS Disabled 183
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_184")
def vuln_endpoint_184():
    user_input = request.args.get("input_184")
    # Weak Crypto 184
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_185")
def vuln_endpoint_185():
    user_input = request.args.get("input_185")
    # SQL Injection 185
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_186")
def vuln_endpoint_186():
    user_input = request.args.get("input_186")
    # Command Injection 186
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_187")
def vuln_endpoint_187():
    user_input = request.args.get("input_187")
    # Insecure Deserialization 187
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_188")
def vuln_endpoint_188():
    user_input = request.args.get("input_188")
    # SSRF & TLS Disabled 188
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_189")
def vuln_endpoint_189():
    user_input = request.args.get("input_189")
    # Weak Crypto 189
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_190")
def vuln_endpoint_190():
    user_input = request.args.get("input_190")
    # SQL Injection 190
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_191")
def vuln_endpoint_191():
    user_input = request.args.get("input_191")
    # Command Injection 191
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_192")
def vuln_endpoint_192():
    user_input = request.args.get("input_192")
    # Insecure Deserialization 192
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_193")
def vuln_endpoint_193():
    user_input = request.args.get("input_193")
    # SSRF & TLS Disabled 193
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_194")
def vuln_endpoint_194():
    user_input = request.args.get("input_194")
    # Weak Crypto 194
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


@app.route("/vuln_endpoint_195")
def vuln_endpoint_195():
    user_input = request.args.get("input_195")
    # SQL Injection 195
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM data WHERE id = '{user_input}'")
    return str(cursor.fetchall())


@app.route("/vuln_endpoint_196")
def vuln_endpoint_196():
    user_input = request.args.get("input_196")
    # Command Injection 196
    os.system("echo " + str(user_input))
    return "Executed"


@app.route("/vuln_endpoint_197")
def vuln_endpoint_197():
    user_input = request.args.get("input_197")
    # Insecure Deserialization 197
    if user_input:
        data = pickle.loads(user_input.encode())
    return "Loaded"


@app.route("/vuln_endpoint_198")
def vuln_endpoint_198():
    user_input = request.args.get("input_198")
    # SSRF & TLS Disabled 198
    if user_input:
        resp = requests.get(user_input, verify=False)
        return resp.text
    return "No input"


@app.route("/vuln_endpoint_199")
def vuln_endpoint_199():
    user_input = request.args.get("input_199")
    # Weak Crypto 199
    if user_input:
        md5 = hashlib.md5(user_input.encode()).hexdigest()
        return md5
    return "No input"


if __name__ == "__main__":
    app.run(debug=True)
