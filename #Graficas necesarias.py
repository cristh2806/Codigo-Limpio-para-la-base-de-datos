#Graficas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que df_json es tu DataFrame
# df_json = pd.read_json('ruta/a/tu/archivo.json', lines=True)

# Configurar el estilo de seaborn
sns.set(style="whitegrid")

# 0. Histograma para 'spl_product_ndc'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['spl_product_ndc'].value_counts(), bins=30, kde=True)
plt.title('Histograma de spl_product_ndc')
plt.xlabel('NDC')
plt.ylabel('Frecuencia')
plt.show()

# 1. Gráfico de barras para 'manufacturer_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='manufacturer_name', data=df_json, order=df_json['manufacturer_name'].value_counts().index)
plt.title('Gráfico de barras de manufacturer_name')
plt.xlabel('Cantidad')
plt.ylabel('Fabricante')
plt.show()

# 2. Gráfico de barras para 'application_number'
plt.figure(figsize=(10, 5))
sns.countplot(y='application_number', data=df_json, order=df_json['application_number'].value_counts().index)
plt.title('Gráfico de barras de application_number')
plt.xlabel('Cantidad')
plt.ylabel('Número de aplicación')
plt.show()

# 3. Gráfico de barras apiladas para 'brand_name_suffix'
brand_suffix_counts = df_json['brand_name_suffix'].value_counts()
brand_suffix_counts.plot(kind='bar', stacked=True)
plt.title('Gráfico de barras apiladas de brand_name_suffix')
plt.xlabel('Sufijo de nombre de marca')
plt.ylabel('Cantidad')
plt.show()

# 4. Histograma para 'spl_version'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['spl_version'], bins=30, kde=True)
plt.title('Histograma de spl_version')
plt.xlabel('Versión SPL')
plt.ylabel('Frecuencia')
plt.show()

# 5. Gráfico de barras para 'route'
plt.figure(figsize=(10, 5))
sns.countplot(y='route', data=df_json, order=df_json['route'].value_counts().index)
plt.title('Gráfico de barras de route')
plt.xlabel('Cantidad')
plt.ylabel('Ruta')
plt.show()

# 6. Gráfico de barras para 'generic_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='generic_name', data=df_json, order=df_json['generic_name'].value_counts().index)
plt.title('Gráfico de barras de generic_name')
plt.xlabel('Cantidad')
plt.ylabel('Nombre genérico')
plt.show()

# 7. Gráfico de pastel para 'brand_name'
plt.figure(figsize=(10, 5))
df_json['brand_name'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Gráfico de pastel de brand_name')
plt.ylabel('')
plt.show()

# 8. Gráfico de barras para 'upc'
plt.figure(figsize=(10, 5))
sns.countplot(y='upc', data=df_json, order=df_json['upc'].value_counts().index)
plt.title('Gráfico de barras de upc')
plt.xlabel('Cantidad')
plt.ylabel('UPC')
plt.show()

# 9. Gráfico de barras para 'substance_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='substance_name', data=df_json, order=df_json['substance_name'].value_counts().index)
plt.title('Gráfico de barras de substance_name')
plt.xlabel('Cantidad')
plt.ylabel('Nombre de sustancia')
plt.show()

# 10. Gráfico de barras para 'product_type'
plt.figure(figsize=(10, 5))
sns.countplot(y='product_type', data=df_json, order=df_json['product_type'].value_counts().index)
plt.title('Gráfico de barras de product_type')
plt.xlabel('Cantidad')
plt.ylabel('Tipo de producto')
plt.show()

# 11. Histograma para 'dosage_form'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['dosage_form'].value_counts(), bins=30, kde=True)
plt.title('Histograma de dosage_form')
plt.xlabel('Forma de dosificación')
plt.ylabel('Frecuencia')
plt.show()

# 12. Gráfico de pastel para 'is_original_packager'
plt.figure(figsize=(10, 5))
df_json['is_original_packager'].value_counts().plot.pie(autopct='%1.1 ```python
f%%')
plt.title('Gráfico de pastel de is_original_packager')
plt.ylabel('')
plt.show()

# 13. Gráfico de barras para 'rxnorm'
plt.figure(figsize=(10, 5))
sns.countplot(y='rxnorm', data=df_json, order=df_json['rxnorm'].value_counts().index)
plt.title('Gráfico de barras de rxnorm')
plt.xlabel('Cantidad')
plt.ylabel('RxNorm')
plt.show()

# 14. Histograma para 'id'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['id'].value_counts(), bins=30, kde=True)
plt.title('Histograma de id')
plt.xlabel('ID')
plt.ylabel('Frecuencia')
plt.show()

# 15. Gráfico de pastel para 'application_number'
plt.figure(figsize=(10, 5))
df_json['application_number'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Gráfico de pastel de application_number')
plt.ylabel('')
plt.show()

# 16. Gráfico de barras para 'brand_name_suffix'
plt.figure(figsize=(10, 5))
sns.countplot(y='brand_name_suffix', data=df_json, order=df_json['brand_name_suffix'].value_counts().index)
plt.title('Gráfico de barras de brand_name_suffix')
plt.xlabel('Cantidad')
plt.ylabel('Sufijo de nombre de marca')
plt.show()

# 17. Gráfico de barras apiladas para 'manufacturer_name'
manufacturer_counts = df_json['manufacturer_name'].value_counts()
manufacturer_counts.plot(kind='bar', stacked=True)
plt.title('Gráfico de barras apiladas de manufacturer_name')
plt.xlabel('Fabricante')
plt.ylabel('Cantidad')
plt.show()

# 18. Histograma para 'route'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['route'].value_counts(), bins=30, kde=True)
plt.title('Histograma de route')
plt.xlabel('Ruta')
plt.ylabel('Frecuencia')
plt.show()

# 19. Gráfico de pastel para 'generic_name'
plt.figure(figsize=(10, 5))
df_json['generic_name'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Gráfico de pastel de generic_name')
plt.ylabel('')
plt.show()