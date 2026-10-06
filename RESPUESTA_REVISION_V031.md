# Respuesta a las observaciones de la revisión v0.3.1

Se trata de una revisión editorial y de auditoría. No se reentrenaron modelos, no se modificaron predicciones, no se seleccionaron hiperparámetros con prueba ni se reemplazaron los resultados originales. La versión de software congelada en Zenodo sigue siendo v0.3.0; el material editorial y la nueva auditoría complementaria se publican en GitHub v0.3.1.

| Observación | Corrección y evidencia | Estado |
|---|---|---|
| 2.1 Calibración común | Se demuestra v < 2016-02-23 y d <= 168 h implica llegada < 2016-03-01. Último objetivo: 22 de febrero 23:00; última llegada a 168 h: 29 de febrero 23:00. 103000 respuestas observadas menos 1988 por corte = 101012. No se eliminan filas por características faltantes. | Verificada |
| 2.1 Columnas y modelos | Existen las 45 columnas fuente; quedan 73/70/66/64/62 columnas codificadas según demora. Se auditaron 20 regresores cuantílicos que forman 10 configuraciones de intervalos; misma clave y hash de respuestas para todos. | Verificada; el comentario confundía regresores con configuraciones |
| 2.2 Nomenclatura | Nombre uniforme: CQR with delay-specific training; se permite la abreviatura CQR una vez definida. Se conservan las claves históricas de archivos para trazabilidad. | Atendida |
| 3.1 Objetivos | Abstract, mapa principal, discusión y conclusión separan recalibración del predictor fijo (P) de comparación exploratoria de pipelines (E). | Atendida |
| 3.2 Multiplicidad | Los títulos de tablas indican intervalos pointwise y ausencia de ajuste simultáneo de multiplicidad. | Atendida |
| 3.3 Bootstrap circular | Se explica la frecuencia uniforme de inicios, el empalme artificial, los posibles sesgos en ambos sentidos y las diferencias con alternativas no implementadas. No se afirma estacionariedad ni validez exacta. | Atendida mediante justificación y límites |
| 3.4 Réplicas | 1000 preserva el protocolo original; 10000 reduce error Monte Carlo en límites exploratorios, sin reforzar validez o estatus confirmatorio. Coberturas previas conservan 1000. | Atendida |
| 3.5 Reproducción | Original: NumPy 2.3.5, default_rng/PCG64, semilla 20261003, flujo continuo en orden 7/14/28, inicios con reemplazo, módulos y truncamiento; percentiles lineales sin redondeo previo. Extensión: 20261006+L; cobertura: 20261005+L. | Atendida |
| 4.1 Interpretación | CQR tiene menor score observado a 72 h, pero cobertura puntual inferior a nominal; ADH se aproxima más al nominal con mayor amplitud y score. | Atendida |
| 4.2 Diferencia | Reducción descriptiva 21.2%, con advertencia de comparación de pipelines junto a la tabla de contrastes. Se distingue rolling global 328.01 de ponderación por estación 328.05. | Atendida |
| 4.3 Cobertura | La tabla exploratoria incluye IC de cobertura. CQR al 90%: 88.91% [86.51,91.18] con bloques de 14 días. Incluir el nominal no prueba calibración. | Atendida |
| 5.1 Disponibilidad | Se distingue UCI, código/documentación Zenodo, y datos derivados/modelos/predicciones/manuscrito de GitHub. Se especifican rutas, versión y commit. | Atendida; no se copió la afirmación incorrecta de que Zenodo contiene modelos/datos |
| 5.2 IA | Se declara OpenAI Codex desktop, identificador registrado gpt-6-astra, periodo 2–6 octubre 2026, alcance y falta de identificador inmutable de backend. Se distingue verificación computacional de revisión personal del autor. | Parcial: aprobación y verificación humana por confirmar |
| 5.3 Declaraciones | No se inventan correo de correspondencia, CRediT, financiación ni conflictos. | Pendientes de respuesta del autor |
| 6.1 Mapa principal | Tabla de estado, datos, comparación y resultado P/E/S. | Atendida |
| 6.2 Título | Latency-aware PM2.5 interval forecasting under simulated measurement and feedback delays: a reproducible Beijing benchmark. Se conserva el carácter simulado. | Atendida |
| 6.3 Cronología | Protocolo creado 2026-10-03 01:12:39.1505342 UTC; selección con hash 01:15:19.6009483; primer comando de prueba registrado 01:15:49.776. El hash coincide con la escritura inicial. Doce comparaciones de archivos contra v0.2.0/v0.3.0 públicas coinciden. | Atendida con límites explícitos de evidencia local |

El archivo `PROTOCOL_PROVENANCE_AUDIT.json` conserva la cronología y las comprobaciones de integridad. Los registros locales son modificables y no equivalen a una autoridad independiente de sellado de tiempo. No permiten probar la inexistencia de cálculos no registrados. No se inventó una fecha adicional de congelamiento independiente.

La política editorial mantiene la responsabilidad humana y exige transparencia sobre el uso de IA: [Springer Nature, AI use](https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation). La declaración de materiales distingue sus ubicaciones: [Springer Nature, data availability statements](https://www.springernature.com/gp/authors/research-data-policy/data-availability-statements). Consulta realizada el 6 de octubre de 2026; la política específica de la revista elegida queda por revisar.

No se adoptó la frase sugerida que atribuye al autor toda la ejecución y verificación independiente: las herramientas fueron operadas por el asistente y esa revisión humana no ha sido confirmada. Tampoco se considera que el DOI del software sea un DOI del artículo o de todo el paquete de investigación.
