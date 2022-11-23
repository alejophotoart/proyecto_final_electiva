import pytest
import os
import sys
import json

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from faker_servicio import app


def test_delete_records():
    print("TEST DELETE RECORDS")
    resp = app.test_client().get("borrar_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert res.get("message") == "proceso correcto"


def test_get_records():
    print("TEST GET RECORDS")
    resp = app.test_client().get("obtener_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert res == []


def test_insert_records():
    print("TEST INSERT RECORDS")
    resp = app.test_client().get("crear_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert resp.status_code == 200
    assert res.get("message") == "proceso realizado correctamente"
    resp = app.test_client().get("obtener_registros")
    res = json.loads(resp.data.decode("utf-8"))
    assert len(res) == 13
