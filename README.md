# Hybrid Code Clone Metrics + ML

Proyecto para calcular metricas de similitud entre dos fragmentos de codigo Python y entrenar modelos que clasifiquen el tipo de plagio detectado.

## Uso

```bash
python main.py
```

Comparar dos archivos:

```bash
python main.py --code-a original.py --code-b sospechoso.py
```

Obtener salida JSON:

```bash
python main.py --code-a original.py --code-b sospechoso.py --json
```

Generar la tabla supervisada del dataset:

```bash
python build_training_table.py
```

El CSV queda en:

```text
dataset/training_metrics.csv
```

## Embeddings semanticos

La tabla incluye la columna `code_embedding_similarity`.

Por defecto se calcula con un embedding semantico local y determinista basado en AST, llamadas, operadores y conceptos del codigo. No requiere internet ni dependencias extra.

Si quieres usar embeddings neuronales, instala `sentence-transformers` y define el modelo con la variable `CODE_EMBEDDING_MODEL` antes de regenerar la tabla:

```bash
pip install sentence-transformers
set CODE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
python build_training_table.py
```

Tambien puedes apuntar `CODE_EMBEDDING_MODEL` a una carpeta local con un modelo ya descargado.

Cada metrica recibe dos strings de codigo y devuelve un valor entre `0` y `1`, donde `1` significa mayor similitud.

## Familias implementadas

- Lexicas: Jaccard, coseno y distancia de edicion sobre tokens normalizados y tokens crudos.
- Sintacticas: similitud de tipos de nodos AST, secuencia AST y profundidad.
- Estructurales: perfil de control, complejidad ciclomatica aproximada y anidamiento.
- Estocasticas: cadena de Markov sobre estados semanticos, divergencia KL, divergencia JS y entropia.
- Semanticas ligeras: AST normalizado con identificadores y literales anonimizados.

## Funcion principal

```python
from metrics import extract_all_metrics

features = extract_all_metrics(code_a, code_b)
print(features["hybrid_score"])
```

## Entrenamiento supervisado

El proyecto genera una tabla de entrenamiento a partir de los pares en `dataset/no_plagiarism`, `dataset/type_1`, `dataset/type_2`, `dataset/type_3` y `dataset/type_4`.

Si necesitas reconstruir la clase negativa inicial:

```bash
python generate_no_plagiarism_dataset.py
```

```bash
python build_training_table.py
```

Despues entrena y evalua tres enfoques:

- `logistic`: un modelo multiclase unico.
- `forest`: un modelo multiclase basado en Random Forest.
- `forest_refined`: Random Forest multiclase con refinador binario para `TYPE_III` vs `TYPE_IV`.
- `specialists`: modelos binarios one-vs-rest, uno por clase.
- `hierarchical`: enfoque por etapas: primero `NO_PLAGIO` vs clon, despues tipo de clon, y finalmente un clasificador separado para `TYPE_III` vs `TYPE_IV`.

```bash
python train_models.py
```

La salida muestra accuracy, macro-F1, metricas por clase, matrices one-vs-rest por tipo, matriz de confusion global y feature importance. Por default usa `--feature-set core`, elige automaticamente el modelo con mejor macro-F1 y guarda el artefacto en:

```text
models/plagiarism_model.joblib
```

Opciones utiles:

```bash
python train_models.py --feature-set core
python train_models.py --feature-set all
python train_models.py --feature-set family
python train_models.py --model specialists
python train_models.py --model forest_refined
python train_models.py --model hierarchical
python train_models.py --feature-set all --model hierarchical
python train_models.py --folds 10
```

Para mejorar la separacion de `TYPE_III` y `TYPE_IV`, prueba primero:

```bash
python train_models.py --feature-set all --model hierarchical
```

## Prediccion de tipo de plagio

Una vez entrenado el modelo:

```bash
python predict_plagiarism.py --code-a dataset/type_3/pair_01_a.py --code-b dataset/type_3/pair_01_b.py
```

Salida JSON:

```bash
python predict_plagiarism.py --code-a original.py --code-b sospechoso.py --json
```

La prediccion incluye:

- tipo estimado: `NO_PLAGIO`, `TYPE_I`, `TYPE_II`, `TYPE_III` o `TYPE_IV`
- confianza del modelo
- probabilidades por tipo
- `hybrid_score`
- scores por familia de metricas

## Recomendacion de arquitectura

El score hibrido sigue siendo util como senal interpretable, pero ya no es la decision final. El flujo recomendado es:

1. Extraer todas las metricas.
2. Entrenar y evaluar modelos con validacion estratificada.
3. Elegir automaticamente el mejor por macro-F1.
4. Usar especialistas solo si superan al modelo multiclase.

Nota: la clase `NO_PLAGIO` incluida es un punto de partida balanceado con 30 pares negativos. Para resultados mas solidos, conviene agregar mas pares negativos reales y mas ejemplos de `TYPE_III`/`TYPE_IV`.
