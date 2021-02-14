#!/usr/bin/env python3
# Python 3.7.7
# -*- coding: utf-8 -*-
"""
Este programa analiza y limpia los datos del fichero de Airbnb

Asignatura: Aprendizaje automático 
Ejercicio: Práctica final
Fecha de entrega: 17 Febrero de 2021

Autora: Helena Antich Homar
"""
#%% Libraries
import os
import numpy as np
import pandas as pd
from copy import deepcopy

#%% Directories
working_directory = '/Users/Helena/Documents/MASTER MUSI/AA - ML - Aprendizaje automático/FINAL'
os.chdir(working_directory)

path_data = os.path.join(os.getcwd(), 'airbnb.csv')
path_figures = os.path.join(os.getcwd(), 'Figures')
#%% Functions
#%% Loading data
df_airbnb = pd.read_csv(path_data)
df_airbnb.head()
df_airbnb.info()
# %%
