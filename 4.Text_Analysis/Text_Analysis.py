from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# creat SparkSession
spark = SparkSession.builder.appName("TextAnalysis").getOrCreate()

# read the file
text_data = spark.read.text(r"C:\Users\User\Downloads\2024\all_shakespeare.txt")
#text_data.show(10)
'''
explode, which is used to split the column containing the array into multiple rows, with each element becoming a row.
split(col("value"), "\s"), nous séparons chaque ligne de texte par des espaces pour former une colonne contenant un tableau de mots.
alias("word"): this assigns an alias to the newly generated column, naming it "word"
'''
words = text_data.select(explode(split(col("value"), "\s")).alias("word"))
#words.show(truncate=False)

# Counting word frequencies
word_count = words.groupBy("word").count().orderBy("count", ascending=False)
# Show results
word_count.show(truncate=False)
# Close SparkSession
spark.stop()
