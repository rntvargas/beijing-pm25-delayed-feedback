# Respuesta a las observaciones

La ampliación es posterior a la inspección de prueba. No se presenta como protocolo confirmatorio ni como validación externa. Autor: Renato Quispe Vargas; Universidad Nacional del Altiplano.

| Observación | Acción y evidencia | Estado |
|---|---|---|
| 3.1 Comparadores | CQR y cuantiles sin calibrar, heurística ADH inspirada en ACI con feedback demorado; 68 métricas verificadas en R | Atendida con variante explícita; SPCI/EnbPI/CP-MDA no ejecutados |
| 3.2 Adaptación | Selección por demora, tres ventanas, purga por llegada, tabla A/B/idealizado | Atendida |
| 3.3 Auditoría temporal | Diagrama, ledgers completos de residuos, auditoría diaria y 90 cuantiles reconstruidos | Atendida |
| 3.4 Cobertura | IC por bloques 7/14/28, diferencias emparejadas, bandas por familia de estaciones/trimestres | Atendida; no prueba exacta bajo no estacionariedad |
| 3.5 Agrupación | Global, por estación y peso uniforme por estación | Atendida |
| 3.6 Respuestas observadas | Tasas por estación/mes/hora/periodo/quintiles de covariables | Parcial: sin IPW ni identificación de MNAR |
| 3.7 Latencias | Escenario heterogéneo por estación con elegibilidad propia | Atendida como sensibilidad sintética; no latencias reales |
| 3.8 Utilidad | Distribución diaria, fracción de mejoras, intervalos más anchos, ganancias/pérdidas/neto de cobertura, estratos y costos hipotéticos | Atendida; no utilidad monetaria validada |
| 3.9 Replicación | Segundo periodo Beijing, 2015–2016 | Parcial: mismo archivo, no réplica externa independiente |
| 3.10 Originalidad | Contribución experimental, sin nuevo algoritmo/teorema ni garantía Q1 | Reformulada |
| 4.1 Metadatos | Nombre y universidad aportados por el autor | Pendientes correo, CRediT, financiación, conflictos, revisión final |
| 4.2 Depósito | Materiales en https://github.com/rntvargas/beijing-pm25-delayed-feedback con código, tablas, predicciones, hashes y licencia de código | Código congelado: https://doi.org/10.5281/zenodo.23171630 |
| 4.3 Bibliografía | 31 referencias; versiones de congreso restauradas, DOI preprint distinguido; dos revisiones generales reemplazadas por trabajos ambientales | Atendida; no se afirma revisión exhaustiva de todos los textos completos |
| 4.4–4.5 PDF y unidades | Fuente recompilada, fórmulas y figuras revisadas; unidades mu g/m3 | Verificación visual documentada al finalizar |
| 4.6 MAE/RMSE | Interpretación del efecto de extremos y métricas por estación de los modelos originales y adaptados | Atendida |

Los resultados originales no se borraron. Los IC de la ampliación usan una semilla distinta registrada y por eso no reemplazan los límites del bootstrap original. La coincidencia de las conclusiones de sensibilidad se verifica por separado.

La ACI implementada proyecta alpha y procesa lotes diarios; no debe etiquetarse como reproducción sin modificaciones del algoritmo original. La comparación CQR frente a reglas residuales incluye diferencias de entrenamiento y modelado, no solo de calibración.

## Cinco prioridades antes del envío: revisión v0.3.0

1. CQR: ecuaciones, pérdida, entrenamiento, truncamiento, ordenación, corte, score firmado, rango y reglas de aserción exactas; 10 configuraciones reconstruidas con error máximo <6e-14.
2. ACI adaptado: renombrado heurística ADH inspirada en ACI, sin atribución de garantías; identificadores históricos conservados para trazabilidad.
3. Score exploratorio: 10000 réplicas emparejadas, bloques 7/14/28, 267 filas, IC puntuales condicionales a modelos ajustados, sin control global de multiplicidad.
4. Código congelado: DOI https://doi.org/10.5281/zenodo.23171630, versión 0.3.0; archivo y suma comprobados en Zenodo. El DOI corresponde al código, no al artículo ni al conjunto completo de modelos.
5. Separación visual: recuadros y secciones P/E/S. P es preespecificación local; no se afirma confirmación independiente. E corresponde a exploración posterior y S a sensibilidad.

El PDF de 22 páginas se recompiló y revisó visualmente. Se conservaron las 31 referencias y los resultados originales.
