# Respuesta a la revisión: factorial y diagnósticos adicionales

Los nuevos análisis son exploratorios, posteriores a inspección de prueba. Se conservan los modelos, las predicciones originales y el código v0.3.0. No se reentrena ni se selecciona por score de prueba. La ampliación se encuentra en `outputs/06_factorial`; no forma parte del DOI de software v0.3.0.

## 1. Confusión entre predictor y calibración

Se ejecutó un factorial completo: 5 demoras × 2 niveles × 2 predictores × 3 calibradores = 60 configuraciones. Los predictores fijo y adaptado almacenados se cruzan con estática ajustada a la demora, rolling global y ADH. Cada predictor genera sus propios residuos. Se mantienen el corte común de 101012 respuestas, los mismos casos de prueba, truncamiento inferior, ventana, reglas de llegada y parámetros de ADH.

A 72 h y 90%, los scores son:

| Predictor | Estática ajustada | Rolling | ADH |
|---|---:|---:|---:|
| Fijo | 375.39 | 328.01 | 317.48 |
| Adaptado | 346.75 | 312.66 | 303.20 |

La diferencia adaptado menos fijo con rolling es -15.35, IC puntual de bloques de 14 días [-24.67,-6.55]. Para ADH es -14.27 [-22.22,-6.86]. Las interacciones frente a estática son 13.29 [-1.25,30.61] y 14.37 [-2.70,34.20]: incluyen cero. Se reportan 270 filas de contrastes con 10000 réplicas y bloques 7/14/28, sin ajuste de multiplicidad y condicionadas a los modelos ajustados.

Este factorial aísla cambios de calibrador dentro de cada predictor residual; no descompone todos los componentes de CQR. Se mantiene explícita esa limitación y no se atribuye la diferencia CQR–rolling íntegramente a calibración.

## 2. Cronología local

Se elimina «locally prespecified» del abstract y del texto. Se describe un «local protocol recorded before execution». Se explicita la duración aproximada de cinco minutos, la mutabilidad de registros y la ausencia de preregistro o confirmación independiente. Los archivos históricos congelados conservan su redacción original para trazabilidad.

## 3. Declaración de IA

Se restaura OpenAI Codex desktop, identificador registrado gpt-6-astra, fechas 2–6 de octubre y ampliación del 7 de octubre de 2026, búsqueda, diseño, programación, ejecución, comprobación, figuras y redacción. Se distingue la revisión del autor ya confirmada para la versión precedente de la revisión todavía necesaria de estos resultados nuevos. La responsabilidad sigue siendo humana.

Referencia editorial consultada: https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation (7 de octubre de 2026).

## 4. Combinaciones y verificación

- Original: 5 demoras × 2 niveles × 4 reglas = 40 configuraciones verificadas en R.
- Ampliación anterior: 60 configuraciones homogéneas + 8 heterogéneas = 68 filas verificadas en R, incluyendo métricas CQR y ADH.
- CQR: reconstrucción de las 10 configuraciones de intervalos a partir de 20 modelos cuantílicos, no solo recálculo de métricas.
- Factorial nuevo: 60 filas y conteos reproducidos en R; las 30 celdas fijas coinciden con los extremos de intervalos guardados.
- ADH y otras reglas heterogéneas: comprobación de la implementación optimizada frente al bucle diario original, incluida la recursión de feedback. Esto verifica concordancia computacional, no una garantía teórica de ACI.

## 5. Demoras heterogéneas

El escenario alfabético se conserva como referencia y se complementa con 40 asignaciones aleatorias balanceadas, tres estaciones por demora, semilla 20261007. Se reportan métricas por asignación y medias, desviaciones y rangos. No se tratan las asignaciones como ciudades independientes ni su dispersión como un intervalo de confianza temporal.

## 6. Cobertura idéntica

No es redondeo: las tres reglas cubren 90493/102465 = 88.3160103450% al 90%. Por estación se ganan 1048 casos y se pierden 1048 respecto a global; con pesos iguales se ganan y pierden 3. Los conjuntos cubiertos sí difieren. Al 95% las coberturas son distintas. Se guardan conteos y desacuerdos exactos.

## 7. Cambio de distribución

Se comparan respuestas y errores absolutos de ambos predictores en calibración/prueba, globalmente, por mes del calendario y por trimestre. Se reportan cuantiles, diferencias de medias estandarizadas, distancias KS y Wasserstein, sin p-valores iid. La respuesta q90 pasa de 169 a 185; el error absoluto fijo q90, de 101.46 a 112.64. Se añade una figura de distribuciones empíricas. Son diagnósticos descriptivos compatibles con variación temporal; no prueban una causa única de subcobertura.

## 8. Referencias y enlaces

La selección de hojas remite a la sección que describe el entrenamiento, no a la tabla que solo muestra errores. Los DOI se presentan como identificadores indivisibles con hipervínculo; los enlaces largos llevan etiquetas legibles. La auditoría final comprueba destinos URI sin espacios, presencia de los 31 DOI bibliográficos y maquetación.
