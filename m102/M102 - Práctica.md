# Módulo 1.2 — Práctica: representar conocimiento para inspeccionar o liberar una pista

> **Inteligencia Artificial**  
> **Módulo 1:** Sistemas cognitivos y representación del conocimiento  
> **Tema:** Arquitecturas de representación del conocimiento

## Propósito

Construir varias representaciones del mismo problema para observar cómo cambia lo que un sistema puede expresar, consultar, inferir, explicar y decidir.

La práctica extiende el caso didáctico **“inspeccionar o liberar una pista”**. El objetivo no es diseñar un procedimiento aeroportuario, sino utilizar un dominio comprensible para comparar arquitecturas de conocimiento.

> **Advertencia:** todos los datos, reglas, umbrales y utilidades son hipotéticos. No representan procedimientos operacionales ni sustituyen normativa, certificación, autoridades o criterio experto.

---

## 1. Resultados de aprendizaje

Al concluir la práctica, el participante podrá:

1. distinguir hechos, observaciones, creencias, reglas, restricciones y decisiones;
2. representar el mismo dominio mediante distintas arquitecturas;
3. formular conocimiento con lógica proposicional y lógica de predicados;
4. ejecutar manualmente reglas mediante encadenamiento hacia adelante;
5. construir marcos y triples sujeto–predicado–objeto;
6. proponer una ontología mínima con clases, relaciones y restricciones;
7. diferenciar mundo abierto, mundo cerrado e incertidumbre probabilística;
8. diseñar una arquitectura híbrida con trazabilidad;
9. explicar qué inferencias permite cada representación y cuáles no;
10. justificar una elección arquitectónica a partir de requisitos.

---

## 2. Modalidad y tiempo sugerido

| Elemento | Sugerencia |
|---|---|
| modalidad | equipos de 3 o 4 participantes |
| duración | 90 a 120 minutos |
| materiales | notas 1.1 y 1.2, glosario 1.2, editor de texto o cuaderno |
| producto | expediente de representación y propuesta de arquitectura |
| cierre | exposición de 5 minutos por equipo |

### Roles sugeridos

- **modelador:** mantiene consistencia entre las representaciones;
- **analista lógico:** revisa reglas, inferencias y restricciones;
- **responsable de datos:** verifica identidad, fuentes, tiempo y unidades;
- **auditor:** busca ambigüedades, contradicciones y conclusiones no justificadas.

Los roles pueden rotarse después de la actividad 4.

---

## 3. Escenario de trabajo

Un sistema de apoyo recibe información acerca de dos pistas. Debe organizar el conocimiento disponible y recomendar si es necesario **inspeccionar**, **mantener el bloqueo** o **solicitar información adicional**.

El sistema no tiene autoridad para liberar una pista. La recomendación debe llegar a una persona autorizada junto con su evidencia y explicación.

### 3.1 Entidades

| Identificador | Tipo | Descripción |
|---|---|---|
| `P09` | pista | pista principal |
| `P14` | pista | pista secundaria |
| `S1` | sensor | sensor que monitorea `P09` |
| `S2` | sensor | sensor que monitorea `P14` |
| `A101` | alerta | alerta emitida por `S1` |
| `A102` | alerta | alerta emitida por `S2` |
| `I51` | inspección | inspección más reciente de `P09` |
| `I52` | inspección | inspección más reciente de `P14` |
| `O7` | operador | persona responsable de revisar la recomendación |

### 3.2 Observaciones iniciales

| ID | Momento | Fuente | Observación | Valor | Calidad declarada |
|---|---|---|---|---:|---|
| `OBS-01` | 08:00 | `S1` | estado del sensor | activo | verificado |
| `OBS-02` | 08:01 | `S1` | alerta de posible objeto | presente | confianza 0.90 |
| `OBS-03` | 08:02 | `S1` | visibilidad local | baja | pertenencia 0.75 |
| `OBS-04` | 08:00 | `S2` | estado del sensor | activo | no verificado |
| `OBS-05` | 08:01 | `S2` | alerta de posible objeto | presente | confianza 0.60 |
| `OBS-06` | 07:45 | `I51` | resultado de inspección de `P09` | sin hallazgos | válida hasta 08:00 |
| `OBS-07` | 07:50 | `I52` | resultado de inspección de `P14` | sin hallazgos | válida hasta 08:20 |

### 3.3 Supuestos

1. Una alerta de un sensor verificado produce una **sospecha**, no una confirmación.
2. Una inspección vencida no prueba contaminación; indica que la evidencia anterior ya no basta.
3. Un sensor no verificado no debe producir por sí solo una recomendación de liberación.
4. Una recomendación debe incluir evidencia, reglas aplicadas y versión del conocimiento.
5. La ausencia de una alerta no significa necesariamente que la pista esté libre.

---

## 4. Actividad 1 — Separar realidad, observación y representación

### Objetivo

Evitar que el sistema confunda una señal con el estado real del mundo.

### Instrucción

Clasificar cada elemento como:

- **estado real:** condición del mundo, aunque no sea directamente observable;
- **observación:** salida de un sensor, reporte o interacción;
- **creencia:** estimación del sistema;
- **regla:** conocimiento general;
- **acción:** intervención o recomendación;
- **meta o restricción:** condición que orienta o limita la decisión.

| Enunciado | Clasificación | Justificación |
|---|---|---|
| `P09` contiene un objeto extraño |  |  |
| `S1` emitió `A101` |  |  |
| la probabilidad de contaminación de `P09` es 26.9 % |  |  |
| toda alerta validada requiere revisión |  |  |
| solicitar una inspección de `P09` |  |  |
| ninguna recomendación libera automáticamente una pista |  |  |
| la visibilidad de `P09` es baja con grado 0.75 |  |  |

### Preguntas de reflexión

1. ¿Qué error se cometería al convertir directamente `A101` en “la pista está contaminada”?
2. ¿Qué diferencia existe entre confianza del sensor y pertenencia a “visibilidad baja”?
3. ¿Qué elementos son descriptivos y cuáles son normativos?

### Entregable 1

Tabla clasificada y una explicación de no más de 100 palabras acerca de la diferencia entre **observar** y **conocer**.

---

## 5. Actividad 2 — Representación tabular

### Objetivo

Reconocer fortalezas y límites de una representación relacional.

### 5.1 Propuesta inicial

Diseñar las siguientes tablas:

```text
PISTA(id_pista, estado_operativo, actualizada_en)
SENSOR(id_sensor, id_pista, estado, verificado_en)
ALERTA(id_alerta, id_sensor, tipo, confianza, ocurrida_en)
INSPECCION(id_inspeccion, id_pista, resultado, realizada_en, valida_hasta)
RECOMENDACION(id_recomendacion, id_pista, accion, creada_en, version_reglas)
```

### 5.2 Trabajo del equipo

1. Identificar las claves primarias.
2. Identificar las claves foráneas.
3. Agregar campos para fuente y procedencia.
4. Decidir cómo representar un dato desconocido.
5. Decidir si `estado_operativo` debe almacenarse o calcularse.

### Matriz de análisis

| Pregunta | Respuesta del equipo |
|---|---|
| ¿Qué consultas son sencillas? |  |
| ¿Qué inferencias no aparecen por sí solas? |  |
| ¿Cómo se registra una contradicción? |  |
| ¿Cómo se representa vigencia temporal? |  |
| ¿Qué ocurre si dos fuentes usan nombres distintos para la misma pista? |  |

### Entregable 2

Esquema tabular corregido y tres restricciones de integridad.

### Punto conceptual

Una tabla organiza datos, pero no constituye automáticamente una arquitectura completa de conocimiento. Las relaciones semánticas, reglas e inferencias deben definirse de forma adicional.

---

## 6. Actividad 3 — Lógica proposicional

### Objetivo

Formalizar condiciones simples y analizar sus límites.

### 6.1 Proposiciones

Para `P09`, se definen:

| Símbolo | Significado |
|---|---|
| $A$ | `S1` produjo una alerta |
| $V$ | `S1` está verificado |
| $E$ | la inspección de `P09` está vigente |
| $R$ | `P09` requiere revisión |
| $B$ | debe mantenerse bloqueada la liberación |

### 6.2 Reglas

$$
(A\land V)\rightarrow R
$$

$$
R\rightarrow B
$$

$$
\neg E\rightarrow R
$$

### 6.3 Datos del caso

$$
A=verdadero,qquad V=verdadero,qquad E=falso
$$

### Trabajo del equipo

1. Determinar el valor de $R$.
2. Determinar el valor de $B$.
3. Construir la tabla de verdad de $(A\land V)\rightarrow R$.
4. Explicar por qué $A\rightarrow R$ sería una regla más débil desde el punto de vista de seguridad de la información.
5. Identificar qué parte del dominio se pierde al utilizar símbolos sin argumentos.

### Pregunta crítica

¿La expresión $\neg E\rightarrow R$ afirma que existe contaminación? Explicar por qué sí o por qué no.

### Entregable 3

Valores inferidos, tabla de verdad y una lista con tres limitaciones de la lógica proposicional para este dominio.

---

## 7. Actividad 4 — Lógica de predicados

### Objetivo

Generalizar reglas para múltiples pistas, sensores y observaciones.

### 7.1 Predicados

```text
Pista(x)
Sensor(s)
monitorea(s,x)
alerta(s)
verificado(s)
inspeccionVigente(x)
requiereRevision(x)
bloquearLiberacion(x)
```

### 7.2 Reglas generales

$$
\forall s\forall x\;
alerta(s)\land verificado(s)\land monitorea(s,x)
\rightarrow requiereRevision(x)
$$

$$
\forall x\;
requiereRevision(x)\rightarrow bloquearLiberacion(x)
$$

$$
\forall x\;
Pista(x)\land\neg inspeccionVigente(x)
\rightarrow requiereRevision(x)
$$

### 7.3 Hechos

```text
Pista(P09)
Pista(P14)
Sensor(S1)
Sensor(S2)
monitorea(S1,P09)
monitorea(S2,P14)
alerta(S1)
alerta(S2)
verificado(S1)
inspeccionVigente(P14)
```

### Trabajo del equipo

1. Derivar las conclusiones justificadas para `P09`.
2. Derivar las conclusiones justificadas para `P14`.
3. Explicar por qué no puede inferirse `verificado(S2)`.
4. Explicar por qué ausencia de `inspeccionVigente(P09)` no equivale necesariamente a $\neg inspeccionVigente(P09)$ bajo mundo abierto.
5. Reescribir la tercera regla para utilizar el predicado explícito `inspeccionVencida(x)`.

### Extensión

Agregar:

```text
requiereConfirmacionHumana(x)
```

y formular una regla que lo derive cuando existe una alerta de un sensor no verificado.

### Entregable 4

Base de hechos ampliada, cuatro reglas generales y conclusiones separadas en:

- demostradas;
- no demostradas;
- desconocidas.

---

## 8. Actividad 5 — Reglas de producción y encadenamiento

### Objetivo

Ejecutar una base de reglas y construir una explicación reproducible.

### 8.1 Base de reglas

```text
R1:
SI alerta(s) Y verificado(s) Y monitorea(s,x)
ENTONCES sospechaContaminacion(x)

R2:
SI sospechaContaminacion(x) Y activoCritico(x)
ENTONCES requiereInspeccion(x)

R3:
SI requiereInspeccion(x)
ENTONCES bloquearLiberacion(x)

R4:
SI alerta(s) Y NO verificado(s) Y monitorea(s,x)
ENTONCES requiereConfirmacionHumana(x)

R5:
SI inspeccionVencida(x)
ENTONCES requiereInspeccion(x)
```

> **Atención:** `NO verificado(s)` es deliberadamente ambiguo. El equipo debe decidir si significa negación explícita, verificación vencida o ausencia de registro. En una implementación formal conviene sustituirlo por un predicado observable, como `verificacionVencida(s)` o `estadoVerificacion(s,desconocido)`.

### 8.2 Hechos iniciales para `P09`

```text
alerta(S1)
verificado(S1)
monitorea(S1,P09)
activoCritico(P09)
inspeccionVencida(P09)
```

### 8.3 Tabla de ejecución

Completar una fila por iteración:

| Iteración | Hechos disponibles | Regla activada | Hecho nuevo | Justificación |
|---:|---|---|---|---|
| $I_0$ | hechos iniciales |  |  |  |
| $I_1$ |  |  |  |  |
| $I_2$ |  |  |  |  |
| $I_3$ |  |  |  |  |
| $I^*$ |  | ninguna nueva |  | punto fijo |

### 8.4 Resolución de conflictos

Supongamos que también existe:

```text
R6:
SI inspeccionRecienteSinHallazgos(x)
ENTONCES candidataLiberacion(x)
```

y la base deriva simultáneamente:

```text
bloquearLiberacion(P09)
candidataLiberacion(P09)
```

Responder:

1. ¿Existe una contradicción lógica o un conflicto operacional?
2. ¿Debe una regla tener prioridad sobre otra?
3. ¿Qué información temporal falta?
4. ¿Qué acción segura debe tomar el sistema mientras se resuelve?
5. ¿Cómo debe registrarse el conflicto?

### Entregable 5

Tabla de ejecución, grafo de prueba de `bloquearLiberacion(P09)` y política de resolución de conflictos.

---

## 9. Actividad 6 — Marcos o frames

### Objetivo

Agrupar información contextual sobre entidades y situaciones típicas.

### 9.1 Frame `Pista`

```yaml
Frame: Pista
  id:
  estado_operativo:
  sensores:
  inspeccion_mas_reciente:
  restricciones:
  responsable_de_autorizacion:
  valor_por_defecto:
```

### 9.2 Frame `Alerta`

```yaml
Frame: Alerta
  id:
  sensor:
  pista:
  tipo:
  confianza:
  ocurrida_en:
  fuente:
  validada:
  acciones_sugeridas:
```

### Trabajo del equipo

1. Completar ambos frames con los datos de `P09` y `A101`.
2. Indicar qué ranuras son obligatorias.
3. Proponer un valor por defecto y una excepción.
4. Evitar que un valor por defecto se confunda con un dato observado.
5. Agregar una ranura que conserve procedencia.

### Preguntas de reflexión

- ¿Qué información queda más legible en un frame que en una lista de predicados?
- ¿Cómo se heredarían propiedades desde `ActivoCritico` hacia `Pista`?
- ¿Qué riesgo presentan los valores por defecto en un dominio crítico?

### Entregable 6

Frames completos y una explicación de cuándo un frame resulta preferible a una tabla plana.

---

## 10. Actividad 7 — Triples y grafo de conocimiento

### Objetivo

Representar entidades y relaciones de forma conectada.

### 10.1 Convertir a triples

Completar al menos doce afirmaciones:

| Sujeto | Predicado | Objeto |
|---|---|---|
| `P09` | `rdf:type` | `Pista` |
| `S1` | `rdf:type` | `Sensor` |
| `S1` | `monitorea` | `P09` |
| `A101` | `emitidaPor` | `S1` |
| `A101` | `ocurridaEn` | `08:01` |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

### 10.2 Contextualizar una afirmación

El triple:

```text
A101 — confianza — 0.90
```

no aclara:

- quién calculó la confianza;
- con qué versión del modelo;
- si es probabilidad calibrada;
- a qué tipo de alerta corresponde;
- durante qué periodo resulta válida.

Proponer una estructura adicional para registrar estos datos. Puede utilizarse un nodo de observación, una afirmación identificable o un grafo nombrado.

### 10.3 Consulta conceptual

Escribir en lenguaje natural los patrones necesarios para responder:

> ¿Qué pistas tienen una alerta producida por un sensor verificado y carecen de una inspección vigente?

### Entregable 7

Doce triples, diagrama del grafo y patrón de consulta.

---

## 11. Actividad 8 — Ontología mínima

### Objetivo

Definir el vocabulario, las jerarquías y las restricciones del dominio.

### 11.1 Clases iniciales

```text
Activo
ActivoCritico
Pista
Dispositivo
Sensor
Observacion
Alerta
Inspeccion
Persona
Operador
Recomendacion
```

### 11.2 Jerarquías

Completar:

$$
Pista\sqsubseteq \underline{\hspace{4cm}}
$$

$$
Sensor\sqsubseteq \underline{\hspace{4cm}}
$$

$$
Alerta\sqsubseteq \underline{\hspace{4cm}}
$$

$$
Operador\sqsubseteq \underline{\hspace{4cm}}
$$

### 11.3 Propiedades

| Propiedad | Dominio | Rango | Descripción |
|---|---|---|---|
| `monitorea` | `Sensor` | `Activo` | sensor asociado con un activo |
| `emitidaPor` | `Alerta` | `Sensor` | sensor que produjo la alerta |
| `seRefiereA` |  |  |  |
| `generadaPor` |  |  |  |
| `requiereAutorizacionDe` |  |  |  |

### 11.4 Restricciones propuestas

Expresar al menos cuatro:

1. toda alerta debe ser emitida por algún sensor;
2. todo sensor monitorea al menos un activo;
3. ninguna `Pista` es una `Persona`;
4. toda recomendación debe referirse a un activo;
5. toda liberación propuesta requiere una persona autorizada.

### 11.5 Inferencias esperadas

Si:

$$
Pista\sqsubseteq ActivoCritico
$$

y:

$$
Pista(P09)
$$

entonces:

$$
ActivoCritico(P09)
$$

Responder:

- ¿la afirmación debe almacenarse o puede inferirse?
- ¿qué ventajas tiene materializarla?
- ¿qué ocurre si cambia la jerarquía?

### Entregable 8

Diagrama de clases, tabla de propiedades, cuatro restricciones y tres inferencias esperadas.

---

## 12. Actividad 9 — Mundo abierto, mundo cerrado y negación

### Objetivo

Evitar conclusiones incorrectas producidas por ausencia de información.

### Casos

| Situación registrada | Mundo cerrado | Mundo abierto |
|---|---|---|
| no aparece `verificado(S2)` | se trata como no verificado | permanece desconocido |
| no aparece una alerta para `P09` | se trata como sin alerta | no se sabe si existió una alerta |
| no existe una orden activa en el sistema autoritativo | puede tratarse como inexistente | depende de la cobertura de fuentes |
| no se registró objeto extraño | se trata como ausente | no existe evidencia suficiente |

### Trabajo del equipo

Para cada afirmación, seleccionar el supuesto adecuado y justificarlo:

1. “No existe una inspección pendiente en el sistema de órdenes oficial”.
2. “No existe un objeto extraño en la pista”.
3. “El operador no tiene una certificación vigente”.
4. “No se recibió una alerta durante el último minuto”.
5. “La fuente externa no menciona a `P14`”.

### Punto conceptual

La arquitectura puede utilizar supuestos diferentes para conjuntos de datos distintos. La decisión debe documentarse por fuente y propósito, no aplicarse globalmente sin análisis.

### Entregable 9

Matriz con el supuesto elegido, justificación y riesgo de una elección incorrecta.

---

## 13. Actividad 10 — Representación probabilística

### Objetivo

Incorporar incertidumbre sin convertirla en una afirmación lógica absoluta.

### 13.1 Datos para `S1`

$$
P(C)=0.02
$$

$$
P(alerta\mid C)=0.90
$$

$$
P(alerta\mid L)=0.05
$$

donde:

- $C$: existe posible contaminación;
- $L$: la pista está libre.

Tras una alerta:

$$
P(C\mid alerta)=
\frac{P(alerta\mid C)P(C)}
{P(alerta\mid C)P(C)+P(alerta\mid L)P(L)}
$$

### Trabajo del equipo

1. Calcular el posterior.
2. Explicar por qué el resultado no es un hecho lógico `contaminada(P09)`.
3. Proponer cómo almacenar el posterior con su fuente, momento y versión.
4. Comparar las siguientes expresiones:

```text
requiereInspeccion(P09)
P(contaminacion(P09) | alerta) = 0.269
μ_visibilidadBaja(P09) = 0.75
```

5. Indicar cuál representa:
   - una conclusión normativa;
   - incertidumbre sobre un evento;
   - gradualidad de un concepto.

### Extensión: utilidad esperada

Usar:

| Acción y estado | Utilidad |
|---|---:|
| liberar si está libre | $+10$ |
| liberar si existe contaminación | $-1000$ |
| inspeccionar | $-8$ |

Calcular:

$$
EU(liberar)=(1-p)(10)+p(-1000)
$$

$$
EU(inspeccionar)=-8
$$

Responder:

- ¿qué conocimiento pertenece a la representación del dominio?
- ¿qué valores pertenecen al modelo de decisión?
- ¿qué restricciones no deberían reducirse a utilidad?

### Entregable 10

Cálculo, interpretación y propuesta de representación para una creencia probabilística trazable.

---

## 14. Actividad 11 — Representación vectorial

### Objetivo

Comprender qué aporta una representación aprendida y por qué no sustituye por sí sola la semántica explícita.

Supongamos que un modelo convierte observaciones en vectores:

$$
e(OBS\text{-}02)=[0.82,-0.14,0.55,0.31]
$$

$$
e(CasoHistorico17)=[0.79,-0.10,0.51,0.35]
$$

La cercanía indica que ambas observaciones presentan patrones similares.

### Trabajo del equipo

1. Proponer un uso válido de la similitud.
2. Proponer un uso inválido o peligroso.
3. Explicar por qué cercanía no implica identidad ni causalidad.
4. Determinar qué metadatos deben acompañar al vector.
5. Diseñar una regla que requiera validación antes de convertir un candidato vectorial en símbolo.

Ejemplo:

```text
SI similitud_visual(o, caso) > umbral
ENTONCES candidato(o, tipo_del_caso)

SI candidato(o,t) Y verificacion_externa(o,t)
ENTONCES observacion_clasificada(o,t)
```

### Entregable 11

Diagrama de la interfaz vector–símbolo y dos salvaguardas.

---

## 15. Actividad 12 — Procedencia, tiempo y versiones

### Objetivo

Construir explicaciones que puedan reproducirse y auditarse.

### Expediente mínimo de una afirmación

| Campo | Ejemplo |
|---|---|
| afirmación | `alerta(S1)` |
| fuente | `OBS-02` |
| generada por | modelo de sensor `MS-4` |
| versión | `4.2` |
| tiempo de observación | `08:01` |
| tiempo de registro | `08:01:03` |
| vigencia | hasta nueva lectura o inspección |
| confianza | `0.90` |
| responsable del sistema | área técnica |

### Trabajo del equipo

Construir la cadena de trazabilidad de:

```text
bloquearLiberacion(P09)
```

Debe incluir:

1. observaciones originales;
2. transformaciones;
3. reglas aplicadas;
4. versión de la base de conocimiento;
5. persona o rol que revisa;
6. acción finalmente autorizada;
7. evidencia posterior que confirma o corrige la recomendación.

### Cambio de versión

La regla `R1` cambia:

```text
Versión 1:
alerta(s) ∧ verificado(s) ∧ monitorea(s,x)
→ sospechaContaminacion(x)

Versión 2:
alerta(s) ∧ verificado(s) ∧ monitorea(s,x) ∧ calidadLectura(s,alta)
→ sospechaContaminacion(x)
```

Responder:

- ¿las conclusiones anteriores deben recalcularse?
- ¿cómo se conserva la explicación original?
- ¿qué versión debe utilizar una auditoría histórica?

### Entregable 12

Cadena de procedencia y política de versionado en cinco reglas breves.

---

## 16. Actividad integradora — Diseñar la arquitectura

### Objetivo

Seleccionar representaciones según la función que deben cumplir.

### 16.1 Requisitos

La solución debe:

1. recibir observaciones de sensores;
2. identificar pistas, sensores y alertas;
3. conservar datos temporales y procedencia;
4. representar reglas explícitas;
5. actualizar una creencia probabilística;
6. detectar conflictos;
7. explicar recomendaciones;
8. requerir autorización humana;
9. aprender de casos históricos sin convertir similitud en certeza;
10. permitir consultas sobre entidades y relaciones.

### 16.2 Matriz de selección

Completar:

| Necesidad | Representación propuesta | Componente | Justificación | Riesgo |
|---|---|---|---|---|
| almacenar observaciones |  |  |  |  |
| identidad y relaciones |  |  |  |  |
| reglas operativas |  |  |  |  |
| incertidumbre |  |  |  |  |
| conceptos graduales |  |  |  |  |
| similitud con históricos |  |  |  |  |
| restricciones semánticas |  |  |  |  |
| selección de acción |  |  |  |  |
| explicación y auditoría |  |  |  |  |

### 16.3 Arquitectura de referencia

El equipo puede partir de la siguiente estructura, pero debe justificar cualquier cambio:

```text
Sensores y reportes
        │
        ▼
Validación y normalización
        │
        ├──────────────► almacén temporal y procedencia
        │
        ▼
Extracción de entidades y observaciones
        │
        ├──────────────► representación vectorial para similitud
        │
        ▼
Grafo de conocimiento + ontología
        │
        ├──────────────► motor de reglas
        ├──────────────► modelo probabilístico
        └──────────────► detector de conflictos
                               │
                               ▼
                    recomendación explicada
                               │
                               ▼
                     revisión y autorización
                               │
                               ▼
                    acción y retroalimentación
```

### 16.4 Contrato entre componentes

Definir para cada flecha:

- formato de entrada;
- significado;
- unidad;
- rango o dominio permitido;
- comportamiento ante datos faltantes;
- versión;
- responsable;
- condición de rechazo.

### 16.5 Consulta final

La arquitectura debe responder:

> ¿Por qué el sistema recomienda inspeccionar `P09`, qué evidencia respalda la recomendación, qué incertidumbre permanece y quién debe autorizar la acción?

### Entregable integrador

1. Diagrama de arquitectura.
2. Matriz de selección completada.
3. Contratos entre componentes.
4. Ejemplo de explicación final.
5. Tres riesgos y su mitigación.

---

## 17. Comparación de representaciones

Completar después de terminar todas las actividades:

| Representación | Unidad principal | Inferencia característica | Fortaleza | Limitación | Uso propuesto |
|---|---|---|---|---|---|
| tabla relacional | fila | consulta y restricciones |  |  |  |
| lógica proposicional | proposición | deducción |  |  |  |
| lógica de predicados | predicado | unificación y deducción |  |  |  |
| reglas de producción | regla | encadenamiento |  |  |  |
| frame | objeto con ranuras | herencia y valores por defecto |  |  |  |
| grafo | triple o arista | recorrido y patrones |  |  |  |
| ontología | axioma | clasificación y consistencia |  |  |  |
| modelo probabilístico | variable aleatoria | actualización de creencias |  |  |  |
| modelo difuso | grado de pertenencia | inferencia gradual |  |  |  |
| embedding | vector | similitud y recuperación |  |  |  |

### Pregunta de síntesis

¿Cuál representación elegiría el equipo si sólo pudiera usar una? ¿Qué capacidad perdería? ¿Por qué una arquitectura híbrida no consiste simplemente en utilizar todas las representaciones disponibles?

---

## 18. Casos de prueba

La arquitectura propuesta debe analizar los siguientes escenarios:

### Caso A — Alerta validada

```text
S1 activo y verificado
S1 monitorea P09
S1 produce alerta
P09 es activo crítico
```

**Resultado esperado:** se deriva sospecha y recomendación de inspección; no se afirma contaminación como certeza.

### Caso B — Sensor no verificado

```text
S2 activo
no existe verificación vigente de S2
S2 produce alerta
```

**Resultado esperado:** se solicita confirmación o una fuente adicional; no se libera automáticamente.

### Caso C — Evidencia contradictoria

```text
alerta validada
inspección reciente sin hallazgos
ambas observaciones siguen vigentes
```

**Resultado esperado:** se registra conflicto, se conserva procedencia y se escala según política.

### Caso D — Información incompleta

```text
no existe lectura reciente del sensor
no existe inspección vigente
```

**Resultado esperado:** se reconoce desconocimiento; ausencia de evidencia no se convierte en evidencia de seguridad.

### Caso E — Cambio de reglas

```text
la conclusión fue generada con R1 versión 1
la versión vigente es R1 versión 2
```

**Resultado esperado:** la explicación histórica conserva versión 1 y el sistema determina si requiere recalcular el estado actual.

### Registro de pruebas

| Caso | Hechos de entrada | Conclusión | Reglas aplicadas | Incertidumbre | ¿Escala? | Resultado correcto |
|---|---|---|---|---|---|---|
| A |  |  |  |  |  |  |
| B |  |  |  |  |  |  |
| C |  |  |  |  |  |  |
| D |  |  |  |  |  |  |
| E |  |  |  |  |  |  |

---

## 19. Guía parcial de resultados

Esta sección permite comprobar el mecanismo sin resolver todos los entregables abiertos.

### 19.1 Clasificación básica

- “`P09` contiene un objeto extraño” describe un **estado real hipotético**.
- “`S1` emitió `A101`” es una **observación registrada**.
- “$P(C\mid alerta)=0.269$” es una **creencia probabilística**.
- “solicitar inspección” es una **acción o recomendación**.
- “ninguna recomendación libera automáticamente” es una **restricción de autoridad**.

### 19.2 Lógica proposicional

Con $A=V=verdadero$:

$$
A\land V=verdadero
$$

por lo que la regla obliga a que $R=verdadero$. Después:

$$
R\rightarrow B
$$

permite concluir $B=verdadero$.

Esto no demuestra que exista contaminación. Demuestra que, bajo las reglas del ejercicio, la evidencia obliga a revisar y mantener el bloqueo.

### 19.3 Mundo abierto

La ausencia de `verificado(S2)` significa **desconocido**, salvo que una fuente completa y autoritativa permita aplicar mundo cerrado. Para evitar ambigüedad, puede registrarse:

```text
verificacionVencida(S2)
```

o:

```text
estadoVerificacion(S2, desconocido)
```

### 19.4 Actualización bayesiana

$$
P(C\mid alerta)=
\frac{0.90(0.02)}{0.90(0.02)+0.05(0.98)}
\approx0.269
$$

El posterior aproxima **26.9 %**.

### 19.5 Utilidad esperada

$$
EU(liberar)=0.731(10)+0.269(-1000)\approx-261.7
$$

$$
EU(inspeccionar)=-8
$$

Bajo estos supuestos, inspeccionar tiene mayor utilidad esperada. La recomendación sigue sujeta a restricciones y autoridad.

### 19.6 Arquitectura híbrida

Una respuesta razonable puede asignar:

- tablas o almacenamiento de eventos para observaciones;
- grafo y ontología para identidad y relaciones;
- reglas para restricciones explícitas;
- Bayes para actualizar creencias;
- lógica difusa para conceptos graduales;
- embeddings para recuperar casos similares;
- optimización para programar recursos;
- revisión humana para decisiones autorizadas.

---

## 20. Rúbrica de evaluación

| Criterio | 4 — sólido | 3 — adecuado | 2 — parcial | 1 — insuficiente |
|---|---|---|---|---|
| separación conceptual | distingue estado, observación, creencia, regla y acción | presenta una confusión menor | presenta varias confusiones | trata señales como hechos sin justificación |
| formalización lógica | predicados y reglas son consistentes y generalizables | existen detalles menores | reglas ambiguas o incompletas | no puede seguirse la inferencia |
| variedad representacional | compara al menos seis formas con ventajas y límites | compara cinco formas | compara tres o cuatro | usa una sola forma sin análisis |
| inferencia | demuestra conclusiones y punto fijo paso a paso | demuestra la mayoría | omite pasos importantes | afirma resultados sin soporte |
| incertidumbre | separa probabilidad, gradualidad y desconocimiento | presenta una imprecisión | mezcla dos conceptos | trata incertidumbre como certeza |
| procedencia | conserva fuentes, tiempos, reglas y versiones | omite un elemento | trazabilidad incompleta | no existe trazabilidad |
| arquitectura | componentes e interfaces responden a requisitos | solución funcional con detalles pendientes | componentes sin contratos claros | acumulación de herramientas sin diseño |
| gobernanza | define autoridad, escalamiento y restricciones | define la mayoría | responsabilidades ambiguas | el modelo decide sin límites |
| comunicación | explicación clara, concisa y reproducible | explicación comprensible | explicación difícil de seguir | no puede justificarse la decisión |

### Puntaje sugerido

$$
Puntaje=\sum_{i=1}^{9} criterio_i
$$

Máximo: **36 puntos**.

---

## 21. Preguntas para el cierre

1. ¿Qué representación hizo más visible la diferencia entre observación y estado real?
2. ¿Qué conocimiento fue más sencillo expresar mediante reglas?
3. ¿Qué información resultó más natural en un grafo?
4. ¿Qué restricciones necesitaron una ontología o lenguaje formal?
5. ¿Dónde apareció la incertidumbre y cómo se representó?
6. ¿Qué conclusión cambió al adoptar mundo abierto?
7. ¿Qué componente produce la explicación más útil?
8. ¿Qué ocurre si un modelo neuronal clasifica incorrectamente una observación?
9. ¿Qué debe recalcularse al cambiar una regla?
10. ¿Qué decisión conservaría siempre bajo autoridad humana?

---

## 22. Entrega final

El expediente del equipo debe contener:

1. tabla de clasificación conceptual;
2. esquema relacional y restricciones;
3. lógica proposicional;
4. lógica de predicados;
5. ejecución del motor de reglas;
6. frames;
7. triples y grafo;
8. ontología mínima;
9. análisis de mundo abierto y cerrado;
10. representación probabilística;
11. interfaz vector–símbolo;
12. cadena de procedencia;
13. arquitectura integradora;
14. registro de casos de prueba;
15. conclusión de una página.

### Formato de la conclusión

Responder en una página:

> ¿Qué arquitectura de representación permite apoyar la decisión de inspeccionar o liberar una pista sin confundir evidencia, inferencia y autoridad?

La respuesta debe mencionar al menos:

- una forma simbólica;
- una forma probabilística o difusa;
- una representación estructural;
- procedencia;
- límites de autoridad;
- un riesgo de la arquitectura.

---

## Referencias de apoyo

- Brachman, R. J. y Levesque, H. J. *Knowledge Representation and Reasoning*. <https://www.cs.toronto.edu/~hector/Papers/krbook.pdf>
- Gruber, T. R. (1993). “A Translation Approach to Portable Ontology Specifications”. <https://tomgruber.org/writing/ontolingua-kaj-1993.pdf>
- Minsky, M. (1974). “A Framework for Representing Knowledge”. <https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d>
- van Emden, M. H. y Kowalski, R. A. (1976). “The Semantics of Predicate Logic as a Programming Language”. <https://maarten.vanemden.com/Publications/kowVE.pdf>
- W3C. *RDF 1.1 Concepts and Abstract Syntax*. <https://www.w3.org/TR/rdf-concepts/>
- W3C. *OWL 2 Web Ontology Language*. <https://www.w3.org/TR/owl-overview/>
- W3C. *PROV-O: The PROV Ontology*. <https://www.w3.org/TR/prov-o/>
