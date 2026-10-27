# Módulo 1.2 — Arquitecturas de representación del conocimiento

> **Inteligencia Artificial**  
> **Módulo 1 — Sistemas cognitivos y representación del conocimiento**  
> Tema 1.2

## Introducción

Un sistema de inteligencia artificial no trabaja directamente con el mundo: trabaja con una **representación** del mundo. Sensores, documentos, bases de datos y personas producen señales; una arquitectura de representación decide cuáles señales se convierten en entidades, propiedades, relaciones, reglas, probabilidades o vectores, y qué operaciones pueden realizarse sobre ellas.

Representar conocimiento no significa almacenar todos los datos disponibles. Significa construir una estructura que permita responder preguntas, detectar inconsistencias, derivar consecuencias, justificar decisiones y actualizar lo conocido cuando cambia el entorno.

Una representación siempre selecciona y simplifica. Por ello, diseñarla implica tomar decisiones acerca de:

- qué aspectos del dominio son relevantes;
- qué distinciones deben conservarse;
- qué inferencias serán necesarias;
- cómo se tratarán incertidumbre, excepciones y cambios;
- qué costo computacional es aceptable;
- cómo se verificará la procedencia del conocimiento;
- qué decisiones requieren intervención humana.

La pregunta central de este tema es:

> **¿Cómo debe organizarse el conocimiento para que un sistema pueda interpretarlo, relacionarlo, inferir sobre él y utilizarlo de forma confiable?**

---

## 1. ¿Qué es una arquitectura de representación del conocimiento?

### 1.1 Definición de trabajo

Una **arquitectura de representación del conocimiento** es el conjunto coordinado de:

1. un **vocabulario** para describir el dominio;
2. una **estructura** para organizar hechos, conceptos y relaciones;
3. una **semántica** que determina qué significan las expresiones;
4. mecanismos de **inferencia** que producen conocimiento derivado;
5. mecanismos de **consulta, actualización y validación**;
6. controles de **procedencia, versión, acceso y gobernanza**;
7. interfaces con percepción, aprendizaje, decisión y acción.

La arquitectura no es sólo el formato de almacenamiento. Una tabla, un documento JSON o una base de grafos pueden guardar datos sin especificar por sí mismos qué consecuencias se siguen de ellos.

### 1.2 Datos, información y conocimiento

Estas palabras suelen utilizarse como sinónimos, pero conviene separarlas:

| Nivel | Ejemplo | Pregunta que responde |
|---|---|---|
| dato | `27.4` | ¿qué valor fue registrado? |
| información | `temperatura_motor = 27.4 °C` | ¿qué mide el valor y en qué unidad? |
| conocimiento | `si la temperatura excede el límite operativo, revisar el sistema de enfriamiento` | ¿qué significa el dato para una tarea? |
| decisión | `programar inspección antes del siguiente ciclo` | ¿qué acción se elige y por qué? |

El conocimiento aparece cuando los datos se conectan con conceptos, restricciones, relaciones, contexto y consecuencias.

### 1.3 Arquitectura cognitiva y arquitectura de conocimiento

No son equivalentes:

- una **arquitectura cognitiva** organiza capacidades como percepción, memoria, aprendizaje, razonamiento y acción;
- una **arquitectura de representación del conocimiento** organiza el contenido y las operaciones mediante las cuales esas capacidades describen el mundo.

Soar y ACT-R, por ejemplo, definen ciclos y memorias cognitivas. Dentro de ellos existen representaciones específicas —estados, operadores, producciones, fragmentos declarativos— que permiten ejecutar dichos ciclos.

### 1.4 Una arquitectura por capas

Una forma útil de analizar cualquier solución es separar seis capas:

| Capa | Función | Pregunta de diseño |
|---|---|---|
| adquisición | obtiene datos y conocimiento | ¿de dónde proviene? |
| conceptualización | identifica entidades y categorías | ¿qué existe en el dominio? |
| codificación | transforma conceptos en estructuras computables | ¿cómo se expresa? |
| inferencia | deriva conclusiones o estimaciones | ¿qué puede concluirse? |
| acceso y acción | conecta consultas con decisiones | ¿cómo se utiliza? |
| gobernanza | conserva procedencia, versiones y responsabilidades | ¿quién responde por el conocimiento? |

Separar estas capas evita confundir un modelo de datos con un modelo de significado o una predicción con una decisión.

---

## 2. Elementos más importantes que se deben comprender

### 2.1 Compromisos ontológicos

Toda representación asume qué tipos de cosas existen en el dominio. Una arquitectura para mantenimiento puede distinguir:

- activos;
- componentes;
- sensores;
- fallas;
- observaciones;
- órdenes de trabajo;
- técnicos;
- restricciones de seguridad.

Estas categorías son **compromisos ontológicos**: delimitan lo que el sistema puede expresar con claridad. Si el modelo no distingue una observación de una falla real, puede tratar una alerta como certeza.

### 2.2 Sintaxis, semántica y pragmática

- **Sintaxis:** determina qué expresiones están bien formadas.
- **Semántica:** determina qué significan y bajo qué interpretaciones son verdaderas.
- **Pragmática:** determina para qué tarea, usuario o contexto resulta útil la expresión.

Por ejemplo, el triple:

```text
SensorS1 — monitorea — MotorM4
```

tiene una estructura sintáctica. Su semántica debe aclarar qué significa `monitorea`, durante qué intervalo y con qué alcance. Su utilidad pragmática depende de si permite diagnosticar, auditar o planear mantenimiento.

### 2.3 Hechos, reglas, restricciones y consultas

Una base de conocimiento suele combinar:

- **hechos:** afirmaciones sobre casos particulares;
- **reglas:** patrones que permiten derivar afirmaciones;
- **restricciones:** condiciones que no deberían violarse;
- **consultas:** preguntas formuladas sobre el conocimiento;
- **metadatos:** autor, fecha, fuente, confianza y versión.

Ejemplo:

```text
Hecho: alerta(S1)
Hecho: monitorea(S1, Pista09)
Regla: alerta(s) ∧ monitorea(s, x) → requiere_revision(x)
Restricción: una pista no puede estar liberada y bloqueada al mismo tiempo
Consulta: ¿qué pistas requieren revisión?
```

### 2.4 Expresividad y tratabilidad

Una representación más expresiva permite formular más tipos de conocimiento, pero puede aumentar el costo de inferencia o volver algunas preguntas indecidibles.

El diseño busca un equilibrio:

- **expresividad:** qué puede decirse;
- **precisión semántica:** qué tan inequívoco es lo expresado;
- **tratabilidad:** cuánto tiempo y memoria exige razonar;
- **mantenibilidad:** qué tan fácil es actualizarlo;
- **explicabilidad:** qué tan fácil es reconstruir una conclusión.

No siempre conviene utilizar el lenguaje más potente. OWL 2, por ejemplo, define perfiles con distintas capacidades y propiedades computacionales para diferentes escenarios ([W3C, OWL 2 Overview](https://www.w3.org/TR/owl-overview/)).

### 2.5 Mundo abierto y mundo cerrado

Dos supuestos producen comportamientos muy distintos:

- **mundo cerrado:** si un hecho no aparece en la base, se trata como falso;
- **mundo abierto:** si un hecho no aparece, se considera desconocido.

En una base transaccional puede ser razonable asumir que una orden no registrada no existe. En una base que integra fuentes externas, la ausencia de un dato no demuestra que el hecho sea falso.

También debe distinguirse:

- **negación:** se sabe que algo no ocurre;
- **ausencia:** no existe evidencia registrada;
- **incertidumbre:** existe evidencia parcial o conflictiva.

### 2.6 Razonamiento monotónico y no monotónico

En un sistema **monotónico**, agregar conocimiento no invalida conclusiones anteriores. La lógica clásica ofrece esta propiedad.

En un sistema **no monotónico**, una nueva observación puede retirar una conclusión previa:

```text
Regla por defecto: si un equipo está disponible, puede asignarse.
Nueva evidencia: el equipo tiene una inspección vencida.
Conclusión revisada: no puede asignarse.
```

Los entornos reales requieren excepciones, prioridades, temporalidad y revisión de creencias. La arquitectura debe declarar cómo las maneja en vez de ocultarlas dentro del código de aplicación.

### 2.7 Conocimiento declarativo y procedimental

- **declarativo:** expresa qué es verdadero o qué relaciones existen;
- **procedimental:** expresa cómo ejecutar una tarea.

Ejemplo declarativo:

```text
todo activo crítico requiere inspección certificada
```

Ejemplo procedimental:

```text
1. bloquear el activo;
2. asignar inspector;
3. registrar evidencia;
4. solicitar autorización.
```

Una arquitectura robusta suele separar las reglas del dominio de los flujos operativos, aunque ambos deban coordinarse.

### 2.8 Identidad, contexto y tiempo

Representar que dos registros se refieren al mismo objeto es un problema central. También deben conservarse:

- unidad de medida;
- ubicación;
- intervalo temporal;
- versión del objeto;
- condiciones de validez;
- fuente del dato.

La afirmación “el sensor está activo” está incompleta si no se sabe cuál sensor, en qué momento, bajo qué configuración y según qué sistema de registro.

### 2.9 Procedencia y trazabilidad

Una conclusión es más útil cuando puede reconstruirse:

```text
fuente → transformación → regla aplicada → conclusión → decisión
```

La procedencia ayuda a:

- auditar decisiones;
- detectar fuentes obsoletas;
- resolver contradicciones;
- recalcular conocimiento derivado;
- asignar responsabilidad;
- explicar una recomendación.

### 2.10 Adquisición y mantenimiento del conocimiento

El conocimiento puede provenir de especialistas, normas, documentos, bases de datos, sensores o modelos aprendidos. Los principales problemas son:

- términos ambiguos;
- criterios tácitos difíciles de verbalizar;
- desacuerdo entre especialistas;
- reglas que cambian;
- conocimiento válido sólo en cierto contexto;
- duplicidad de entidades;
- inferencias que quedan obsoletas después de una actualización.

La arquitectura debe incluir un ciclo de mantenimiento, no sólo una carga inicial.

### 2.11 Evaluación de una representación

No basta con medir exactitud predictiva. Deben evaluarse:

| Dimensión | Pregunta |
|---|---|
| cobertura | ¿representa los casos relevantes? |
| competencia inferencial | ¿produce las conclusiones necesarias? |
| corrección | ¿evita inferencias inválidas? |
| consistencia | ¿detecta o administra contradicciones? |
| eficiencia | ¿responde dentro del tiempo disponible? |
| modificabilidad | ¿puede actualizarse sin rehacer todo el sistema? |
| interoperabilidad | ¿comparte significado con otros sistemas? |
| trazabilidad | ¿puede explicar fuentes y pasos? |
| robustez | ¿qué ocurre con datos faltantes o adversos? |

---

## 3. Principales familias de representación

### 3.1 Lógica formal

Representa hechos y relaciones mediante proposiciones, predicados, cuantificadores y axiomas.

**Fortalezas:** semántica precisa, inferencia verificable y buena capacidad explicativa.  
**Limitaciones:** modelar excepciones, contexto y conocimiento cotidiano puede ser costoso.

El proyecto *Advice Taker* de McCarthy planteó tempranamente el uso de lógica para almacenar conocimiento de sentido común y deducir acciones ([McCarthy, 1959](https://www-formal.stanford.edu/jmc/mcc59/mcc59.html)).

### 3.2 Reglas de producción

Utilizan expresiones del tipo:

```text
SI condición1 Y condición2 ENTONCES conclusión o acción
```

Pueden ejecutarse mediante:

- encadenamiento hacia adelante: partir de hechos y generar consecuencias;
- encadenamiento hacia atrás: partir de una meta y buscar hechos que la demuestren;
- agenda y resolución de conflictos: elegir qué regla aplicar primero.

Son comprensibles y editables, pero grandes colecciones de reglas pueden interactuar de formas difíciles de anticipar.

### 3.3 Redes semánticas y marcos

Las redes semánticas representan conceptos como nodos y relaciones como enlaces. Los marcos agrupan atributos, valores por defecto y expectativas alrededor de situaciones típicas.

Minsky propuso los **frames** como estructuras recordadas que se adaptan a una situación modificando detalles; también pueden incluir expectativas y procedimientos para cuando éstas fallan ([Minsky, 1974](https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d)).

KL-ONE formalizó redes de herencia estructurada e influyó en las posteriores lógicas descriptivas ([Brachman y Schmolze, 1985](https://doi.org/10.1207/s15516709cog0902_1)).

### 3.4 Ontologías y lógicas descriptivas

Una ontología define vocabulario compartido: clases, relaciones, individuos, restricciones y axiomas. Su objetivo es que personas y sistemas compartan una conceptualización explícita.

Gruber formuló la ontología como una especificación del vocabulario representacional de un dominio compartido y propuso mecanismos para intercambiarla entre sistemas ([Gruber, 1993](https://tomgruber.org/writing/ontolingua-kaj-1993.pdf)).

OWL 2 proporciona clases, propiedades, individuos y semánticas formales. Permite tareas como verificar consistencia, clasificar conceptos y recuperar instancias ([W3C, OWL 2](https://www.w3.org/TR/owl-overview/)).

Este enfoque se desarrollará con mayor profundidad en el tema **1.4 Ontologías y grafos de conocimiento**.

### 3.5 Grafos de conocimiento

Un grafo expresa hechos mediante relaciones entre entidades. RDF utiliza triples sujeto–predicado–objeto; un grafo RDF es un conjunto de triples y un conjunto de grafos puede organizarse como *dataset* ([W3C, RDF 1.1](https://www.w3.org/TR/rdf-concepts/)).

Ejemplo:

```text
Pista09 — tieneSensor — SensorS1
SensorS1 — produjo — AlertaA7
AlertaA7 — ocurrióEn — InstanteT
```

Los grafos facilitan integración, navegación y consulta de relaciones. Sin un vocabulario controlado, validación y procedencia, también pueden convertirse en una colección de enlaces ambiguos.

### 3.6 Modelos probabilísticos

Representan incertidumbre mediante variables aleatorias y dependencias. Las redes bayesianas, modelos de Markov y POMDP permiten actualizar creencias y decidir con información parcial.

**Fortalezas:** incertidumbre explícita y combinación de evidencia.  
**Limitaciones:** requieren probabilidades, supuestos de dependencia y mecanismos de calibración.

### 3.7 Representaciones distribuidas o vectoriales

Una entidad o concepto se representa mediante un vector de números. La información no reside necesariamente en una sola dimensión, sino en un patrón distribuido.

Hinton destacó que estas representaciones pueden facilitar generalización porque conceptos relacionados comparten patrones de actividad ([Hinton, 1986](https://repositories.cdlib.org/uc/item/79w838g1)). Métodos posteriores, como TransE, aprendieron vectores para entidades y relaciones de bases multirrelacionales ([Bordes et al., 2013](https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html)).

**Fortalezas:** similitud, aprendizaje a escala y tolerancia a variación.  
**Limitaciones:** significado distribuido, difícil edición directa y explicaciones incompletas.

### 3.8 Arquitecturas híbridas y neuro-simbólicas

Combinan componentes con propiedades diferentes:

- percepción neuronal;
- símbolos o entidades identificables;
- reglas u ontologías;
- inferencia probabilística;
- políticas de decisión;
- supervisión humana.

El objetivo no es acumular tecnologías, sino asignar cada función a la representación más apropiada. El *Neuro-Symbolic Concept Learner*, por ejemplo, combina percepción visual, análisis semántico y ejecución de programas simbólicos ([Mao et al., ICLR 2019](https://openreview.net/pdf/a0f215dd254bc10d946ccc26632ca8e42defee17.pdf)).

---

## 4. Cinco preguntas de investigación

### Pregunta 1. ¿Existe una representación universal para cualquier tipo de conocimiento?

**Respuesta desarrollada:** no existe una representación que sea simultáneamente la mejor para percepción, explicación, razonamiento temporal, incertidumbre, aprendizaje y acción. Cada formalismo privilegia ciertas operaciones. La investigación estudia arquitecturas híbridas y mecanismos de traducción, pero toda traducción puede perder información o alterar propiedades inferenciales.

**Pregunta abierta:** ¿cómo seleccionar o aprender automáticamente la representación adecuada para cada subtarea sin fragmentar el significado global?

### Pregunta 2. ¿Cuánta expresividad conviene incorporar?

**Respuesta parcial:** la expresividad debe justificarse por las consultas e inferencias requeridas. Lenguajes restringidos suelen ofrecer inferencia más eficiente y predecible. Lenguajes muy expresivos facilitan describir el dominio, pero elevan el costo de razonamiento y validación.

**Pregunta abierta:** ¿cómo medir el valor práctico de una construcción expresiva frente a su costo computacional y de mantenimiento?

### Pregunta 3. ¿Cómo se conectan símbolos explícitos con representaciones vectoriales aprendidas?

**Respuesta parcial:** pueden utilizarse modelos neuronales para extraer entidades y relaciones, vectores para recuperar candidatos, y reglas u ontologías para validar, restringir o explicar. También pueden incorporarse restricciones lógicas en el aprendizaje.

**Problema pendiente:** una similitud vectorial no equivale a una relación lógica. Hace falta evitar que una coincidencia aproximada se interprete como un hecho verificado.

### Pregunta 4. ¿Cómo debe comportarse el sistema cuando el conocimiento es incompleto, contradictorio o cambia?

**Respuesta parcial:** se requieren procedencia, temporalidad, niveles de confianza, políticas de prioridad y razonamiento no monotónico. Algunas arquitecturas conservan perspectivas incompatibles; otras rechazan inconsistencias o seleccionan una fuente preferente.

**Pregunta abierta:** ¿qué contradicciones pueden tolerarse y cuáles deben bloquear una decisión?

### Pregunta 5. ¿Cómo se evalúa si una representación es adecuada?

**Respuesta desarrollada:** debe evaluarse con las tareas que habilita, no sólo por su elegancia formal. Una representación es adecuada si permite las inferencias necesarias con corrección, eficiencia, trazabilidad y capacidad de actualización.

**Línea de investigación:** desarrollar pruebas de competencia que incluyan casos normales, límites, contradicciones, cambios de versión y preguntas no respondibles.

---

## 5. Tres casos de estudio

### Caso 1. MYCIN: conocimiento experto mediante reglas

MYCIN fue un sistema experto para apoyar la selección de terapias antimicrobianas. Representaba conocimiento mediante reglas y utilizaba factores de certeza para manejar evidencia incompleta.

#### Arquitectura conceptual

```text
datos del caso
      ↓
reglas clínicas
      ↓
encadenamiento y factores de certeza
      ↓
recomendación y explicación de reglas aplicadas
```

#### Aportes

- separó parte del conocimiento experto del programa general de inferencia;
- mostró el valor de explicaciones basadas en reglas aplicadas;
- permitió examinar y modificar conocimiento explícito;
- evidenció el costo de adquirir, validar y mantener reglas.

#### Lección

La transparencia local de una regla no garantiza que una base completa sea sencilla de validar. El sistema debe analizar interacciones, cobertura y excepciones.

### Caso 2. Wikidata: conocimiento compartido a escala

Wikidata organiza afirmaciones sobre entidades y permite que una comunidad mantenga datos reutilizables y multilingües. Su diseño incorpora identificadores, propiedades, calificadores y referencias.

#### Problema representacional

La afirmación “A es capital de B” puede requerir:

- periodo de validez;
- fuente;
- rango preferido;
- coexistencia con afirmaciones históricas;
- etiquetas en múltiples idiomas.

#### Aportes

- identidad estable separada de las etiquetas lingüísticas;
- afirmaciones enriquecidas con calificadores y referencias;
- edición colaborativa y reutilización;
- integración de información heterogénea.

El artículo de diseño presenta las decisiones centrales del modelo y sus posibles aplicaciones ([Vrandečić y Krötzsch, 2014](https://research.google/pubs/wikidata-a-free-collaborative-knowledge-base/)).

#### Lección

Un grafo operativo necesita mucho más que nodos y aristas: requiere identidad, contexto, procedencia, políticas editoriales y mecanismos de calidad.

### Caso 3. Neuro-Symbolic Concept Learner: percepción y razonamiento componible

NS-CL aborda preguntas sobre escenas visuales. Un componente neuronal identifica objetos y atributos; un analizador convierte preguntas en programas; un ejecutor simbólico opera sobre la representación de la escena.

#### Arquitectura conceptual

```text
imagen → objetos y atributos → representación de escena
pregunta → programa simbólico ────────────────┘
                           ↓
                     respuesta
```

#### Aportes

- separa percepción aproximada de ejecución simbólica;
- permite composición de operaciones;
- hace visible una estructura intermedia;
- muestra cómo varias representaciones pueden cooperar.

#### Riesgos y límites

- errores perceptivos contaminan símbolos posteriores;
- el vocabulario simbólico puede ser insuficiente;
- una estructura intermedia interpretable no garantiza que todo el proceso sea correcto;
- el sistema puede aprender atajos si los datos no exigen el razonamiento esperado.

#### Lección

Una arquitectura híbrida debe gobernar sus interfaces. El punto donde un vector se convierte en símbolo es una hipótesis que también necesita calibración y validación.

---

## 6. Línea de tiempo: avances e hitos

| Año | Hito | Relevancia |
|---:|---|---|
| 1958–1959 | McCarthy presenta *Programs with Common Sense* | propone lógica como medio para representar conocimiento y deducir acciones |
| 1965 | Robinson desarrolla el principio de resolución | ofrece un mecanismo general de demostración automática |
| 1968–1970 | redes semánticas y sistemas como SIR | impulsan representaciones relacionales para comprensión y consulta |
| 1972 | aparece Prolog | conecta lógica, unificación y ejecución de programas |
| 1974 | Minsky formula los marcos | representa situaciones típicas, expectativas y valores por defecto |
| 1976 | van Emden y Kowalski formalizan semántica operacional y de punto fijo | relacionan programas lógicos, modelos e inferencia ([artículo](https://maarten.vanemden.com/Publications/kowVE.pdf)) |
| década de 1970 | MYCIN y otros sistemas expertos | muestran utilidad y límites de reglas y adquisición de conocimiento |
| 1977–1985 | KL-ONE y lógicas descriptivas | estructuran conceptos, roles, herencia y clasificación |
| 1986 | representaciones distribuidas y aprendizaje por retropropagación | fortalecen la representación aprendida en redes neuronales |
| 1988 | Pearl sistematiza redes bayesianas | consolida razonamiento probabilístico mediante dependencias gráficas |
| 1993 | Gruber y Ontolingua | promueven vocabularios compartidos y ontologías portables |
| 1999–2004 | RDF, RDFS y OWL | estandarizan representación e intercambio semántico en la Web |
| 2006–2012 | DBpedia, Freebase, Wikidata y Google Knowledge Graph | llevan grafos de entidades y relaciones a gran escala |
| 2013 | TransE | conecta grafos multirrelacionales con representaciones vectoriales aprendidas |
| 2017–presente | modelos fundacionales, recuperación aumentada y agentes | reactivan preguntas sobre memoria, grounding, procedencia y verificación |
| 2019–presente | arquitecturas neuro-simbólicas modernas | combinan percepción aprendida, conceptos y programas de razonamiento |

### Lectura crítica de la línea de tiempo

La historia no sustituye una representación por otra de forma lineal. La lógica, las reglas, los grafos, la probabilidad y los vectores continúan coexistiendo porque resuelven problemas distintos. Muchos sistemas actuales recuperan ideas antiguas bajo nuevas condiciones de escala, datos e infraestructura.

---

## 7. Modelo matemático: inferencia como cierre de una base de reglas

### 7.1 Objetivo del modelo

Para aproximar una arquitectura simbólica se utilizará una base de hechos y reglas ejecutada mediante **encadenamiento hacia adelante**. El modelo permite estudiar:

- representación explícita;
- separación entre hechos y reglas;
- inferencia reproducible;
- trazabilidad de conclusiones;
- actualización incremental.

No pretende representar toda forma de conocimiento ni modelar incertidumbre numérica.

### 7.2 Componentes

Sea una base de conocimiento:

$$
K=\langle F,R,C,Q \rangle
$$

donde:

- $F$ es el conjunto de hechos conocidos;
- $R$ es el conjunto de reglas;
- $C$ es el conjunto de restricciones de integridad;
- $Q$ es el conjunto de consultas relevantes.

Una regla de Horn tiene la forma:

$$
b_1\land b_2\land\cdots\land b_m\rightarrow h
$$

donde $b_i$ son condiciones y $h$ es la conclusión.

### 7.3 Operador de consecuencia inmediata

Sea $I$ un conjunto de hechos. El operador $T_R$ agrega todas las conclusiones cuyas condiciones ya se cumplen:

$$
T_R(I)=I\cup
\left\{
h\theta\;\middle|\;
(b_1\land\cdots\land b_m\rightarrow h)\in R,
\{b_1\theta,\ldots,b_m\theta\}\subseteq I
\right\}
$$

$\theta$ es una sustitución que asigna objetos concretos a las variables.

La inferencia se repite:

$$
I_0=F
$$

$$
I_{n+1}=T_R(I_n)
$$

hasta alcanzar un punto fijo:

$$
I^*=T_R(I^*)
$$

En una base finita y sin funciones que generen términos ilimitados, el proceso termina cuando una iteración ya no produce hechos nuevos. Esta interpretación se relaciona con la semántica de punto fijo de los programas lógicos ([van Emden y Kowalski, 1976](https://maarten.vanemden.com/Publications/kowVE.pdf)).

### 7.4 Ejemplo: autorizar o bloquear la liberación de una pista

Supongamos los hechos iniciales:

$$
F=\{
sensor(S1),
monitorea(S1,P09),
alerta(S1),
verificado(S1),
activoCritico(P09)
\}
$$

Reglas:

$$
r_1:\ alerta(s)\land verificado(s)\land monitorea(s,x)
\rightarrow sospechaContaminacion(x)
$$

$$
r_2:\ sospechaContaminacion(x)\land activoCritico(x)
\rightarrow requiereInspeccion(x)
$$

$$
r_3:\ requiereInspeccion(x)
\rightarrow bloquearLiberacion(x)
$$

#### Iteración 0

Sólo están disponibles los hechos de $F$.

#### Iteración 1

$r_1$ coincide con $s=S1$ y $x=P09$:

$$
I_1=F\cup\{sospechaContaminacion(P09)\}
$$

#### Iteración 2

$r_2$ utiliza el hecho recién derivado:

$$
I_2=I_1\cup\{requiereInspeccion(P09)\}
$$

#### Iteración 3

$r_3$ produce:

$$
I_3=I_2\cup\{bloquearLiberacion(P09)\}
$$

#### Iteración 4

No aparecen nuevos hechos:

$$
I_4=I_3=I^*
$$

La consulta:

$$
Q(x)=bloquearLiberacion(x)
$$

devuelve $x=P09$.

### 7.5 Explicación como grafo de prueba

La conclusión puede explicarse mediante dependencias:

```text
alerta(S1) ───────────────┐
verificado(S1) ──────────┼→ sospechaContaminacion(P09)
monitorea(S1,P09) ───────┘                 │
activoCritico(P09) ───────────────────────┼→ requiereInspeccion(P09)
                                          │
                                          └→ bloquearLiberacion(P09)
```

La explicación debe registrar:

- hechos utilizados;
- fuentes y tiempos de esos hechos;
- reglas aplicadas;
- sustituciones;
- restricciones verificadas;
- versión de la base de conocimiento.

### 7.6 Restricciones de integridad

Puede declararse que ciertos estados son incompatibles:

$$
\neg\big(liberada(x)\land bloquearLiberacion(x)\big)
$$

Si la base deriva ambos, la arquitectura no debería elegir silenciosamente uno. Debe detectar el conflicto y aplicar una política: rechazar la transacción, priorizar una fuente, solicitar revisión o conservar perspectivas separadas.

### 7.7 Limitaciones del modelo

El cierre monotónico tiene ventajas de reproducibilidad, pero simplifica varios problemas:

- una alerta aparece como hecho binario;
- no existe grado de confianza;
- no se representa tiempo de manera explícita;
- no se retiran conclusiones cuando cambia la evidencia;
- todas las reglas parecen tener la misma autoridad;
- no se comparan costos ni beneficios;
- los símbolos se dan por identificados correctamente.

### 7.8 Extensiones hacia los siguientes temas

#### Puente a 1.3 — Lógica difusa e inferencia

La condición `alerta(S1)` puede sustituirse o complementarse con grados:

$$
\mu_{riesgoAlto}(x)\in[0,1]
$$

Así se representa gradualidad, por ejemplo “visibilidad baja” o “contaminación significativa”. Esto no equivale a probabilidad: una membresía difusa expresa grado de pertenencia a un concepto.

#### Puente a 1.4 — Ontologías y grafos

Los predicados pueden relacionarse con clases y propiedades explícitas:

```text
Sensor ⊑ Dispositivo
monitorea: Sensor × Activo
Pista ⊑ ActivoCritico
```

Los hechos pueden publicarse como triples con identidad, procedencia y vocabularios compartidos.

#### Puente a 1.5 — Optimización de procesos

Una conclusión como `requiereInspeccion(P09)` no determina por sí sola quién inspecciona, cuándo ni con qué recursos. La optimización agrega:

- tiempos;
- capacidades;
- prioridades;
- costos;
- restricciones regulatorias;
- objetivos de seguridad y disponibilidad.

La representación define el espacio de decisión; la optimización busca una acción dentro de ese espacio.

---

## 8. Guía de diseño de una arquitectura

### Paso 1. Definir tareas y preguntas

Evitar comenzar por la tecnología. Enumerar consultas, decisiones y explicaciones necesarias.

### Paso 2. Delimitar el dominio

Definir entidades, procesos, eventos, actores, unidades, tiempos y límites organizacionales.

### Paso 3. Elegir compromisos semánticos

Precisar identidad, mundo abierto o cerrado, manejo de negación, temporalidad y excepciones.

### Paso 4. Seleccionar representaciones

Elegir lógica, reglas, grafos, probabilidad, vectores o combinaciones según la tarea.

### Paso 5. Diseñar inferencia y actualización

Definir qué conclusiones pueden derivarse, qué conocimiento se materializa y cómo se retira o recalcula.

### Paso 6. Incorporar procedencia y gobernanza

Registrar fuente, versión, responsable, vigencia, confianza y permisos.

### Paso 7. Probar competencia y fallas

Evaluar casos normales, límites, contradicciones, datos faltantes y cambios de contexto.

### Paso 8. Observar el uso real

Medir si la arquitectura ayuda a las personas a decidir o sólo desplaza trabajo y ambigüedad.

---

## 9. Síntesis para estudio

1. Representar conocimiento implica seleccionar aspectos del mundo y darles estructura computable.
2. Una arquitectura incluye vocabulario, semántica, inferencia, actualización, acceso y gobernanza.
3. Sintaxis correcta no garantiza significado compartido.
4. La ausencia de un hecho no siempre equivale a su negación.
5. Expresividad y eficiencia forman un compromiso de diseño.
6. Las reglas son explicables localmente, pero sus interacciones pueden ser complejas.
7. Las ontologías formalizan conceptos compartidos; los grafos conectan instancias y afirmaciones.
8. Los modelos probabilísticos representan incertidumbre; los modelos difusos representan gradualidad.
9. Los vectores facilitan similitud y aprendizaje, pero no sustituyen automáticamente semántica y verificación.
10. Las arquitecturas híbridas requieren interfaces explícitas entre percepción, símbolos, razonamiento y acción.
11. Procedencia, temporalidad y versión son parte del conocimiento operativo.
12. Una representación debe evaluarse por las tareas e inferencias que habilita de forma confiable.

---

## 10. Actividades

### Actividad A — La misma situación en cuatro representaciones

Representar “un activo presenta riesgo de sobrecalentamiento” como:

1. regla lógica;
2. distribución probabilística;
3. variable difusa;
4. conjunto de triples.

Comparar qué pregunta responde bien cada representación y qué información pierde.

### Actividad B — Mundo abierto o cerrado

Clasificar los siguientes casos y justificar el supuesto:

- inventario de piezas dentro de un almacén controlado;
- base pública de investigadores;
- historial clínico integrado desde varias instituciones;
- lista de permisos activos en una aplicación;
- catálogo de incidentes reportados por usuarios.

### Actividad C — Construir un cierre inferencial

Partir de tres hechos y tres reglas. Ejecutar manualmente $T_R$ hasta alcanzar el punto fijo. Dibujar después el grafo de prueba de una conclusión.

### Actividad D — Diseñar una arquitectura híbrida

Para un sistema que inspecciona imágenes industriales:

1. decidir qué componente usa vectores;
2. decidir qué conceptos requieren símbolos;
3. proponer dos reglas;
4. incluir una fuente de incertidumbre;
5. definir qué decisión debe escalarse a una persona.

---

## 11. Preguntas de comprobación

1. ¿Por qué una base de datos no constituye automáticamente una base de conocimiento?
2. ¿Qué diferencia existe entre sintaxis, semántica y pragmática?
3. ¿Qué es un compromiso ontológico?
4. ¿Cómo difieren los supuestos de mundo abierto y mundo cerrado?
5. ¿Qué significa que un razonamiento sea monotónico?
6. ¿Qué ventajas y límites presentan las reglas de producción?
7. ¿Qué aporta la procedencia a una conclusión?
8. ¿Por qué una similitud vectorial no equivale a una relación lógica?
9. ¿Qué expresa el punto fijo del operador de consecuencia inmediata?
10. ¿Qué debe gobernarse en la interfaz entre un modelo neuronal y un razonador simbólico?

---

## Referencias y lecturas recomendadas

- Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J. y Yakhnenko, O. (2013). “Translating Embeddings for Modeling Multi-relational Data”. *NeurIPS*. <https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html>
- Brachman, R. J. y Schmolze, J. G. (1985). “An Overview of the KL-ONE Knowledge Representation System”. *Cognitive Science*, 9(2), 171–216. <https://doi.org/10.1207/s15516709cog0902_1>
- Gruber, T. R. (1993). “A Translation Approach to Portable Ontology Specifications”. *Knowledge Acquisition*, 5(2), 199–220. <https://tomgruber.org/writing/ontolingua-kaj-1993.pdf>
- Hinton, G. E. (1986). “Learning Distributed Representations of Concepts”. *Proceedings of the Eighth Annual Conference of the Cognitive Science Society*. <https://repositories.cdlib.org/uc/item/79w838g1>
- Mao, J., Gan, C., Kohli, P., Tenenbaum, J. B. y Wu, J. (2019). “The Neuro-Symbolic Concept Learner”. *ICLR*. <https://openreview.net/pdf/a0f215dd254bc10d946ccc26632ca8e42defee17.pdf>
- McCarthy, J. (1959). “Programs with Common Sense”. <https://www-formal.stanford.edu/jmc/mcc59/mcc59.html>
- Minsky, M. (1974). “A Framework for Representing Knowledge”. MIT AI Laboratory Memo 306. <https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d>
- van Emden, M. H. y Kowalski, R. A. (1976). “The Semantics of Predicate Logic as a Programming Language”. *Journal of the ACM*, 23(4), 733–742. <https://maarten.vanemden.com/Publications/kowVE.pdf>
- Vrandečić, D. y Krötzsch, M. (2014). “Wikidata: A Free Collaborative Knowledgebase”. *Communications of the ACM*, 57(10), 78–85. <https://research.google/pubs/wikidata-a-free-collaborative-knowledge-base/>
- W3C. *RDF 1.1 Concepts and Abstract Syntax*. <https://www.w3.org/TR/rdf-concepts/>
- W3C. *OWL 2 Web Ontology Language — Document Overview*. <https://www.w3.org/TR/owl-overview/>

### Nota de uso académico

Estas notas presentan una introducción estructurada y ejemplos simplificados. El diseño de una arquitectura operacional debe contrastarse con requisitos del dominio, normativa, especialistas, datos disponibles, amenazas, costos computacionales y responsabilidades institucionales.
