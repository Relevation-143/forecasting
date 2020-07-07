# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pytest
import pandas as pd

from fclib.models.multiple_linear_regression import fit, predict

def test_fit_and_predict(generate_ojdata, generate_data):
    data = pd.read_csv("fclib/tests/resources/ojdatagen.csv")
    newdata = generate_data.ojdata(61, 70)

    keyvars = ["store", "brand"]
    xvars = ["price1", "price2", "price3"]
    target = "logmove"

    mods = fit(data, keyvars, xvars, target)
    predict(newdata, mods, "week", keyvars, xvars, False, False)
