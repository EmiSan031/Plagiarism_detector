# Hybrid Code Clone Metrics

Proyecto base para calcular metricas de similitud entre dos fragmentos de codigo Python.

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

- Lexicas: Jaccard, coseno y distancia de edicion sobre tokens normalizados.
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
