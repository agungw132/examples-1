# Databricks notebook source
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
    return a

# COMMAND ----------

# MAGIC %md
# MAGIC ![](https://agungwahyudi.xyz/spark-optim/test-1.png)

# COMMAND ----------

import sys

# COMMAND ----------

Niter = 100000

# COMMAND ----------

for i in range(Niter):
    fib(i)

# COMMAND ----------

# MAGIC %load_ext Cython

# COMMAND ----------

# MAGIC %%cython
# MAGIC def cfib(int n):
# MAGIC     cdef int i
# MAGIC     cdef double a=0.0, b=1.0
# MAGIC     for i in range(n):
# MAGIC         a, b = a + b, a
# MAGIC     return a

# COMMAND ----------

for i in range(Niter):
    cfib(i)

# COMMAND ----------


