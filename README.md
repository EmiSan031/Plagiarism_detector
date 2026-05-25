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

El proyecto genera una tabla de entrenamiento a partir de los pares en `dataset/type_1`, `dataset/type_2`, `dataset/type_3` y `dataset/type_4`.

```bash
python build_training_table.py
```

Despues entrena y evalua tres enfoques:

- `logistic`: un modelo multiclase unico.
- `forest`: un modelo multiclase basado en Random Forest.
- `specialists`: cuatro modelos binarios one-vs-rest, uno por tipo de plagio.

```bash
python train_models.py
```

La salida muestra accuracy, macro-F1 y matriz de confusion. Por default usa `--feature-set core`, elige automaticamente el modelo con mejor macro-F1 y guarda el artefacto en:

```text
models/plagiarism_model.joblib
```

Opciones utiles:

```bash
python train_models.py --feature-set core
python train_models.py --feature-set all
python train_models.py --feature-set family
python train_models.py --model specialists
python train_models.py --folds 10
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

- tipo estimado: `TYPE_I`, `TYPE_II`, `TYPE_III` o `TYPE_IV`
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

Nota: el dataset actual solo contiene pares con plagio/clones. Para detectar tambien "no plagio", agrega ejemplos negativos y una etiqueta adicional como `NO_PLAGIO`.
