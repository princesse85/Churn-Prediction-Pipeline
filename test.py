import pandas as pd
import sklearn
import streamlit as st
import boto3
import sys

print("Python version:", sys.version)
print("Pandas version:", pd.__version__)
print("Scikit-learn version:", sklearn.__version__)
print("Streamlit version:", st.__version__)
print("Boto3 version:", boto3.__version__)

print("\nEnvironment setup is complete!")