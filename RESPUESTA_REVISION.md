# Respuesta a las observaciones

La ampliación es posterior a la inspección de prueba. No se presenta como protocolo confirmatorio ni como validación externa. Autor: Renato Quispe Vargas; Universidad Nacional del Altiplano.

| Observación | Acción y evidencia | Estado |
|---|---|---|
| 3.1 Comparadores | CQR y cuantiles sin calibrar, variante ACI diaria proyectada con feedback demorado; 68 métricas verificadas en R | Atendida con variante explícita; SPCI/EnbPI/CP-MDA no ejecutados |
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
| 4.2 Depósito | Materiales en https://github.com/rntvargas/beijing-pm25-delayed-feedback con código, tablas, predicciones, hashes y licencia de código | DOI archivístico pendiente |
| 4.3 Bibliografía | 31 referencias; versiones de congreso restauradas, DOI preprint distinguido; dos revisiones generales reemplazadas por trabajos ambientales | Atendida; no se afirma revisión exhaustiva de todos los textos completos |
| 4.4–4.5 PDF y unidades | Fuente recompilada, fórmulas y figuras revisadas; unidades mu g/m3 | Verificación visual documentada al finalizar |
| 4.6 MAE/RMSE | Interpretación del efecto de extremos y métricas por estación de los modelos originales y adaptados | Atendida |

Los resultados originales no se borraron. Los IC de la ampliación usan una semilla distinta registrada y por eso no reemplazan los límites del bootstrap original. La coincidencia de las conclusiones de sensibilidad se verifica por separado.

La ACI implementada proyecta alpha y procesa lotes diarios; no debe etiquetarse como reproducción sin modificaciones del algoritmo original. La comparación CQR frente a reglas residuales incluye diferencias de entrenamiento y modelado, no solo de calibración.
