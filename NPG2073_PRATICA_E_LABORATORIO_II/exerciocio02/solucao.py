from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_

# Inicializa a sessão Spark
spark = SparkSession.builder.appName("ExemploBigData").getOrCreate()

# Dados de exemplo: lista de tuplas (categoria, valor)
dados = [
    ("A", 10),
    ("B", 20),
    ("A", 30),
    ("C", 40),
    ("B", 50),
    ("C", 60)
]

# Define os nomes das colunas
colunas = ["categoria", "valor"]

# Cria o DataFrame diretamente dos dados
df = spark.createDataFrame(dados, schema=colunas)

# Exibe o schema do DataFrame
df.printSchema()

# Adiciona uma nova coluna "valor_dobrado" que contém o dobro do valor original
df = df.withColumn("valor_dobrado", col("valor") * 2)

# Realiza uma agregação para calcular a soma de "valor_dobrado" para cada categoria
resultado = df.groupBy("categoria").agg(sum_("valor_dobrado").alias("soma_valor_dobrado"))

# Ordena os resultados do maior para o menor valor agregado
resultado = resultado.orderBy(col("soma_valor_dobrado").desc())

# Exibe o resultado final
resultado.show()

# Encerra a sessão Spark
spark.stop()
